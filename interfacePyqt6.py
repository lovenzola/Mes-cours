from PyQt6.QtWidgets import (
    QApplication, QWidget, QHBoxLayout, QVBoxLayout, QPushButton, QLabel, 
    QFrame, QSizePolicy
)
from PyQt6.QtCore import Qt, QPropertyAnimation, QRect
from PyQt6.QtGui import QPainter, QColor, QBrush

class BurgerButton(QPushButton):
    def __init__(self):
        super().__init__()
        self.setFixedSize(40, 30)
        self.setStyleSheet("background-color: transparent; border: none;")
    
    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)
        pen_color = QColor(255, 255, 255)
        brush = QBrush(pen_color)
        painter.setBrush(brush)
        painter.setPen(Qt.PenStyle.NoPen)
        # Draw 3 horizontal bars
        bar_height = 4
        spacing = 6
        for i in range(3):
            rect = QRect(5, 5 + i*(bar_height + spacing), self.width() - 10, bar_height)
            painter.drawRoundedRect(rect, 2, 2)

class SidePanel(QFrame):
    def __init__(self):
        super().__init__()
        self.setFixedWidth(200)
        self.setStyleSheet("background-color: #2c3e50;")  # Dark blue
        layout = QVBoxLayout()
        layout.setContentsMargins(20, 20, 20, 20)
        layout.setSpacing(15)
        # Add some buttons or labels for menu
        for text in ("Accueil", "Étudiants", "Paramètres", "Déconnexion"):
            btn = QPushButton(text)
            btn.setStyleSheet(
                """
                QPushButton {
                    color: white;
                    background-color: transparent;
                    border: none;
                    font-size: 16px;
                    text-align: left;
                    padding: 8px;
                }
                QPushButton:hover {
                    background-color: #34495e;
                    border-radius: 5px;
                }
                """
            )
            btn.setCursor(Qt.CursorShape.PointingHandCursor)
            layout.addWidget(btn)
        layout.addStretch()
        self.setLayout(layout)

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PyQt6 Menu Burger Animé")
        self.resize(800, 500)
        self.setStyleSheet("background-color: #ecf0f1;")  # Light gray

        # Header
        self.header = QFrame()
        self.header.setFixedHeight(50)
        self.header.setStyleSheet("background-color: #1a237e;")  # Blue dark
        header_layout = QHBoxLayout()
        header_layout.setContentsMargins(10, 0, 10, 0)
        header_layout.setSpacing(10)

        self.burger_btn = BurgerButton()
        self.burger_btn.clicked.connect(self.toggle_menu)

        header_label = QLabel("Gestion Étudiants")
        header_label.setStyleSheet("color: white; font-weight: bold; font-size: 18px;")
        header_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        header_layout.addWidget(self.burger_btn, alignment=Qt.AlignmentFlag.AlignLeft)
        header_layout.addWidget(header_label)
        header_layout.addStretch()
        self.header.setLayout(header_layout)

        # Side panel (menu)
        self.side_panel = SidePanel()
        self.side_panel.setGeometry(-200, 50, 200, self.height() - 50)  # Start hidden left

        # Main content
        self.main_content = QLabel("Bienvenue sur CARD GENERATOR !")
        self.main_content.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.main_content.setStyleSheet("font-size: 30px; color: #34495e;")

        # Layout
        main_layout = QVBoxLayout()
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.setSpacing(0)

        main_layout.addWidget(self.header)
        main_layout.addWidget(self.main_content, 1)

        self.setLayout(main_layout)

        # Animation setup
        self.menu_visible = False
        self.animation = QPropertyAnimation(self.side_panel, b"geometry")
        self.animation.setDuration(300)

        # Put side panel on top of main window
        self.side_panel.setParent(self)
        self.side_panel.show()

    def toggle_menu(self):
        if self.menu_visible:
            # Hide menu: slide left out of view
            start_rect = QRect(0, 50, 200, self.height() - 50)
            end_rect = QRect(-200, 50, 200, self.height() - 50)
        else:
            # Show menu: slide in from left
            start_rect = QRect(-200, 50, 200, self.height() - 50)
            end_rect = QRect(0, 50, 200, self.height() - 50)
        self.animation.stop()
        self.animation.setStartValue(start_rect)
        self.animation.setEndValue(end_rect)
        self.animation.start()
        self.menu_visible = not self.menu_visible

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())