import sys
from PyQt6.QtCore import QSize, Qt, QDate, QTime
from PyQt6.QtWidgets import *


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.tlacitko_prepnute = True

        self.setWindowTitle('Moja Appka')

        self.label = QLabel()  # nadpis v okne
        self.vstup = QLineEdit()
        self.tlacitko = QPushButton()
        self.tlacitko.setCheckable(True)

        # SIGNALY EVENTOV
        self.vstup.textChanged.connect(self.label.setText)  # vysielam signal z VSTUPU aMENIM LABEL
        self.tlacitko.clicked.connect(self.tlacitko_bolo_stlacene)  # signal pre tlacitko aby vykonal funkciu
        self.tlacitko.clicked.connect(self.tlacitko_bolo_prepnute)

        # VZHLAD
        layout = QVBoxLayout()  # vertikalna skatulka
        layout.addWidget(self.vstup)
        layout.addWidget(self.tlacitko)
        layout.addWidget(self.label)

        # CENTRALNY WIDGET
        kontajner = QWidget()
        kontajner.setLayout(layout)   # definujes

        # Nastav Centralny Widget
        self.setCentralWidget(kontajner)

    def tlacitko_bolo_stlacene(self, checked):
        print('STLACENE')
        self.tlacitko.setText(str(checked))
        self.tlacitko.setEnabled(True)

        self.setWindowTitle('MOJA JEDNOTLACITKOVA APPKA')

    def tlacitko_bolo_prepnute(self, checked):
        print('PREPNUTE', checked)
        self.tlacitko.setText(str(checked))
        self.tlacitko_prepnute = checked

        self.setWindowTitle('MOJA JEDNOTLACITKOVA APPKA')



app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()  # HLAVNY CYKLUS


