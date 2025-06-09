import datetime
import json
import os
import sys
import time
from PIL import Image
import io
import requests

from API_Functions.request_API import set_Register
from Loggin.Loggin_Class import *
from PySide6.QtCore import Slot, QCoreApplication, QTimer, QObject, QEvent, QPropertyAnimation, QEasingCurve
from PySide6.QtGui import QPixmap, Qt, QKeyEvent
from PySide6.QtWidgets import QMainWindow, QApplication, QMessageBox, QVBoxLayout, QWidget, QTableWidget, QHeaderView
from Interfaz.interfaz_gui import Ui_MainWindow as Interfaz
from LAN.LAN_Connection import WifiMonitor
from Manager_DB.SQL import managerDataBase
from Printer_Functions.Zebra_Printer import ZebraPrinterThread
from Server.ServerMonitor import ConnectionMonitor
from Interfaz.Setup_gui import Ui_Form as Setup
from Interfaz.Dialogo_ConfirmData_gui import Ui_Dialog as ConfirmData

class ConfirmData(QDialog, ConfirmData):
    def __init__(self, parent=None):
        super(ConfirmData, self).__init__(parent)
        self.setupUi(self)
        self.state=False

        # Elimina la barra de menú y el botón de cierre
        self.setWindowFlag(Qt.FramelessWindowHint)


        self.btn_Accept.released.connect(lambda:self.GetState(True))
        self.btn_Reject.released.connect(lambda:self.GetState(False))

        # Esconde los que no requerimos
        self.horizontalLayout_2.setEnabled(False)
        self.horizontalLayout_3.setEnabled(False)
        self.client.hide()
        self.lbl_client.hide()
        self.Proveddor.hide()
        self.lbl_Proveedor.hide()
        self.Cantidad.hide()
        self.lbl_Cantidad.hide()
    def SetData(self, partNo, Qty, Supplier, Serial, Ot, Client, Tittle="VERIFICACION DE DATOS"):
        self.lbl_PartNo.setText(QCoreApplication.translate("Dialog",
                                                           f"<html><head/><body><p><span style=\" font-size:16pt; font-weight:700; color:#ffc400;\">{partNo}</span></p></body></html>",
                                                           None))
        self.lbl_Cantidad.setText(QCoreApplication.translate("Dialog", f"<html><head/><body><p><span style=\" font-size:16pt; font-weight:700; color:#ffc400;\">{Qty}</span></p></body></html>", None))
        self.lbl_Proveedor.setText(QCoreApplication.translate("Dialog", f"<html><head/><body><p><span style=\" font-size:16pt; font-weight:700; color:#ffc400;\">{Supplier}</span></p></body></html>", None))
        self.lbl_Serial.setText(QCoreApplication.translate("Dialog", f"<html><head/><body><p><span style=\" font-size:16pt; font-weight:700; color:#ffc400;\">{Serial}</span></p></body></html>", None))
        self.lbl_OT.setText(QCoreApplication.translate("Dialog", f"<html><head/><body><p><span style=\" font-size:16pt; font-weight:700; color:#ffc400;\">{Ot}</span></p></body></html>", None))
        self.lbl_client.setText(QCoreApplication.translate("Dialog",
                                                           f"<html><head/><body><p><span style=\" font-size:16pt; font-weight:700; color:#ffc400;\">{Client}</span></p></body></html>",
                                                           None))
        self.label.setText(QCoreApplication.translate("Dialog", f"<html><head/><body><p align=\"center\"><span style=\" font-size:22pt; font-weight:700; color:#ffffff;\">{Tittle}</span></p></body></html>", None))


    def GetState(self, respuesta):
        result = respuesta
        if result == True:
            self.state = True
            self.accept()

        else:
            self.state = False
            self.reject()

class NoPasteFilter(QObject):
    def eventFilter(self, obj, event):
        if isinstance(event, QKeyEvent):
            # Bloquear Ctrl+V y Shift+Insert
            if event.key() == Qt.Key_V and event.modifiers() == Qt.ControlModifier:
                return True
            if event.key() == Qt.Key_Insert and event.modifiers() == Qt.ShiftModifier:
                return True
        elif event.type() == QEvent.ContextMenu:
            # Bloquear el menú contextual (clic derecho)
            return True
        return super().eventFilter(obj, event)
