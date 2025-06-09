import os
import random
import re
import sys


from PySide6.QtCore import Qt, QPropertyAnimation, QEasingCurve, QTimer, QObject, Signal, QCoreApplication, QThread, \
    QSize
from PySide6.QtWidgets import QMainWindow, QApplication, QWidget, QVBoxLayout, QDialog, QLineEdit, QMessageBox

import serial
import serial.tools.list_ports
from Interfaz.interfaz_gui import Ui_MainWindow as Interfaz
from Alerts_Functions.Alerts import *
from Animations_Functions.Animations import *
from Slots.Slots import *
from Printer_Functions.Zebra_Printer import *
from Interfaz.container_gui import Ui_Form as Container
from Server.ServerMonitor import *
from LAN.LAN_Connection import *
from Manager_DB.SQL import managerDataBase
from Loggin.Loggin_Class import *
from Interfaz.Setup_gui import Ui_Form as Setup
from Comm_Class.Com_Class import *
from API_Functions.request_API import *

class New_Station(QObject):
    def __init__(self, station, host, puertoCom, parent_widget=None, parent_setupWidget=None):
        # Llama al constructor de QObject
        super().__init__()
        self.Station = station
        self.host = host
        self.ui_main = parent_widget
        self.ui_setup = parent_setupWidget
        self.comm = puertoCom
        self.leak =""
        self.app_running = True
        self.server_running= False

        # variable que contiene el index de la etiqueta a usar
        self.label=0

        # Inicia la configuracion de la estacion
        self.init_Station()

    @Slot()
    def init_Station(self):
        """
        Metodo que inicializa la nueva estacion de trabajo.
        :return:
        """
        #Inicia el Template de la estacion
        self.init_Template()

        #Inicia el Widget Setup
        self.init_widget_Setup()

        # Iniciar el monitor de puerto COM
        self.serial_monitor = SerialMonitor(self.comm)
        self.serial_monitor.data_received.connect(self.on_data_received)
        self.serial_monitor.start()

        # Iniciar la Impresora
        self.Printer = ZebraPrinterThread(self.host)
        self.Printer.status_signal.connect(self.Printer_Status)
        self.Printer.error_signal.connect(self.show_error)
        self.Printer.start()

        # Crea el timer para alarmas
        self.Alerts = QTimer()

        # Oculta el label de alertas
        HideAlerts(self.container)

        # Inica DB
        self.DataBase = managerDataBase(self.Station)

        # Recupera el numero de parte en la base BackUp
        data = self.DataBase.GetDataBackUp()
        self.PartNumber = data[1]

        # Recupera el numero de Serie Actual por modelo
        SerialData = self.DataBase.GetSerialBackUp(self.PartNumber)
        self.SerialNum = SerialData[2]

        # Actualiza el label del contenedor de configuracion
        self.Setup_Container.lbl_PartNo.setText(QCoreApplication.translate("Form",
                                                                           f"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:700; color:#c8c8c8;\">{self.PartNumber}</span></p></body></html>",
                                                                           None))

        # Actualiza el label del contenedor principal
        self.container.lbl_part_num.setText(QCoreApplication.translate("Form",
                                                                       f"<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:700; color:#c8c8c8;\">{self.PartNumber}</span></p></body></html>",
                                                                       None))
        # Actualiza el Combo Box
        self.Setup_Container.Box_PartNo.setCurrentText(self.PartNumber)

        # Inicia los labels de la GUI
        self.init_Label(self.Station)

        # inicia el slot de Re-Impresion
        self.container.btn_RePrint.released.connect(self.rePrint)

        # Bandera de primer escaneo
        self.firstScan=1

    @Slot()
    def init_Template(self):
        """
        Metodo que inicializa el Template de Interfaz de cada estacion, ademas genera una instancia de la clase Container.
        :return:
        """
        if not self.ui_main:
            print("⚠ Error: No se proporcionó un widget padre válido.")
            return

            # Asegurar que el widget padre tiene un layout
        if self.ui_main.layout() is None:
            self.ui_main.setLayout(QVBoxLayout())

        layout = self.ui_main.layout()

        # Si ya se creó el widget, no lo duplicamos
        if not hasattr(self, "template"):
            # Instanciamos Container como un QWidget
            self.template = QWidget(self.ui_main)  # Se define como QWidget con parent
            self.container = Container()           # Instanciamos el Container
            self.container.setupUi(self.template)  # Cargamos la UI en el QWidget

            # Agregar el widget al layout
            layout.addWidget(self.template)
        else:
            print("⚠ El widget ya está agregado. No se duplicará.")

    @Slot(int)
    def init_Label(self, station):
        """
        Metodo que inicializa el label del titulo de cada estacion.
        :param station: int - Numero de estacion que se inicia
        :return:
        """
        self.container.lbl_titleStation.setText(QCoreApplication.translate("Form", f"<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:700; color:#c8c8c8;\">ESTACION {station}</span></p></body></html>", None))
        count = self.DataBase.count_records_today(self.DataBase.Device_Table, self.PartNumber, self.Station)
        self.container.lcd_display.display(count)

    @Slot()
    def init_widget_Setup(self):
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
            self.templateSetup = QWidget(self.ui_setup)       # Se define como QWidget con parent
            self.Setup_Container = Setup()                    # Instanciamos el Container
            self.Setup_Container.setupUi(self.templateSetup)  # Cargamos la UI en el QWidget

            # Agregar el widget al layout
            layout.addWidget(self.templateSetup)
        else:
            print("⚠ El widget ya está agregado. No se duplicará.")

        # Agrega los numero de parte al ComoBox
        self.Setup_Container.Box_PartNo.addItems(["5QM121251P", "5QM121251Q", "5QM121251R"])

        # Define los Slots a utilizar
        self.Setup_Container.btn_Save.released.connect(self.SetPart_Number)
        self.Setup_Container.btn_Cancel.released.connect(self.Hide_Buttom)
        self.Setup_Container.Box_PartNo.currentIndexChanged.connect(self.index_changed)

        # Guarda lso botones
        self.Setup_Container.btn_Save.hide()
        self.Setup_Container.btn_Cancel.hide()

    @Slot()
    def Hide_Buttom(self):
        """
        Metodo que esconde los botones de interaccion con el usuario de la instancia Setup-Container.
        :return:
        """
        # Guarda lso botones
        self.Setup_Container.btn_Save.hide()
        self.Setup_Container.btn_Cancel.hide()

    @Slot()
    def SetPart_Number(self):
        """
        Metodo que setea el numero de parte y actualiza los contenedores corresponndientes.
        :return:
        """
        # Asigana el modelo actual seleccionado en el combo-box
        partNo = self.Setup_Container.Box_PartNo.currentText()

        #Guarda el nuevo numero de parte a evaluar
        self.PartNumber = partNo

        # Bandera de primer escaneo al cambiar el numero de parte
        self.firstScan = 1

        # Actualiza el label del contenedor de configuracion
        self.Setup_Container.lbl_PartNo.setText(QCoreApplication.translate("Form", f"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:700; color:#c8c8c8;\">{partNo}</span></p></body></html>", None))

        # Actualiza el label del contenedor principal
        self.container.lbl_part_num.setText(QCoreApplication.translate("Form", f"<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:700; color:#c8c8c8;\">{partNo}</span></p></body></html>", None))

        # Guarda los datos actuales en la base de datos
        self.DataBase.updateData(self.PartNumber, self.SerialNum)

        # Recupera el numero de Serie Actual por modelo
        SerialData = self.DataBase.GetSerialBackUp(self.PartNumber)
        self.SerialNum = SerialData[2]


        # Actualiza el LCD
        count = self.DataBase.count_records_today(self.DataBase.Device_Table, self.PartNumber, self.Station)
        self.container.lcd_display.display(count)

        # Guarda los botones de Interaccion
        self.Setup_Container.btn_Save.hide()
        self.Setup_Container.btn_Cancel.hide()

    @Slot()
    def index_changed(self, index):
        """
        Método que se ejecuta cuando cambia el índice del ComboBox.
        :param index: int - Index Actual en el Combobox
        :return:
        """
        # muestra los botones de interaccion
        self.Setup_Container.btn_Save.show()
        self.Setup_Container.btn_Cancel.show()

    @Slot(str,int)
    def Printer_Status(self, message, code):
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
            label = self.container.lbl_PrintState

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
                f"""<html><head/><body><p align="center">
                               <span style="font-size:16pt; font-weight:700;">IMPRESORA:<br/></span>
                               <span style="font-size:16pt; font-weight:700; color:{text_color};">{display_text}</span>
                               </p></body></html>""",
                None
            ))

        # Evalua el estado de la impresora
        if code !=0:
            self.app_running=False
        else:
            self.app_running=True

    @Slot(str)
    def show_error(self, error_message):
        """
        Metodo que envia los errores a la Interfaz Principal.
        :param error_message: str
        :return:
        """
        print(f"Error: {error_message}")

    @Slot()
    def Ok_Piece(self):
        """
        Metodo para Aprovar una pieza OK, Imprime Etiqueta, Guarda datos en DB, manda datos al servidor y Actualiza los datos.
        :return:
        """
        #Reinicia bandera de primer scaneo
        self.firstScan = 0

        # Aqui hay que cambiar el vaor de fuga por la conversion de pascales a sccm
        self.leak = round(random.uniform(0.10, 0.20), 2)

        # Muestra label de Aprovado
        Approve(self.container)

        # Incrementa el numero de Serie
        self.SerialNum = self.SerialNum + 1

        # Evalua si el contador es > 46655
        if self.SerialNum > 46655:
            self.SerialNum = 1

        # Esconde el label de Aprovado
        self.Alerts.singleShot(1500, lambda: HideAlerts(self.container))

        # Envia datos al server si este se encuentra Activo
        if self.server_running==True:
            set_Register(self.Station, self.PartNumber, self.SerialNum, self.leak)

        # crea la fecha de la etiqueta
        self.date = datetime.datetime.now().strftime("%d%m%Y%H%M%S")

        # Envia datos a Imprimir
        self.Printer.Print_Request(self.PartNumber, self.SerialNum, self. Station, self.leak, self.date)

        # Agregar el modulo a la base de Datos
        self.DataBase.addModule("ZAR", self.Station, self.PartNumber, self.SerialNum, self.leak, 7172, 0,
                                self.DataBase.Device_Table)

        # Adquiere el valor actual de piezas registradas en la base de datos
        count = self.DataBase.count_records_today(self.DataBase.Device_Table, self.PartNumber, self.Station)

        # Actualiza el valor en el LCD
        self.container.lcd_display.display(count)

        # Actualiza el numero de serie correspondiente al numero de parte actual
        self.DataBase.updateTable_BackUp(self.PartNumber, self.SerialNum)

    @Slot(str, str)
    def on_data_received(self, port, data):
        """
        Metodo que recibe las datos del puerto serie de la ATEQ.
        :param port: str
        :param data: str
        :return:
        """
        #print(f"Dato recibido en {port}: {data}")

        # Define el patron a buscar en el array de datos
        pattern = r"<01>:(\d{2}/\d{2}/\d{4} \d{2}:\d{2}:\d{2})\r?\n<01>:\s*(\d+\.\d+)\s*bar:\((PB|OK)\):\s*(-?\d+)\s*Pa"

        match = re.search(pattern, data)

        if match:
            # Obtiene el valor de Fuga Registrado en la pieza
            self.leak = match.group(3)  # El valor después de 'bar:(PB):' o 'bar:(OK):'

            #Verifica si la App esta disponible
            if self.app_running == True:
                self.Ok_Piece()
            else:
                RejectPrint(self.container)
                self.Alerts.singleShot(1000, lambda: HideAlerts(self.container))

        else:
            pass
            #print("error en el mensaje")

    @Slot()
    def rePrint(self):
        """
        Metodo para imprimir la etiqueta actual.
        :return:
        """
        # Asegura que se pueda re-imprimir solo despues de una pieza ok
        if self.app_running == True and self.firstScan==0:
            # Envia la Re-impresion
            leak = " "
            ApproveReprint(self.container)  # Esconde el label de Aprovado
            self.Printer.Print_Request(self.PartNumber, self.SerialNum, self.Station, self.leak, self.date)

            self.Alerts.singleShot(1000, lambda: HideAlerts(self.container))
        else:
            RejectFirstScan(self.container) if self.firstScan == 1 else RejectPrint(self.container)
            self.Alerts.singleShot(1000, lambda: HideAlerts(self.container)) # Esconde el label de alerta

