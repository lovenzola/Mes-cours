import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QTableView
from PyQt6.QtCore import Qt, QAbstractTableModel

class MonModele(QAbstractTableModel):
    def __init__(self):
        super().__init__()
        # Nos données : liste de listes
        self.donnees = [
            ["Alice", 20, "L1 FASI"],
            ["Bob", 22, "L2 FASE"],
            ["Charlie", 21, "L1 DROIT"],
        ]

    def rowCount(self, parent=None):
        return len(self.donnees)

    def columnCount(self, parent=None):
        if self.donnees:
            return len(self.donnees[0])
        return 0

    def data(self, index, role=Qt.ItemDataRole.DisplayRole):
        if role == Qt.ItemDataRole.DisplayRole:
            ligne = index.row()
            colonne = index.column()
            return str(self.donnees[ligne][colonne])
        return None

class Fenetre(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Exemple QAbstractTableModel")
        self.resize(400, 300)

        self.table = QTableView()
        self.modele = MonModele()
        self.table.setModel(self.modele)

        self.setCentralWidget(self.table)

app = QApplication(sys.argv)
fenetre = Fenetre()
fenetre.show()
sys.exit(app.exec())