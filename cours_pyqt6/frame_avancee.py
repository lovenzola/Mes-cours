import sys
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QFrame
)
from PyQt6.QtCore import Qt

class FenetreStructurée(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Combinaison de 3 QFrames")
        self.setGeometry(150, 150, 600, 400)

        widget = QWidget()
        layout_principal = QVBoxLayout()

        # 1️⃣ Partie haute avec deux cadres côte à côte
        cadre_haut = QHBoxLayout()

        cadre_gauche = QFrame()
        cadre_gauche.setFrameShape(QFrame.Shape.Box)
        cadre_gauche.setFrameShadow(QFrame.Shadow.Sunken)

        layout_gauche = QVBoxLayout()
        layout_gauche.addWidget(QLabel("Nom"))
        layout_gauche.addWidget(QLineEdit())
        layout_gauche.addWidget(QLabel("Email"))
        layout_gauche.addWidget(QLineEdit())
        cadre_gauche.setLayout(layout_gauche)

        cadre_droit = QFrame()
        cadre_droit.setFrameShape(QFrame.Shape.Box)
        cadre_droit.setFrameShadow(QFrame.Shadow.Sunken)

        layout_droit = QVBoxLayout()
        layout_droit.addWidget(QLabel("Âge"))
        layout_droit.addWidget(QLineEdit())
        layout_droit.addWidget(QLabel("Pays"))
        layout_droit.addWidget(QLineEdit())
        cadre_droit.setLayout(layout_droit)

        cadre_haut.addWidget(cadre_gauche)
        cadre_haut.addWidget(cadre_droit)

        # 2️⃣ Cadre bas (indépendant)
        cadre_bas = QFrame()
        cadre_bas.setFrameShape(QFrame.Shape.Panel)
        cadre_bas.setFrameShadow(QFrame.Shadow.Raised)

        layout_bas = QHBoxLayout()
        layout_bas.addWidget(QPushButton("Valider"))
        layout_bas.addWidget(QPushButton("Annuler"))
        layout_bas.setAlignment(Qt.AlignmentFlag.AlignCenter)

        cadre_bas.setLayout(layout_bas)

        # Ajout au layout principal
        layout_principal.addLayout(cadre_haut)
        layout_principal.addWidget(cadre_bas)

        widget.setLayout(layout_principal)
        self.setCentralWidget(widget)

app = QApplication(sys.argv)
fenetre = FenetreStructurée()
fenetre.show()
sys.exit(app.exec())