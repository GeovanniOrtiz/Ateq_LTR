# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Setup.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QHBoxLayout, QLabel,
    QPushButton, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(240, 320)
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout_15 = QVBoxLayout()
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.horizontalSpacer_3 = QSpacerItem(40, 0, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.verticalLayout_15.addItem(self.horizontalSpacer_3)

        self.lbl_PartNo = QLabel(Form)
        self.lbl_PartNo.setObjectName(u"lbl_PartNo")
        self.lbl_PartNo.setStyleSheet(u"font: 700 20pt \"Segoe UI\";\n"
"background-color: rgba(0, 0, 0, 80);\n"
"border: 3px solid;\n"
"border-color: rgb(0, 85, 255);")

        self.verticalLayout_15.addWidget(self.lbl_PartNo)

        self.verticalSpacer_2 = QSpacerItem(20, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_15.addItem(self.verticalSpacer_2)

        self.lbl_tittle = QLabel(Form)
        self.lbl_tittle.setObjectName(u"lbl_tittle")
        self.lbl_tittle.setStyleSheet(u"color: rgb(200, 200, 200);")

        self.verticalLayout_15.addWidget(self.lbl_tittle)

        self.Box_PartNo = QComboBox(Form)
        self.Box_PartNo.setObjectName(u"Box_PartNo")
        self.Box_PartNo.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 12pt \"Segoe UI\";\n"
"background-color: rgb(44, 49, 58);")

        self.verticalLayout_15.addWidget(self.Box_PartNo)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_15.addItem(self.verticalSpacer)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.btn_Save = QPushButton(Form)
        self.btn_Save.setObjectName(u"btn_Save")
        self.btn_Save.setStyleSheet(u"QPushButton{\n"
"background-color: rgba(0, 85, 127, 150);\n"
"font:18pt \"Segoe UI\";\n"
"color: rgb(200, 200, 200);\n"
"border-radius: 4px;\n"
"border: 2px solid black;\n"
"border-color: rgb(0, 85, 127);}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(0, 85, 127);\n"
"}\n"
"")

        self.horizontalLayout_5.addWidget(self.btn_Save)

        self.btn_Cancel = QPushButton(Form)
        self.btn_Cancel.setObjectName(u"btn_Cancel")
        self.btn_Cancel.setStyleSheet(u"QPushButton{background-color: rgba(207, 162, 9,150);\n"
"font:18pt \"Segoe UI\";\n"
"color: rgb(200, 200, 200);\n"
"border-radius: 4px;\n"
"border: 2px solid black;\n"
"border-color: rgb(207, 162, 9);}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(255, 233, 51 );\n"
"}")

        self.horizontalLayout_5.addWidget(self.btn_Cancel)


        self.verticalLayout_15.addLayout(self.horizontalLayout_5)


        self.verticalLayout.addLayout(self.verticalLayout_15)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.lbl_PartNo.setText(QCoreApplication.translate("Form", u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:700; color:#c8c8c8;\">5QM121251R</span></p></body></html>", None))
        self.lbl_tittle.setText(QCoreApplication.translate("Form", u"<html><head/><body><p><span style=\" font-size:14pt; font-weight:700;\">Numero de Parte:</span></p></body></html>", None))
        self.btn_Save.setText(QCoreApplication.translate("Form", u"Guardar", None))
        self.btn_Cancel.setText(QCoreApplication.translate("Form", u"Cancelar", None))
    # retranslateUi

