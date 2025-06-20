from PyQt6.QtWidgets import QApplication, QWidget, QLabel
import sys

class interface(QWidget):
    def __init__(self, fenetre):
        super().__init__()
        self.fenetre = fenetre

    def create_fenetre(self):
        self.fenetre.setWindowTitle("Un petit exercice")
        self.fenetre.setGeometry(100,100,800,500)
    
    def ajout_background(self,color):
        self.fenetre.setStyleSheet("background: "+color+";")

if __name__ == "__main__":
    app= QApplication(sys.argv)
    ma_fenetre= QWidget()
    interface1= interface(ma_fenetre)
    interface1.create_fenetre()
    interface1.ajout_background("violet")
    ma_fenetre.show()
    sys.exit(app.exec())