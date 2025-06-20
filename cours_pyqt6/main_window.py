from PyQt6.QtWidgets import (
    QWidget, QMainWindow, QApplication, QVBoxLayout, QLabel, QStatusBar, QPushButton,
    QMenuBar, QToolBar
) 
from PyQt6.QtGui import QAction
import sys
class container(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Un exerice tout bete")
        self.setGeometry(100,100,300,300)
        central= QWidget()
        central_contain= QVBoxLayout()
        central_contain.addWidget(QLabel("Fenêtre principale"))
        bouton= QPushButton("Afficher")
        bouton.clicked.connect(self.afficher)
        central_contain.addWidget(bouton)


        central.setLayout(central_contain) # La fenetre est rajoute a la fenetre centrale
        self.setCentralWidget(central)
        # Ajout d'un statusbar: barre d'en dessous
        self.setStatusBar(QStatusBar(self))
        self.statusBar().showMessage("Application lancee")
        # Ajout d'un menu
        # Creation d'un menu bar
        menu= self.menuBar()
        # Ajout des elements du menu et sous menus
        menu_fichier= menu.addMenu("Fichier") # elements
        action_quitter = QAction("Quitter",self) # sous menu
        action_quitter.triggered.connect(self.close)  # Action lié au sous menu
        menu_fichier.addAction(action_quitter)
        #--------------------------------------------------------------------------------------------
        menu_aide= menu.addMenu("Aide")
        action_aide= QAction("A propos",self)
        action_aider= QAction("Quitter",self)
        action_aider.triggered.connect(self.close)
        action_aide.triggered.connect(self.apropos)
        menu_aide.addAction(action_aide)
        menu_aide.addSeparator()
        menu_aide.addAction(action_aider)
        # LES TOOLBARS : barre d'outils
        barre_outil= QToolBar("Barre d'outils")
        self.addToolBar(barre_outil)
        ouvrir= QAction("Ouvrir",self)
        ouvrir.triggered.connect(lambda: self.afficher_texte("Fichier ouvert"))
        barre_outil.addAction(ouvrir)
    def afficher(self):
        self.statusBar().showMessage("Vous avez clique")
    def apropos(self):
        self.statusBar().showMessage("Ce n'est qu'un exercice boss")
    def afficher_texte(self,texte):
        self.statusBar().showMessage(f"{texte}")
app= QApplication(sys.argv)
fenetre= container()
fenetre.show()
sys.exit(app.exec())