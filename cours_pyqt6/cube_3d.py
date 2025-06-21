import sys
import os
from PyQt6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QLabel, QProgressBar
)
from PyQt6.QtCore import QTimer, Qt
from PyQt6.QtGui import QPixmap

class AnimationAccueil(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Chargement")
        self.setGeometry(100, 100, 400, 400)

        # Layout principal
        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Label pour simuler l’animation du cube 3D
        self.image_label = QLabel()
        self.image_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.image_label.setFixedSize(200, 200)
        layout.addWidget(self.image_label)

        # Barre de progression
        self.progress_bar = QProgressBar()
        self.progress_bar.setRange(0, 100)
        self.progress_bar.setValue(0)
        layout.addWidget(self.progress_bar)

        # Titre (caché au début)
        self.titre = QLabel("CARD GENERATOR")
        self.titre.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.titre.setStyleSheet("font-size: 24px; font-weight: bold; color: #3498db;")
        self.titre.hide()
        layout.addWidget(self.titre)

        self.setLayout(layout)

        # Liste des images du cube (tu dois les avoir dans le même dossier)
        self.images = [f"cube{i}.png" for i in range(1, 9)]  # cube1.png à cube8.png
        self.current_image = 0

        # Timer pour animation
        self.animation_timer = QTimer()
        self.animation_timer.timeout.connect(self.animer_cube)
        self.animation_timer.start(150)  # change chaque 150 ms

        # Timer pour progression
        self.progress_value = 0
        self.progress_timer = QTimer()
        self.progress_timer.timeout.connect(self.augmenter_progression)
        self.progress_timer.start(50)  # chaque 100 ms

    def animer_cube(self):
        image_path = self.images[self.current_image % len(self.images)]
        if os.path.exists(image_path):
            pixmap = QPixmap(image_path).scaled(200, 200, Qt.AspectRatioMode.KeepAspectRatio)
            self.image_label.setPixmap(pixmap)
        self.current_image += 1

    def augmenter_progression(self):
        if self.progress_value <= 100:
            self.progress_bar.setValue(self.progress_value)
            self.progress_value += 2
        else:
            self.progress_timer.stop()
            self.animation_timer.stop()
            self.image_label.hide()
            self.titre.show()

# Lancer l'application
app = QApplication(sys.argv)
fenetre = AnimationAccueil()
fenetre.show()
sys.exit(app.exec())