class Label_Edit(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui_main = Interfaz()
        self.ui_main.setupUi(self)

        # Inicializa la Interfaz Grafica
        self.initGui()

        # Inicializamos el Monitoreo del Servidor
        self.init_Server()

        # inicializamos el Monitoreo de la conexion WIFI
        self.init_LanConnection()

        # Inicializa el Monitoreo de la impresora
        self.init_Printer()

        # Inicializa la base de datos
        self.init_DataBase()

        # Inicializa los slots
        self.initSlot()

    @Slot()
    def initGui(self):
        #Envia la GUI a la pagina principal
        self.ui_main.MenuPrincipal.setCurrentIndex(6)

        # Configura la ventana principal
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.showFullScreen()

        # Iniciar variables de sistema
        self.PartNo = "5QM121251R"
        self.Station = 6
        self.state = 0
        self.CodeRadd = ""
        self.host = "192.168.1.22"
        self.app_running = False
        self.server_status = 0
        self.Wifi_status = 0
        self.firstScan = 1
        self.retries=0
        self.Key=0

        # Recuperar datos de archivo Json
        try:
            wifi, server, Code = self.Read_Json()
            self.wifiControl = wifi == "1"
            self.Servercontrol = server == "1"
            self.CodeControl = Code == "1"

        except Exception as e:
            QMessageBox.critical(self, "Alerta de Registro", "No se encontro registro solicitado, ejecuta el setup!")

            # Si el archivo esta roto se procede a eliminarlo
            archivo = "./Data/setup.json"
            if os.path.exists(archivo):
                os.remove(archivo)
                print(f"{archivo} ha sido eliminado")

            else:
                print(f"{archivo} no se encontró")
            sys.exit(0)


        # Actualizar label de UI
        self.ui_main.label_6.setText(QCoreApplication.translate("MainWindow",
                                                                u"<html><head/><body><p align=\"center\"><span style=\" font-size:20pt; font-weight:700; color:#c8c8c8;\">ESCANEAR ETIQUETA CON </span><span style=\" font-size:20pt; font-weight:700; color:#0055ff;\">INDICE R</span><span style=\" font-size:20pt; font-weight:700; color:#c8c8c8;\">:</span></p></body></html>",
                                                                None))
        self.ui_main.lbl_subtitulo.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:700; color:#0055ff;\">PUEBLA</span></p></body></html>", None))


        # Crea el timer del proceso de lectura
        self.timerProcess = QTimer(self)
        self.timerProcess.timeout.connect(self._run_process)
        self.timerProcess.start(450)

        # configura la GUI
        self.ui_main.lbl_oldPza.setVisible(False)
        self.ui_main.lbl_arrowDown.setVisible(False)
        self.ui_main.lbl_newPza.setVisible(False)
        self.ui_main.lbl_tittle_3.setVisible(False)
        self.ui_main.btn_modelos.setVisible(False)
        #self.ui_main.btn_historial.setVisible(False)
        self.ui_main.btn_topconfig.setVisible(False)
        self.ui_main.btn_reportes.setVisible(False)
        self.ui_main.btn_EditAction.setVisible(False)

        # Esconde las barras de dezplazamiento del Text Edit
        self.ui_main.line_CurrLabel.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        # Establece el bloqueo de Copy & Page en el line Edit
        self.filter = NoPasteFilter(self)
        self.ui_main.line_CurrLabel.installEventFilter(self.filter)

        # Crea el timer para las Alarmas
        self.Alerts = QTimer()

        #Crea el contenedor de la clase setup para la configuracion de Interfaz
        self.ui_setup = self.ui_main.widget_setup_E6

        # Crea la tabla de piezas reemplazadas
        self._create_Table()

        # Inicializa el contenedor
        self._init_widgetSetup()

        # Inicializa las animaciones
        self.init_Animations()

    @Slot()
    def initSlot(self):
        # Slot para mostrar el Loggin
        self.ui_main.btn_config.released.connect(self.ShowLoggin)
        self.ui_main.btn_SaveSetup_2.released.connect(self._saveData)

        # Slots para interaccion con el toolBar
        self.ui_main.btn_minimize.released.connect(self.showMinimized)
        self.ui_main.btn_close.released.connect(QApplication.instance().quit)
        self.ui_main.btn_maximize.released.connect(self._RestoreWindow)
        self.ui_main.btn_home.released.connect(self.Home_Pressed)
        self.ui_main.btn_reportes.released.connect(lambda : self.ui_main.MenuPrincipal.setCurrentIndex(4))
        self.ui_main.btn_historial.released.connect(self.HistorialPressed)
        self.ui_main.line_CurrLabel.textChanged.connect(self.on_text_changed)
        self.tableWidgetdataBase.cellClicked.connect(self._RePrint)
        self.ui_main.btn_PrintAction.released.connect(lambda : self.ui_main.MenuPrincipal.setCurrentIndex(2))
    @Slot()
    def init_Animations(self):
        # Configuración de la animación menu principal
        self.ui_main.animation = QPropertyAnimation(self.ui_main.Left_Menu, b'minimumWidth')
        self.ui_main.animation.setDuration(1000)
        self.ui_main.animation.setEasingCurve(QEasingCurve.OutCirc)  # Cambia la curva de aceleración aquí

        self.ui_main.btn_latchMenu.setChecked(True)
        timer = QTimer()
        timer.singleShot(1000, lambda: self._control_LeftMenu())
        self.ui_main.btn_latchMenu.setEnabled(False)

    @Slot()
    def init_Printer(self):
        # Iniciar la Impresora
        self.Printer = ZebraPrinterThread(self.host)
        self.Printer.status_signal.connect(self._printer_Status)
        self.Printer.error_signal.connect(self.show_error)
        self.Printer.start()

    @Slot()
    def init_DataBase(self):
        # Inica DB
        self.DataBase = managerDataBase(self.Station)

    @Slot()
    def init_LanConnection(self):
        """
        Metodo que crea la instancia de la Clase LAN_Connection que monitorear la conexion WIFI.
        :return:
        """
        # Define variables para conexion de red
        self.ssid = "ADMINISTRATIVOS"  # SSID
        self.password = "M3X1C086"  # Password

        #self.ssid = "FAMILIA ORTIZ"    # SSID
        #self.password = "123OrtizFam"  # Password

        #self.ssid = "MEGACABLE-ADA2-5G"  # SSID
        #self.password = "qe3e6vBU"  # Password

        # Instancia de la Clase de Red Wifi
        self.WIFI = WifiMonitor(self.ssid, self.password)
        self.WIFI.connection_status_changed.connect(self._update_WifiLabel)

    @Slot()
    def init_Server(self):
        """
        Metodo que crea la Instancia de la Clase ConnectionMonitor que verifica  la conexion con el servidor.
        :return:
        """
        # Inicia el Monitor del Servidor
        self.ServerMonitor = ConnectionMonitor()
        self.ServerMonitor.connection_status_changed.connect(self._update_ServerLabel)
        self.ServerMonitor.start()
    @Slot()
    def _create_Table(self):
        # Crear la tabla sin especificar el número de filas y columnas
        self.tableWidgetdataBase = QTableWidget(0, 4, self.ui_main.DatabaseWidget)
        #self.tableWidgetdataBase.setStyleSheet(u"background-color: rgb(18, 118, 118);border: 2px transparent #000000;border-radius: 5px;")

        self.tableWidgetdataBase.setObjectName(u"tableWidget")
        self.tableWidgetdataBase.setHorizontalHeaderLabels(
            ['ID', 'FECHA DE CAMBIO', 'ETIQUETA ORIGINAL', 'ETIQUETA MODIFICADA'])
        self.tableWidgetdataBase.horizontalHeader().setStyleSheet("background-color: #A9A9A9; color: black")
        self.tableWidgetdataBase.setStyleSheet("color: black")

        # Ajustar el tamaño de las columnas para que se expandan automáticamente
        #self.tableWidgetdataBase.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        self.tableWidgetdataBase.setAlternatingRowColors(True)
        self.tableWidgetdataBase.setEditTriggers(QTableWidget.NoEditTriggers)
        self.tableWidgetdataBase.setSelectionBehavior(QTableWidget.SelectRows)
        self.tableWidgetdataBase.setSelectionMode(QTableWidget.SingleSelection)

        if self.ui_main.DatabaseWidget.layout() is not None:
            self.ui_main.DatabaseWidget.layout().addWidget(self.tableWidgetdataBase)
        else:
            # Puedes crear un nuevo QVBoxLayout si aún no hay un layout
            new_layout = QVBoxLayout()
            new_layout.addWidget(self.tableWidgetdataBase)
            self.ui_main.DatabaseWidget.setLayout(new_layout)
    @Slot()
    def _RePrint(self, row, column):
        row_data = []
        for col in range(self.tableWidgetdataBase.columnCount()):
            item = self.tableWidgetdataBase.item(row, col)
            if item is not None:
                row_data.append(item.text())
            else:
                row_data.append('')
        # print(f"Row {row} data: {row_data}")
        label_selected = row_data[3]

        partNo, serialNumber, station, year, month, day, format_date, leak_rate = self._extract_label_data(
            label_selected)
        SerialNumb = int(serialNumber, 36)
        serialNumber = str(serialNumber).zfill(5)

        fecha = datetime.datetime.strptime(format_date, "%d%m%Y%H%M%S")
        fecha_formateada = fecha.strftime("%d/%m/%Y %H:%M:%S")
        self.ConfirmPrint(partNo, 1, serialNumber, fecha_formateada, label_selected)
    @Slot()
    def ConfirmPrint(self, PartNo, Qty, Serial, date, DMC):
        ConfirmPrint = ConfirmData()
        ConfirmPrint.setModal(True)
        if self.Key == 2:
            ConfirmPrint.SetData(PartNo, Qty, "N/A", Serial, date, "N/A", "CONFIRMAR IMPRESION")
        else:
            ConfirmPrint.SetData(PartNo, Qty, "N/A", Serial, date, "N/A")

        ConfirmPrint.exec()
        result = ConfirmPrint.state

        if result == True:
            if self.Key == 2:
                print("Imprimiendo Etiqueta...")
                partNo, serialNumber, station, year, month, day, format_date, leak_rate = self._extract_label_data(
                    DMC)
                SerialNumb = int(serialNumber, 36)
                self.Printer.Print_Request(partNo, SerialNumb, station, leak_rate, format_date)
                QMessageBox.information(self, "Etiqueta Lista", "Etiqueta Impresa con Exito!")
                self.Key=0
                self.ui_main.MenuPrincipal.setCurrentIndex(6)
        else:
            print("Se Cancelo la operacion")
    @Slot()
    def Home_Pressed(self):
        self.Key = 0
        self.ui_main.MenuPrincipal.setCurrentIndex(6)

    @Slot()
    def HistorialPressed(self):
        self.ui_main.btn_printCurrIndex.hide()
        partNo =self.PartNo
        #self.tableWidgetdataBase.show()
        self.DataBase.InsertinTable(1, self.tableWidgetdataBase, 200, partNo)
        # Después de agregar los datos a la tabla, ajusta el ancho de las columnas al contenido máximo
        self.tableWidgetdataBase.resizeColumnsToContents()
        self.ui_main.MenuPrincipal.setCurrentIndex(2)
        self.Key = 0
    @Slot()
    def _control_LeftMenu(self):
        if self.ui_main.btn_latchMenu.isChecked():
            self.ui_main.animation.setStartValue(55)
            self.ui_main.animation.setEndValue(185)
        else:
            self.ui_main.animation.setStartValue(185)
            self.ui_main.animation.setEndValue(55)  # Ajusta el ancho según tus necesidades
        self.ui_main.animation.start()

    @Slot()
    def _run_process(self):
        """Manejo del proceso según el estado actual."""

        if self.ui_main.MenuPrincipal.currentIndex() != 6:
            return

        if not self._is_ready():
            #self._disable_input()
            self._handle_errors()
            return

        # Sistema listo, iniciar proceso
        self.retries = 0

        # Gestiona en el text edit el cursor
        self._enable_input()

        # Inicia la verificacion
        self.DMC_SCAN()

    @Slot()
    def on_text_changed(self):
        # Hanilita el Line Edit
        self._enable_input()

        # Obtiene los valores obtenidos del scaneo
        text = self.ui_main.line_CurrLabel.toPlainText()

        # Esperar a que el escáner termine de enviar (incluye \n o \r)
        if not text.endswith('\n') and not text.endswith('\r'):
            return

        # Limpiar texto de caracteres invisibles
        text = text.strip()
        print(text)

        # Verifica longitud y parte
        if len(text) == 55:
            if text[1:11] == self.PartNo:
                self.CodeRadd = text
                # Enviamos al siguiente estado del proceso
                self._set_state(1)
            else:
                QMessageBox.critical(self, "Número de Parte Inválido", f"Verificar Número de Parte: {text[1:11]}")
        else:
            print("Longitud incorrecta")

        # Limpia después de procesar
        self.ui_main.line_CurrLabel.clear()

    @Slot()
    def DMC_SCAN(self):
        match self.state:
            case 0:
                pass
            case 1:
                if self.DataBase.Check_label_Exist(self.DataBase.Device_Table, self.CodeRadd) != True:

                    # Actualiza la imagen de la etiqueta leida si esta disponible el internet.
                    if self.Wifi_status == 1:
                        # Actualiza la informacion en el DMC para la etiqueta
                        self._updateLabel_API_ZPL(self.CodeRadd, 1)

                    # Despues de generar la imagen de la etiqueta se procede a mostararla en la GUI
                    QTimer.singleShot(200, lambda: {self.ui_main.lbl_oldPza.setPixmap(QPixmap("./old_label.png"))})

                    # Enviamos al siguiente estado del proceso
                    self._set_state(2)
                else:
                    # Si la etiqueta ya ha sido leida por el sistema ignora la solicitud
                    self._show_error("Etiqueta Existente", "Esta Etiqueta ya ha realizado un proceso de Re-Etiquetado.")

                    # Limpia el contenedor del line edit
                    self.ui_main.line_CurrLabel.clear()

                    # Envia el sistema al estado inicial
                    self._set_state(0)
            case 2:
                """Agrega la modificacion en la base de datos y genera la nueva etiqueta."""

                # Obtiene los valores actuales de la Etiqueta
                partNo, serialNumber, station, year, month, day, format_date, leak_rate = self._extract_label_data(self.CodeRadd)

                # Convierte el serial en base 36
                _serial = int(serialNumber, 36)

                # Actualiza la linea de liberacion
                line = 6

                # Muestra los labels de etiqueta escaneada
                if self.Wifi_status == 1:
                    self.ui_main.lbl_oldPza.setVisible(True)
                    self.ui_main.lbl_arrowDown.setVisible(True)

                # Verifica la existencia del numero de parte escaneado con los disponibles en sistema
                if partNo in ["5QM121251R", "5QM121251P"]:
                    # Crea el numero de parte alterno al leido
                    new_partNo = "5QM121251P" if partNo == "5QM121251R" else "5QM121251R"

                    # Crea la fecha de la etiqueta
                    date = datetime.datetime.now().strftime("%d%m%Y%H%M%S")

                    # Crea el nuevo DMC de la etiqueta
                    new_label = self.Printer.createDMC(new_partNo, _serial, line, leak_rate, date)

                    # Verifica la conexion con el servidor
                    if self.server_status == 1 and self.Servercontrol == 1:
                        try:
                            # Envia al servidor el numero dado de baja en el servidor
                            set_Register(station, partNo, serialNumber, "0.00", 7172, 0)

                            # Envia al servidor el numero que sera dado de alta en eel servidor
                            set_Register(station, new_partNo, serialNumber, "0.00", 7172, line)

                        except Exception as e:
                            print("Error al enviar datos al servidor")
                            self._show_error("SERVIDOR", "Error al enviar los datos al servidor")

                    # Guarda en la base de datos la etiqueta leida y la etiqueta generada
                    self.DataBase.addlabel(self.DataBase.Device_Table, self.CodeRadd, new_label[0])

                    # Actualiza el label con la nueva etiqueta si esta disponible el internet.
                    if self.Wifi_status == 1:
                        self._updateLabel_API_ZPL(new_label[0], 2)

                    # Envia a imprimir la Etiqueta, en ndate esta la fecha y hora de la etiqueta escaneada solo que se manda en lugar del valor de fuga
                    self.Printer.Print_Request(new_partNo, _serial, line, leak_rate, date)

                    # Despues de generar la imagen de la etiqueta se procede a mostararla en la GUI y Envia el sistema al siguiente estado
                    QTimer.singleShot(200, lambda: (self.ui_main.lbl_newPza.setPixmap(QPixmap("./new_label.png"))))

                    # Envia al siguiente estado
                    self._set_state(3)

            case 3:
                """Muestra la nueva etiqueta y que el proceso ha terminado."""
                # Muestra la Etiqueta generada en la GUI si existe conexion wifi
                if self.Wifi_status == 1:
                    self.ui_main.lbl_newPza.setVisible(True)

                # Muestra mensaje de etiqueta impresa
                QMessageBox.information(self, "OK", "Etiqueta Impresa!\nRemplazar la etiqueta en el Radiador.")

                # Envia el sistema al siguiente estado
                self._set_state(4)

            case 4:
                """Estado final."""
                # Actualiza los labels d ela interfaz para poder reiniciar el proceso
                self.ui_main.lbl_newPza.setPixmap(QPixmap(u":/prefijoNuevo/icons/label_edit.png"))
                self.ui_main.lbl_oldPza.setPixmap(QPixmap(u":/prefijoNuevo/icons/label_edit.png"))
                self.ui_main.lbl_arrowDown.setVisible(False)
                self.ui_main.lbl_newPza.setVisible(False)
                self.ui_main.lbl_oldPza.setVisible(False)

                # Limpia el buffer del line edit
                self.ui_main.line_CurrLabel.clear()

                # Envia al estado inicial
                self._set_state(0)

    @Slot()
    def _reset_first_scan(self):
        self.firstScan = 0

    @Slot(int)
    def _set_state(self, new_state: int):
        """Cambia el estado y lo imprime para depuración."""
        self.state = new_state
        print(f"Nuevo estado: {new_state}")

    @Slot(str)
    def _extract_label_data(self, code: str):
        try:
            numero_parte = code[1:11]
            año = code[26]
            mes = code[27]
            dia = code[28]
            numero_serie = code[29:32]
            cabina = code[32]
            fecha_formateada = code[36:50]
            rate_fuga = float(code[51:].strip())
        except (IndexError, ValueError):
            numero_parte = año = mes = dia = numero_serie = cabina = fecha_formateada = rate_fuga = None

        return numero_parte, numero_serie, cabina, año, mes, dia, fecha_formateada, rate_fuga
    @Slot(str, str)
    def _show_error(self, title: str, message: str):
        """Muestra un mensaje de error y limpia la entrada."""
        print(f"Error: {message}")
        QMessageBox.critical(self, title, message)
        self.ui_main.line_CurrLabel.clear()

    @Slot()
    def _is_ready(self):
        """Verifica si la aplicación está lista para procesar la etiqueta."""
        _wifi = self.wifiControl
        _server = self.Servercontrol

        if _wifi and _server:
            return self.app_running and self.Wifi_status == 1 and self.server_status == 1
        elif _wifi:
            return self.app_running and self.Wifi_status == 1
        elif _server:
            return self.app_running and self.server_status == 1

        return self.app_running  # Si ninguno está activado, la app no está lista.

    @Slot()
    def _enable_input(self):
        """Habilita el campo de entrada y establece el foco."""
        self.ui_main.line_CurrLabel.setEnabled(True)
        self.ui_main.line_CurrLabel.setFocus()

    @Slot()
    def _disable_input(self):
        """Deshabilita el campo de entrada y lo limpia."""
        self.ui_main.line_CurrLabel.setEnabled(False)
        self.ui_main.line_CurrLabel.clear()

    @Slot(str)
    def _validate_label(self, text: str):
        """Valida el formato de la etiqueta."""
        if len(text) != 55:
            return False

        part_number = text[1:11]
        if part_number != self.PartNo:
            self._show_error("Número de Parte Inválido", f"Verificar Número de Parte: {part_number}")
            return False

        return True
    @Slot()
    def _handle_errors(self):
        """Maneja los mensajes de error dependiendo del estado de la aplicación."""
        if self.firstScan == 1:
            self.Alerts.singleShot(3000, lambda: self._reset_first_scan())

        elif not self.app_running:
            self._show_error("IMPRESORA", "Verificar el estado de la Impresora")

        elif self.Wifi_status == 0:
            self.retries += 1
            self._show_error("CONEXION", f"Verificar la conexión WIFI del equipo.\nIntentos: {self.retries}/5")

        elif self.server_status == 0:
            self.retries += 1
            self._show_error("SERVIDOR", f"Verificar el SERVIDOR\nIntentos: {self.retries}/5")


        if self.retries >4:
            self._show_error("CONEXION FALLIDA", "El dispositivo no logra establecer una conexion exitosa.\nEjecute el setup para deshabilitar el monitoreo.")
            sys.exit(0)

    @Slot(str, int)
    def _printer_Status(self, message: str, code: int):
        """
        Metodo para actualizar el label del estado de la impresora.
        :param message: str
        :param code:    int
        :return:
        """
        # Mapeo de colores y bordes según el estado
        state_styles = {
            0: ("#00aa00", "#00aa00", message),
            1: ("#ffc400", "#FF0000", message),
            2: ("#ffc400", "#FF0000", message),
            3: ("#ffc400", "#FF0000", message),
            4: ("#ffc400", "#FF0000", message),
            5: ("#FF0000", "#FF0000", "DESCONECTADA")
        }

        if code in state_styles:
            text_color, border_color, display_text = state_styles[code]

            # Obtener referencia al label
            label = self.ui_main.lbl_print_State_1

            # Aplicar estilo y texto
            label.setStyleSheet(f"""
                               QLabel {{
                                   color: rgb(200, 200, 200);
                                   border: 2px solid {border_color};
                                   border-color: {border_color};
                                   border-radius: 5px;
                               }}
                           """)

            label.setText(QCoreApplication.translate(
                "MainWindow",
                f"""<html><head/><body><p><span style=\" font-size:16pt; font-weight:700; color:#c8c8c8;\">IMPRESORA: </span><span style=\" font-size:16pt; font-weight:700; color:{text_color};\">{display_text}</span></p></body></html>""",
                None
            ))

        # Evalua el estado de la impresora
        if code != 0:
            self.app_running = False
        else:
            self.app_running = True

    @Slot(str)
    def show_error(self, error_message: str):
        """
        Metodo que envia los errores a la Interfaz Principal.
        :param error_message: str
        :return:
        """
        print(f"Error: {error_message}")

    @Slot(str, int)
    def _updateLabel_API_ZPL(self, code: str, label: int):
        # Obtiene los valores actuales de la Etiqueta
        partNo, serialNumber, station, year, month, day, format_date, leak_rate = self._extract_label_data(code)
        BGR = "X58"
        Supplier = "ZAR"
        levelChange = self.Printer.Get_levelChange(partNo)
        serial = int(serialNumber, 36)
        serial = str(serial).zfill(5)
        date = f"{code[36:38]}/{code[38:40]}/{code[42:44]}"

        mode43 = self.Printer.mod43_check_char(f"{BGR} {Supplier}{year}{month}{day}{serialNumber}{station}")
        aditional_data = f"{format_date} {leak_rate}"
        DMC = f"#{partNo}    ###*{BGR} {Supplier}{year}{month}{day}{serialNumber}{station}{mode43}*={aditional_data}"
        BGR_Final = f"{BGR} {Supplier}{year}{month}{day}{serialNumber}{station}{mode43}"

        command_last = f"""^XZ
        ^XA
        ^MMT
        ^PW599
        ^LL80
        ^LS0
        ^FT168,32^A0N,30,38^FH\^CI28^FD{partNo}^FS^CI27
        ^FO22,11^GFA,269,488,8,:Z64:eJyd0TEOgjAUBuBCE7rJwKITG6xGD4C34RiFuHIAnDiKL3oAjyCJBxDiwtD0+WgbIzDpW76k6f+a9yrRFMg/1Cw2KpZNHGZ2H6WxdcJhagHUN0PsRzl1K0jGWOgUpZWPAumRQ4xHz+Ze3OW4vbdy+t9SzhekkngRZo6ycyqrp0Ijt2o+GJVwhvTkz/tis0J3vvDR3GmTgNfzzboN1lxAG22rk59CK/b1ZpeTad0nZJBXURKCzrFBLUE/x49Y9n0D0QFG8g==:F85E
        ^FT89,73^BXN,2,200,32,32,1,_,1
        ^FH\^FD{DMC}^FS
        ^FT168,47^A0N,14,15^FH\^CI28^FDZAR^FS^CI27
        ^FT239,47^A0N,14,15^FH\^CI28^FD{levelChange}^FS^CI27
        ^FT168,60^A0N,14,15^FH\^CI28^FDRAD ASSY^FS^CI27
        ^FO521,8^GFA,401,512,8,:Z64:eJw9kcFtBCEMRf+IA7e4gWhdR6QRk5LmOJHQLqlgSwoVpISEEjgSCS35ZjcZAW/wt5D9Dfx/l9uEG6MYdYw2w02mMLgSZV4uTPC8Xyog38APEzdJaB04S1pqALrPS1WgGS3miis+2/n4q1SKp/LIaHyh2iu21TaWphmR7MYA17eCQN6MEf72UqHk1xvZIZ9Hg3Bd79TrQZGS7GdjkD1YL+RmjH7XPybqze+ShJRdsjSWdfg/Fu2uyOGKRm+s4ezz08pmg+TTihaDpEnV9HxCbKpYjfKBVbGZj4dgq96YtPqO6pMW1+lOluLaQmckL83luys+s6Rk7iC6hMJigwMKm9B34JV+SwZtgnU3t2OMZtmwFpsXtjHm/OQxz2WMPAdNv4BfaHyoLA==:26A2
        ^FT416,54^A0N,14,15^FH\^CI28^FDSN:^FS^CI27
        ^FT470,54^A0N,14,15^FH\^CI28^FD{serial}^FS^CI27
        ^FT416,21^A0N,14,15^FH\^CI28^FDDEVICE:^FS^CI27
        ^FT472,21^A0N,14,15^FH\^CI28^FD{station}^FS^CI27
        ^FT293,58^A0N,20,20^FH\^CI28^FDX58^FS^CI27
        ^FT416,70^A0N,14,15^FH\^CI28^FDDATE:^FS^CI27
        ^FT464,70^A0N,14,15^FH\^CI28^FD{date}^FS^CI27
        ^FT168,73^A0N,14,15^FH\^CI28^FDMADE IN MEXICO^FS^CI27
        ^PQ1,,,N
        ^XZ"""
        command = f"""^XA
        ^MMT
        ^PW599
        ^LL80
        ^LS0
        ^FT168,32^A0N,30,38^FH\^CI28^FD{partNo}^FS^CI27
        ^FO22,11^GFA,269,488,8,:Z64:eJyd0TEOgjAUBuBCE7rJwKITG6xGD4C34RiFuHIAnDiKL3oAjyCJBxDiwtD0+WgbIzDpW76k6f+a9yrRFMg/1Cw2KpZNHGZ2H6WxdcJhagHUN0PsRzl1K0jGWOgUpZWPAumRQ4xHz+Ze3OW4vbdy+t9SzhekkngRZo6ycyqrp0Ijt2o+GJVwhvTkz/tis0J3vvDR3GmTgNfzzboN1lxAG22rk59CK/b1ZpeTad0nZJBXURKCzrFBLUE/x49Y9n0D0QFG8g==:F85E
        ^FT89,73^BXN,2,200,32,32,1,_,1
        ^FH\^FD{DMC}^FS
        ^FT168,47^A0N,14,15^FH\^CI28^FDZAR^FS^CI27
        ^FT239,47^A0N,14,15^FH\^CI28^FD{levelChange}^FS^CI27
        ^FT168,60^A0N,14,15^FH\^CI28^FDRAD ASSY^FS^CI27
        ^FO521,8^GFA,401,512,8,:Z64:eJw9kcFtBCEMRf+IA7e4gWhdR6QRk5LmOJHQLqlgSwoVpISEEjgSCS35ZjcZAW/wt5D9Dfx/l9uEG6MYdYw2w02mMLgSZV4uTPC8Xyog38APEzdJaB04S1pqALrPS1WgGS3miis+2/n4q1SKp/LIaHyh2iu21TaWphmR7MYA17eCQN6MEf72UqHk1xvZIZ9Hg3Bd79TrQZGS7GdjkD1YL+RmjH7XPybqze+ShJRdsjSWdfg/Fu2uyOGKRm+s4ezz08pmg+TTihaDpEnV9HxCbKpYjfKBVbGZj4dgq96YtPqO6pMW1+lOluLaQmckL83luys+s6Rk7iC6hMJigwMKm9B34JV+SwZtgnU3t2OMZtmwFpsXtjHm/OQxz2WMPAdNv4BfaHyoLA==:26A2
        ^FT416,54^A0N,14,15^FH\^CI28^FDSN:^FS^CI27
        ^FT470,54^A0N,14,15^FH\^CI28^FD{serial}^FS^CI27
        ^FT472,21^A0N,14,15^FH\^CI28^FD{station}^FS^CI27
        ^FT249,60^A0N,14,15^FH\^CI28^FD{BGR_Final}^FS^CI27
        ^FT464,70^A0N,14,15^FH\^CI28^FD{date}^FS^CI27
        ^FT168,73^A0N,14,15^FH\^CI28^FDMADE IN MEXICO^FS^CI27
        ^FT416,70^A0N,14,15^FH\^CI28^FDDATE:^FS^CI27
        ^FT416,21^A0N,14,15^FH\^CI28^FDDEVICE:^FS^CI27
        ^PQ1,,,N
        ^XZ
        """

        if label == 1:
            self._convert_ZPL(command, "old_label.png")
        if label == 2:
            self._convert_ZPL(command, "new_label.png")

    @Slot(str, str)
    def _convert_ZPL(self, zpl_code: str, filename="old_label.png"):
        url = "http://api.labelary.com/v1/printers/8dpmm/labels/2.95276x0.390551/0/"
        headers = {"Accept": "image/png", "Content-Type": "application/x-www-form-urlencoded"}

        response = requests.post(url, headers=headers, data=zpl_code.encode('utf-8'))

        if response.status_code == 200:
            img = Image.open(io.BytesIO(response.content))
            img.save(filename)
            print(f"Etiqueta guardada como {filename}")
            return img
        else:
            print("Error al generar la imagen:", response.text)
            return None

    @Slot(bool)
    def _update_ServerLabel(self, status):
        """
        Metodo que actiualiza el label del servidor y las variables en las estaciones activas.
        :param status: bool
        :return:
        """

        if status:
            self.server_status = 1
            self.ui_main.lbl_Server_state.setStyleSheet(u"QLabel {\n"
                                                        "    border: 2px solid #00aa00;\n"
                                                        "	border-color: #00aa00;\n"
                                                        "	border-radius:5px;\n"
                                                        "}")
            self.ui_main.lbl_Server_state.setText(QCoreApplication.translate("MainWindow",
                                                                             u"<html><head/><body><p><span style=\" font-size:16pt; font-weight:700; color:#c8c8c8;\">SERVIDOR: </span><span style=\" font-size:16pt; font-weight:700; color:#00aa00;\"> CONECTADO  </span></p></body></html>",
                                                                             None))


        else:
            self.server_status = 0
            self.ui_main.lbl_Server_state.setStyleSheet(u"QLabel {\n"
                                                        "    border: 2px solid #FF0000;\n"
                                                        "	border-color: #FF0000;\n"
                                                        "	border-radius:5px;\n"
                                                        "}")

            self.ui_main.lbl_Server_state.setText(QCoreApplication.translate("MainWindow",
                                                                             u"<html><head/><body><p><span style=\" font-size:16pt; font-weight:700; color:#c8c8c8;\">SERVIDOR: </span><span style=\" font-size:16pt; font-weight:700; color:#FF0000;\">DESCONECTADO</span></p></body></html>",
                                                                             None))

    @Slot(bool)
    def _update_WifiLabel(self, status):
        """
        Metodo que actualiza la etiqueta de estado con la información más reciente de la conexion WIFI.
        """
        if status == False:
            self.Wifi_status = 0
            self.ui_main.lbl_Wifi_State.setStyleSheet(u"QLabel {\n"
                                                      "    border: 2px solid #FF0000; /* Cambia el color del borde a rojo */\n"
                                                      "	border-color: #FF0000;\n"
                                                      "	border-radius:5px;\n"
                                                      "}")

            self.ui_main.lbl_Wifi_State.setText(QCoreApplication.translate("MainWindow",
                                                                           u"<html><head/><body><p><span style=\" font-size:16pt; font-weight:700; color:#c8c8c8;\">WIFI: </span><span style=\" font-size:16pt; font-weight:700; color:#FF0000;\">DESCONECTADO</span></p></body></html>",
                                                                           None))

        else:
            self.Wifi_status = 1
            self.ui_main.lbl_Wifi_State.setStyleSheet(u"QLabel {\n"
                                                      "    border: 2px solid #FF0000;\n"
                                                      "	border-color: #00aa00;\n"
                                                      "	border-radius:5px;\n"
                                                      "}")

            self.ui_main.lbl_Wifi_State.setText(QCoreApplication.translate("MainWindow",
                                                                           u"<html><head/><body><p><span style=\" font-size:16pt; font-weight:700; color:#c8c8c8;\">WIFI: </span><span style=\" font-size:16pt; font-weight:700; color:#00aa00;\">CONECTADO</span></p></body></html>",
                                                                           None))

    @Slot()
    def ShowLoggin(self):
        """
        Metodo que muestra el Dialogo de Loggin para configurar la App.
        :return:
        """
        loggin = Loggin(self)
        loggin.setModal(True)
        loggin.exec()
        self.Key = loggin.state

        if self.Key == 1:

            # Actualiza el valor del box de numero de parte
            self.Setup_Container.Box_PartNo.setCurrentText(self.PartNo)

            # Actualiza el label del contenedor de configuracion
            self.Setup_Container.lbl_PartNo.setText(QCoreApplication.translate("Form",
                                                                               f"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:700; color:#c8c8c8;\">{self.PartNo}</span></p></body></html>",
                                                                               None))
            self._hide_buttom()
            # Envia a la pagina de configuracion
            self.ui_main.MenuPrincipal.setCurrentIndex(7)

        if self.Key == 2:
            # Esconde el boton de Imprimir (se dejo de usar)
            self.ui_main.btn_printCurrIndex.hide()

            # Adquiere el actual numero de parte
            partNo = self.PartNo

            # Muestra los ultimos 200 registros
            self.DataBase.InsertinTable(1, self.tableWidgetdataBase, 200, partNo)

            # Después de agregar los datos a la tabla, ajusta el ancho de las columnas al contenido máximo
            self.tableWidgetdataBase.resizeColumnsToContents()

            # Envia a la hoja de Historial
            self.ui_main.MenuPrincipal.setCurrentIndex(0)

        else:
            self.Key = 0

    @Slot()
    def _init_widgetSetup(self):
        """
        Metodo que inicia la instancia de la Clase Setup para los widget de configuracion.
        :return:
        """
        if not self.ui_setup:
            print("⚠ Error: No se proporcionó un widget padre válido.")
            return

            # Asegurar que el widget padre tiene un layout
        if self.ui_setup.layout() is None:
            self.ui_setup.setLayout(QVBoxLayout())

        layout = self.ui_setup.layout()

        # Si ya se creó el widget, no lo duplicamos
        if not hasattr(self, "template_Setup"):
            # Instanciamos Container como un QWidget
            self.templateSetup = QWidget(self.ui_setup)  # Se define como QWidget con parent
            self.Setup_Container = Setup()  # Instanciamos el Container
            self.Setup_Container.setupUi(self.templateSetup)  # Cargamos la UI en el QWidget

            # Agregar el widget al layout
            layout.addWidget(self.templateSetup)
        else:
            print("⚠ El widget ya está agregado. No se duplicará.")

        # Agrega los numero de parte al ComoBox
        self.Setup_Container.Box_PartNo.addItems(["5QM121251P", "5QM121251R"])

        # Define los Slots a utilizar
        self.Setup_Container.btn_Save.released.connect(self._setPart_Number)
        self.Setup_Container.btn_Cancel.released.connect(self._hide_buttom)
        self.Setup_Container.Box_PartNo.currentIndexChanged.connect(self._index_changed)

        # Guarda lso botones
        self.Setup_Container.btn_Save.hide()
        self.Setup_Container.btn_Cancel.hide()

    @Slot()
    def _index_changed(self, index):
        """
        Método que se ejecuta cuando cambia el índice del ComboBox.
        :param index: int - Index Actual en el Combobox
        :return:
        """
        # muestra los botones de interaccion
        self.Setup_Container.btn_Save.show()
        self.Setup_Container.btn_Cancel.show()

    @Slot()
    def _hide_buttom(self):
        """
        Metodo que esconde los botones de interaccion con el usuario de la instancia Setup-Container.
        :return:
        """
        # Guarda lso botones
        self.Setup_Container.btn_Save.hide()
        self.Setup_Container.btn_Cancel.hide()

    @Slot()
    def _setPart_Number(self):
        """
        Metodo que setea el numero de parte y actualiza los contenedores corresponndientes.
        :return:
        """
        # Asigana el modelo actual seleccionado en el combo-box
        partNo = self.Setup_Container.Box_PartNo.currentText()

        # Actualiza el label del contenedor de configuracion
        self.Setup_Container.lbl_PartNo.setText(QCoreApplication.translate("Form",
                                                                           f"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:700; color:#c8c8c8;\">{partNo}</span></p></body></html>",
                                                                           None))

        # Guarda los botones de Interaccion
        self.Setup_Container.btn_Save.hide()
        self.Setup_Container.btn_Cancel.hide()

    @Slot()
    def _saveData(self):
        # obtiene el numero de parte actual seleccionado
        partNo =  self.Setup_Container.Box_PartNo.currentText()

        # Guarda el nuevo numero de parte a evaluar
        self.PartNo = partNo

        if partNo == "5QM121251R":
            self.ui_main.label_6.setText(QCoreApplication.translate("MainWindow",
                                                            u"<html><head/><body><p align=\"center\"><span style=\" font-size:20pt; font-weight:700; color:#c8c8c8;\">ESCANEAR ETIQUETA CON </span><span style=\" font-size:20pt; font-weight:700; color:#0055ff;\">INDICE R</span><span style=\" font-size:20pt; font-weight:700; color:#c8c8c8;\">:</span></p></body></html>",
                                                            None))


        if partNo == "5QM121251P":
            self.ui_main.label_6.setText(QCoreApplication.translate("MainWindow",
                                                                    u"<html><head/><body><p align=\"center\"><span style=\" font-size:20pt; font-weight:700; color:#c8c8c8;\">ESCANEAR ETIQUETA CON </span><span style=\" font-size:20pt; font-weight:700; color:#0055ff;\">INDICE P</span><span style=\" font-size:20pt; font-weight:700; color:#c8c8c8;\">:</span></p></body></html>",
                                                                    None))
        self.ui_main.MenuPrincipal.setCurrentIndex(6)
        QMessageBox.information(self, "Datos Guardados", "Datos Guardados Correctamente")

    @Slot()
    def _RestoreWindow(self):
        if self.isMaximized():
            self.showNormal()
            self.ui_main.btn_maximize.setChecked(False)
        else:
            self.showMaximized()
            self.ui_main.btn_maximize.setChecked(True)

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

if __name__ == "__main__":
    app = QApplication([])
    window = Label_Edit()
    window.show()
    app.exec()