import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QProgressBar, QPushButton
from PyQt6.QtCore import QTimer

class ExempleProgress(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Progression en cours...")
        self.resize(300, 150)

        self.layout = QVBoxLayout()

        self.progress = QProgressBar()
        self.progress.setMinimum(0)
        self.progress.setMaximum(100)
        self.progress.setValue(0)

        self.bouton = QPushButton("Démarrer")
        self.bouton.clicked.connect(self.demarrer)

        self.layout.addWidget(self.progress)
        self.layout.addWidget(self.bouton)
        self.setLayout(self.layout)

        self.timer = QTimer()
        self.timer.timeout.connect(self.charger)

        self.valeur = 0

    def demarrer(self):
        self.valeur = 0
        self.timer.start(100)  # 100 ms entre chaque incrément

    def charger(self):
        if self.valeur <= 100:
            self.progress.setValue(self.valeur)
            self.valeur += 5
        else:
            self.timer.stop()

app = QApplication(sys.argv)
fenetre = ExempleProgress()
fenetre.show()
sys.exit(app.exec())