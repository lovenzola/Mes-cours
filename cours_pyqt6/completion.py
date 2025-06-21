from PyQt6.QtWidgets import QWidget, QLabel, QLineEdit, QCompleter, QVBoxLayout, QApplication
from PyQt6.QtCore import Qt
import sys

class completion(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(500,500)
        self.setWindowTitle("Un petit exercice")
        contenu= QVBoxLayout()
        suggestions= ["Love", "Joyce", "Hope", "Parfaite", "Salem"]
        self.completer= QCompleter(suggestions)
        self.completer.setCaseSensitivity(Qt.CaseSensitivity.CaseInsensitive)
        champ = QLineEdit()
        champ.setPlaceholderText("Tapez un prenom feminin")
        champ.setCompleter(self.completer)
        contenu.addWidget(champ)
        self.setLayout(contenu)

app= QApplication(sys.argv)
fenetre= completion()
fenetre.show()
sys.exit(app.exec())

