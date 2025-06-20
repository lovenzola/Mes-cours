from PyQt6.QtWidgets import (
    QWidget, QApplication, QLabel, QLineEdit, QTextEdit, QListWidget, QPushButton,
    QRadioButton, QComboBox, QVBoxLayout, QHBoxLayout, QFormLayout, QMessageBox
)
import sys
class formulaire(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(100,100,500,500)
        self.setWindowTitle("Formulaire d'inscription")
        self.interface()
    def interface(self):
        form_principale= QFormLayout()
        # Entree texte
        self.nom= QLineEdit()
        self.prenom= QLineEdit()
        # Sexe
        self.masculin= QRadioButton("Masculin")
        self.feminin= QRadioButton("Feminin")
        sexe= QHBoxLayout()
        sexe.addWidget(self.masculin)
        sexe.addWidget(self.feminin)
        # Promotion
        self.promotion= QComboBox()
        self.promotion.addItems(["L1","L2","L3","L4"])
        # Adresse
        self.adresse= QTextEdit()
        # Remplissage du formulaire
        form_principale.addRow("Nom :",self.nom)
        form_principale.addRow("Prenom :",self.prenom)
        form_principale.addRow("Sexe:",sexe)
        form_principale.addRow("Promotion", self.promotion)
        form_principale.addRow("Adresse:",self.adresse)

        # Bouton
        self.bouton_save= QPushButton("Enregistrer")
        self.bouton_save.clicked.connect(self.enregistrer)
        self.bouton_renit= QPushButton("Renitialiser")
        self.bouton_renit.clicked.connect(self.renitialiser)
        bouton= QHBoxLayout()
        bouton.addStretch() # Pour positionner a droite
        bouton.addWidget(self.bouton_save)
        bouton.addWidget(self.bouton_renit)

        # Liste des etudiants
        self.liste_etudiant= QListWidget()
        # Bouton fermer
        self.fermer= QPushButton("Fermer")
        self.fermer.clicked.connect(self.fermer_app)
        # Ecran principale
        main= QVBoxLayout()
        main.addLayout(form_principale)
        main.addLayout(bouton)
        main.addWidget(QLabel("Etudiants enregistres"))
        main.addWidget(self.liste_etudiant)
        main.addWidget(self.fermer)
        self.setLayout(main)
    # Fonctions
    def enregistrer(self):
        nom= self.nom.text()
        prenom= self.prenom.text()
        sexe= "Homme" if self.masculin.isChecked else "Femme" if self.feminin.isChecked else "?"        
        promo= self.promotion.currentText()

        if nom and prenom:
            ligne= f"{nom} - {prenom} - {sexe} - {promo}"
            self.liste_etudiant.addItem(ligne)
            QMessageBox.information(self,"Notification",f"Etudiant {nom} enregistre avec succes!")
            self.renitialiser()
        else:
            QMessageBox.warning(self,"Erreur survenue","Veuillez les case nom et prenom")
    def renitialiser(self):
        self.nom.clear()
        self.prenom.clear()
        self.masculin.setChecked(False)
        self.feminin.setChecked(False)
        self.adresse.clear()
        self.promotion.setCurrentIndex(0)
    def fermer_app(self):
        reponse= QMessageBox.question(
            self, "Confirmation", "Voulez-vous quitter?",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
        )
        if reponse == QMessageBox.StandardButton.Yes:
            self.close()


app= QApplication(sys.argv)
interface= formulaire()
interface.show()
sys.exit(app.exec())





        