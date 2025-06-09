# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'interfaz.ui'
##
## Created by: Qt User Interface Compiler version 6.6.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QGridLayout,
    QHBoxLayout, QLabel, QLayout, QMainWindow,
    QPushButton, QSizePolicy, QSpacerItem, QStackedWidget,
    QTextEdit, QVBoxLayout, QWidget)
import resources_rc
import resources_rc
import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1024, 768)
        MainWindow.setMinimumSize(QSize(0, 0))
        MainWindow.setMaximumSize(QSize(1024, 768))
        MainWindow.setStyleSheet(u"/*Estilo para la ventana Principal*/\n"
"QMainWindow{\n"
"background-color: rgb(37, 41, 48);\n"
"}\n"
"\n"
"/*Estilo para los widgets*/\n"
"QWidget{\n"
"background-color: rgb(37, 41, 48);\n"
"}\n"
"\n"
"/*Estilo para los Frames*/\n"
"QFrame{\n"
"background-color: rgb(37, 41, 48);\n"
"}\n"
"\n"
"/*Estilo para los Botones*/\n"
"#Right_Menu QPushButton{\n"
"    background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 20px solid transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"	color: rgb(113, 126, 149);\n"
"}\n"
"\n"
"/*Estilo de botones del Menu Derecho - Show Menu*/\n"
"#btn_latchMenu.QPushButton{\n"
"background-image: url(:/prefijoNuevo/icons/icon_menu.png);\n"
"}\n"
"\n"
"/*Estilo de botones del Menu Izquierdo - Home*/\n"
"#btn_home.QPushButton{\n"
"background-image: url(:/prefijoNuevo/icons/cil-home.png);\n"
"}\n"
"\n"
"/*Estilo de botones del Menu Izquierdo - Modelos*/\n"
"#btn_modelos.QPushButton{\n"
"background-image: url(:/prefijoNuevo/i"
                        "cons/cil-loop-circular.png);\n"
"}\n"
"\n"
"/*Estilo de botones del Menu Izquierdo - Historial*/\n"
"#btn_historial.QPushButton{\n"
"  background-image: url(:/prefijoNuevo/icons/cil-file.png);\n"
"}\n"
"\n"
"/*Estilo de botones del Menu Izquierdo - Reportes*/\n"
"#btn_reportes.QPushButton{\n"
"background-image: url(:/prefijoNuevo/icons/cil-notes.png);\n"
"}\n"
"\n"
"/*Estilo de botones del Menu Izquierdo - Configuraciones*/\n"
"#btn_config.QPushButton{\n"
"background-image: url(:/prefijoNuevo/icons/icon_settings.png);\n"
"}\n"
"\n"
"/*Estilos para el Frame del logo y Titulo*/\n"
"#frame_titulo.QFrame{\n"
"background-color: rgb(33, 37, 43);\n"
"}\n"
"\n"
"/*Layout Frame Top Menu - Horizontal*/\n"
"#topMenu_FrameH.QFrame{\n"
"background-color: rgb(33, 37, 43);\n"
"}\n"
"\n"
"#verticalFrame.QFrame{\n"
"background-color: rgb(33, 37, 43);\n"
"}\n"
"\n"
"\n"
"/*Estilos para el Widget del menu Izquierdo*/\n"
"#Left_Menu.QWidget{\n"
"	background-color: rgb(33, 37, 43);\n"
"}\n"
"\n"
"/*Estilo para el Frame de Botones "
                        "de interaccion con la App*/\n"
"#appButtons_frame.QFrame{\n"
"background-color: rgb(33, 37, 43);\n"
"}\n"
"\n"
"/*Estilo del Menu Superior*/\n"
"#topControl_layout.QFrame{\n"
"	background-color: rgb(33, 37, 43);\n"
"}\n"
"\n"
"/*Estilo para el boton del menu superior - Cerrar*/\n"
"#btn_close.QPushButton{\n"
"	border: none;\n"
"	border-left: none;\n"
"	text-align: center;\n"
"	padding-left:0px;\n"
"	color: rgb(113, 126, 149);\n"
"	image: url(:/prefijoNuevo/icons/icon_close.png);\n"
"}\n"
"\n"
"/*Estilo para el boton del menu superior - Maximizar*/\n"
"#btn_maximize.QPushButton{\n"
"	border: none;\n"
"	border-left: none;\n"
"	text-align: center;\n"
"	padding-left:0px;\n"
"	color: rgb(113, 126, 149);\n"
"	image: url(:/prefijoNuevo/icons/icon_maximize.png);\n"
"}\n"
"\n"
"/*Estilo para el boton del menu superior - Minimizar*/\n"
"#btn_minimize.QPushButton{\n"
"	border: none;\n"
"	border-left: none;\n"
"	text-align: center;\n"
"	padding-left: 0px;\n"
"	color: rgb(113, 126, 149);\n"
"	image: url(:/prefijoNuevo/icon"
                        "s/icon_minimize.png);\n"
"}\n"
"\n"
"/*Estilo para el boton del menu superior - Configuracion*/\n"
"#btn_topconfig.QPushButton{\n"
"	border: none;\n"
"	border-left: none;\n"
"	text-align: center;\n"
"	padding-left: 0px;\n"
"	color: rgb(113, 126, 149);\n"
"	image: url(:/prefijoNuevo/icons/icon_settings.png);\n"
"	border-radius:2px;\n"
"}\n"
"\n"
"/*Estilo para el menu Lateral Derecho - Mensajes*/\n"
"#btn_rightConfig.QPushButton{\n"
"    border-left: -40px solid transparent;\n"
"    text-align: right;\n"
"    padding-left: 0px;\n"
"	padding-right:30px;\n"
"	image: url(:/prefijoNuevo/icons/cil-notes.png);\n"
"}\n"
"\n"
"/*Estilo para el menu Lateral Derecho - Data Base*/\n"
"#btn_rightDatabase.QPushButton{\n"
"    border-left: -40px solid transparent;\n"
"    text-align: right;\n"
"    padding-left: 0px;\n"
"	padding-right:30px;	\n"
"	image: url(:/prefijoNuevo/icons/cil-calendar-check.png);\n"
"}\n"
"\n"
"/*Estilo para el menu Lateral Derecho - LogOut*/\n"
"#btn_rightLogout.QPushButton{\n"
"    border-left: -40p"
                        "x solid transparent;\n"
"    text-align: right;\n"
"    padding-left: 0px;\n"
"	padding-right:30px;\n"
"	image: url(:/prefijoNuevo/icons/cil-account-logout.png);\n"
"}\n"
"\n"
"#Menus QPushButton {\n"
"    background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 20px solid transparent;\n"
"	/*background-color: rgb(37, 41, 48);*/\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"	color: rgb(113, 126, 149);\n"
"}\n"
"\n"
"/* Estilos para el bot\u00f3n cuando est\u00e1 checkeado */\n"
"QPushButton:checked {\n"
"   background-color: rgb(0, 85, 255);\n"
"}\n"
"\n"
"/* Estilos para el bot\u00f3n cuando no est\u00e1 checkeado */\n"
"QPushButton:!checked {\n"
"    background-color: rgb(33,37,43);\n"
"}\n"
"\n"
"/*Estilo general para la dinamica de botones*/\n"
"QPushButton:hover {\n"
"	background-color: rgb(0, 170, 255);\n"
"}\n"
"QPushButton:pressed {\n"
"	background-color: rgb(0, 85, 255);\n"
"}\n"
"\n"
" QMessageBox {\n"
"            background: white;  /* Fondo"
                        " blanco */\n"
"            border: 2px solid #CCCCCC;  /* Borde gris claro */\n"
"            border-radius: 10px;  /* Esquinas redondeadas */\n"
"            padding: 10px;\n"
"        }\n"
"\n"
"        QMessageBox QLabel {\n"
"            background: transparent;\n"
"            color: #333333;  /* Texto oscuro elegante */\n"
"            font-size: 14px;\n"
"            font-weight: bold;\n"
"        }\n"
"\n"
"        QMessageBox QLabel[objectName=\"qt_msgbox_label\"] {\n"
"            background: transparent;\n"
"        }\n"
"\n"
"        /* Botones con dise\u00f1o moderno */\n"
"        QMessageBox QPushButton {\n"
"            background-color: #0078D7;  /* Azul profesional (similar a Windows) */\n"
"            color: white;\n"
"            border: 1px solid #005A9E;\n"
"            padding: 8px 16px;\n"
"            font-size: 13px;\n"
"            font-weight: bold;\n"
"            border-radius: 5px;\n"
"            min-width: 80px;\n"
"        }\n"
"\n"
"        QMessageBox QPushButton:hover {\n"
""
                        "            background-color: #005A9E;\n"
"        }\n"
"\n"
"        QMessageBox QPushButton:pressed {\n"
"            background-color: #004680;\n"
"        }")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setMinimumSize(QSize(0, 0))
        self.centralwidget.setMaximumSize(QSize(1024, 768))
        self.centralwidget.setStyleSheet(u"")
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.MainLayout = QGridLayout()
        self.MainLayout.setObjectName(u"MainLayout")
        self.MainLayout.setHorizontalSpacing(0)
        self.Contenedor = QFrame(self.centralwidget)
        self.Contenedor.setObjectName(u"Contenedor")
        sizePolicy.setHeightForWidth(self.Contenedor.sizePolicy().hasHeightForWidth())
        self.Contenedor.setSizePolicy(sizePolicy)
        self.Contenedor.setMaximumSize(QSize(16777215, 16777215))
        self.Container_Layout = QVBoxLayout(self.Contenedor)
        self.Container_Layout.setSpacing(0)
        self.Container_Layout.setObjectName(u"Container_Layout")
        self.Container_Layout.setContentsMargins(5, 0, 0, 0)
        self.topMenu = QWidget(self.Contenedor)
        self.topMenu.setObjectName(u"topMenu")
        self.topMenu.setMinimumSize(QSize(0, 45))
        self.topMenu.setStyleSheet(u"")
        self.horizontalLayout_2 = QHBoxLayout(self.topMenu)
        self.horizontalLayout_2.setSpacing(8)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.topMenu_FrameH = QFrame(self.topMenu)
        self.topMenu_FrameH.setObjectName(u"topMenu_FrameH")
        self.topMenu_FrameH.setFrameShadow(QFrame.Shadow.Raised)
        self.topMenu_layoutH = QHBoxLayout(self.topMenu_FrameH)
        self.topMenu_layoutH.setSpacing(0)
        self.topMenu_layoutH.setObjectName(u"topMenu_layoutH")
        self.topMenu_layoutH.setContentsMargins(0, 5, 0, 0)
        self.topControl_layout = QFrame(self.topMenu_FrameH)
        self.topControl_layout.setObjectName(u"topControl_layout")
        sizePolicy.setHeightForWidth(self.topControl_layout.sizePolicy().hasHeightForWidth())
        self.topControl_layout.setSizePolicy(sizePolicy)
        self.topControl_layout.setMinimumSize(QSize(0, 10))
        self.topControl_layout.setFrameShape(QFrame.Shape.StyledPanel)
        self.topControl_layout.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.topControl_layout)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(2, 0, 0, 0)
        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_6)

        self.lbl_Server_state = QLabel(self.topControl_layout)
        self.lbl_Server_state.setObjectName(u"lbl_Server_state")
        self.lbl_Server_state.setStyleSheet(u"background-color: None;")

        self.horizontalLayout_3.addWidget(self.lbl_Server_state)

        self.horizontalSpacer = QSpacerItem(40, 0, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)

        self.lbl_Wifi_State = QLabel(self.topControl_layout)
        self.lbl_Wifi_State.setObjectName(u"lbl_Wifi_State")
        self.lbl_Wifi_State.setStyleSheet(u"background-color: None;")

        self.horizontalLayout_3.addWidget(self.lbl_Wifi_State)

        self.appButtons_frame = QFrame(self.topControl_layout)
        self.appButtons_frame.setObjectName(u"appButtons_frame")
        self.appButtons_layout = QHBoxLayout(self.appButtons_frame)
        self.appButtons_layout.setSpacing(10)
        self.appButtons_layout.setObjectName(u"appButtons_layout")
        self.appButtons_layout.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.appButtons_layout.addItem(self.horizontalSpacer_9)

        self.btn_topconfig = QPushButton(self.appButtons_frame)
        self.btn_topconfig.setObjectName(u"btn_topconfig")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.btn_topconfig.sizePolicy().hasHeightForWidth())
        self.btn_topconfig.setSizePolicy(sizePolicy1)
        self.btn_topconfig.setMinimumSize(QSize(0, 20))
        self.btn_topconfig.setCheckable(True)

        self.appButtons_layout.addWidget(self.btn_topconfig)

        self.btn_minimize = QPushButton(self.appButtons_frame)
        self.btn_minimize.setObjectName(u"btn_minimize")
        sizePolicy1.setHeightForWidth(self.btn_minimize.sizePolicy().hasHeightForWidth())
        self.btn_minimize.setSizePolicy(sizePolicy1)
        self.btn_minimize.setMinimumSize(QSize(0, 20))

        self.appButtons_layout.addWidget(self.btn_minimize)

        self.btn_maximize = QPushButton(self.appButtons_frame)
        self.btn_maximize.setObjectName(u"btn_maximize")
        sizePolicy1.setHeightForWidth(self.btn_maximize.sizePolicy().hasHeightForWidth())
        self.btn_maximize.setSizePolicy(sizePolicy1)
        self.btn_maximize.setMinimumSize(QSize(0, 20))
        self.btn_maximize.setCheckable(True)

        self.appButtons_layout.addWidget(self.btn_maximize)

        self.btn_close = QPushButton(self.appButtons_frame)
        self.btn_close.setObjectName(u"btn_close")
        sizePolicy1.setHeightForWidth(self.btn_close.sizePolicy().hasHeightForWidth())
        self.btn_close.setSizePolicy(sizePolicy1)
        self.btn_close.setMinimumSize(QSize(0, 20))

        self.appButtons_layout.addWidget(self.btn_close)


        self.horizontalLayout_3.addWidget(self.appButtons_frame)


        self.topMenu_layoutH.addWidget(self.topControl_layout)


        self.horizontalLayout_2.addWidget(self.topMenu_FrameH)


        self.Container_Layout.addWidget(self.topMenu)

        self.horizontalLayout_container = QHBoxLayout()
        self.horizontalLayout_container.setObjectName(u"horizontalLayout_container")
        self.Main_widgetContainer = QWidget(self.Contenedor)
        self.Main_widgetContainer.setObjectName(u"Main_widgetContainer")
        self.gridLayout_3 = QGridLayout(self.Main_widgetContainer)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setHorizontalSpacing(0)
        self.gridLayout_3.setVerticalSpacing(6)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.MenuPrincipal = QStackedWidget(self.Main_widgetContainer)
        self.MenuPrincipal.setObjectName(u"MenuPrincipal")
        sizePolicy.setHeightForWidth(self.MenuPrincipal.sizePolicy().hasHeightForWidth())
        self.MenuPrincipal.setSizePolicy(sizePolicy)
        self.MenuPrincipal.setMaximumSize(QSize(16777215, 16777215))
        self.MenuPrincipal.setStyleSheet(u"background-color: rgb(33, 37, 43);")
        self.MenuPrincipal.setFrameShape(QFrame.Shape.NoFrame)
        self.Edit_page = QWidget()
        self.Edit_page.setObjectName(u"Edit_page")
        self.verticalLayout_8 = QVBoxLayout(self.Edit_page)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.vertical_model = QVBoxLayout()
        self.vertical_model.setObjectName(u"vertical_model")
        self.titulo_modelo = QLabel(self.Edit_page)
        self.titulo_modelo.setObjectName(u"titulo_modelo")

        self.vertical_model.addWidget(self.titulo_modelo)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.vertical_model.addItem(self.verticalSpacer_3)

        self.horizontal_model = QHBoxLayout()
        self.horizontal_model.setObjectName(u"horizontal_model")
        self.btn_EditAction = QPushButton(self.Edit_page)
        self.btn_EditAction.setObjectName(u"btn_EditAction")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.btn_EditAction.sizePolicy().hasHeightForWidth())
        self.btn_EditAction.setSizePolicy(sizePolicy2)
        self.btn_EditAction.setMinimumSize(QSize(0, 100))
        self.btn_EditAction.setMaximumSize(QSize(250, 16777215))
        self.btn_EditAction.setStyleSheet(u"QPushButton{\n"
"background-color: rgba(0, 85, 255, 150);\n"
"font: 700 36pt \"Segoe UI\";\n"
"	color: rgba(255, 255, 255, 200);\n"
"border-radius: 10px;\n"
"border: 4px solid black;\n"
"border-color: rgb(0, 85, 255);}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(0, 0, 255);\n"
"	/*background-color: rgb(255, 233, 51 );*/\n"
"}")
        self.btn_EditAction.setIconSize(QSize(25, 25))

        self.horizontal_model.addWidget(self.btn_EditAction)

        self.btn_PrintAction = QPushButton(self.Edit_page)
        self.btn_PrintAction.setObjectName(u"btn_PrintAction")
        sizePolicy2.setHeightForWidth(self.btn_PrintAction.sizePolicy().hasHeightForWidth())
        self.btn_PrintAction.setSizePolicy(sizePolicy2)
        self.btn_PrintAction.setMinimumSize(QSize(0, 100))
        self.btn_PrintAction.setMaximumSize(QSize(250, 16777215))
        self.btn_PrintAction.setSizeIncrement(QSize(20, 25))
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        font.setPointSize(36)
        font.setBold(True)
        font.setItalic(False)
        self.btn_PrintAction.setFont(font)
        self.btn_PrintAction.setStyleSheet(u"QPushButton{\n"
"background-color: rgba(0, 85, 255, 150);\n"
"font: 700 36pt \"Segoe UI\";\n"
"	color: rgba(255, 255, 255, 200);\n"
"border-radius: 10px;\n"
"padding-left:7px;\n"
"border: 4px solid black;\n"
"border-color: rgb(0, 85, 255);}\n"
"\n"
"QPushButton:pressed {\n"
"	/*background-color: rgb(255, 233, 51 );*/\n"
"    background-color: rgb(0, 0, 255);\n"
"}")

        self.horizontal_model.addWidget(self.btn_PrintAction)


        self.vertical_model.addLayout(self.horizontal_model)


        self.verticalLayout_8.addLayout(self.vertical_model)

        self.spacer_model = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_8.addItem(self.spacer_model)

        self.MenuPrincipal.addWidget(self.Edit_page)
        self.Printer_page = QWidget()
        self.Printer_page.setObjectName(u"Printer_page")
        sizePolicy.setHeightForWidth(self.Printer_page.sizePolicy().hasHeightForWidth())
        self.Printer_page.setSizePolicy(sizePolicy)
        self.Printer_page.setMaximumSize(QSize(16777215, 16777215))
        self.verticalLayout_17 = QVBoxLayout(self.Printer_page)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalLayout_35 = QVBoxLayout()
        self.verticalLayout_35.setObjectName(u"verticalLayout_35")
        self.label_7 = QLabel(self.Printer_page)
        self.label_7.setObjectName(u"label_7")

        self.verticalLayout_35.addWidget(self.label_7)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalSpacer_14 = QSpacerItem(40, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_11.addItem(self.horizontalSpacer_14)

        self.label_3 = QLabel(self.Printer_page)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_11.addWidget(self.label_3)

        self.Box_printerStation = QComboBox(self.Printer_page)
        self.Box_printerStation.addItem("")
        self.Box_printerStation.addItem("")
        self.Box_printerStation.addItem("")
        self.Box_printerStation.setObjectName(u"Box_printerStation")
        self.Box_printerStation.setStyleSheet(u"font: 700 26pt \"Segoe UI\";\n"
"color: rgb(200, 200, 200);")
        self.Box_printerStation.setEditable(False)

        self.horizontalLayout_11.addWidget(self.Box_printerStation)

        self.horizontalSpacer_15 = QSpacerItem(40, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_11.addItem(self.horizontalSpacer_15)


        self.verticalLayout_35.addLayout(self.horizontalLayout_11)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_35.addItem(self.verticalSpacer_5)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.btn_speed = QPushButton(self.Printer_page)
        self.btn_speed.setObjectName(u"btn_speed")
        self.btn_speed.setMaximumSize(QSize(300, 16777215))
        self.btn_speed.setStyleSheet(u"QPushButton{\n"
"background-color: rgba(0, 85, 255, 150);\n"
"font: 700 36pt \"Segoe UI\";\n"
"	color: rgba(255, 255, 255, 200);\n"
"border-radius: 10px;\n"
"padding-left:7px;\n"
"border: 4px solid black;\n"
"border-color: rgb(0, 85, 255);}\n"
"\n"
"QPushButton:pressed {\n"
"	/*background-color: rgb(255, 233, 51 );*/\n"
"    background-color: rgb(0, 0, 255);\n"
"}")

        self.horizontalLayout_4.addWidget(self.btn_speed)

        self.btn_stroke = QPushButton(self.Printer_page)
        self.btn_stroke.setObjectName(u"btn_stroke")
        self.btn_stroke.setMaximumSize(QSize(300, 16777215))
        self.btn_stroke.setStyleSheet(u"QPushButton{\n"
"background-color: rgba(0, 85, 255, 150);\n"
"font: 700 36pt \"Segoe UI\";\n"
"	color: rgba(255, 255, 255, 200);\n"
"border-radius: 10px;\n"
"padding-left:7px;\n"
"border: 4px solid black;\n"
"border-color: rgb(0, 85, 255);}\n"
"\n"
"QPushButton:pressed {\n"
"	/*background-color: rgb(255, 233, 51 );*/\n"
"    background-color: rgb(0, 0, 255);\n"
"}")

        self.horizontalLayout_4.addWidget(self.btn_stroke)

        self.btn_calibrate = QPushButton(self.Printer_page)
        self.btn_calibrate.setObjectName(u"btn_calibrate")
        self.btn_calibrate.setMaximumSize(QSize(300, 16777215))
        self.btn_calibrate.setStyleSheet(u"QPushButton{\n"
"background-color: rgba(0, 85, 255, 150);\n"
"font: 700 36pt \"Segoe UI\";\n"
"	color: rgba(255, 255, 255, 200);\n"
"border-radius: 10px;\n"
"padding-left:7px;\n"
"border: 4px solid black;\n"
"border-color: rgb(0, 85, 255);}\n"
"\n"
"QPushButton:pressed {\n"
"	/*background-color: rgb(255, 233, 51 );*/\n"
"    background-color: rgb(0, 0, 255);\n"
"}")

        self.horizontalLayout_4.addWidget(self.btn_calibrate)


        self.verticalLayout_35.addLayout(self.horizontalLayout_4)


        self.verticalLayout_17.addLayout(self.verticalLayout_35)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_17.addItem(self.verticalSpacer_4)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(-1, -1, -1, 10)
        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_4)

        self.btn_FinCal = QPushButton(self.Printer_page)
        self.btn_FinCal.setObjectName(u"btn_FinCal")
        self.btn_FinCal.setMaximumSize(QSize(500, 16777215))
        self.btn_FinCal.setStyleSheet(u"QPushButton{\n"
"background-color: rgba(235, 211, 26,110);\n"
"font: 700 28pt \"Segoe UI\";\n"
"color: rgba(255, 255, 255, 200);\n"
"border-radius: 5px;\n"
"padding:7px;\n"
"border: 4px solid black;\n"
"border-color: rgb(235, 211, 26);}\n"
"\n"
"QPushButton:pressed {\n"
"	/*background-color: rgb(255, 233, 51 );*/\n"
"    background-color: rgb(235, 211, 26);\n"
"}\n"
"")

        self.horizontalLayout_9.addWidget(self.btn_FinCal)

        self.horizontalSpacer_13 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_13)


        self.verticalLayout_17.addLayout(self.horizontalLayout_9)

        self.MenuPrincipal.addWidget(self.Printer_page)
        self.DataBase_page = QWidget()
        self.DataBase_page.setObjectName(u"DataBase_page")
        self.verticalLayout_19 = QVBoxLayout(self.DataBase_page)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.verticalLayout_18 = QVBoxLayout()
        self.verticalLayout_18.setSpacing(10)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.verticalLayout_18.setContentsMargins(10, 10, 10, 10)
        self.label = QLabel(self.DataBase_page)
        self.label.setObjectName(u"label")

        self.verticalLayout_18.addWidget(self.label)

        self.DatabaseWidget = QWidget(self.DataBase_page)
        self.DatabaseWidget.setObjectName(u"DatabaseWidget")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.DatabaseWidget.sizePolicy().hasHeightForWidth())
        self.DatabaseWidget.setSizePolicy(sizePolicy3)
        self.DatabaseWidget.setStyleSheet(u"background-color: rgb(0, 85, 255);\n"
"background-color: rgba(0, 85, 255, 150);\n"
"background-color: rgba(122, 114, 127,150);")

        self.verticalLayout_18.addWidget(self.DatabaseWidget)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(-1, -1, -1, 0)
        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_7)

        self.btn_printCurrIndex = QPushButton(self.DataBase_page)
        self.btn_printCurrIndex.setObjectName(u"btn_printCurrIndex")
        self.btn_printCurrIndex.setStyleSheet(u"QPushButton{\n"
"background-color: rgba(0, 85, 127, 150);\n"
"font: 700 22pt \"Segoe UI\";\n"
"padding-left:4px;\n"
"border-radius: 4px;\n"
"border: 4px solid black;\n"
"border-color: rgb(0, 85, 127);}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(0, 85, 127);\n"
"}")

        self.horizontalLayout_6.addWidget(self.btn_printCurrIndex)

        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_8)


        self.verticalLayout_18.addLayout(self.horizontalLayout_6)


        self.verticalLayout_19.addLayout(self.verticalLayout_18)

        self.MenuPrincipal.addWidget(self.DataBase_page)
        self.Black_page = QWidget()
        self.Black_page.setObjectName(u"Black_page")
        self.gridLayout = QGridLayout(self.Black_page)
        self.gridLayout.setObjectName(u"gridLayout")
        self.Container_widget = QWidget(self.Black_page)
        self.Container_widget.setObjectName(u"Container_widget")
        self.Container_widget.setStyleSheet(u"")
        self.verticalLayout_30 = QVBoxLayout(self.Container_widget)
        self.verticalLayout_30.setObjectName(u"verticalLayout_30")
        self.verticalLayout_30.setContentsMargins(-1, -1, -1, 0)
        self.verticalLayout_29 = QVBoxLayout()
        self.verticalLayout_29.setObjectName(u"verticalLayout_29")
        self.verticalLayout_29.setContentsMargins(-1, -1, -1, 0)
        self.horizontalFrame_3 = QFrame(self.Container_widget)
        self.horizontalFrame_3.setObjectName(u"horizontalFrame_3")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.horizontalFrame_3.sizePolicy().hasHeightForWidth())
        self.horizontalFrame_3.setSizePolicy(sizePolicy4)
        self.horizontalFrame_3.setMinimumSize(QSize(0, 0))
        self.horizontalFrame_3.setFrameShape(QFrame.Shape.NoFrame)
        self.horizontalLayout = QHBoxLayout(self.horizontalFrame_3)
        self.horizontalLayout.setSpacing(15)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(-1, -1, 1, 1)
        self.verticalSpacer_9 = QSpacerItem(0, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.horizontalLayout.addItem(self.verticalSpacer_9)

        self.Mesa1_Widget = QWidget(self.horizontalFrame_3)
        self.Mesa1_Widget.setObjectName(u"Mesa1_Widget")
        self.Mesa1_Widget.setStyleSheet(u"background-color: rgba(0, 0, 0, 80);\n"
"border-radius:5px;")
        self.verticalLayout_21 = QVBoxLayout(self.Mesa1_Widget)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.horizontalSpacer_20 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.verticalLayout_21.addItem(self.horizontalSpacer_20)


        self.horizontalLayout.addWidget(self.Mesa1_Widget)

        self.horizontalSpacer_16 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_16)

        self.Mesa2_Widget = QWidget(self.horizontalFrame_3)
        self.Mesa2_Widget.setObjectName(u"Mesa2_Widget")
        self.Mesa2_Widget.setStyleSheet(u"background-color: rgba(0, 0, 0, 80);\n"
"border-radius:5px;")
        self.verticalLayout_23 = QVBoxLayout(self.Mesa2_Widget)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.verticalLayout_23.setContentsMargins(-1, 9, -1, 9)
        self.horizontalSpacer_19 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.verticalLayout_23.addItem(self.horizontalSpacer_19)


        self.horizontalLayout.addWidget(self.Mesa2_Widget)

        self.horizontalSpacer_17 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_17)

        self.Mesa3_Widget = QWidget(self.horizontalFrame_3)
        self.Mesa3_Widget.setObjectName(u"Mesa3_Widget")
        self.Mesa3_Widget.setMinimumSize(QSize(0, 0))
        self.Mesa3_Widget.setStyleSheet(u"background-color: rgba(0, 0, 0, 80);\n"
"border-radius:5px;")
        self.verticalLayout_22 = QVBoxLayout(self.Mesa3_Widget)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.horizontalSpacer_18 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.verticalLayout_22.addItem(self.horizontalSpacer_18)


        self.horizontalLayout.addWidget(self.Mesa3_Widget)


        self.verticalLayout_29.addWidget(self.horizontalFrame_3)

        self.horizontalSpacer_5 = QSpacerItem(40, 0, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.verticalLayout_29.addItem(self.horizontalSpacer_5)


        self.verticalLayout_30.addLayout(self.verticalLayout_29)


        self.gridLayout.addWidget(self.Container_widget, 0, 0, 1, 1)

        self.Free_widget = QWidget(self.Black_page)
        self.Free_widget.setObjectName(u"Free_widget")
        self.verticalLayout_38 = QVBoxLayout(self.Free_widget)
        self.verticalLayout_38.setObjectName(u"verticalLayout_38")
        self.verticalLayout_37 = QVBoxLayout()
        self.verticalLayout_37.setObjectName(u"verticalLayout_37")

        self.verticalLayout_38.addLayout(self.verticalLayout_37)


        self.gridLayout.addWidget(self.Free_widget, 1, 1, 1, 1)

        self.MenuPrincipal.addWidget(self.Black_page)
        self.Datamatrix_Page = QWidget()
        self.Datamatrix_Page.setObjectName(u"Datamatrix_Page")
        self.verticalLayout_33 = QVBoxLayout(self.Datamatrix_Page)
        self.verticalLayout_33.setObjectName(u"verticalLayout_33")
        self.verticalLayout_32 = QVBoxLayout()
        self.verticalLayout_32.setObjectName(u"verticalLayout_32")
        self.label_2 = QLabel(self.Datamatrix_Page)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_32.addWidget(self.label_2)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(-1, -1, -1, 40)
        self.label_4 = QLabel(self.Datamatrix_Page)
        self.label_4.setObjectName(u"label_4")
        sizePolicy5 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy5)
        self.label_4.setMaximumSize(QSize(800, 500))
        self.label_4.setStyleSheet(u"QLabel {\n"
"    border: 3px solid #FF0000; /* Cambia el color del borde a rojo */\n"
"	border-color: rgb(0, 85, 255);\n"
"	border-radius:1px;\n"
"}")
        self.label_4.setPixmap(QPixmap(u":/prefijoNuevo/icons/DMC.PNG"))
        self.label_4.setScaledContents(True)
        self.label_4.setMargin(5)

        self.horizontalLayout_7.addWidget(self.label_4)


        self.verticalLayout_32.addLayout(self.horizontalLayout_7)

        self.verticalSpacer_10 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_32.addItem(self.verticalSpacer_10)


        self.verticalLayout_33.addLayout(self.verticalLayout_32)

        self.MenuPrincipal.addWidget(self.Datamatrix_Page)
        self.Config_Page = QWidget()
        self.Config_Page.setObjectName(u"Config_Page")
        self.verticalLayout_6 = QVBoxLayout(self.Config_Page)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.widget = QWidget(self.Config_Page)
        self.widget.setObjectName(u"widget")
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.verticalLayout_7 = QVBoxLayout(self.widget)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.horizontal_model_2 = QHBoxLayout()
        self.horizontal_model_2.setObjectName(u"horizontal_model_2")
        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.pushButton_3 = QPushButton(self.widget)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setStyleSheet(u"QPushButton{\n"
"background-color: rgba(0, 85, 255, 150);\n"
"font: 700 28pt \"Segoe UI\";\n"
"color: rgba(255, 255, 255, 200);\n"
"border-radius: 5px;\n"
"padding-left:7px;\n"
"border: 4px solid black;\n"
"border-color: rgb(0, 85, 255);}\n"
"\n"
"QPushButton:pressed {\n"
"	/*background-color: rgb(255, 233, 51 );*/\n"
"    background-color: rgb(0, 0, 255);\n"
"}\n"
"")

        self.verticalLayout_9.addWidget(self.pushButton_3)

        self.horizontalSpacer_10 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.verticalLayout_9.addItem(self.horizontalSpacer_10)

        self.widget_setup_M1 = QWidget(self.widget)
        self.widget_setup_M1.setObjectName(u"widget_setup_M1")
        self.widget_setup_M1.setMinimumSize(QSize(0, 350))
        self.widget_setup_M1.setStyleSheet(u"background-color: rgba(0, 0, 0, 80);")

        self.verticalLayout_9.addWidget(self.widget_setup_M1)


        self.horizontal_model_2.addLayout(self.verticalLayout_9)

        self.verticalLayout_10 = QVBoxLayout()
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.pushButton = QPushButton(self.widget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setStyleSheet(u"QPushButton{\n"
"background-color: rgba(0, 85, 255, 150);\n"
"font: 700 28pt \"Segoe UI\";\n"
"color: rgba(255, 255, 255, 200);\n"
"border-radius: 5px;\n"
"padding-left:7px;\n"
"border: 4px solid black;\n"
"border-color: rgb(0, 85, 255);}\n"
"\n"
"QPushButton:pressed {\n"
"	/*background-color: rgb(255, 233, 51 );*/\n"
"    background-color: rgb(0, 0, 255);\n"
"}\n"
"")

        self.verticalLayout_10.addWidget(self.pushButton)

        self.horizontalSpacer_11 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.verticalLayout_10.addItem(self.horizontalSpacer_11)

        self.widget_setup_M2 = QWidget(self.widget)
        self.widget_setup_M2.setObjectName(u"widget_setup_M2")
        self.widget_setup_M2.setMinimumSize(QSize(0, 350))
        self.widget_setup_M2.setMaximumSize(QSize(16777215, 16777215))
        self.widget_setup_M2.setStyleSheet(u"background-color: rgba(0, 0, 0, 80);")

        self.verticalLayout_10.addWidget(self.widget_setup_M2)


        self.horizontal_model_2.addLayout(self.verticalLayout_10)

        self.verticalLayout_11 = QVBoxLayout()
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.pushButton_4 = QPushButton(self.widget)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setStyleSheet(u"QPushButton{\n"
"background-color: rgba(0, 85, 255, 150);\n"
"font: 700 28pt \"Segoe UI\";\n"
"color: rgba(255, 255, 255, 200);\n"
"border-radius: 5px;\n"
"padding-left:7px;\n"
"border: 4px solid black;\n"
"border-color: rgb(0, 85, 255);}\n"
"\n"
"QPushButton:pressed {\n"
"	/*background-color: rgb(255, 233, 51 );*/\n"
"    background-color: rgb(0, 0, 255);\n"
"}\n"
"")

        self.verticalLayout_11.addWidget(self.pushButton_4)

        self.horizontalSpacer_12 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.verticalLayout_11.addItem(self.horizontalSpacer_12)

        self.widget_setup_M3 = QWidget(self.widget)
        self.widget_setup_M3.setObjectName(u"widget_setup_M3")
        self.widget_setup_M3.setMinimumSize(QSize(0, 350))
        self.widget_setup_M3.setStyleSheet(u"background-color: rgba(0, 0, 0, 80);")

        self.verticalLayout_11.addWidget(self.widget_setup_M3)


        self.horizontal_model_2.addLayout(self.verticalLayout_11)


        self.verticalLayout_7.addLayout(self.horizontal_model_2)

        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_7.addItem(self.verticalSpacer_6)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_3)

        self.btn_SaveSetup = QPushButton(self.widget)
        self.btn_SaveSetup.setObjectName(u"btn_SaveSetup")
        self.btn_SaveSetup.setStyleSheet(u"QPushButton{\n"
"background-color: rgba(235, 211, 26,110);\n"
"font: 700 30pt \"Segoe UI\";\n"
"color: rgba(255, 255, 255, 200);\n"
"border-radius: 5px;\n"
"padding-left:7px;\n"
"border: 4px solid black;\n"
"border-color: rgb(235, 211, 26);}\n"
"\n"
"QPushButton:pressed {\n"
"	/*background-color: rgb(255, 233, 51 );*/\n"
"    background-color: rgb(235, 211, 26);\n"
"}\n"
"")

        self.horizontalLayout_5.addWidget(self.btn_SaveSetup)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_2)


        self.verticalLayout_7.addLayout(self.horizontalLayout_5)


        self.verticalLayout_6.addWidget(self.widget)

        self.MenuPrincipal.addWidget(self.Config_Page)
        self.EditLabel_Page = QWidget()
        self.EditLabel_Page.setObjectName(u"EditLabel_Page")
        self.verticalLayout_13 = QVBoxLayout(self.EditLabel_Page)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_12 = QVBoxLayout()
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.lbl_tittle_3 = QLabel(self.EditLabel_Page)
        self.lbl_tittle_3.setObjectName(u"lbl_tittle_3")

        self.verticalLayout_12.addWidget(self.lbl_tittle_3)

        self.verticalSpacer_8 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_12.addItem(self.verticalSpacer_8)

        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalSpacer_30 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacer_30)

        self.label_6 = QLabel(self.EditLabel_Page)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setStyleSheet(u"padding-left:5px;\n"
"")

        self.horizontalLayout_13.addWidget(self.label_6)

        self.horizontalSpacer_22 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacer_22)


        self.verticalLayout_12.addLayout(self.horizontalLayout_13)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalSpacer_29 = QSpacerItem(160, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_12.addItem(self.horizontalSpacer_29)

        self.line_CurrLabel = QTextEdit(self.EditLabel_Page)
        self.line_CurrLabel.setObjectName(u"line_CurrLabel")
        sizePolicy6 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.line_CurrLabel.sizePolicy().hasHeightForWidth())
        self.line_CurrLabel.setSizePolicy(sizePolicy6)
        self.line_CurrLabel.setMinimumSize(QSize(0, 42))
        self.line_CurrLabel.setMaximumSize(QSize(16777215, 42))
        self.line_CurrLabel.setStyleSheet(u"font: 700 22pt \"Segoe UI\";\n"
"color: rgb(235, 211, 26);\n"
"border: 1px solid;\n"
"border-color: rgb(63, 90, 140);")
        self.line_CurrLabel.setFrameShape(QFrame.Shape.NoFrame)
        self.line_CurrLabel.setFrameShadow(QFrame.Shadow.Plain)

        self.horizontalLayout_12.addWidget(self.line_CurrLabel)

        self.horizontalSpacer_21 = QSpacerItem(160, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_12.addItem(self.horizontalSpacer_21)


        self.verticalLayout_12.addLayout(self.horizontalLayout_12)

        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.verticalSpacer_11 = QSpacerItem(13, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.horizontalLayout_14.addItem(self.verticalSpacer_11)

        self.horizontalSpacer_23 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_14.addItem(self.horizontalSpacer_23)

        self.lbl_oldPza = QLabel(self.EditLabel_Page)
        self.lbl_oldPza.setObjectName(u"lbl_oldPza")
        self.lbl_oldPza.setAutoFillBackground(False)
        self.lbl_oldPza.setStyleSheet(u"background-color: rgb(170, 0, 0);")
        self.lbl_oldPza.setPixmap(QPixmap(u":/prefijoNuevo/icons/label_edit.png"))
        self.lbl_oldPza.setScaledContents(False)
        self.lbl_oldPza.setMargin(5)

        self.horizontalLayout_14.addWidget(self.lbl_oldPza)

        self.horizontalSpacer_25 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_14.addItem(self.horizontalSpacer_25)


        self.verticalLayout_12.addLayout(self.horizontalLayout_14)

        self.horizontalLayout_16 = QHBoxLayout()
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalSpacer_27 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_16.addItem(self.horizontalSpacer_27)

        self.lbl_arrowDown = QLabel(self.EditLabel_Page)
        self.lbl_arrowDown.setObjectName(u"lbl_arrowDown")
        self.lbl_arrowDown.setMaximumSize(QSize(100, 100))
        self.lbl_arrowDown.setPixmap(QPixmap(u":/prefijoNuevo/icons/flecha.png"))
        self.lbl_arrowDown.setScaledContents(True)

        self.horizontalLayout_16.addWidget(self.lbl_arrowDown)

        self.horizontalSpacer_28 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_16.addItem(self.horizontalSpacer_28)

        self.verticalSpacer_7 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.horizontalLayout_16.addItem(self.verticalSpacer_7)


        self.verticalLayout_12.addLayout(self.horizontalLayout_16)

        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.verticalSpacer_12 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.horizontalLayout_15.addItem(self.verticalSpacer_12)

        self.horizontalSpacer_24 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_15.addItem(self.horizontalSpacer_24)

        self.lbl_newPza = QLabel(self.EditLabel_Page)
        self.lbl_newPza.setObjectName(u"lbl_newPza")
        self.lbl_newPza.setStyleSheet(u"background-color: rgb(0, 170, 0);")
        self.lbl_newPza.setPixmap(QPixmap(u":/prefijoNuevo/icons/label_edit.png"))
        self.lbl_newPza.setScaledContents(False)
        self.lbl_newPza.setMargin(5)

        self.horizontalLayout_15.addWidget(self.lbl_newPza)

        self.horizontalSpacer_26 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_15.addItem(self.horizontalSpacer_26)


        self.verticalLayout_12.addLayout(self.horizontalLayout_15)


        self.verticalLayout_13.addLayout(self.verticalLayout_12)

        self.verticalSpacer_13 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_13.addItem(self.verticalSpacer_13)

        self.horizontalLayout_17 = QHBoxLayout()
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.horizontalSpacer_32 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_17.addItem(self.horizontalSpacer_32)

        self.lbl_print_State_1 = QLabel(self.EditLabel_Page)
        self.lbl_print_State_1.setObjectName(u"lbl_print_State_1")

        self.horizontalLayout_17.addWidget(self.lbl_print_State_1)

        self.horizontalSpacer_31 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_17.addItem(self.horizontalSpacer_31)


        self.verticalLayout_13.addLayout(self.horizontalLayout_17)

        self.MenuPrincipal.addWidget(self.EditLabel_Page)
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.verticalLayout_24 = QVBoxLayout(self.page)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.widget_2 = QWidget(self.page)
        self.widget_2.setObjectName(u"widget_2")
        sizePolicy.setHeightForWidth(self.widget_2.sizePolicy().hasHeightForWidth())
        self.widget_2.setSizePolicy(sizePolicy)
        self.verticalLayout_14 = QVBoxLayout(self.widget_2)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.horizontal_model_3 = QHBoxLayout()
        self.horizontal_model_3.setObjectName(u"horizontal_model_3")
        self.verticalLayout_15 = QVBoxLayout()
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.horizontalSpacer_33 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.verticalLayout_15.addItem(self.horizontalSpacer_33)


        self.horizontal_model_3.addLayout(self.verticalLayout_15)

        self.verticalLayout_16 = QVBoxLayout()
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.pushButton_2 = QPushButton(self.widget_2)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setStyleSheet(u"QPushButton{\n"
"background-color: rgba(0, 85, 255, 150);\n"
"font: 700 28pt \"Segoe UI\";\n"
"color: rgba(255, 255, 255, 200);\n"
"border-radius: 5px;\n"
"padding-left:7px;\n"
"border: 4px solid black;\n"
"border-color: rgb(0, 85, 255);}\n"
"\n"
"QPushButton:pressed {\n"
"	/*background-color: rgb(255, 233, 51 );*/\n"
"    background-color: rgb(0, 0, 255);\n"
"}\n"
"")

        self.verticalLayout_16.addWidget(self.pushButton_2)

        self.horizontalSpacer_34 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.verticalLayout_16.addItem(self.horizontalSpacer_34)

        self.widget_setup_E6 = QWidget(self.widget_2)
        self.widget_setup_E6.setObjectName(u"widget_setup_E6")
        self.widget_setup_E6.setMinimumSize(QSize(0, 350))
        self.widget_setup_E6.setMaximumSize(QSize(16777215, 16777215))
        self.widget_setup_E6.setStyleSheet(u"background-color: rgba(0, 0, 0, 80);")

        self.verticalLayout_16.addWidget(self.widget_setup_E6)


        self.horizontal_model_3.addLayout(self.verticalLayout_16)

        self.verticalLayout_20 = QVBoxLayout()
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.horizontalSpacer_35 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.verticalLayout_20.addItem(self.horizontalSpacer_35)


        self.horizontal_model_3.addLayout(self.verticalLayout_20)


        self.verticalLayout_14.addLayout(self.horizontal_model_3)

        self.verticalSpacer_14 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_14.addItem(self.verticalSpacer_14)

        self.horizontalLayout_18 = QHBoxLayout()
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.horizontalSpacer_36 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_18.addItem(self.horizontalSpacer_36)

        self.btn_SaveSetup_2 = QPushButton(self.widget_2)
        self.btn_SaveSetup_2.setObjectName(u"btn_SaveSetup_2")
        self.btn_SaveSetup_2.setStyleSheet(u"QPushButton{\n"
"background-color: rgba(235, 211, 26,110);\n"
"font: 700 30pt \"Segoe UI\";\n"
"color: rgba(255, 255, 255, 200);\n"
"border-radius: 5px;\n"
"padding-left:7px;\n"
"border: 4px solid black;\n"
"border-color: rgb(235, 211, 26);}\n"
"\n"
"QPushButton:pressed {\n"
"	/*background-color: rgb(255, 233, 51 );*/\n"
"    background-color: rgb(235, 211, 26);\n"
"}\n"
"")

        self.horizontalLayout_18.addWidget(self.btn_SaveSetup_2)

        self.horizontalSpacer_37 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_18.addItem(self.horizontalSpacer_37)


        self.verticalLayout_14.addLayout(self.horizontalLayout_18)


        self.verticalLayout_24.addWidget(self.widget_2)

        self.MenuPrincipal.addWidget(self.page)

        self.gridLayout_3.addWidget(self.MenuPrincipal, 0, 0, 1, 1)


        self.horizontalLayout_container.addWidget(self.Main_widgetContainer)

        self.Right_Menu = QWidget(self.Contenedor)
        self.Right_Menu.setObjectName(u"Right_Menu")
        self.Right_Menu.setMinimumSize(QSize(0, 0))
        self.Right_Menu.setMaximumSize(QSize(0, 16777215))
        self.verticalLayout_2 = QVBoxLayout(self.Right_Menu)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(1, 1, 1, 1)
        self.verticalFrame = QFrame(self.Right_Menu)
        self.verticalFrame.setObjectName(u"verticalFrame")
        self.verticalLayout = QVBoxLayout(self.verticalFrame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.line = QFrame(self.verticalFrame)
        self.line.setObjectName(u"line")
        self.line.setMinimumSize(QSize(0, 3))
        self.line.setStyleSheet(u"background-color: rgb(0, 85, 255);")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.verticalLayout.addWidget(self.line)

        self.frame = QFrame(self.verticalFrame)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Shape.NoFrame)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.btn_rightConfig = QPushButton(self.frame)
        self.btn_rightConfig.setObjectName(u"btn_rightConfig")
        self.btn_rightConfig.setMinimumSize(QSize(0, 45))

        self.verticalLayout_4.addWidget(self.btn_rightConfig)

        self.btn_rightDatabase = QPushButton(self.frame)
        self.btn_rightDatabase.setObjectName(u"btn_rightDatabase")
        self.btn_rightDatabase.setMinimumSize(QSize(0, 45))

        self.verticalLayout_4.addWidget(self.btn_rightDatabase)

        self.btn_rightLogout = QPushButton(self.frame)
        self.btn_rightLogout.setObjectName(u"btn_rightLogout")
        self.btn_rightLogout.setMinimumSize(QSize(0, 45))

        self.verticalLayout_4.addWidget(self.btn_rightLogout)


        self.verticalLayout_5.addLayout(self.verticalLayout_4)


        self.verticalLayout.addWidget(self.frame)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.verticalLayout_2.addWidget(self.verticalFrame)


        self.horizontalLayout_container.addWidget(self.Right_Menu)


        self.Container_Layout.addLayout(self.horizontalLayout_container)


        self.MainLayout.addWidget(self.Contenedor, 0, 2, 1, 1)

        self.Menus = QWidget(self.centralwidget)
        self.Menus.setObjectName(u"Menus")
        sizePolicy.setHeightForWidth(self.Menus.sizePolicy().hasHeightForWidth())
        self.Menus.setSizePolicy(sizePolicy)
        self.Menus.setMinimumSize(QSize(50, 0))
        self.Menus.setMaximumSize(QSize(16777215, 16777215))
        self.horizontalLayout_10 = QHBoxLayout(self.Menus)
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, -1, -1, -1)
        self.Left_Menu = QWidget(self.Menus)
        self.Left_Menu.setObjectName(u"Left_Menu")
        sizePolicy7 = QSizePolicy(QSizePolicy.Policy.Ignored, QSizePolicy.Policy.Preferred)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.Left_Menu.sizePolicy().hasHeightForWidth())
        self.Left_Menu.setSizePolicy(sizePolicy7)
        self.Left_Menu.setMinimumSize(QSize(55, 0))
        self.Left_Menu.setMaximumSize(QSize(185, 16777215))
        self.Left_Menu.setSizeIncrement(QSize(0, 0))
        self.Left_Menu.setStyleSheet(u"")
        self.verticalLayout_3 = QVBoxLayout(self.Left_Menu)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.LeftMenu_main = QVBoxLayout()
        self.LeftMenu_main.setSpacing(9)
        self.LeftMenu_main.setObjectName(u"LeftMenu_main")
        self.LeftMenu_main.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.LeftMenu_main.setContentsMargins(0, 5, 0, 3)
        self.frame_titulo = QFrame(self.Left_Menu)
        self.frame_titulo.setObjectName(u"frame_titulo")
        self.frame_titulo.setMinimumSize(QSize(0, 50))
        self.frame_titulo.setMaximumSize(QSize(16777215, 50))
        self.frame_titulo.setStyleSheet(u"")
        self.frame_titulo.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_titulo.setFrameShadow(QFrame.Shadow.Raised)
        self.lbl_titulo = QLabel(self.frame_titulo)
        self.lbl_titulo.setObjectName(u"lbl_titulo")
        self.lbl_titulo.setGeometry(QRect(58, -2, 101, 31))
        self.lbl_subtitulo = QLabel(self.frame_titulo)
        self.lbl_subtitulo.setObjectName(u"lbl_subtitulo")
        self.lbl_subtitulo.setGeometry(QRect(58, 22, 99, 29))
        self.lbl_subtitulo.setStyleSheet(u"background-color: none;")
        self.frame_logo = QFrame(self.frame_titulo)
        self.frame_logo.setObjectName(u"frame_logo")
        self.frame_logo.setGeometry(QRect(-6, 0, 65, 53))
        self.frame_logo.setStyleSheet(u"background-color: none;\n"
"image: url(:/prefijoNuevo/icons/logo.ico);")
        self.frame_logo.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_logo.setFrameShadow(QFrame.Shadow.Raised)
        self.lbl_subtitulo.raise_()
        self.lbl_titulo.raise_()
        self.frame_logo.raise_()

        self.LeftMenu_main.addWidget(self.frame_titulo)

        self.btn_latchMenu = QPushButton(self.Left_Menu)
        self.btn_latchMenu.setObjectName(u"btn_latchMenu")
        self.btn_latchMenu.setEnabled(True)
        self.btn_latchMenu.setMinimumSize(QSize(0, 50))
        self.btn_latchMenu.setSizeIncrement(QSize(0, 0))
        self.btn_latchMenu.setBaseSize(QSize(0, 0))
        self.btn_latchMenu.setStyleSheet(u"/*QPushButton{\n"
"    background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 20px solid transparent;\n"
"	background-color: rgb(37, 41, 48);\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"	color: rgb(113, 126, 149);\n"
"	background-image: url(:/prefijoNuevo/icons/icon_menu.png);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"QPushButton:pressed {\n"
"	background-color: rgb(189, 147, 249);\n"
"}\n"
"*/\n"
"")
        self.btn_latchMenu.setCheckable(True)
        self.btn_latchMenu.setChecked(False)

        self.LeftMenu_main.addWidget(self.btn_latchMenu)

        self.btn_home = QPushButton(self.Left_Menu)
        self.btn_home.setObjectName(u"btn_home")
        self.btn_home.setMinimumSize(QSize(0, 50))
        self.btn_home.setStyleSheet(u"/*QPushButton{\n"
"    background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 20px solid transparent;\n"
"	background-color: rgb(37, 41, 48);\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"	color: rgb(113, 126, 149);\n"
"    background-image: url(:/prefijoNuevo/icons/cil-home.png);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"QPushButton:pressed {\n"
"	background-color: rgb(189, 147, 249);\n"
"}\n"
"\n"
"*/")

        self.LeftMenu_main.addWidget(self.btn_home)

        self.btn_modelos = QPushButton(self.Left_Menu)
        self.btn_modelos.setObjectName(u"btn_modelos")
        self.btn_modelos.setMinimumSize(QSize(0, 50))
        self.btn_modelos.setStyleSheet(u"/*QPushButton{\n"
"    background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 20px solid transparent;\n"
"	background-color: rgb(37, 41, 48);\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"	color: rgb(113, 126, 149);\n"
"		\n"
"	background-image: url(:/prefijoNuevo/icons/cil-loop-circular.png);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"QPushButton:pressed {\n"
"	background-color: rgb(189, 147, 249);\n"
"}*/\n"
"\n"
"")

        self.LeftMenu_main.addWidget(self.btn_modelos)

        self.btn_historial = QPushButton(self.Left_Menu)
        self.btn_historial.setObjectName(u"btn_historial")
        self.btn_historial.setMinimumSize(QSize(0, 50))
        self.btn_historial.setStyleSheet(u"/*QPushButton{\n"
"    background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 20px solid transparent;\n"
"	background-color: rgb(37, 41, 48);\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"	color: rgb(113, 126, 149);\n"
"    background-image: url(:/prefijoNuevo/icons/cil-file.png);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"QPushButton:pressed {\n"
"	background-color: rgb(189, 147, 249);\n"
"}\n"
"*/\n"
"")

        self.LeftMenu_main.addWidget(self.btn_historial)

        self.btn_reportes = QPushButton(self.Left_Menu)
        self.btn_reportes.setObjectName(u"btn_reportes")
        self.btn_reportes.setMinimumSize(QSize(0, 50))
        self.btn_reportes.setStyleSheet(u"/*\n"
"QPushButton{\n"
"    background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 20px solid transparent;\n"
"	background-color: rgb(37, 41, 48);\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"	color: rgb(113, 126, 149);\n"
"    background-image: url(:/prefijoNuevo/icons/cil-notes.png);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"QPushButton:pressed {\n"
"	background-color: rgb(189, 147, 249);\n"
"}\n"
"*/\n"
"")

        self.LeftMenu_main.addWidget(self.btn_reportes)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.LeftMenu_main.addItem(self.verticalSpacer_2)

        self.btn_config = QPushButton(self.Left_Menu)
        self.btn_config.setObjectName(u"btn_config")
        self.btn_config.setMinimumSize(QSize(0, 50))
        self.btn_config.setStyleSheet(u"/*QPushButton{\n"
"    background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 20px solid transparent;\n"
"	background-color: rgb(37, 41, 48);\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"	color: rgb(113, 126, 149);\n"
"    \n"
"	background-image: url(:/prefijoNuevo/icons/icon_settings.png);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"QPushButton:pressed {\n"
"	background-color: rgb(189, 147, 249);\n"
"}*/\n"
"")

        self.LeftMenu_main.addWidget(self.btn_config)


        self.verticalLayout_3.addLayout(self.LeftMenu_main)


        self.horizontalLayout_8.addWidget(self.Left_Menu)


        self.horizontalLayout_10.addLayout(self.horizontalLayout_8)


        self.MainLayout.addWidget(self.Menus, 0, 0, 1, 1)


        self.gridLayout_2.addLayout(self.MainLayout, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.MenuPrincipal.setCurrentIndex(4)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.lbl_Server_state.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:16pt; font-weight:700; color:#c8c8c8;\">SERVIDOR: </span><span style=\" font-size:16pt; font-weight:700; color:#ebd31a;\">CONECTANDO...</span></p></body></html>", None))
        self.lbl_Wifi_State.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:16pt; font-weight:700; color:#c8c8c8;\">WIFI: </span><span style=\" font-size:16pt; font-weight:700; color:#ebd31a;\">CONECTANDO...</span></p></body></html>", None))
        self.btn_topconfig.setText("")
        self.btn_minimize.setText("")
        self.btn_maximize.setText("")
        self.btn_close.setText("")
        self.titulo_modelo.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:26pt; font-weight:700; color:#0055ff;\">Seleccionar Accion</span></p></body></html>", None))
        self.btn_EditAction.setText(QCoreApplication.translate("MainWindow", u"EDITAR", None))
        self.btn_PrintAction.setText(QCoreApplication.translate("MainWindow", u"IMPRIMIR", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:26pt; font-weight:700; color:#0055ff;\">CONFIGURAR IMPRESORA</span></p></body></html>", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:26pt; font-weight:700; color:#0055ff;\">ESTACION:</span></p></body></html>", None))
        self.Box_printerStation.setItemText(0, QCoreApplication.translate("MainWindow", u"Estacion 3", None))
        self.Box_printerStation.setItemText(1, QCoreApplication.translate("MainWindow", u"Estacion 4", None))
        self.Box_printerStation.setItemText(2, QCoreApplication.translate("MainWindow", u"Estacion 5", None))

        self.Box_printerStation.setPlaceholderText("")
        self.btn_speed.setText(QCoreApplication.translate("MainWindow", u"SPEED", None))
        self.btn_stroke.setText(QCoreApplication.translate("MainWindow", u"STROKE", None))
        self.btn_calibrate.setText(QCoreApplication.translate("MainWindow", u"CALIBRATE", None))
        self.btn_FinCal.setText(QCoreApplication.translate("MainWindow", u"FINALIZAR", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:26pt; font-weight:700; color:#0055ff;\">Historial Modelo Actual</span></p></body></html>", None))
        self.btn_printCurrIndex.setText(QCoreApplication.translate("MainWindow", u"IMPRIMIR", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:26pt; font-weight:700; color:#0055ff;\">Data Matrix</span></p></body></html>", None))
        self.label_4.setText("")
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"ESTACION 3", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"ESTACION 4", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"ESTACION 5", None))
        self.btn_SaveSetup.setText(QCoreApplication.translate("MainWindow", u"GUARDAR ", None))
        self.lbl_tittle_3.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:26pt; font-weight:700; color:#c8c8c8;\">INDICE R - INDICE P</span></p></body></html>", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:20pt; font-weight:700; color:#c8c8c8;\">ESCANEAR ETIQUETA CON </span><span style=\" font-size:20pt; font-weight:700; color:#0055ff;\">INDICE P</span><span style=\" font-size:20pt; font-weight:700; color:#c8c8c8;\">:</span></p></body></html>", None))
        self.lbl_oldPza.setText("")
        self.lbl_arrowDown.setText("")
        self.lbl_newPza.setText("")
        self.lbl_print_State_1.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:16pt; font-weight:700; color:#c8c8c8;\">IMPRESORA: </span><span style=\" font-size:16pt; font-weight:700; color:#ebd31a;\">CONECTANDO...</span></p></body></html>", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"ESTACION 6", None))
        self.btn_SaveSetup_2.setText(QCoreApplication.translate("MainWindow", u"GUARDAR ", None))
        self.btn_rightConfig.setText(QCoreApplication.translate("MainWindow", u"Mensajes", None))
        self.btn_rightDatabase.setText(QCoreApplication.translate("MainWindow", u"DataBase", None))
        self.btn_rightLogout.setText(QCoreApplication.translate("MainWindow", u"LogOut", None))
        self.lbl_titulo.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:700; color:#f2f2f2;\">RAD LTR</span></p></body></html>", None))
        self.lbl_subtitulo.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:700; color:#0055ff;\">ATEQ</span></p></body></html>", None))
        self.btn_latchMenu.setText("")
        self.btn_home.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.btn_modelos.setText(QCoreApplication.translate("MainWindow", u"Modelos", None))
        self.btn_historial.setText(QCoreApplication.translate("MainWindow", u"Historial", None))
        self.btn_reportes.setText(QCoreApplication.translate("MainWindow", u"DataMatrix", None))
        self.btn_config.setText(QCoreApplication.translate("MainWindow", u"Configuracion", None))
    # retranslateUi

