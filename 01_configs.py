from PyQt6.QtWidgets import QApplication, QWidget
from PyQt6.QtGui import QIcon
import sys

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Projeto Leandro Dukiévicz")
        self.setGeometry(400, 250, 850, 450)
        self.setWindowIcon(QIcon("ability.png"))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())
