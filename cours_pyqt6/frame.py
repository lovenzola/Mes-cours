from PyQt6.QtWidgets import (
    QWidget, QApplication, QLabel, QPushButton, QVBoxLayout, QHBoxLayout, QFormLayout, QFrame,
    QMainWindow, QLineEdit, QComboBox
)
from PyQt6.QtCore import Qt
import sys

class fenetre(QMainWindow):
    def __init__(self):
        super().__init__()
        self.resize(800,800)
        self.setWindowTitle("Formulaire stylise")
        # Creation de l'ecran central
        widget= QWidget()
        layout= QVBoxLayout()
        # Creation du cadre
        cadre= QFrame()
        cadre.setFrameShape(QFrame.Shape.Box)
        cadre.setFrameShadow(QFrame.Shadow.Raised)
        # Contenu du cadre
        form_layout= QFormLayout()
        form_layout.addRow("Nom :",QLineEdit())
        form_layout.addRow("Prenom :",QLineEdit())
        sexe= QComboBox()
        sexe.addItems(["Homme","Femme"])
        form_layout.addRow("Sexe :", sexe)
        cadre.setLayout(form_layout)

        self.label= QLabel("Veuillez remplir ce formulaire")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.label)
        layout.addWidget(cadre)
        self.bouton = QPushButton("Valider")
        layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.bouton)

        widget.setLayout(layout)
        self.setCentralWidget(widget)
app= QApplication(sys.argv)
fenestra= fenetre()
fenestra.show()
sys.exit(app.exec())



