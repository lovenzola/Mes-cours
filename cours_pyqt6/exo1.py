import sys
from PyQt6.QtWidgets import QWidget, QApplication,QLabel,QPushButton, QLineEdit, QVBoxLayout

class Ma_fenetre(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Premier exercice")
        self.resize(800,500)
        self.label= QLabel("Bienvenue dans PyQt6",self)
        self.bouton= QPushButton("Changer le texte",self)
        self.bouton.clicked.connect(self.change_texte)
        self.bouton2= QPushButton("Fermer",self)
        self.bouton2.clicked.connect(self.close)
        
        layout= QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.bouton)
        layout.addWidget(self.bouton2)
        self.setLayout(layout)
    
    def change_texte(self):
        self.label.setText("Le texte a change")

        

if __name__ == "__main__":
    app= QApplication(sys.argv)
    ma_fenetre= Ma_fenetre()
    ma_fenetre.show()
    sys.exit(app.exec())
