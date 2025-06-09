from PySide6.QtWidgets import QApplication, QMessageBox
from Animations_Functions.Animations import RightMenu_Control, MainMenu_Control
from main import *
def initSlot(self, ui_main):
    """
    Metodo que inicializa los Slots de la interfaz principal.
    :param self: instancia de la clase principal.
    :param ui_main: instancia de la clase Interfaz
    :return:
    """
    #Slots para animaciones de GUI
    ui_main.btn_latchMenu.released.connect(lambda:MainMenu_Control(ui_main))
    ui_main.btn_topconfig.released.connect(lambda: RightMenu_Control(ui_main))

    #Slots para interaccion con el toolBar
    ui_main.btn_minimize.released.connect(self.showMinimized)
    ui_main.btn_close.released.connect(QApplication.instance().quit)

    # Slots para mover de Stacked Widget
    ui_main.btn_home.released.connect(lambda: Home_Pressed(ui_main))
    ui_main.btn_reportes.released.connect(lambda: DMC_Pressed(ui_main))

    #Slots para Retornar a Home
    ui_main.btn_SaveSetup.released.connect(lambda: Save_Setup(ui_main))
    ui_main.btn_FinCal.released.connect(lambda: Ok_Calibrate(ui_main))

    # Slot para mostrar el Loggin
    ui_main.btn_config.released.connect(self.ShowLoggin)

    #Botonres de calibracion
    ui_main.btn_speed.released.connect(lambda: Send_Speed(self))
    ui_main.btn_stroke.released.connect(lambda: Send_Stroke(self))
    ui_main.btn_calibrate.released.connect(lambda: Send_Label_Calibrate(self))

    # Slot de testeo de Datos seriales
    ui_main.btn_rightConfig.released.connect(lambda : Test_Data(self))

def Home_Pressed(ui_main):
    """
    Metodo que Envia la interfaz a la pagina de Home
    :param ui_main: Instancia de la clase Interfaz
    :return:
    """
    ui_main.MenuPrincipal.setCurrentIndex(3)

def Modelos_Pressed(ui_main):
    """
    Metodo que Envia la interfaz a la pagina de Modelos
    :param ui_main: Instancia de la clase Interfaz
    :return:
    """
    ui_main.MenuPrincipal.setCurrentIndex(3)

def Historial_Pressed(ui_main):
    """
    Metodo que Envia la interfaz a la pagina de Historial
    :param ui_main: Instancia de la clase Interfaz
    :return:
    """
    ui_main.MenuPrincipal.setCurrentIndex(3)

def DMC_Pressed(ui_main):
    """
    Metodo que Envia la interfaz a la pagina de Data_Matrix
    :param ui_main: Instancia de la clase Interfaz
    :return:
    """
    ui_main.MenuPrincipal.setCurrentIndex(4)

def Save_Setup(ui_main):
    """
    Metodo que envia la interfaz a home desde la pagina de Configuracion.
    :param ui_main: Instancia de la clase Interfaz
    :return:
    """
    QMessageBox.information(None, "Datos Guardados", "Datos Guardados Correctamente")
    ui_main.MenuPrincipal.setCurrentIndex(3)

def Ok_Calibrate(ui_main):
    """
    Metodo que envia la interfaz a home desde la pagina de Configuracion de Impresora.
    :param ui_main: Instancia de la clase Interfaz
    :return:
    """
    QMessageBox.information(None, "Impresora Calibrada", "Impresora Calibrada Correctamente")
    ui_main.MenuPrincipal.setCurrentIndex(3)

def Send_Speed(self):
    """
    Metodo que envia a la impresora el comando de calibracion de Velocidad.
    :param self: Instancia de la clase Principal
    :return:
    """
    estacion = self.ui_main.Box_printerStation.currentText()
    estacion = int(estacion[-1:])

    match estacion:
        case 3:
            self.estacion_3.Printer.calibrate_speed()
        case 4:
            self.estacion_4.Printer.calibrate_speed()
        case 5:
            self.estacion_5.Printer.calibrate_speed()

def Send_Stroke(self):
    """
    Metodo que envia a la impresora el comando de calibracion de Intencidad.
    :param self: Instancia de la clase Principal
    :return:
    """
    estacion = self.ui_main.Box_printerStation.currentText()
    estacion = int(estacion[-1:])

    match estacion:
        case 3:
            self.estacion_3.Printer.calibrate_stroke()
        case 4:
            self.estacion_4.Printer.calibrate_stroke()
        case 5:
            self.estacion_5.Printer.calibrate_stroke()

def Send_Label_Calibrate(self):
    """
    Metodo que envia a la impresora el comando de calibracion de Etiqueta.
    :param self: Instancia de la clase Principal
    :return:
    """
    estacion = self.ui_main.Box_printerStation.currentText()
    estacion = int(estacion[-1:])

    match estacion:
        case 3:
            self.estacion_3.Printer.calibrate_label()
        case 4:
            self.estacion_4.Printer.calibrate_label()
        case 5:
            self.estacion_5.Printer.calibrate_label()

def Test_Data(self):
    """
    Metodo que Simula la recepcion de datos en el puerto COM de las estaciones activas.
    :param self: Instancia de la clase Principal
    :return:
    """

    # Cadena original
    data = """<01>:03/03/2025 22:04:48\n<01>:2.69 bar:(OK):4 Pa\n"""
    # Simular recepción como bytes
    simulated_received = data.encode("utf-8")  # Convierte la cadena a bytes
    # Simular procesamiento en el receptor
    decoded_data = simulated_received.decode("utf-8").strip()

    #self.estacion_3.on_data_received(self.estacion_3.comm, decoded_data)
    #self.estacion_4.on_data_received(self.estacion_4.comm, decoded_data)
    self.estacion_5.on_data_received(self.estacion_5.comm, decoded_data)