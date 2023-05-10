import sys
from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.tlacitko_prepnute = True

        self.setWindowTitle('Moja Appka')
        tlacitko = QPushButton('STLAC')
        tlacitko.setCheckable(True)  # toto robi prepinac
        tlacitko.clicked.connect(self.tlacitko_bolo_stlacene)  #
        tlacitko.clicked.connect(self.tlacitko_bolo_prepnute)

        # nastav velkost
        # self.setFixedSize(QSize(400, 400))
        self.setMinimumSize(QSize(100,100))
        # self.setMaximumSize(QSize(640,480))

        # Nastav Centralny Widget
        self.setCentralWidget(tlacitko)

    def tlacitko_bolo_stlacene(self):
        print('STLACENE')


    def tlacitko_bolo_prepnute(self, checked):
        print('Prepnute ?', checked)
        self.tlacitko_prepnute = checked

app = QApplication(sys.argv)
window = MainWindow()
window.show()

app.exec()