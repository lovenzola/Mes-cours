import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton
app= QApplication(sys.argv) # Contient les fenetres et composantes
fenetre= QWidget()
fenetre.setWindowTitle("Ma premiere fenetre")
# Recois 4 valeurs: vertical, horizontal, largeur, hauteur
fenetre.setGeometry(100,100,400,500)

 # Pour afficher la fenêtre
label= QLabel(fenetre)
label.setText("Voila un premier texte bien chill")
label.setGeometry(50,50,300,450)
label.show()
#-------------------------------------------------------------------------------------------------------------------
zone_texte= QLineEdit(fenetre)
zone_texte.setGeometry(30,30,200,30)
# On peut definir une fonction à la zone de texte
# Cette fonction permet de recuperer ce qui est ecrit dans la zone de texte
def action():
    texte= zone_texte.text()
    print(texte)
#--------------------------------------------------------------------------------------------------------------------
zone_texte.textChanged.connect(action) # permet d'executer la fonction
zone_texte.show()
#-------------------------------------------------------------------------------------------------------------------
#  LES BOUTONS
#----------------------------------------------------------------------------------------------------------------------
bouton= QPushButton(fenetre)
bouton.setText("Envoyer")
bouton.setGeometry(233,30,70,30)
#------------------------------------------------------------------------------------------------------------------
def envoyer():
    print("Message envoyé avec succès")

bouton.clicked.connect(envoyer) # lorsque le bouton est cliqué, il est connecté à l'action
fenetre.show()
sys.exit(app.exec()) # Pour executer l'application
