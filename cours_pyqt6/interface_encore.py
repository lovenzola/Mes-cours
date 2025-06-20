from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QLabel, QPushButton, QLineEdit, QTableWidget, QTableWidgetItem,
    QListWidget, QGroupBox, QFormLayout, QStatusBar, QFrame
)
from PyQt6.QtGui import QFont, QPixmap
from PyQt6.QtCore import Qt
import sys

class InterfaceEtudiant(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Cartes Étudiants+")
        self.setMinimumSize(1000, 600)

        # ======== Widget central ========
        central_widget = QWidget()
        central_layout = QVBoxLayout(central_widget)
        self.setCentralWidget(central_widget)

        # ======== En-tête ========
        header = QLabel("📚 Cartes Étudiants+")
        header.setAlignment(Qt.AlignmentFlag.AlignLeft)
        header.setStyleSheet("background-color: #d0e7ff; font-size: 22px; font-weight: bold; padding: 10px;")
        central_layout.addWidget(header)

        # ======== Corps principal (Horizontal) ========
        main_body = QHBoxLayout()

        # ----- Menu de navigation -----
        navigation = QListWidget()
        navigation.addItems(["Étudiants", "Paiements", "Préconceptions", "Conceptions"])
        navigation.setFixedWidth(160)
        navigation.setStyleSheet("background-color: #f0f0f0; font-weight: bold;")
        main_body.addWidget(navigation)

        # ----- Contenu principal (tableau + formulaire) -----
        content_layout = QHBoxLayout()

        # -- Tableau des étudiants --
        table = QTableWidget(8, 2)
        table.setHorizontalHeaderLabels(["Nom", "Prénom"])
        data = [("Rachel", "Davis"), ("Samuel", "Wilson"), ("Hannah", "Brown"),
                ("Michael", "Taylor"), ("Anna", "Moore"), ("Joshua", "Anderson"),
                ("Emily", "Thomas"), ("Christopher", "Lee")]
        for i, (nom, prenom) in enumerate(data):
            table.setItem(i, 0, QTableWidgetItem(nom))
            table.setItem(i, 1, QTableWidgetItem(prenom))
        table.setStyleSheet("font-size: 13px;")
        table.setFixedWidth(400)
        content_layout.addWidget(table)

        # -- Formulaire à droite --
        right_side = QVBoxLayout()

        group_form = QGroupBox("Générer une carte")
        form_layout = QFormLayout()
        self.nom_input = QLineEdit()
        self.prenom_input = QLineEdit()
        self.date_input = QLineEdit()
        form_layout.addRow("Nom :", self.nom_input)
        form_layout.addRow("Prénom :", self.prenom_input)
        form_layout.addRow("Date de naissance :", self.date_input)
        group_form.setLayout(form_layout)
        right_side.addWidget(group_form)

        # -- Bouton Générer --
        btn_generate = QPushButton("🎫 Générer la carte")
        btn_generate.setStyleSheet("background-color: #80c1ff; padding: 8px; font-weight: bold;")
        right_side.addWidget(btn_generate)

        # -- Aperçu carte étudiant --
        group_preview = QGroupBox("Aperçu de la carte")
        preview_layout = QVBoxLayout()

        photo = QLabel()
        photo.setPixmap(QPixmap(100, 100))
        photo.setFixedSize(100, 100)
        photo.setStyleSheet("background-color: #ccc; border: 1px solid #999;")
        name_preview = QLabel("Emily Thomas")
        id_preview = QLabel("ID : 123456789")

        preview_layout.addWidget(photo, alignment=Qt.AlignmentFlag.AlignCenter)
        preview_layout.addWidget(name_preview, alignment=Qt.AlignmentFlag.AlignCenter)
        preview_layout.addWidget(id_preview, alignment=Qt.AlignmentFlag.AlignCenter)

        group_preview.setLayout(preview_layout)
        right_side.addWidget(group_preview)

        content_layout.addLayout(right_side)
        main_body.addLayout(content_layout)

        central_layout.addLayout(main_body)

        # ======== Barre de statut ========
        status = QStatusBar()
        status.showMessage("✅ 10 étudiants atteints | 🕓 Dernière génération : aujourd’hui")
        self.setStatusBar(status)

# Pour exécuter (à mettre à part si tu importes dans un autre script)
if __name__ == "__main__":
    app = QApplication(sys.argv)
    fenetre = InterfaceEtudiant()
    fenetre.show()
    sys.exit(app.exec())