from PyQt6.QtWidgets  import QWidget, QLabel, QLineEdit, QDialog, QVBoxLayout, QPushButton, QApplication, QMainWindow
import sys

class dialogue(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Dialogue d'enregistrement")
        self.setFixedSize(300,300)
        layout= QVBoxLayout()
        self.nom= QLineEdit()
        self.prenom= QLineEdit()
        layout.addWidget(QLabel("Entrez  votre nom :"))
        layout.addWidget(self.nom)
        layout.addWidget(QLabel("Entrez votre prenom :"))
        layout.addWidget(self.prenom)
        bouton= QPushButton("Fermer")
        bouton.clicked.connect(self.accept)
        layout.addWidget(bouton)
        self.setLayout(layout)
    def afficher_texte(self):
        return f"L'etudiant {self.nom.text()} {self.prenom.text()}"

class fenetre(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Fenetre principale")
        self.resize(500,500)
        self.label= QLabel("Authentifiez-vous")
        self.bouton= QPushButton("Go")
        self.bouton.clicked.connect(self.authentifier)
        self.labele= QLabel("")
        layout= QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.bouton)
        layout.addWidget(self.labele)
        container= QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)
    def authentifier(self):
        authentification= dialogue()
        if authentification.exec():
            resultat= authentification.afficher_texte()
            self.labele.setText(resultat)
app= QApplication(sys.argv)
application= fenetre()
application.show()
sys.exit(app.exec())