from PySide6.QtCore import QCoreApplication

from main import *
def HideAlerts(ui_main):
    ui_main.lbl_StatePza.hide()
def Approve(ui_main):
    ui_main.lbl_StatePza.setStyleSheet(u"QLabel {\n"
                                         "    border: 2px solid #FF0000; /* Cambia el color del borde a rojo */\n"
                                         "	border-color: rgb(0, 255, 0);\n"
                                         "	border-radius:9px;\n"
                                         "}")
    ui_main.lbl_StatePza.setText(QCoreApplication.translate("MainWindow",
                                                              u"<html><head/><body><p align=\"center\"><span style=\" font-size:20pt; font-weight:700; color:#00ff00;\">PIEZA APROBADA</span></p></body></html>",
                                                              None))
    ui_main.lbl_StatePza.show()

def Reject(ui_main):
    ui_main.lbl_StatePza.setStyleSheet(u"QLabel {\n"
                                         "    border: 2px solid #FF0000; /* Cambia el color del borde a rojo */\n"
                                         "	border-color: rgb(255, 0, 0); /* Color rojo */\n"
                                         "	border-radius: 9px;\n"
                                         "    color: #FF0000; /* Cambia el color del texto a rojo */\n"
                                         "}")

    ui_main.lbl_StatePza.setText(QCoreApplication.translate("MainWindow",
                                                              u"<html><head/><body><p align=\"center\"><span style=\" font-size:20pt; font-weight:700; color:#FF0000;\">PIEZA RECHAZADA</span></p></body></html>",
                                                              None))
    ui_main.lbl_StatePza.show()
def Repeat(ui_main):
    ui_main.lbl_StatePza.setStyleSheet(u"QLabel {\n"
                                         "    border: 2px solid #FFD700; /* Cambia el color del borde a amarillo caterpillar */\n"
                                         "	border-color: rgb(255, 215, 0); /* Color amarillo caterpillar */\n"
                                         "	border-radius: 9px;\n"
                                         "    color: #FFD700; /* Cambia el color del texto a amarillo caterpillar */\n"
                                         "}")

    ui_main.lbl_StatePza.setText(QCoreApplication.translate("MainWindow",
                                                              u"<html><head/><body><p align=\"center\"><span style=\" font-size:20pt; font-weight:700; color:#FFD700;\">PIEZA REPETIDA</span></p></body></html>",
                                                              None))
    ui_main.lbl_StatePza.show()

def ApproveServer(ui_main):
    ui_main.lbl_StatePza.setStyleSheet(u"QLabel {\n"
                                         "    border: 2px solid #FF0000; /* Cambia el color del borde a rojo */\n"
                                         "	border-color: rgb(0, 255, 0);\n"
                                         "	border-radius:9px;\n"
                                         "}")
    ui_main.lbl_StatePza.setText(QCoreApplication.translate("MainWindow",
                                                              u"<html><head/><body><p align=\"center\"><span style=\" font-size:20pt; font-weight:700; color:#00ff00;\">PIEZA GUARDADA EN EL SERVIDOR</span></p></body></html>",
                                                              None))
    ui_main.lbl_StatePza.show()


def ApproveReprint(ui_main):
    ui_main.lbl_StatePza.setStyleSheet(u"QLabel {\n"
                                         "    border: 2px solid #FF0000; /* Cambia el color del borde a rojo */\n"
                                         "	border-color:rgb(0, 85, 255);\n"
                                         "	border-radius:9px;\n"
                                         "}")
    ui_main.lbl_StatePza.setText(QCoreApplication.translate("MainWindow",
                                                              u"<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:700; color:rgb(0, 85, 255);\">ETIQUETA RE-IMPRESA</span></p></body></html>",
                                                              None))
    ui_main.lbl_StatePza.show()


def RejectPrint(ui_main):
    ui_main.lbl_StatePza.setStyleSheet(u"QLabel {\n"
                                         "    border: 2px solid #FF0000; /* Cambia el color del borde a rojo */\n"
                                         "	border-color:#FF0000;\n"
                                         "	border-radius:9px;\n"
                                         "}")
    ui_main.lbl_StatePza.setText(QCoreApplication.translate("MainWindow",
                                                              u"<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:700; color:#FF0000;\">ERROR IMPRESORA</span></p></body></html>",
                                                              None))
    ui_main.lbl_StatePza.show()

def RejectFirstScan(ui_main):
    ui_main.lbl_StatePza.setStyleSheet(u"QLabel {\n"
                                         "    border: 2px solid #FF0000; /* Cambia el color del borde a rojo */\n"
                                         "	border-color:#FF0000;\n"
                                         "	border-radius:9px;\n"
                                         "}")
    ui_main.lbl_StatePza.setText(QCoreApplication.translate("MainWindow",
                                                              u"<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:700; color:#FF0000;\">SIN DATOS</span></p></body></html>",
                                                              None))
    ui_main.lbl_StatePza.show()