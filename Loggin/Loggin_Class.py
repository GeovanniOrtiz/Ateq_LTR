from PySide6.QtWidgets import QDialog, QLineEdit, QMessageBox
from Interfaz.Loggin_gui import Ui_Dialog as Loggin
from PySide6.QtCore import Qt
class Loggin(QDialog, Loggin):
    def __init__(self, parent=None):
        super(Loggin, self).__init__(parent)
        self.setupUi(self)
        self.line_contra.setEchoMode(QLineEdit.Password)

        self.state=0

        # Elimina la barra de menú y el botón de cierre
        self.setWindowFlag(Qt.FramelessWindowHint)

        self.box_Admin.addItems(["Usuario", "Administrador"])
        self.btn_iniciarSesion.released.connect(self.tryInit)
        self.btn_cancelar.released.connect(self.Cancel)

    def tryInit(self):
        #len(self.box_Admin.currentText())>0
        if self.box_Admin.currentText()=="Usuario" and len(self.txt_User.toPlainText())>0 and len(self.line_contra.text())>0:
            print("Get data")
            username = self.txt_User.toPlainText()
            password = self.line_contra.text()

            # Aquí puedes realizar la validación del usuario y contraseña
            if username == "LTR" and password == "0300":
                # Ejemplo simple de validación: solo imprimir los valores ingresados
                #print(f"Usuario: {username}, Contraseña: {password}")
                # Cerrar el cuadro de diálogo después de iniciar sesión
                self.state=1
                self.accept()
                QMessageBox.information(self, "Bienvenido", "Usuario registrado con exito")

            else:
                QMessageBox.information(self, "Verificar Informacion", "Usuario o Contraseña Incorrectos")
        elif self.box_Admin.currentText()=="Administrador" and len(self.txt_User.toPlainText())>0 and len(self.line_contra.text())>0:
            print("Get data")
            username = self.txt_User.toPlainText()
            password = self.line_contra.text()

            # Aquí puedes realizar la validación del usuario y contraseña
            if username == "Admin" and password == "0900":
                # Ejemplo simple de validación: solo imprimir los valores ingresados
                #print(f"Usuario: {username}, Contraseña: {password}")
                # Cerrar el cuadro de diálogo después de iniciar sesión
                self.state=2
                self.accept()
                QMessageBox.information(self, "Bienvenido", "Administrador registrado con exito")

            else:
                QMessageBox.information(self, "Verificar Informacion", "Usuario o Contraseña Incorrectos")
        else:
            QMessageBox.information(self, "Verificar Informacion", "Usuario o Contraseña Incorrectos")

    def Cancel(self):
        self.state=0
        self.reject()