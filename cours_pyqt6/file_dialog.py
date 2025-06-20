from PyQt6.QtWidgets import (
    QWidget, QApplication, QLabel, QPushButton, QFileDialog, QVBoxLayout, QLineEdit
)
import sys 
class fenetre(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(400,400)

        layout= QVBoxLayout()
        self.bouton= QPushButton("Ouvrir fichier")
        self.bouton.clicked.connect(self.ouvrir)
        self.bouton1= QPushButton("Choisir un dossier")
        self.label= QLabel("Aucun fichier selectionné")
        self.entree= QLabel("Entrez le chemin du dossier:")
        self.chemin= QLineEdit()
        self.bouton1.clicked.connect(self.choisir)
        layout.addWidget(self.bouton)
        layout.addWidget(self.label)
        layout.addWidget(self.entree)
        layout.addWidget(self.chemin)
        layout.addWidget(self.bouton1)
        self.setLayout(layout)
    
    def ouvrir(self):
        # Variable ,_ parce que le chemin renvoie deux valeurs et cela signifie qu'on ne prend que le chemin du fichier
        fichier, _ = QFileDialog.getOpenFileName(
            self,
            "Ouvrir un fichier", # Le titre du dialogue
            "",   # Dossier par defaut 
            "Tous les fichiers (*)" # Acces a tous les fichiers : "PDF Files", "Images(*.png, *.jpg, ...);; Tous les fichiers(*)"
        )
        if fichier :
            self.label.setText(f"Fichier selectionne : {fichier}")
    def choisir(self):
        fichier = QFileDialog.getExistingDirectory(
            self,
            "Choisir un fichier",
            ""
        )
        if fichier :
            self.chemin.setText(fichier)
        else: 
            print("Fichier inexistant")

app= QApplication(sys.argv)
fenestra= fenetre()
fenestra.show()
sys.exit(app.exec())