import sys
from PyQt6.QtCore import QSize, Qt, QDate, QTime
from PyQt6.QtWidgets import *
from PyQt6.QtGui import QAction, QIcon


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle('Moja Appka')

        label = QLabel('HELLO')  # nadpis v okne
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.setCentralWidget(label)

        toolbar = QToolBar('NASTROJE')
        toolbar.setIconSize(QSize(30,30))
        self.addToolBar(toolbar)
        # TA1
        tlacitkova_akcia = QAction(QIcon('cc.jpg'), 'Moje Tlacitko', self)
        tlacitkova_akcia.setCheckable(True)
        tlacitkova_akcia.setStatusTip('Moja tlacitkova akcia')
        #TA2
        tlacitkova_akcia2 = QAction(QIcon('cc.jpg'),'DruheTlacitko', self)
        tlacitkova_akcia2.setCheckable(True)
        tlacitkova_akcia2.setStatusTip('Moja tlacitkova akcia')

        menu = self.menuBar()
        # FILE MENU
        file_menu = menu.addMenu('&File')
        file_menu.addAction(tlacitkova_akcia)
        file_menu.addSeparator()
        file_menu.addAction(tlacitkova_akcia2)
        file_submenu = file_menu.addMenu('SUBMENU')
        file_submenu.addAction(tlacitkova_akcia)
        file_submenu.addAction(tlacitkova_akcia2)

        # EDIT MENU
        file_menu = menu.addMenu('&Edit')
        file_menu.addAction(tlacitkova_akcia)
        file_menu.addSeparator()
        file_menu.addAction(tlacitkova_akcia2)
        file_submenu = file_menu.addMenu('SUBMENU')
        file_submenu.addAction(tlacitkova_akcia)
        file_submenu.addAction(tlacitkova_akcia2)



        # SIGNALY
        tlacitkova_akcia.triggered.connect(self.toolbar_click)   # SIGNAL
        tlacitkova_akcia2.triggered.connect(self.toolbar_click)  # SIGNAL


        toolbar.addAction(tlacitkova_akcia)
        toolbar.addAction(tlacitkova_akcia2)
        toolbar.addWidget(QCheckBox())

        self.setStatusBar(QStatusBar(self))

    def toolbar_click(self, signal):
        print('click', signal)





app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()  # HLAVNY CYKLUS


# TODO Prestacka do 19:55

