from PyQt6.QtWidgets import (
    QApplication, QWidget, QLabel, QLineEdit, QRadioButton,
    QComboBox, QTextEdit, QPushButton, QListWidget,
    QVBoxLayout, QHBoxLayout, QGridLayout
)
import sys

class FormulaireEtudiant(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Inscription Étudiant")
        self.resize(600, 400)
        self.init_ui()

    def init_ui(self):
        # Widgets de base
        self.nom_input = QLineEdit()
        self.prenom_input = QLineEdit()

        self.radio_homme = QRadioButton("Homme")
        self.radio_femme = QRadioButton("Femme")

        self.promo_combo = QComboBox()
        self.promo_combo.addItems(["Licence 1", "Licence 2", "Licence 3"])

        self.adresse_input = QTextEdit()

        self.liste_etudiants = QListWidget()

        self.bouton_enregistrer = QPushButton("Enregistrer")
        self.bouton_reset = QPushButton("Réinitialiser")
        self.bouton_fermer = QPushButton("Fermer")

        # Layout sexe
        layout_sexe = QHBoxLayout()
        layout_sexe.addWidget(self.radio_homme)
        layout_sexe.addWidget(self.radio_femme)

        # Layout grille pour formulaire
        layout_formulaire = QGridLayout()
        layout_formulaire.addWidget(QLabel("Nom :"), 0, 0)
        layout_formulaire.addWidget(self.nom_input, 0, 1)

        layout_formulaire.addWidget(QLabel("Prénom :"), 1, 0)
        layout_formulaire.addWidget(self.prenom_input, 1, 1)

        layout_formulaire.addWidget(QLabel("Sexe :"), 2, 0)
        layout_formulaire.addLayout(layout_sexe, 2, 1)

        layout_formulaire.addWidget(QLabel("Promotion :"), 3, 0)
        layout_formulaire.addWidget(self.promo_combo, 3, 1)

        layout_formulaire.addWidget(QLabel("Adresse :"), 4, 0)
        layout_formulaire.addWidget(self.adresse_input, 4, 1)

        # Layout boutons
        layout_boutons = QHBoxLayout()
        layout_boutons.addWidget(self.bouton_enregistrer)
        layout_boutons.addWidget(self.bouton_reset)
        layout_boutons.addStretch()

        # Layout principal vertical
        layout_principal = QVBoxLayout()
        layout_principal.addLayout(layout_formulaire)
        layout_principal.addLayout(layout_boutons)
        layout_principal.addWidget(QLabel("Liste des étudiants :"))
        layout_principal.addWidget(self.liste_etudiants)
        layout_principal.addWidget(self.bouton_fermer)

        self.setLayout(layout_principal)

        # Connexions basiques
        self.bouton_enregistrer.clicked.connect(self.enregistrer)
        self.bouton_reset.clicked.connect(self.reinitialiser)
        self.bouton_fermer.clicked.connect(self.close)

    def enregistrer(self):
        nom = self.nom_input.text()
        prenom = self.prenom_input.text()
        sexe = "Homme" if self.radio_homme.isChecked() else "Femme" if self.radio_femme.isChecked() else "?"
        promo = self.promo_combo.currentText()

        if nom and prenom:
            ligne = f"{nom} {prenom} - {sexe} - {promo}"
            self.liste_etudiants.addItem(ligne)
            self.reinitialiser()
    def reinitialiser(self):
        self.nom_input.clear()
        self.prenom_input.clear()
        self.radio_homme.setChecked(False)
        self.radio_femme.setChecked(False)
        self.promo_combo.setCurrentIndex(0)
        self.adresse_input.clear()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    fen = FormulaireEtudiant()
    fen.show()
    sys.exit(app.exec())