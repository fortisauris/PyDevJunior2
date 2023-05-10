import sys
import random
from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import *

class DalsieOkno(QWidget):

    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        self.label = QLabel('Ns Novy PIN je: % d' % random.randint(0, 9999))
        layout.addWidget(self.label)
        self.setLayout(layout)


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        # self.w = None # iba pre nove_okno2 a nove_okno3
        self.w = DalsieOkno()
        self.setWindowTitle('Moja Appka')
        tlacitko = QPushButton('STLAC')
        tlacitko.clicked.connect(self.nove_okno5)

        # Nastav Centralny Widget
        self.setCentralWidget(tlacitko)

    def nove_okno(self, checked):
        print(checked)
        self.w = DalsieOkno()
        self.w.show()

    def nove_okno2(self, checked):
        if self.w is None:
            self.w = DalsieOkno()
        self.w.show()

    def nove_okno3(self, checked):
        if self.w is None:
            self.w = DalsieOkno()
            self.w.show()
        else:
            self.w.close()  # korektne uzatvaranie okna
            self.w = None

    # PERSISTENTNE OKNO
    def nove_okno4(self, checked):
        self.w.show()

    # PERSISTENTNE OKNO SCHOVANE
    def nove_okno5(self, checked):
        if self.w.isVisible():
            self.w.hide()
        else:
            self.w.show()

app = QApplication(sys.argv)
window = MainWindow()
window.show()

app.exec()

# TODO Prestavka do 20:10