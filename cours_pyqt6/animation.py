
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout
from PyQt6.QtCore import QPropertyAnimation, QRect, QSize, QPoint, QEasingCurve, QSequentialAnimationGroup, QParallelAnimationGroup
import sys

class AnimationDemo(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Animation complète - PyQt6")
        self.resize(500, 400)

        self.bouton = QPushButton("0")
        self.bouton.setFixedSize(100, 40)
        self.bouton.setStyleSheet("background-color: thistle;")
        self.bouton.clicked.connect(self.lancer_animations)

        layout = QVBoxLayout()
        layout.addWidget(self.bouton)
        self.setLayout(layout)

    def lancer_animations(self):
        animations = QSequentialAnimationGroup()

        # 1. Geometry (position + taille)
        anim1 = QPropertyAnimation(self.bouton, b"geometry")
        anim1.setDuration(1000)
        anim1.setStartValue(QRect(200, 50, 100, 40))
        anim1.setEndValue(QRect(250, 150, 150, 60))
        anim1.setEasingCurve(QEasingCurve.Type.InOutCubic)

        # 2. Taille seulement
        anim2 = QPropertyAnimation(self.bouton, b"size")
        anim2.setDuration(800)
        anim2.setStartValue(QSize(150, 60))
        anim2.setEndValue(QSize(100, 40))
        self.bouton.setText("90")
        # 3. Position uniquement
        anim3 = QPropertyAnimation(self.bouton, b"pos")
        anim3.setDuration(800)
        anim3.setStartValue(QPoint(500, 150))
        anim3.setEndValue(QPoint(50, 200))
        self.bouton.setText("180")

        # 4. Opacité (transparence)
        anim4 = QPropertyAnimation(self.bouton, b"windowOpacity")
        anim4.setDuration(800)
        anim4.setStartValue(1.0)
        anim4.setEndValue(0.3)

        # 5. Taille minimale
        anim5 = QPropertyAnimation(self.bouton, b"minimumSize")
        anim5.setDuration(1000)
        anim5.setStartValue(QSize(100, 40))
        anim5.setEndValue(QSize(200, 60))

        animations.addAnimation(anim1)
        animations.addAnimation(anim2)
        animations.addAnimation(anim3)
        animations.addAnimation(anim4)
        animations.addAnimation(anim5)
        animations.start()
        self.anime= animations

app = QApplication(sys.argv)
demo = AnimationDemo()
demo.show()
sys.exit(app.exec())