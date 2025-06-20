from PyQt6.QtWidgets import(
    QWidget, QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QVBoxLayout, QFormLayout, QHBoxLayout,
    QFrame, QComboBox, QFileDialog
)
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import Qt
import sys

class application(QMainWindow):
    def __init__(self):
        super().__init__()
        self.resize(700,700)
        self.setWindowTitle("Essai interface Conception")

        central =QWidget()
        principal= QHBoxLayout()

        # Premiere frame
        formulaire= QFrame()
        formulaire.setFixedWidth(400)
        form= QFormLayout()
        form.addWidget(QLabel("Formulaire d'inscription"))
        form.addRow("Nom :", QLineEdit())
        form.addRow("Postnom :", QLineEdit())
        form.addRow("Prenom :",QLineEdit())
        form.addRow("Matricule :", QLineEdit())
        sexe= QComboBox()
        sexe.addItems(["Femme","Homme"])
        form.addRow("Sexe :",sexe)
        promotion= QComboBox()
        promotion.addItems(["L1 LMD FASI","L1 LMD FASE","L1 LMD DROIT","L1 LMD THEOLOGIE","G0 MEDECINE "])
        form.addRow("Promotion :", promotion)
        bouton= QPushButton("Concevoir la carte")
        bouton.clicked.connect(self.concevoir)
        form.addRow(bouton)
        formulaire.setLayout(form)
        # Deuxieme frame
        carte= QFrame()
        carte.setFixedHeight(400)
        image= QVBoxLayout()
        texte= QLabel("Apercu de la carte")
        texte.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_image= QLabel()
        self.label_image.setPixmap(QPixmap()) # Pour initialiser une image vide
        self.label_image.resize(150,150)
        self.label_image.setScaledContents(True)
        image.addWidget(texte)
        image.addWidget(self.label_image)
        carte.setLayout(image)

        principal.addWidget(formulaire)
        principal.addWidget(carte)
        central.setLayout(principal)
        self.setCentralWidget(central)
    def concevoir(self):
        image, _ = QFileDialog.getOpenFileName(
            self,
            "Choix une image",
            "",
            "Images (*.JPG *.PNG);; Tous les fichiers(*)"
        )
        chemin = QPixmap(image)
        if image:
            self.label_image.setPixmap(chemin.scaled(self.label_image.size()))

app= QApplication(sys.argv)
fenetre= application()
fenetre.show()
sys.exit(app.exec())        

        