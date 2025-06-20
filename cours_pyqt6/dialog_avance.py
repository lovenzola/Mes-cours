import sys
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QLabel, QPushButton,
    QDialog, QLineEdit, QComboBox, QFormLayout, QHBoxLayout
)

# ------- QDialog personnalisé -------
class FormulaireEtudiant(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Formulaire étudiant")
        self.setFixedSize(350, 200)

        # Champs du formulaire
        self.nom_input = QLineEdit()
        self.prenom_input = QLineEdit()
        self.sexe_input = QComboBox()
        self.sexe_input.addItems(["Homme", "Femme"])
        self.matricule_input = QLineEdit()

        # Layout du formulaire
        form_layout = QFormLayout()
        form_layout.addRow("Nom :", self.nom_input)
        form_layout.addRow("Prénom :", self.prenom_input)
        form_layout.addRow("Sexe :", self.sexe_input)
        form_layout.addRow("Matricule :", self.matricule_input)

        # Boutons
        bouton_valider = QPushButton("Valider")
        bouton_annuler = QPushButton("Annuler")
        bouton_valider.clicked.connect(self.accept)
        bouton_annuler.clicked.connect(self.reject)

        bouton_layout = QHBoxLayout()
        bouton_layout.addWidget(bouton_valider)
        bouton_layout.addWidget(bouton_annuler)

        # Layout principal
        layout = QVBoxLayout()
        layout.addLayout(form_layout)
        layout.addLayout(bouton_layout)

        self.setLayout(layout)

    def get_donnees(self):
        return {
            "nom": self.nom_input.text(),
            "prenom": self.prenom_input.text(),
            "sexe": self.sexe_input.currentText(),
            "matricule": self.matricule_input.text()
        }

# ------- Fenêtre principale -------
class FenetrePrincipale(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Interface principale")
        self.setGeometry(100, 100, 400, 300)

        self.label_info = QLabel("Aucun étudiant enregistré.")
        bouton_ouvrir_formulaire = QPushButton("Ajouter un étudiant")
        bouton_ouvrir_formulaire.clicked.connect(self.ouvrir_dialogue)

        layout = QVBoxLayout()
        layout.addWidget(self.label_info)
        layout.addWidget(bouton_ouvrir_formulaire)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def ouvrir_dialogue(self):
        dialogue = FormulaireEtudiant()
        if dialogue.exec():
            infos = dialogue.get_donnees()
            texte = f"Nom : {infos['nom']}\nPrénom : {infos['prenom']}\nSexe : {infos['sexe']}\nMatricule : {infos['matricule']}"
            self.label_info.setText(texte)

# ------- Lancer l'application -------
app = QApplication(sys.argv)
fenetre = FenetrePrincipale()
fenetre.show()
sys.exit(app.exec())