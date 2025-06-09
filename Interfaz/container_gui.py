# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'container.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QLCDNumber, QLabel,
    QPushButton, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(277, 432)
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.Mesa1_Frame = QFrame(Form)
        self.Mesa1_Frame.setObjectName(u"Mesa1_Frame")
        self.Mesa1_Frame.setStyleSheet(u"background-color: rgba(0, 0, 0, 80);\n"
"border-radius:5px;")
        self.verticalLayout_21 = QVBoxLayout(self.Mesa1_Frame)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.lbl_titleStation = QLabel(self.Mesa1_Frame)
        self.lbl_titleStation.setObjectName(u"lbl_titleStation")
        self.lbl_titleStation.setMinimumSize(QSize(0, 50))
        self.lbl_titleStation.setStyleSheet(u"background-color: rgb(0, 85, 255);\n"
"\n"
"")

        self.verticalLayout_21.addWidget(self.lbl_titleStation)

        self.lbl_part_num = QLabel(self.Mesa1_Frame)
        self.lbl_part_num.setObjectName(u"lbl_part_num")
        self.lbl_part_num.setMinimumSize(QSize(0, 50))
        self.lbl_part_num.setStyleSheet(u"background-color: rgba(100, 100, 100,100);\n"
"border: 3px solid transparent;\n"
"border-color: rgb(33, 37, 43);")
        self.lbl_part_num.setFrameShape(QFrame.Shape.NoFrame)
        self.lbl_part_num.setScaledContents(False)
        self.lbl_part_num.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_21.addWidget(self.lbl_part_num)

        self.lcd_display = QLCDNumber(self.Mesa1_Frame)
        self.lcd_display.setObjectName(u"lcd_display")
        self.lcd_display.setMinimumSize(QSize(0, 100))
        self.lcd_display.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.lcd_display.setStyleSheet(u"color: rgb(200, 200, 200);\n"
"background-color: none;")
        self.lcd_display.setFrameShape(QFrame.Shape.NoFrame)
        self.lcd_display.setSmallDecimalPoint(False)

        self.verticalLayout_21.addWidget(self.lcd_display)

        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_21.addItem(self.verticalSpacer_6)

        self.lbl_StatePza = QLabel(self.Mesa1_Frame)
        self.lbl_StatePza.setObjectName(u"lbl_StatePza")
        self.lbl_StatePza.setStyleSheet(u"QLabel {\n"
"    border: 2px solid #FF0000; /* Cambia el color del borde a rojo */\n"
"	border-color: rgb(0, 255, 0);\n"
"	border-radius:9px;\n"
"}")
        self.lbl_StatePza.setTextInteractionFlags(Qt.TextInteractionFlag.LinksAccessibleByMouse)

        self.verticalLayout_21.addWidget(self.lbl_StatePza)

        self.btn_RePrint = QPushButton(self.Mesa1_Frame)
        self.btn_RePrint.setObjectName(u"btn_RePrint")
        self.btn_RePrint.setMinimumSize(QSize(0, 60))
        self.btn_RePrint.setStyleSheet(u"QPushButton{\n"
"    border: 2px solid transparent; \n"
"	border-color: rgb(33, 37, 43);\n"
"	border-radius:5px;\n"
"	font: 700 14pt \"Segoe UI\";\n"
"	color: rgb(200, 200, 200);\n"
"	background-color: rgba(100, 100, 100,100);\n"
"}\n"
"\n"
"QPushButton:Pressed{\n"
"	background-color: rgb(0, 85, 255);\n"
"}")

        self.verticalLayout_21.addWidget(self.btn_RePrint)

        self.lbl_PrintState = QLabel(self.Mesa1_Frame)
        self.lbl_PrintState.setObjectName(u"lbl_PrintState")
        self.lbl_PrintState.setStyleSheet(u"QLabel {\n"
"color: rgb(200, 200, 200);\n"
"    border: 2px solid #FF0000; /* Cambia el color del borde a rojo */\n"
"	border-color: rgb(0, 85, 255);\n"
"	border-radius:5px;\n"
"}")

        self.verticalLayout_21.addWidget(self.lbl_PrintState)


        self.verticalLayout.addWidget(self.Mesa1_Frame)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.lbl_titleStation.setText(QCoreApplication.translate("Form", u"<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:700; color:#c8c8c8;\">ESTACION 1</span></p></body></html>", None))
        self.lbl_part_num.setText(QCoreApplication.translate("Form", u"<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:700; color:#c8c8c8;\">5QM121251Q</span></p></body></html>", None))
        self.lbl_StatePza.setText(QCoreApplication.translate("Form", u"<html><head/><body><p align=\"center\"><span style=\" font-size:20pt; font-weight:700; color:#00ff00;\">PIEZA APROBADA</span></p></body></html>", None))
        self.btn_RePrint.setText(QCoreApplication.translate("Form", u"IMPRIMIR", None))
        self.lbl_PrintState.setText(QCoreApplication.translate("Form", u"<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:700;\">IMPRESORA:<br/></span><span style=\" font-size:16pt; font-weight:700; color:#00aa00;\">CONECTADA</span></p></body></html>", None))
    # retranslateUi

