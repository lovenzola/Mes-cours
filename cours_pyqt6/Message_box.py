import sys
from PyQt6.QtWidgets import (
    QApplication, QWidget, QLabel, QLineEdit, QPushButton,
    QVBoxLayout, QMessageBox
)

class Formulaire(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Exemple de QMessageBox")
        self.setGeometry(100, 100, 300, 200)

        # Widgets
        self.label_nom = QLabel("Nom :")
        self.input_nom = QLineEdit()

        self.bouton_valider = QPushButton("Valider")
        self.bouton_erreur = QPushButton("Simuler Erreur")
        self.bouton_quitter = QPushButton("Quitter")

        # Connexions
        self.bouton_valider.clicked.connect(self.valider)
        self.bouton_erreur.clicked.connect(self.simuler_erreur)
        self.bouton_quitter.clicked.connect(self.quitter)

        # Layout
        layout = QVBoxLayout()
        layout.addWidget(self.label_nom)
        layout.addWidget(self.input_nom)
        layout.addWidget(self.bouton_valider)
        layout.addWidget(self.bouton_erreur)
        layout.addWidget(self.bouton_quitter)
        self.setLayout(layout)

    def valider(self):
        nom = self.input_nom.text().strip()
        if not nom:
            QMessageBox.warning(self, "Champs vide", "Veuillez entrer le nom.")
        else:
            QMessageBox.information(self, "Succès", f"L'étudiant {nom} a été enregistré.")

    def simuler_erreur(self):
        QMessageBox.critical(self, "Erreur critique", "Une erreur interne s’est produite !")

    def quitter(self):
        reponse = QMessageBox.question(
            self, "Confirmation", "Voulez-vous vraiment quitter ?",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
        )
        if reponse == QMessageBox.StandardButton.Yes:
            self.close()

# Lancer l’application
app = QApplication(sys.argv)
form = Formulaire()
form.show()
sys.exit(app.exec())