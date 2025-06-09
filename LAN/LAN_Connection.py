import subprocess
import platform
import time
from PySide6.QtCore import QObject, QTimer, Signal, Slot, QProcess, QThread
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel
import datetime
class WifiMonitor(QObject):
    connection_status_changed = Signal(bool)  # Señal para notificar cambios de conexión

    def __init__(self, ssid, password, interval=5000, parent=None):
        """
        Monitoriza la conexión a una red Wi-Fi específica y reconecta si es necesario.

        Args:
            ssid (str): Nombre de la red Wi-Fi.
            password (str): Contraseña de la red Wi-Fi.
            interval (int): Intervalo en milisegundos para verificar la conexión.
        """
        super().__init__(parent)
        self.ssid = ssid
        self.password = password

        # Temporizador para iniciar la verificación periódica
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.start_check_thread)
        self.timer.start(interval)

        # Hilo para verificación de conexión
        self.check_thread = None

        # Hacer una verificación inicial
        self.start_check_thread()

    def start_check_thread(self):
        """Inicia un hilo para verificar la conexión sin bloquear la GUI."""
        if self.check_thread and self.check_thread.isRunning():
            return  # Evitar iniciar múltiples hilos

        self.check_thread = WifiCheckThread(self.ssid)
        self.check_thread.connection_checked.connect(self.handle_connection_status)
        self.check_thread.start()

    def handle_connection_status(self, connected):
        """Maneja el resultado de la verificación de conexión."""
        self.connection_status_changed.emit(connected)
        if not connected:
            print("Wi-Fi desconectado. Intentando reconectar...")
            self.start_reconnect_thread()

    def start_reconnect_thread(self):
        """Inicia un hilo para reconectar sin bloquear la GUI."""
        self.reconnect_thread = WifiReconnectThread(self.ssid, self.password)
        self.reconnect_thread.connection_result.connect(self.connection_status_changed.emit)
        self.reconnect_thread.start()

class WifiCheckThread(QThread):
    """Hilo para verificar si el sistema está conectado a una red Wi-Fi específica."""
    connection_checked = Signal(bool)

    def __init__(self, ssid, parent=None):
        super().__init__(parent)
        self.ssid = ssid

    def run(self):
        """Ejecuta la verificación en segundo plano."""
        connected = self.is_connected_to_wifi()
        self.connection_checked.emit(connected)

    def is_connected_to_wifi(self) -> bool:
        """Verifica si está conectado a la red Wi-Fi especificada."""
        try:
            if platform.system() == "Windows":
                startupinfo = subprocess.STARTUPINFO()
                startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW  # Evita mostrar consola
                result = subprocess.run(
                    ["netsh", "wlan", "show", "interfaces"],
                    capture_output=True, text=True, timeout=2,
                    startupinfo=startupinfo, creationflags=subprocess.CREATE_NO_WINDOW
                )
                return f"SSID                   : {self.ssid}" in result.stdout

            elif platform.system() == "Linux":
                result = subprocess.run(["iwgetid", "-r"], capture_output=True, text=True, timeout=2)
                return result.stdout.strip() == self.ssid

            elif platform.system() == "Darwin":  # macOS
                result = subprocess.run(
                    ["/System/Library/PrivateFrameworks/Apple80211.framework/Versions/Current/Resources/airport", "-I"],
                    capture_output=True, text=True, timeout=2
                )
                return self.ssid in result.stdout

        except subprocess.SubprocessError as e:
            print(f"Error verificando Wi-Fi: {e}")
            return False

class WifiReconnectThread(QThread):
    """Hilo para reconectar a la red Wi-Fi sin bloquear la GUI."""
    connection_result = Signal(bool)

    def __init__(self, ssid, password, parent=None):
        super().__init__(parent)
        self.ssid = ssid
        self.password = password

    def run(self):
        """Ejecuta la reconexión en segundo plano."""
        connected = self.connect_to_wifi()
        self.connection_result.emit(connected)

    def connect_to_wifi(self) -> bool:
        """Intenta conectarse a la red Wi-Fi específica sin mostrar ventana en Windows."""
        try:
            if platform.system() == "Windows":
                startupinfo = subprocess.STARTUPINFO()
                startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW
                subprocess.run(
                    ["netsh", "wlan", "connect", "name=" + self.ssid],
                    timeout=5,
                    startupinfo=startupinfo, creationflags=subprocess.CREATE_NO_WINDOW
                )
            return WifiCheckThread(self.ssid).is_connected_to_wifi()  # Verificar conexión
        except subprocess.SubprocessError as e:
            print(f"Error reconectando Wi-Fi: {e}")
            return False
