from PyQt6.QtWidgets import QWidget, QMainWindow, QPushButton, QLineEdit, QApplication, QVBoxLayout,  QLabel, QSpinBox, QDoubleSpinBox, QDateEdit, QSlider, QDial
import sys
from PyQt6.QtCore import Qt, QDate

class application(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Un essai ")
        self.resize(500,500)
        central= QWidget()
        layout= QVBoxLayout()
        # Ajout d'un calendrier avec Qdateedit()
        layout.addWidget(QLabel("Date de naissance"))
        self.date_naissance= QDateEdit()
        self.date_naissance.setCalendarPopup(True)
        self.date_naissance.setDate(QDate.currentDate())
        layout.addWidget(self.date_naissance)
        # Qdoublespinbox
        layout.addWidget(QLabel("Montant paye :"))
        self.montant= QDoubleSpinBox()
        self.montant.setPrefix("$")
        self.montant.setDecimals(2)
        self.montant.setRange(0.0, 1000.0)
        self.montant.setSingleStep(5.0)
        layout.addWidget(self.montant)
        bouton= QPushButton("Voir la progression")
        bouton.clicked.connect(self.progression)
        layout.addWidget(bouton)
        # Qslider
        layout.addWidget(QLabel("Progression"))
        self.reglage= QSlider(Qt.Orientation.Horizontal)
        self.reglage.setRange(0,1000)
        self.reglage.setValue(50)
        layout.addWidget(self.reglage)
        
        
        # Qdial 
        layout.addWidget(QLabel("Reglage"))
        self.dial= QDial()
        self.dial.setValue(50)
        layout.addWidget(self.dial)
        central.setLayout(layout)
        self.setCentralWidget(central)

    def progression(self):
        valeur = self.montant.value()
        self.reglage.setValue(int(valeur))
        self.dial.setValue(int(valeur))
app= QApplication(sys.argv)
fenetre= application()
fenetre.show()
sys.exit(app.exec())

    