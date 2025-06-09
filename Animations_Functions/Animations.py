from PySide6.QtCore import QPropertyAnimation, QEasingCurve, QTimer


def initAnimation(ui_main):
    """
    Inicializa las animaciones implementadas en la App
    :param ui_main: instancia de la Clase UI principal
    :return:
    """
    # Configuración de la animación menu principal
    ui_main.animation = QPropertyAnimation(ui_main.Left_Menu, b'minimumWidth')
    ui_main.animation.setDuration(1000)
    ui_main.animation.setEasingCurve(QEasingCurve.OutCirc)  # Cambia la curva de aceleración aquí

    # Configuración de la animación menu secundario
    ui_main.animation_secundario = QPropertyAnimation(ui_main.Right_Menu, b'minimumWidth')
    ui_main.animation_secundario.setDuration(1000)
    ui_main.animation_secundario.setEasingCurve(QEasingCurve.InOutCirc)  # Cambia la curva de aceleración aquí

    ui_main.btn_latchMenu.setChecked(True)
    timer = QTimer()
    timer.singleShot(1000, lambda : MainMenu_Control(ui_main))
    ui_main.btn_latchMenu.setEnabled(False)

def MainMenu_Control(ui_main):
        if ui_main.btn_latchMenu.isChecked():
            ui_main.animation.setStartValue(55)
            ui_main.animation.setEndValue(185)
        else:
            ui_main.animation.setStartValue(185)
            ui_main.animation.setEndValue(55)  # Ajusta el ancho según tus necesidades
        ui_main.animation.start()
def RightMenu_Control(ui_main):
        if ui_main.btn_topconfig.isChecked():
            ui_main.animation_secundario.setStartValue(0)
            ui_main.animation_secundario.setEndValue(145)
        else:
            ui_main.animation_secundario.setStartValue(145)
            ui_main.animation_secundario.setEndValue(0)  # Ajusta el ancho según tus necesidades
        ui_main.animation_secundario.start()