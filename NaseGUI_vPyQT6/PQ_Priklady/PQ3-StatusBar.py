import sys
from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import *
from PyQt6.QtGui import QAction, QIcon



class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle('Moja Appka')
        #  VNUTRO OKNA
        label = QLabel('Hello')
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.setCentralWidget(label)
        # TOOLBAR DEFINICIA
        toolbar = QToolBar('Nase Hlavne nastroje')
        toolbar.setIconSize(QSize(30,30))
        self.addToolBar(toolbar)
        # TLACITKOVE AKCIE DEFINICIA
        tlacitkova_akcia = QAction(QIcon('icon_cc.png'),'Moje Tlacitko', self)
        tlacitkova_akcia.setCheckable(True)
        tlacitkova_akcia.setStatusTip('Toto je moje tlacitko')

        tlacitkova_akcia2 = QAction(QIcon('icons_cc.png'), 'Moje Tlacitko 2', self)
        tlacitkova_akcia2.setCheckable(True)
        tlacitkova_akcia2.setStatusTip('Toto je moje tlacitko')
        # SIGNALY
        tlacitkova_akcia.triggered.connect(self.toolbar_click)
        tlacitkova_akcia2.triggered.connect(self.toolbar_click)
        # PRIDANIE TLACITKOVYCH AKCII DO TOOLBARU
        toolbar.addAction(tlacitkova_akcia)
        toolbar.addAction(tlacitkova_akcia2)
        # VECI NAVYSE V TOOLBARE
        toolbar.addWidget(QLabel('Hello'))
        toolbar.addWidget(QCheckBox())
        # STATUS BAR
        self.setStatusBar(QStatusBar(self))
        # MENU DEFINICIA
        menu = self.menuBar()
        # FILE MENU
        file_menu = menu.addMenu("&File")
        file_menu.addAction(tlacitkova_akcia)
        file_menu.addSeparator()
        file_menu.addAction(tlacitkova_akcia2)
        file_submenu = file_menu.addMenu('SUBMENU')
        file_submenu.addAction(tlacitkova_akcia)
        file_submenu.addAction(tlacitkova_akcia2)
        # EDIT MENU
        edit_menu = menu.addMenu('&Edit')
        edit_menu.addAction(tlacitkova_akcia)
        edit_menu.addSeparator()
        edit_menu.addAction(tlacitkova_akcia2)




    def toolbar_click(self, signal):
        print('click', signal)


app = QApplication(sys.argv)
window = MainWindow()
window.show()

app.exec()