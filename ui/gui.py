from PyQt5.QtWidgets import (
    QWidget, QLabel, QLineEdit, QPushButton,
    QVBoxLayout, QHBoxLayout
)
from PyQt5.QtCore import Qt

class SolverUI(QWidget):
    """Interface graphique pour la résolution d'équations du second degré (réelles uniquement)."""

    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        self.setWindowTitle("DirtyCalc 2.0")

        self.setFixedSize(420, 350)
        self._init_ui()

    def _init_ui(self):
        layout = QVBoxLayout()

        # Titre
        title = QLabel("Résolution : ax² + bx + c = 0")
        title.setAlignment(Qt.AlignCenter)
        title.setStyleSheet("font-size: 18px; font-weight: bold;")
        layout.addWidget(title)

        # Inputs
        self.input_a = self._create_input("valeur de a : ")
        self.input_b = self._create_input("valeur de b : ")
        self.input_c = self._create_input("valeur de c : ")

        layout.addLayout(self.input_a)
        layout.addLayout(self.input_b)
        layout.addLayout(self.input_c)

        # Bouton calculer
        self.btn_calculer = QPushButton("Resoudre")
        self.btn_calculer.clicked.connect(self._on_calculer)
        layout.addWidget(self.btn_calculer)

        # Résultat
        self.result_label = QLabel("")
        self.result_label.setAlignment(Qt.AlignCenter)
        self.result_label.setStyleSheet("font-size: 16px; color: darkblue; margin-top: 15px;")
        layout.addWidget(self.result_label)

        self.setLayout(layout)

    def _create_input(self, label_text: str) -> QHBoxLayout:
        layout = QHBoxLayout()
        label = QLabel(label_text)
        input_field = QLineEdit()
        input_field.setFixedWidth(100)
        layout.addWidget(label)
        layout.addWidget(input_field)
        layout.addStretch()

        if "valeur de a" in label_text:
            self.input_a_field = input_field
        elif "valeur de b" in label_text:
            self.input_b_field = input_field
        else:
            self.input_c_field = input_field

        return layout

    def _on_calculer(self):
        value_a = self.input_a_field.text()
        value_b = self.input_b_field.text()
        value_c = self.input_c_field.text()

        result = self.controller.compute(value_a, value_b, value_c)
        self.result_label.setText(result)
