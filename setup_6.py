import json
import os
import sys
import serial.tools.list_ports
import cv2
import numpy as np
from PySide6.QtCore import QTimer, QCoreApplication, Slot
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
        #Renombrar los titulos
        self.ui_main.lbl_Station.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:700; color:#b4b4b4;\">WIFI</span></p></body></html>", None))
        self.ui_main.lbl_Label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:700; color:#b4b4b4;\">SERVER</span></p></body></html>", None))

        #Esconder ComboBox restante
        self.ui_main.lbl_COM.setVisible(False)
        self.ui_main.box_com.setVisible(False)

        # Actualiza items de combo Box DMC
        #self.ui_main.box_com.clear()
        #self.ui_main.box_com.addItems(["BAR CODE", "DMC"])

        # Actualizar items de combo Box WIFI
        self.ui_main.box_station.clear()
        self.ui_main.box_station.addItems(["HABILITADO", "DESHABILITADO"])

        # Actualizar items de combo Box SERVER
        self.ui_main.box_label.clear()
        self.ui_main.box_label.addItems(["HABILITADO", "DESHABILITADO"])

        # Recuperar datos de archivo Json
        try:
            wifi, server, Code = self.Read_Json()
            self.wifiControl = wifi == "1"
            self.Servercontrol = server == "1"
            self.CodeControl = Code == "1"

            if self.wifiControl:
                self.ui_main.box_station.setCurrentText("HABILITADO")
            else:
                self.ui_main.box_station.setCurrentText("DESHABILITADO")

            if self.CodeControl:
                self.ui_main.box_com.setCurrentText("DMC")
            else:
                self.ui_main.box_com.setCurrentText("BAR CODE")

            if self.Servercontrol:
                self.ui_main.box_label.setCurrentText("HABILITADO")
            else:
                self.ui_main.box_label.setCurrentText("DESHABILITADO")

        except Exception as e:
            #QMessageBox.critical(None, "Alerta de Registro", "No se encontro registro solicitado, ejecuta el setup!")
            print(e)
            pass

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

    def on_item_selected(self, index):
        print(index)
        """Se ejecuta al seleccionar un ítem del ComboBox."""
        selected_text = self.ui_main.box_station.currentText()

        if index == 1:
            self.ui_main.box_label.setCurrentText(selected_text)
            self.ui_main.box_label.setEnabled(False)
        else:
            self.ui_main.box_label.setEnabled(True)

        print(f"Ítem seleccionado: {selected_text}")
    def initSlots(self):
        self.ui_main.btn_aceptar.released.connect(self.OkSettings)
        self.ui_main.btn_cancelar.released.connect(lambda:sys.exit(0))

        # Conectar señal al método
        self.ui_main.box_station.currentIndexChanged.connect(self.on_item_selected)

    def OkSettings(self):
        WIFI = self.ui_main.box_station.currentText()
        SERVER = self.ui_main.box_label.currentText()
        CODE = self.ui_main.box_com.currentText()

        #print(station, com, label)
        if WIFI == "HABILITADO":
            nwifi = "1"
        else:
            nwifi = "0"

        if SERVER == "HABILITADO":
            nserver = "1"
        else:
            nserver = "0"

        if CODE == "DMC":
            ncode = "1"
        else:
            ncode = "0"

        self.Write_Json(nwifi,nserver,ncode)
        QMessageBox.information(self, "Guardado", "Datos Guardados con Exito!")
        sys.exit(0)

    def Write_Json(self, WIFI=None, SERVER=None, CODE=None):
        """
        Método que escribe los valores en el archivo JSON.
        Si el archivo no existe, lo crea con valores predeterminados.

        :param WIFI:
        :param SERVER:
        """
        archivo = "./Data/setup.json"

        # Valores predeterminados
        default_data = {
            "WIFI": "1",
            "SERVER": "1",
            "CODE": "0"
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
        if WIFI is not None:
            data["WIFI"] = WIFI
        if SERVER is not None:
            data["SERVER"] = SERVER
        if CODE is not None:
            data["CODE"] = CODE

        # Guardar los cambios en el archivo JSON
        with open(archivo, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)

    @Slot()
    def Read_Json(self):
        """
        Metodo que obtiene los valores base de cada estacion. Se define los Puertos COM y direcciones IP.
        :return:
        """
        archivo = "./Data/setup.json"
        with open(archivo, "r", encoding="utf-8") as f:
            data = json.load(f)

        # Asignar los valores a variables individuales
        WIFI = data["WIFI"]
        SERVER = data["SERVER"]
        CODE = data["CODE"]
        return WIFI, SERVER, CODE
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