from PyQt6.QtWidgets import (
    QApplication, QWidget, QLabel, QLineEdit, QTextEdit, QTableWidget, QTableWidgetItem, QCheckBox, QPushButton,
    QRadioButton, QComboBox, QListWidget
)
from PyQt6.QtGui import QPixmap
import sys
class interface(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Essai d'interface")
        self.resize(800,800)
        self.setStyleSheet("background-color: lightsteelblue")
        self.interface()
    def interface(self):
        # Image comprise dans le label
        self.logo= QLabel(self)
        self.logo.setPixmap(QPixmap("C:\Exercice_projet\icone_femme.jpg"))
        self.logo.setGeometry(20,10,50,50)
        self.logo.setScaledContents(True)
        # Le titre
        self.titre= QLabel("Inscription d'etudiant",self)
        self.titre.setGeometry(100,30, 300,30)
        # Champ a remplir
        # Nom
        self.nom= QLabel("Nom:",self)
        self.nom.setGeometry(30,80,50,20)
        self.texte_nom= QLineEdit(self)
        self.texte_nom.setGeometry(100,80,100,20)
        # Postnom
        self.postnom= QLabel("Postnom:",self)
        self.postnom.setGeometry(30,140,50,20)
        self.texte_postnom= QLineEdit(self)
        self.texte_postnom.setGeometry(100,140,100,20)
        # Matricule
        self.matricule= QLabel("Matricule:",self)
        self.matricule.setGeometry(30,180,50,20)
        self.texte_matricule= QLineEdit(self)
        self.texte_matricule.setGeometry(100,180,100,20)
        # Sexe 
        self.sexe= QLabel("Sexe:",self)
        self.sexe.setGeometry(30,220,50,20)
        self.radio1= QRadioButton("Masculin",self)
        self.radio1.setGeometry(130,220,70,20)
        self.radio2= QRadioButton("Feminin",self)
        self.radio2.setGeometry(230,220,70,20)

        # Promotion
        self.promo= QLabel("Promotion:",self)
        self.promo.setGeometry(30,260,70,20)
        self.promo_choix= QComboBox(self)
        self.promo_choix.addItems(["L1","L2","L3","L4"])
        self.promo_choix.setGeometry(120,260,70,20)

        # Description 
        self.description= QLabel("Description",self)
        self.description.setGeometry(30,300,70,20)
        self.texte_description= QTextEdit(self)
        self.texte_description.setGeometry(120,300,200,20)

        # Inscription checkbox ne donne qu'un choix
        self.inscrit= QCheckBox("Inscrit",self)
        self.inscrit.setGeometry(30,340,70,20)
        
        # Bouton
        self.enregistrer= QPushButton("Enregistrer",self)
        self.enregistrer.setGeometry(150,340,70,20)

        # Liste de cours
        self.cours= QLabel("Cours:",self)
        self.cours.setGeometry(30,380,50,20)
        self.liste_cours = QListWidget(self)
        self.liste_cours.addItems(["Python","C","HTML-CSS-JS","Electronique"])
        self.liste_cours.setGeometry(100,380,100,100)

        # Tableau etudiants
        self.tableau= QLabel("Tableau etudiant",self)
        self.tableau.setGeometry(300,500,100,20)
        self.etudiants= QTableWidget(self)
        self.etudiants.setGeometry(50,540,300,400)
        self.etudiants.setColumnCount(3)
        self.etudiants.setRowCount(3)
        self.etudiants.setHorizontalHeaderLabels(["Nom","Postnom","Matricucle"])
        self.etudiants.setItem(0,0, QTableWidgetItem("Nzola"))
        self.etudiants.setItem(0,1, QTableWidgetItem("Samba"))
        self.etudiants.setItem(0,2, QTableWidgetItem("si013724"))
        self.etudiants.setItem(1,0, QTableWidgetItem("Kotalo"))
        self.etudiants.setItem(1,1, QTableWidgetItem("Samba"))
        self.etudiants.setItem(1,2, QTableWidgetItem("ae013724"))
        self.etudiants.setItem(2,0, QTableWidgetItem("Bembida"))
        self.etudiants.setItem(2,1, QTableWidgetItem("Samba"))
        self.etudiants.setItem(2,2, QTableWidgetItem("dr013724"))

if __name__ == "__main__":
    app= QApplication([])
    fenetre= interface()
    fenetre.show()
    sys.exit(app.exec())

        




        


