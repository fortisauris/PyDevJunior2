import sys
import time
from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QLineEdit, QVBoxLayout, QWidget


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle('Moja Appka')
        self.label = QLabel()  # Nadpis v okne
        self.vstup = QLineEdit()
        self.tlacitko = QPushButton()
        # vysli signal
        self.vstup.textChanged.connect(self.label.setText)  # SLOT kde menime text

        # definujeme vzhlad
        layout = QVBoxLayout()
        layout.addWidget(self.vstup)
        layout.addWidget(self.tlacitko)
        layout.addWidget(self.label)

        kontajner = QWidget()
        kontajner.setLayout(layout)

        # Nastav Centralny Widget
        self.setCentralWidget(kontajner)

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