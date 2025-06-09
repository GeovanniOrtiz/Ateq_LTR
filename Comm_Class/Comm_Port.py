from PySide6.QtCore import QThread, Signal
import serial

class SerialMonitor_original(QThread):
    data_received = Signal(str, bytes)  # Señal (puerto COM, datos)

    def __init__(self, com_ports, baudrate=9600, parent=None):
        super().__init__(parent)
        self.com_ports = com_ports  # Lista de puertos COM (ejemplo: ["COM3", "COM4", "COM5"])
        self.baudrate = baudrate
        self.running = True  # Bandera para detener el hilo

    def run(self):
        """Ejecuta la lectura continua de los puertos COM en un hilo."""
        serial_connections = {}

        try:
            # Intentar abrir cada puerto COM especificado
            for port in self.com_ports:
                try:
                    serial_connections[port] = serial.Serial(port, self.baudrate, timeout=1)
                except serial.SerialException as e:
                    print(f"Error al abrir {port}: {e}")

            while self.running:
                for port, ser in serial_connections.items():
                    if ser.is_open and ser.in_waiting > 0:
                        data = ser.read(ser.in_waiting)  # Leer todos los datos disponibles
                        self.data_received.emit(port, data)  # Emitir señal con el puerto y los datos

        finally:
            # Cerrar todas las conexiones al salir del hilo
            for ser in serial_connections.values():
                if ser.is_open:
                    ser.close()

    def stop(self):
        """Detiene el hilo y cierra los puertos serie."""
        self.running = False
        self.wait()  # Espera a que el hilo termine

class SerialMonitor(QThread):
    data_received = Signal(str, bytes)  # Señal (puerto COM, datos)

    def __init__(self, port, baudrate=9600, parent=None):
        super().__init__(parent)
        self.port = port  # Puerto COM único
        self.baudrate = baudrate
        self.running = True
        self.ser = None  # Inicializar la conexión como None

    def run(self):
        """Ejecuta la lectura continua del puerto COM en un hilo."""
        try:
            # Intentar abrir el puerto
            self.ser = serial.Serial(self.port, self.baudrate, timeout=1)
        except serial.SerialException as e:
            print(f"Error al abrir {self.port}: {e}")
            return

        while self.running:
            if self.ser.is_open and self.ser.in_waiting > 0:
                data = self.ser.read(self.ser.in_waiting)  # Leer todos los datos disponibles
                self.data_received.emit(self.port, data)  # Emitir señal con los datos

        # Cerrar la conexión al salir del bucle
        if self.ser and self.ser.is_open:
            self.ser.close()

    def stop(self):
        """Detiene el hilo y cierra el puerto serie."""
        self.running = False
        self.wait()  # Espera a que el hilo termine
