import serial
from PySide6.QtCore import QThread, Signal


class SerialMonitor(QThread):
    data_received = Signal(str, str)  # Señal que emite los datos recibidos

    def __init__(self, puerto: str, baudrate: int = 9600, timeout: float = 1):
        super().__init__()
        self.puerto = puerto
        self.baudrate = baudrate
        self.timeout = timeout
        self.running = False  # Estado de ejecución

    def run(self):
        """Método principal del hilo: escucha continuamente el puerto serial."""
        try:
            with serial.Serial(self.puerto, self.baudrate, timeout=self.timeout) as ser:
                self.running = True
                while self.running:
                    datos = ser.readall().decode("utf-8").strip()
                    if datos:  # Solo emitir señal si hay datos
                        self.data_received.emit(self.puerto, datos)

        except serial.SerialException as e:
            self.data_received.emit(f"Error: {e}")

    def start_listening(self):
        """Inicia el monitoreo del puerto en un hilo separado."""
        if not self.isRunning():
            self.start()

    def stop_listening(self):
        """Detiene el monitoreo del puerto."""
        self.running = False
        self.quit()
        self.wait()
