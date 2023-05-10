import sys
import time
from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle('Moja Appka')
        self.tlacitko = QPushButton('STLAC')
        # self.tlacitko.setCheckable(True)
        self.tlacitko.clicked.connect(self.tlacitko_bolo_stlacene)  # SLOT kde je FN
        # tlacitko.clicked.connect(self.tlacitko_bolo_prepnute)

        # nastav velkost
        # self.setFixedSize(QSize(400, 400))
        self.setMinimumSize(QSize(100,100))
        # self.setMaximumSize(QSize(640,480))

        # Nastav Centralny Widget
        self.setCentralWidget(self.tlacitko)

    def tlacitko_bolo_stlacene(self):
        print('STLACENE')
        self.tlacitko.setText('STLACENE TLACITKO')
        self.tlacitko.setEnabled(True)

        self.setWindowTitle('Moja jednotlacitkova aplikacia')



    def tlacitko_bolo_prepnute(self, checked):
        print('Prepnute ?', checked)
        self.tlacitko_prepnute = checked

app = QApplication(sys.argv)
window = MainWindow()
window.show()

app.exec()

# TODO Prestavka 20:10