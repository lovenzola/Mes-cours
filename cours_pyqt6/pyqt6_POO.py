# Approche avec de l'orienté objet: elle permet de reutiliser le code definit sur la classe mère
# On commence par definir la classe mere qui doit etre instanciée avec le module qui sera utilisé 
#--------------------------------------------------------------------------------------------------------------------
#  Approche de POO avec les fenetres
#---------------------------------------------------------------------------------------------------------------------
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QLineEdit
import sys
class mywindow(QWidget):
    def __init__(self, fenetre):
        super().__init__()  # Les elts heritent des l'instance QWidget
        self.fenetre= fenetre
# On aura plus à recreer la fenetre puis que les elts de la classe herite deja de QWidget
    def create_fenetre(self):
        self.fenetre.setWindowTitle("UNE FENETRE VOILA QUOI")
        self.fenetre.setGeometry(100,100,400,300)
#----------------------------------------------------------------------------------------------------------------------
#           AJOUT D'UN LABEL
#---------------------------------------------------------------------------------------------------------------------
        self.label= QLabel(self.fenetre)
        self.label.setGeometry(50,80,300,50)
        self.label.setText("Un label en POO voila quoi")
        self.label.setStyleSheet("color:white; background: black; font-size: 22px")
#---------------------------------------------------------------------------------------------------------------------
#                  AJOUT D'UNE ZONE DE TEXTE
#---------------------------------------------------------------------------------------------------------------------
        self.zone_texte= QLineEdit(self.fenetre)
        self.zone_texte.setGeometry(30,30, 250,30)
        self.zone_texte.setStyleSheet("background: white; border-radius:3; color: blue; font-size: 14px;")

    def ajout_background(self,color):
        self.fenetre.setStyleSheet("background: "+ color + ";")
    
# Le label etant dans la fenetre, nul besoin d'afficher le label puisqu'il est deja compris dans la fenetre
if __name__== "__main__":
    app= QApplication(sys.argv)
    root= QWidget() # On crée la fenetre
    ma_fenetre= mywindow(root) # la classe recoit cela en parametres
    ma_fenetre.create_fenetre()
    ma_fenetre.ajout_background("bisque")
    
    root.show()
    sys.exit(app.exec())

    

