from PyQt6.QtWidgets import (
    QWidget, QApplication, QLabel, QVBoxLayout, QLineEdit, QGroupBox, QPushButton, QMainWindow, QFormLayout,
    QComboBox
)
from PyQt6.QtCore import Qt
import sys

class application(QMainWindow):
    def __init__(self):
        super().__init__()
        self.resize(400,400)
        # Widget central
        central= QWidget()
        layout_princ= QVBoxLayout()

        # groupe principal
        principal= QGroupBox("Formulaire d'inscription")
        layout= QFormLayout()
        # Groupe 1:
        group_infos= QGroupBox("Authentification")
        formulaire= QFormLayout()
        formulaire.addRow("Nom:",QLineEdit())
        formulaire.addRow("Prenom :",QLineEdit())
        formulaire.addRow("Mot de Passe :", QLineEdit())
        group_infos.setLayout(formulaire)

        # Groupe 2
        group_rens= QGroupBox("Renseignements")
        form= QFormLayout()
        form.addRow("Faculte :", QLineEdit())
        promotion= QComboBox()
        promotion.addItems(["L1","L2","L3","L4"])
        form.addRow("Promotion :",promotion)
        group_rens.setLayout(form)

        layout.addRow(group_infos)
        layout.addRow(group_rens)
        principal.setLayout(layout)
        
        layout_princ.addWidget(principal)
        
        central.setLayout(layout_princ)
        self.setCentralWidget(central)
app= QApplication(sys.argv)
fenetre= application()
fenetre.show()
sys.exit(app.exec())
        
