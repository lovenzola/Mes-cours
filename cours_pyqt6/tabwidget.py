from PyQt6.QtWidgets import QMainWindow,QWidget, QApplication, QLabel, QTabWidget, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout, QFormLayout
import sys
from PyQt6.QtCore import Qt
class application(QMainWindow):
    def __init__(self):
        super().__init__()
        self.resize(800,800)
        self.setWindowTitle("Une presque application")

        # Creation d'un widget central et son layout
        central= QWidget()
        layout_princ= QVBoxLayout()
        # Creation du tabwidget
        self.tab= QTabWidget()

        # Ajout des onglets : contenant un titre et des widgets propres

        onglet_etudiant = QWidget()
        layout_et= QVBoxLayout()
        label= QLabel("Enregistrement")
        label.setStyleSheet("width: 100; max-height: 15;")
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout_et.addWidget(label)
        layout_et.addWidget(QLineEdit("Nom :"))
        layout_et.addWidget(QLineEdit("Prenom :"))
        onglet_etudiant.setLayout(layout_et)

        onglet_paiement= QWidget()
        layout_pay= QVBoxLayout()
        labele= QLabel("Enregistrement Paiement")
        labele.setStyleSheet("width: 100; max-height: 15;")
        labele.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout_pay.addWidget(labele)
        layout_pay.addWidget(QLineEdit("Nom :"))
        layout_pay.addWidget(QLineEdit("Montant :"))
        onglet_paiement.setLayout(layout_pay)

        # Ajout des onglets crees 
        self.tab.addTab(onglet_etudiant,"Etudiant")
        self.tab.addTab(onglet_paiement,"Paiement")

        # Ajout dans le layout principal 
        layout_princ.addWidget(self.tab)
        central.setLayout(layout_princ)
        self.tab.setCurrentIndex(1)
        self.setCentralWidget(central)
        

app= QApplication(sys.argv)
fenetre= application()
fenetre.show()
sys.exit(app.exec())




