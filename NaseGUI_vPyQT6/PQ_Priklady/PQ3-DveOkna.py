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
        self.w1 = DalsieOkno()
        self.w2 = DalsieOkno()
        self.setWindowTitle('Moja Appka')
        l = QVBoxLayout()

        self.tlacitko1 = QPushButton('STLAC')
        # tlacitko1.clicked.connect(self.prepni_okno1)  # PRVA VERZIA
        # DRUHA VERZIA
        self.tlacitko1.clicked.connect(
            lambda checked: self.prepni_okno(self.w1)
        )
        l.addWidget(self.tlacitko1)

        self.tlacitko2 = QPushButton('STLAC')
        #tlacitko2.clicked.connect(self.prepni_okno2)
        self.tlacitko2.clicked.connect(
            lambda checked: self.prepni_okno(self.w2)
        )
        l.addWidget(self.tlacitko2)

        w = QWidget()
        w.setLayout(l)
        # Nastav Centralny Widget
        self.setCentralWidget(w)

    def prepni_okno(self, window):
        print(window)
        print(type(window))
        print(dir(window))
        if window.isVisible():
            window.hide()
        else:
            window.show()


'''
    def prepni_okno1(self, checked):
        print(checked)
        if self.w1.isVisible():
            self.w1.hide()
        else:
            self.w1.show()

    def prepni_okno2(self, checked):
        print(checked)
        if self.w2.isVisible():
            self.w2.hide()
        else:
            self.w2.show()
'''




app = QApplication(sys.argv)
window = MainWindow()
window.show()

app.exec()

# Prestavka do 20:10

# PyQt6 Designer je sucastou balika pyqt6-tools
designer = r'venv\Lib\site-packages\qt6-applications\Qt\bin\designer.exe'

ui_compiler = 'pyuic design.ui -o MainWin.py'