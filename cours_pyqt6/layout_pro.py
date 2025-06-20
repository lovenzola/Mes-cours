from PyQt6.QtWidgets import (
    QApplication, QWidget, QLabel, QLineEdit, QRadioButton, QComboBox,
    QTextEdit, QListWidget, QPushButton, QFormLayout, QHBoxLayout,
    QVBoxLayout
)
import sys

class FenetreInscription(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Formulaire d'inscription")
        self.setGeometry(200, 100, 500, 400)
        self.setStyleSheet("Background-color: lightsteelblue;")
        # Champs de texte
        self.nom_input = QLineEdit()
        self.prenom_input = QLineEdit()

        # Sexe (radio buttons dans un layout horizontal)
        self.homme_radio = QRadioButton("Homme")
        self.femme_radio = QRadioButton("Femme")
        sexe_layout = QHBoxLayout()
        sexe_layout.addWidget(self.homme_radio)
        sexe_layout.addWidget(self.femme_radio)

        # ComboBox Promotion
        self.promo_combo = QComboBox()
        self.promo_combo.addItems(["L1", "L2", "L3", "Master", "Doctorat"])

        # Adresse (multiligne)
        self.adresse_input = QTextEdit()

        # Liste des étudiants
        self.liste_etudiants = QListWidget()

        # Boutons
        self.btn_enregistrer = QPushButton("Enregistrer")
        self.btn_reinitialiser = QPushButton("Réinitialiser")

        # Connexions des boutons
        self.btn_enregistrer.clicked.connect(self.enregistrer)
        self.btn_reinitialiser.clicked.connect(self.reinitialiser)

        # --- Organisation des layouts ---

        # Layout du formulaire (FormLayout)
        form_layout = QFormLayout()
        form_layout.addRow("Nom :", self.nom_input)
        form_layout.addRow("Prénom :", self.prenom_input)
        form_layout.addRow("Sexe :", sexe_layout)
        form_layout.addRow("Promotion :", self.promo_combo)
        form_layout.addRow("Adresse :", self.adresse_input)

        # Layout des boutons (HBox)
        bouton_layout = QHBoxLayout()
        bouton_layout.addStretch()  # pousse les boutons à droite
        bouton_layout.addWidget(self.btn_enregistrer)
        bouton_layout.addWidget(self.btn_reinitialiser)

        # Layout principal (VBox)
        main_layout = QVBoxLayout()
        main_layout.addLayout(form_layout)
        main_layout.addLayout(bouton_layout)
        main_layout.addWidget(QLabel("Étudiants enregistrés :"))
        main_layout.addWidget(self.liste_etudiants)

        self.setLayout(main_layout)

    def enregistrer(self):
        nom = self.nom_input.text().strip()
        prenom = self.prenom_input.text().strip()
        sexe = "Homme" if self.homme_radio.isChecked() else "Femme" if self.femme_radio.isChecked() else "Non spécifié"
        promo = self.promo_combo.currentText()

        if nom and prenom:
            ligne = f"{nom} {prenom} - {sexe} ({promo})"
            self.liste_etudiants.addItem(ligne)
            self.reinitialiser()
        else:
            print("Nom ou prénom manquant")

    def reinitialiser(self):
        self.nom_input.clear()
        self.prenom_input.clear()
        self.homme_radio.setChecked(False)
        self.femme_radio.setChecked(False)
        self.promo_combo.setCurrentIndex(0)
        self.adresse_input.clear()

# Lancement
app = QApplication(sys.argv)
fen = FenetreInscription()
fen.show()
sys.exit(app.exec())