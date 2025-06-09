from PySide6.QtWidgets import QWidget, QPushButton, QVBoxLayout, QGridLayout, QLineEdit
from PySide6.QtCore import Qt, Signal
class NumericKeypad(QWidget):
    number_entered = Signal(str)  # Señal para enviar el número ingresado

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setFixedSize(200, 250)  # Tamaño compacto

        # Campo de texto para la entrada
        self.display = QLineEdit(self)
        self.display.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.display.setReadOnly(True)
        self.display.setStyleSheet("font-size: 18px; padding: 5px;")

        # Botones del teclado numérico
        buttons = [
            '7', '8', '9',
            '4', '5', '6',
            '1', '2', '3',
            '←', '0', '✔'
        ]

        grid_layout = QGridLayout()
        row, col = 0, 0

        for button in buttons:
            btn = QPushButton(button)
            btn.setFixedSize(50, 50)  # Tamaño compacto de botones
            btn.setStyleSheet("font-size: 16px;")
            btn.clicked.connect(self.button_clicked)
            grid_layout.addWidget(btn, row, col)

            col += 1
            if col > 2:
                col = 0
                row += 1

        # Diseño principal
        main_layout = QVBoxLayout(self)
        main_layout.addWidget(self.display)
        main_layout.addLayout(grid_layout)

    def button_clicked(self):
        sender = self.sender().text()

        if sender == "←":  # Borrar último dígito
            self.display.setText(self.display.text()[:-1])
        elif sender == "✔":  # Enviar entrada y emitir señal
            self.number_entered.emit(self.display.text())
        else:
            self.display.setText(self.display.text() + sender)