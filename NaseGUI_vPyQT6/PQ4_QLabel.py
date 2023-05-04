import sys
from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel
from PyQt6.QtGui import QFont

class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle('Moja Druha Appka')
        # tlacitko =  QPushButton('STLAC')
        self.widget = QLabel(('HELLO'))
        self.widget.setFont(QFont('Impact', 30))



        # nastav velkost okna
        # self.setFixedSize(QSize(400,400))
        self.setMinimumSize(QSize(100,100))
        self.setMaximumSize(QSize(500, 500))

        # Nastav Centralny Widget
        self.setCentralWidget(self.widget)



app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()  # HLAVNY CYKLUS


