import sys
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QPushButton,
    QLabel, QStackedWidget, QHBoxLayout, QLineEdit, QFormLayout,QGridLayout
)
from PyQt6.QtCore import Qt
class interface(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Une fenetre evolutive")
        self.setGeometry(100,100,500,500)
        #  On cree le stack: empilateurs des pages
        self.pages= QStackedWidget()
        # On cree les pages: Appelable par une fonction
        self.accueil= self.afficher_accueil()  
        self.paiement= self.afficher_paiement()
        self.pages.addWidget(self.accueil)
        self.pages.addWidget(self.paiement)
        # Partie navigation
        nav= QWidget()
        navigation= QHBoxLayout()
        bouton1= QPushButton("Accueil")
        bouton1.clicked.connect(lambda: self.pages.setCurrentIndex(0)) # Affiche la premiere page
        bouton2= QPushButton("Paiment")
        bouton2.clicked.connect(lambda: self.pages.setCurrentIndex(1)) # Affiche la deuxieme page
        navigation.addWidget(bouton1)
        navigation.addWidget(bouton2)
        navigation.setAlignment(Qt.AlignmentFlag.AlignCenter)
        nav.setLayout(navigation)

        # Ecran principal
        ecran= QWidget()
        element= QGridLayout()
        element.addWidget(self.pages,1,0,)
        element.addWidget(nav,0,0)
        ecran.setLayout(element)
        self.setCentralWidget(ecran)
    def afficher_accueil(self):
        page= QWidget()
        page.setWindowTitle("Inscription")
        element= QGridLayout()
        nom= QLineEdit()
        element.addWidget(QLabel("Nom:"),0,0)
        element.addWidget(nom,0,1)
        prenom= QLineEdit()
        element.addWidget(QLabel("Prenom: "),1,0)
        element.addWidget(prenom,1,1)
        page.setLayout(element)
        return page
    def afficher_paiement(self):
        page= QWidget()
        page.setWindowTitle("Inscription")
        element= QGridLayout()
        nom= QLineEdit()
        element.addWidget(QLabel("Nom:"),0,0)
        element.addWidget(nom,0,1)
        montant= QLineEdit()
        element.addWidget(QLabel("Montant: "),1,0)
        element.addWidget(montant,1,1)
        page.setLayout(element)
        return page
app= QApplication(sys.argv)
fenetre= interface()
fenetre.show()

sys.exit(app.exec())