import sys
from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle('Moja Appka')
        tlacitko = QPushButton('STLAC')

        # nastav velkost
        # self.setFixedSize(QSize(400, 400))
        self.setMinimumSize(QSize(100,100))
        # self.setMaximumSize(QSize(640,480))

        # Nastav Centralny Widget
        self.setCentralWidget(tlacitko)

app = QApplication(sys.argv)
window = MainWindow()
window.show()

app.exec()