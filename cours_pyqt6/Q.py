from PyQt6.QtWidgets import QApplication, QLabel, QVBoxLayout, QWidget, QPushButton
from PyQt6.QtCore import QTimer
import sys

class Fenetre(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QTimer - Exemple")
        self.compteur = 0
        
        # Label pour afficher la valeur
        self.label = QLabel("Compteur : 0")

        # Boutons
        self.bouton_start = QPushButton("Démarrer")
        self.bouton_stop = QPushButton("Arrêter")

        # Timer
        self.timer = QTimer()
        self.timer.timeout.connect(self.incremente)

        # Connexions
        self.bouton_start.clicked.connect(lambda: self.timer.start(1000))
        self.bouton_stop.clicked.connect(self.timer.stop)

        # Layout
        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.bouton_start)
        layout.addWidget(self.bouton_stop)
        self.setLayout(layout)

    def incremente(self):
        self.compteur += 1
        self.label.setText(f"Compteur : {self.compteur}")

app = QApplication(sys.argv)
f = Fenetre()
f.show()
sys.exit(app.exec())