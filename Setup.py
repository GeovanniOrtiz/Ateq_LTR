import json
import os
import sys
import serial.tools.list_ports
import cv2
import numpy as np
from PySide6.QtCore import QTimer, Slot
from PySide6.QtGui import QImage, QPixmap, Qt
from PySide6.QtWidgets import QMainWindow, QApplication, QMessageBox

from Interfaz.Config_gui import Ui_MainWindow

class Config(QMainWindow):
    def __init__(self):
        super().__init__()

        # Crea la instancia de la clase de la interfaz
        self.ui_main = Ui_MainWindow()
        self.ui_main.setupUi(self)

        self.setWindowTitle("Setup de Estacion")  # Título de la ventana
        #self.setWindowFlag(Qt.FramelessWindowHint)
        # Deshabilitar el botón de maximizar
        self.setWindowFlags(Qt.Window | Qt.WindowMinimizeButtonHint | Qt.WindowCloseButtonHint)
        self.initGui()
        self.initSlots()

    def initGui(self):
        try:
            # verifica los puerto com disponibles
            PortsCom = self.get_rs232_ports()
            self.ui_main.box_com.addItems(PortsCom)
        except Exception as e:
            QMessageBox.critical(None, "Puerto COM",
                                 f"No se encontro Puerto COM Disponible\nVerificar conexion fisica.")
            sys.exit(0)


        if PortsCom:
            try:
                # Obtener valores actuales desde el JSON
                self.COM, self.IP, self.station_available, self.TEST = self.Read_Json()

                # Configurar valores en la GUI
                self.ui_main.box_com.setCurrentText(self.COM)

                # Configurar el índice del box_label
                TEST_mapping = {"1": 0, "0": 1}
                if self.TEST in TEST_mapping:
                    self.ui_main.box_label.setCurrentIndex(TEST_mapping[self.TEST])

                # Configurar el índice del box_station
                station_mapping = {"3": 0, "4": 1, "5": 2}
                if self.station_available in station_mapping:
                    self.ui_main.box_station.setCurrentIndex(station_mapping[self.station_available])

            except Exception as e:
                print(f"Error al leer el JSON o actualizar la GUI: {e}")

            # Video de fondo
            video_path = "./video.mp4"
            self.video_path = video_path
            self.capture = cv2.VideoCapture(self.video_path)

            # Comprobar si el video se ha cargado correctamente
            if not self.capture.isOpened():
                print("Error: El video no se pudo abrir.")
                sys.exit(0)

            # Obtener el total de fotogramas del video
            self.total_frames = int(self.capture.get(cv2.CAP_PROP_FRAME_COUNT))

            # Timer para actualizar el video en la interfaz
            self.timer = QTimer(self)
            self.timer.timeout.connect(self.update_video)
            self.timer.start(30)
        else:
            QMessageBox.critical(None, "Puerto COM",
                                 f"No se encontro Puerto COM Disponible\nVerificar conexion fisica.")
            sys.exit(0)

    def initSlots(self):
        self.ui_main.btn_aceptar.released.connect(self.OkSettings)
        self.ui_main.btn_cancelar.released.connect(lambda:sys.exit(0))

    def OkSettings(self):
        station = self.ui_main.box_station.currentText()
        com = self.ui_main.box_com.currentText()
        label = self.ui_main.box_label.currentText()

        #print(station, com, label)
        if label == "ACTIVADO":
            nlabel = "1"
        else:
            nlabel = "0"
        nstation = station[-1:]
        self.Write_Json(com,nstation,nlabel)
        QMessageBox.information(None, "Guardado", "Datos Guardados con Exito!")
        sys.exit(0)

    def Write_Json(self, COM=None, STATION=None, TEST=None, IP="192.168.1.22"):
        """
        Método que escribe los valores en el archivo JSON.
        Si el archivo no existe, lo crea con valores predeterminados.

        :param COM: Puertos COM
        :param IP: Direcciones IP
        :param STATION: Estaciones
        :param LABEL: Etiquetas
        """
        archivo = "./Data/data.json"

        # Valores predeterminados
        default_data = {
            "COM": "COM9",
            "IP": "192.168.1.22",
            "STATION": "3",
            "TEST": "0"
        }

        # Asegurar que el directorio existe
        os.makedirs(os.path.dirname(archivo), exist_ok=True)

        # Si el archivo no existe, crearlo con la estructura predeterminada
        if not os.path.exists(archivo):
            with open(archivo, "w", encoding="utf-8") as f:
                json.dump(default_data, f, ensure_ascii=False, indent=4)

        # Leer el contenido actual del archivo
        with open(archivo, "r", encoding="utf-8") as f:
            data = json.load(f)

        # Actualizar solo los valores proporcionados
        if COM is not None:
            data["COM"] = COM
        if IP is not None:
            data["IP"] = IP
        if STATION is not None:
            data["STATION"] = STATION
        if TEST is not None:
            data["TEST"] = TEST


        # Guardar los cambios en el archivo JSON
        with open(archivo, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)

    @Slot()
    def Read_Json(self):
        """
        Metodo que obtiene los valores base de cada estacion. Se define los Puertos COM y direcciones IP.
        :return:
        """
        archivo = "./Data/data.json"
        with open(archivo, "r", encoding="utf-8") as f:
            data = json.load(f)

        # Asignar los valores a variables individuales
        COM = data["COM"]
        IP = data["IP"]
        STATION = data["STATION"]
        TEST = data["TEST"]

        # print(COM, IP, STATION, LABEL)
        return COM, IP, STATION, TEST
    def get_rs232_ports(self):
        """
        Obtiene la lista de puertos COM disponibles y filtra solo los dispositivos RS232 y conversores USB-Serial.
        :return: Lista de puertos COM RS232 disponibles.
        """
        rs232_ports = []
        ports = serial.tools.list_ports.comports()

        for port in ports:
            # Se agregan dispositivos USB-Serial como CH340, CP210x, FTDI, etc.
            if any(x in port.description.upper() for x in ["RS-232", "SERIAL", "UART", "USB"]):
                rs232_ports.append(port.device)

        return rs232_ports if rs232_ports else None
    def update_video(self):
        ret, frame = self.capture.read()
        if ret:
            # Convertir el frame a formato adecuado para QLabel
            frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            h, w, c = frame_rgb.shape
            q_image = np.array(frame_rgb)
            q_image = QImage(q_image.data, w, h, 3 * w, QImage.Format_RGB888)
            self.ui_main.lbl_video.setPixmap(QPixmap.fromImage(q_image))
        else:
            # Si el video llega al final, volver al primer fotograma
            self.capture.set(cv2.CAP_PROP_POS_FRAMES, 0)

    def closeEvent(self, event):
        self.capture.release()
        event.accept()

if __name__ == "__main__":
    app = QApplication([])
    window = Config()
    window.show()
    app.exec()