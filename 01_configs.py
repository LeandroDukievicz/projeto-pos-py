from PyQt6.QtWidgets import QApplication, QWidget
from PyQt6.QtGui import QIcon
import sys

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Projeto Leandro Dukiévicz")
        self.setGeometry(300, 110, 950, 650)
        self.setWindowIcon(QIcon("ability.png"))
    
        self.setStyleSheet("""
            background: qlineargradient(
                spread:pad, 
                x1:0, y1:0, x2:0, y2:1,
                stop:0 #010221, 
                stop:1 #13678A);
        """)
        
        self.setWindowOpacity(.95)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())