class Ateq(QMainWindow):
    def __init__(self):
        super().__init__()

        # Crea la instancia de la clase de la interfaz
        self.ui_main = Interfaz()
        self.ui_main.setupUi(self)

        # Configura la ventana principal
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.showFullScreen()

        # Inicializa los slots de la App
        initSlot(self, self.ui_main)

        # inicializa las animaciones de la App
        initAnimation(self.ui_main)

        # Manda la interfaz a la pagina principal
        self.ui_main.MenuPrincipal.setCurrentIndex(3)

        # Setup Inicial de la App
        # Inicia las Estaciones
        self.init_Station()

        # Inicia el Monitor del Servidor
        self.init_Server()

        # Inicia el Monitor de la conexion LAN
        self.init_LanConnection()

        # Inicia la Interfaz Principal
        self.initGui()

    @Slot()
    def initGui(self):
        """
        Metodo que inicializa la GUI Principal
        :return:
        """
        # Envia a la hoja principal la interfaz
        self.ui_main.MenuPrincipal.setCurrentIndex(3)

        # Esconde y deshabilita los botones que no se usaran
        self.ui_main.btn_modelos.setEnabled(False)
        self.ui_main.btn_modelos.setVisible(False)
        self.ui_main.btn_historial.setEnabled(False)
        self.ui_main.btn_historial.setVisible(False)

        # Esconde el boton para realizar pruebas de envio de datos
        self.ui_main.btn_rightConfig.setEnabled(False)
        self.ui_main.btn_rightConfig.setVisible(False)

        # Evalua el registro para habilitar el testeo
        setup = self.TEST == "1"

        if setup == True:
            # Muestra el boton para realizar pruebas de envio de datos
            self.ui_main.btn_rightConfig.setEnabled(True)
            self.ui_main.btn_rightConfig.setVisible(True)

        if self.check_station(self.estacion_3, "estacion_3") == False:
            self.ui_main.Mesa1_Widget.setEnabled(False)
            self.ui_main.Mesa1_Widget.setVisible(False)

        if self.check_station(self.estacion_4, "estacion_4") == False:
            self.ui_main.Mesa2_Widget.setEnabled(False)
            self.ui_main.Mesa2_Widget.setVisible(False)

        if self.check_station(self.estacion_5, "estacion_5") == False:
            self.ui_main.Mesa3_Widget.setEnabled(False)
            self.ui_main.Mesa3_Widget.setVisible(False)

    @Slot()
    def init_Station(self):
        """
        Metodo que crea las instancias de las estaciones que estaran activas.
        :return:
        """
        # crea las instancias en None
        self.estacion_3 = None
        self.estacion_4 = None
        self.estacion_5 = None

        #Carga los valores desde el archivo Json
        try:
            self.COM, self.IP, self.station_available, self.TEST = self.Read_Json()
        except Exception as e:
            QMessageBox.critical(self, "Alerta de Registro", "No se encontro registro solicitado!")
            archivo = "./Data/data.json"
            if os.path.exists(archivo):
                os.remove(archivo)
                print(f"{archivo} ha sido eliminado")

            else:
                print(f"{archivo} no se encontró")
            self.close()

        try:
            #Verifica si existe el puerto COM
            available_ports = self.get_rs232_ports()

            if available_ports:
                if self.station_available == "3":
                    self.estacion_3 = New_Station(3, self.IP, self.COM, self.ui_main.Mesa1_Widget,
                                                  self.ui_main.widget_setup_M1)
                    self.estacion_3.label = int(3)

                if self.station_available == "4":
                    self.estacion_4 = New_Station(4, self.IP, self.COM, self.ui_main.Mesa2_Widget,
                                                  self.ui_main.widget_setup_M2)
                    self.estacion_4.label = int(4)

                if self.station_available == "5":
                    self.estacion_5 = New_Station(5, self.IP, self.COM, self.ui_main.Mesa3_Widget,
                                                  self.ui_main.widget_setup_M3)
                    self.estacion_5.label = int(5)

            else:
                QMessageBox.critical(None, "Puerto COM", f"No se encontro Puerto COM Disponible\nVerificar conexion fisica.")
                sys.exit(0)


        except Exception as e:
            QMessageBox.critical(None, "Puerto COM",
                                 f"No se encontro Puerto COM Disponible.\nVerificar conexion fisica.")
            sys.exit(0)

    @Slot()
    def check_station(self, station, name):
        return hasattr(self, f"{name}") and station is not None

    @Slot()
    def init_Server(self):
        """
        Metodo que crea la Instancia de la Clase ConnectionMonitor que verifica  la conexion con el servidor.
        :return:
        """
        #Inicia el Monitor del Servidor
        self.ServerMonitor = ConnectionMonitor()
        self.ServerMonitor.connection_status_changed.connect(self.Update_ServerLabel)
        self.ServerMonitor.start()

    @Slot()
    def init_LanConnection(self):
        """
        Metodo que crea la instancia de la Clase LAN_Connection que monitorear la conexion WIFI.
        :return:
        """
        # Define variables para conexion de red
        self.ssid = "ADMINISTRATIVOS"  # SSID
        self.password = "M3X1C086"  # Password

        # Instancia de la Clase de Red Wifi
        self.WIFI = WifiMonitor(self.ssid, self.password)
        self.WIFI.connection_status_changed.connect(self.Update_WifiLabel)

    @Slot(bool)
    def Update_ServerLabel(self, status):
        """
        Metodo que actiualiza el label del servidor y las variables en las estaciones activas.
        :param status: bool
        :return:
        """

        if status:
            if self.check_station(self.estacion_3, "estacion_3")==True:
                self.estacion_3.server_running = True

            if self.check_station(self.estacion_4, "estacion_4")==True:
                self.estacion_4.server_running = True

            if self.check_station(self.estacion_5, "estacion_5")==True:
                self.estacion_5.server_running = True


            self.ui_main.lbl_Server_state.setStyleSheet(u"QLabel {\n"
                                                       "    border: 2px solid #00aa00;\n"
                                                       "	border-color: #00aa00;\n"
                                                       "	border-radius:5px;\n"
                                                       "}")
            self.ui_main.lbl_Server_state.setText(QCoreApplication.translate("MainWindow",
                                                                     u"<html><head/><body><p><span style=\" font-size:16pt; font-weight:700; color:#c8c8c8;\">SERVIDOR: </span><span style=\" font-size:16pt; font-weight:700; color:#00aa00;\"> CONECTADO  </span></p></body></html>",
                                                                     None))


        else:
            if self.check_station(self.estacion_3, "estacion_3") == True:
                self.estacion_3.server_running = False

            if self.check_station(self.estacion_4, "estacion_4") == True:
                self.estacion_4.server_running = False

            if self.check_station(self.estacion_5, "estacion_5") == True:
                self.estacion_5.server_running = False

            self.ui_main.lbl_Server_state.setStyleSheet(u"QLabel {\n"
                                                       "    border: 2px solid #FF0000;\n"
                                                       "	border-color: #FF0000;\n"
                                                       "	border-radius:5px;\n"
                                                       "}")

            self.ui_main.lbl_Server_state.setText(QCoreApplication.translate("MainWindow",
                                                                             u"<html><head/><body><p><span style=\" font-size:16pt; font-weight:700; color:#c8c8c8;\">SERVIDOR: </span><span style=\" font-size:16pt; font-weight:700; color:#FF0000;\">DESCONECTADO</span></p></body></html>",
                                                                             None))

    @Slot(bool)
    def Update_WifiLabel(self, status):
        """
        Metodo que actualiza la etiqueta de estado con la información más reciente de la conexion WIFI.
        """
        if status == False:
            self.mStatus_Wifi = 0
            self.ui_main.lbl_Wifi_State.setStyleSheet(u"QLabel {\n"
                                                     "    border: 2px solid #FF0000; /* Cambia el color del borde a rojo */\n"
                                                     "	border-color: #FF0000;\n"
                                                     "	border-radius:5px;\n"
                                                     "}")

            self.ui_main.lbl_Wifi_State.setText(QCoreApplication.translate("MainWindow",
                                                                   u"<html><head/><body><p><span style=\" font-size:16pt; font-weight:700; color:#c8c8c8;\">WIFI: </span><span style=\" font-size:16pt; font-weight:700; color:#FF0000;\">DESCONECTADO</span></p></body></html>",
                                                                   None))

        else:
            self.mStatus_Wifi = 1
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
        loggin = Loggin()
        loggin.setModal(True)
        loggin.exec()
        self.Key = loggin.state

        if self.Key == 1:
            # Envia a la pagina de configuracion
            self.ui_main.MenuPrincipal.setCurrentIndex(5)

            # Configura la vista del contenedor de la estacion 3
            if self.check_station(self.estacion_3, "estacion_3")== True:
                self.estacion_3.Setup_Container.Box_PartNo.setCurrentText(self.estacion_3.PartNumber)
                self.estacion_3.Setup_Container.btn_Save.hide()
                self.estacion_3.Setup_Container.btn_Cancel.hide()

            # Configura la vista del contenedor de la estacion 4
            if self.check_station(self.estacion_4,"estacion_4")==True:
                self.estacion_4.Setup_Container.Box_PartNo.setCurrentText(self.estacion_4.PartNumber)
                self.estacion_4.Setup_Container.btn_Save.hide()
                self.estacion_4.Setup_Container.btn_Cancel.hide()

            # Configura la vista del contenedor de la estacion 5
            if self.check_station(self.estacion_5, "estacion_5")==True:
                self.estacion_5.Setup_Container.Box_PartNo.setCurrentText(self.estacion_5.PartNumber)
                self.estacion_5.Setup_Container.btn_Save.hide()
                self.estacion_5.Setup_Container.btn_Cancel.hide()

        if self.Key == 2:
            # Envia a la pagina de configuracion
            self.ui_main.MenuPrincipal.setCurrentIndex(1)

        else:
            self.Key = 0

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

        #print(COM, IP, STATION, LABEL)
        return COM, IP, STATION, TEST
    @Slot()
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

if __name__ == "__main__":
    app = QApplication([])
    window = Ateq()
    window.show()
    app.exec()