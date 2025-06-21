from PyQt6.QtWidgets import(
    QWidget, QApplication, QLabel, QPushButton, QLineEdit, QVBoxLayout, QMainWindow, QDialog
)
from PyQt6.QtCore import QTimer, Qt
import sys
class jeu (QDialog):
    def __init__(self):
        super().__init__()
        self.setStyleSheet(
            """
            background-color: aliceblue;
            font-size : 12px;
            font-weight: bold;
            """
        )
        self.operation()
    def operation(self):
        principal = QVBoxLayout()
        self.compteur = QVBoxLayout()
        self.resultat= None
        self.label_compte= QLabel("Compte à rebours : 5")
        self.label_compte.setStyleSheet("color : red; font-size: 14px;")
        self.compteur.addWidget(self.label_compte)
        self.comptage= 5
        self.rebours= QTimer()
        self.rebours.timeout.connect(self.incrementer)
        self.rebours.start(1000)
        jeu= QVBoxLayout()
        label= QLabel("Combien font 5 fois 5")
        label.setStyleSheet("font-size: 14px;")
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        jeu.addWidget(label)
        self.repondra= QLineEdit()
        
        validation= QPushButton("Envoyer")
        validation.clicked.connect(self.valider)
        jeu.addWidget(self.repondra)
        jeu.addWidget(validation)
        principal.addLayout(self.compteur)
        principal.addLayout(jeu)
        self.setLayout(principal)
    def incrementer(self):
        self.label_compte.setText(f"Compte à rebours : {self.comptage}")
        self.comptage -= 1
        if self.comptage <-1:
            self.rebours.stop()
            self.resultat = "timeout"
            self.accept()
    def valider (self):
        self.repondre= self.repondra.text()
        self.rebours.stop()

        if self.repondre == "25":
            self.resultat= "valide"
        else: 
            self.resultat = "non_valide"
        self.accept()
class reglement(QDialog):
    def __init__(self):
        super().__init__()
        self.setStyleSheet(
            """
            background-color: thistle;
            padding :5px;
            font-size: 14px;
            font-weight: bold;
            }
            """
        )
        self.setWindowTitle("Les regles !!!")
        self.setFixedSize(400,400)
        container= QVBoxLayout()
        self.label= QLabel("Il n'y a qu'une regle!  ")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label2 =QLabel("Vous avez 5 secondes pour placer la bonne reponse!!")
        self.label.setStyleSheet("font-size: 14px;")
        self.reponse= QLabel("Votre reponse apparaitra ici !!")
        self.reponse.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.message= QLabel("En attente de votre reponse")
        self.message.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.message.setStyleSheet("border: 1px solid; border-radius: 3px;")
        self.bouton= QPushButton("Commencer")
        self.bouton.clicked.connect(self.jeu)
        container.addWidget(self.label)
        container.addWidget(self.label2)
        container.addWidget(self.reponse)
        container.addWidget(self.message)
        container.addWidget(self.bouton)
        container.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.setLayout(container)
    def jeu(self): 
        ope= jeu()
        ope.exec()
        if ope.resultat == "valide":
            self.message.setText(f" {ope.repondre} : Reponse validee")
            self.message.setStyleSheet("border: 1px solid; border-radius: 3px;color: green;")
            self.bouton.setText("Continuer")
        elif ope.resultat == "non_valide":
            self.message.setText(f"{ope.repondre} : Reponse non validee")
            self.message.setStyleSheet("border: 1px solid; border-radius: 3px;color: blue;")
            self.bouton.setText("Reessayer")
        elif  ope.resultat == "timeout":
            
            self.message.setText("Delai depassé")
            self.message.setStyleSheet("border: 1px solid; border-radius: 3px;color: red;")
            self.bouton.setText("Reessayer")

        
class compte_rebours(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QUIZ !!!")
        self.resize(400,400)
        self.setStyleSheet(
            """
            background-color: lightsteelblue;
            font-size: 22;
            color : whitesmoke;
            font-weight: bold;
            QPushButton {
                border : 1.5px solid black;
                border-radius: 4px;
                font-size: 18px;
            }
            
            """
        )

        principale= QWidget()
        self.central= QVBoxLayout()
        self.central.setAlignment(Qt.AlignmentFlag.AlignCenter)
        label= QLabel("Bienvenue dans le Sablier")
        label.setStyleSheet("font-size: 24px;")
        self.central.addWidget(label)
        self.bouton= QPushButton("LES REGLES")
        self.bouton.clicked.connect(self.reglement)
        self.central.addWidget(self.bouton)
        principale.setLayout(self.central)
        self.setCentralWidget(principale)
    def reglement(self):
        regles= reglement()
        regles.exec()  # Pour executer

app= QApplication(sys.argv)
fenetre= compte_rebours()
fenetre.show()
sys.exit(app.exec())

