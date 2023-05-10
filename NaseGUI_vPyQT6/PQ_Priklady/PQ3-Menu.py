import sys
from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import *
from PyQt6.QtGui import QAction, QIcon



class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle('Moja Appka')
        label = QLabel('Hello')
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.setCentralWidget(label)

        toolbar = QToolBar('Nase Hlavne nastroje')
        self.addToolBar(toolbar)

        tlacitkova_akcia = QAction('Moje Tlacitko', self)
        tlacitkova_akcia.setCheckable(True)
        tlacitkova_akcia.setStatusTip('Toto je moje tlacitko')

        tlacitkova_akcia.triggered.connect(self.toolbar_click)
        toolbar.addAction(tlacitkova_akcia)


    def toolbar_click(self, signal):
        print('click', signal)


app = QApplication(sys.argv)
window = MainWindow()
window.show()

app.exec()