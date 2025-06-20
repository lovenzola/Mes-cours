import sys
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QStackedWidget, QVBoxLayout,
    QHBoxLayout, QPushButton, QLabel, QLineEdit, QMessageBox,
    QDialog, QStatusBar, QMenuBar, QMenu
)
from PyQt6.QtGui  import QAction
from PyQt6.QtCore import Qt

# Fenêtre secondaire : Confirmation
class DialogConfirmation(QDialog):
    def __init__(self, message):
        super().__init__()
        self.setWindowTitle("Confirmation")
        self.setFixedSize(300, 100)

        layout = QVBoxLayout()
        layout.addWidget(QLabel(message))
        btn = QPushButton("OK")
        btn.clicked.connect(self.accept)
        layout.addWidget(btn)
        self.setLayout(layout)

# Page 1 : Étudiants
class PageEtudiants(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        layout.addWidget(QLabel("Page des étudiants"))
        self.setLayout(layout)

# Page 2 : Paiements
class PagePaiements(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        layout.addWidget(QLabel("Page des paiements"))
        self.setLayout(layout)

# Page 3 : Cartes
class PageCartes(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        layout.addWidget(QLabel("Page des cartes d'étudiant"))
        self.setLayout(layout)

# Fenêtre principale
class FenetrePrincipale(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Application Étudiants")
        self.setFixedSize(800, 600)

        self.stack = QStackedWidget()
        self.page1 = PageEtudiants()
        self.page2 = PagePaiements()
        self.page3 = PageCartes()

        self.stack.addWidget(self.page1)
        self.stack.addWidget(self.page2)
        self.stack.addWidget(self.page3)

        # Boutons de navigation
        nav_layout = QHBoxLayout()
        btn1 = QPushButton("Étudiants")
        btn1.clicked.connect(lambda: self.stack.setCurrentWidget(self.page1))
        btn2 = QPushButton("Paiements")
        btn2.clicked.connect(lambda: self.stack.setCurrentWidget(self.page2))
        btn3 = QPushButton("Cartes")
        btn3.clicked.connect(lambda: self.stack.setCurrentWidget(self.page3))
        nav_layout.addWidget(btn1)
        nav_layout.addWidget(btn2)
        nav_layout.addWidget(btn3)

        layout = QVBoxLayout()
        layout.addLayout(nav_layout)
        layout.addWidget(self.stack)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

        self.init_menu()
        self.setStatusBar(QStatusBar(self))

    def init_menu(self):
        menubar = self.menuBar()
        fichier = menubar.addMenu("Fichier")

        action_confirmer = QAction("Confirmer", self)
        action_confirmer.triggered.connect(self.afficher_dialogue)
        fichier.addAction(action_confirmer)

        quitter = QAction("Quitter", self)
        quitter.triggered.connect(self.close)
        fichier.addAction(quitter)

    def afficher_dialogue(self):
        dlg = DialogConfirmation("Voulez-vous vraiment continuer ?")
        dlg.exec()

# Fenêtre de connexion
class FenetreConnexion(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Connexion")
        self.setFixedSize(300, 150)

        self.user_input = QLineEdit()
        self.pass_input = QLineEdit()
        self.pass_input.setEchoMode(QLineEdit.EchoMode.Password)

        btn = QPushButton("Se connecter")
        btn.clicked.connect(self.verifier_connexion)

        layout = QVBoxLayout()
        layout.addWidget(QLabel("Nom d'utilisateur :"))
        layout.addWidget(self.user_input)
        layout.addWidget(QLabel("Mot de passe :"))
        layout.addWidget(self.pass_input)
        layout.addWidget(btn)

        self.setLayout(layout)

    def verifier_connexion(self):
        user = self.user_input.text()
        mdp = self.pass_input.text()
        if user == "admin" and mdp == "123":
            self.main = FenetrePrincipale()
            self.main.show()
            self.close()
        else:
            QMessageBox.critical(self, "Erreur", "Identifiants incorrects")

# Lancer l'app
if __name__ == "__main__":
    app = QApplication(sys.argv)
    login = FenetreConnexion()
    login.show()
    sys.exit(app.exec())