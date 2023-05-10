import sys
from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt6.QtGui import QFont, QPixmap


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle('Moja Appka')
        self.widget = QLabel('HELLO')
        self.widget.setFont(QFont('Impact', 30))

        font = self.widget.font()
        font.setPointSize(30)
        self.widget.setFont(font)
        self.widget.setAlignment(Qt.AlignmentFlag.AlignVCenter | Qt.AlignmentFlag.AlignHCenter)
        self.widget.setPixmap(QPixmap('coder.jpg'))

        # Nastav Centralny Widget
        self.setCentralWidget(self.widget)

app = QApplication(sys.argv)
window = MainWindow()
window.show()

app.exec()