import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QTableView
from PyQt6.QtGui import QStandardItemModel, QStandardItem

class Fenetre(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Exemple QTableView avec modèle MVC")
        self.resize(500, 300)

        central = QWidget()
        layout = QVBoxLayout()

        # Création du modèle
        self.modele = QStandardItemModel()
        self.modele.setHorizontalHeaderLabels(["Nom", "Postnom", "Âge"])
        
        # Ajouter quelques lignes
        ligne1 = [QStandardItem("Love"), QStandardItem("Nzola"), QStandardItem("20")]
        ligne2 = [QStandardItem("Samba"), QStandardItem("Chéri"), QStandardItem("22")]
        self.modele.appendRow(ligne1)
        self.modele.appendRow(ligne2)

        # Vue : QTableView
        self.table = QTableView()
        self.table.setModel(self.modele)

        layout.addWidget(self.table)
        central.setLayout(layout)
        self.setCentralWidget(central)

app = QApplication(sys.argv)
fen = Fenetre()
fen.show()
sys.exit(app.exec())