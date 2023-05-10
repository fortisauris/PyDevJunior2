import sys
from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import *
from PyQt6.QtGui import QAction, QIcon


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle('Moja Appka')
        tlacitko = QPushButton('STLAC')
        # SIGNAL
        tlacitko.clicked.connect(self.button_click)

        # Nastav Centralny Widget
        self.setCentralWidget(tlacitko)

    def button_click(self, signal):
        #dlg = QMessageBox(self)
        #dlg.setWindowTitle('MAM OTAZKU')
        #dlg.setText('JE TOTO JEDNODUCHY DIALOG ?')
        #dlg.setStandardButtons(QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        #dlg.setIcon(QMessageBox.Icon.Question)
        #tlacitko = dlg.exec()
        #print(tlacitko)

        # I N Y   S P O S O B
        #tlacitko = QMessageBox.question(self, 'Otazka', 'Je na Marse zivot ?')
        #if tlacitko == QMessageBox.StandardButton.Yes:
        #    print(tlacitko,'NA MARSE JE ZIVOT')
        #else:
        #    print(tlacitko, 'NA MARSE NIE JE ZIVOT')

        # CRITICAL MSG
        tlacitko = QMessageBox.critical(self, 'POZOR', 'NIECO SA POKASLALO',
                                        buttons=QMessageBox.StandardButton.Discard | QMessageBox.StandardButton.NoToAll
                                                | QMessageBox.StandardButton.Ignore,
                                        defaultButton=QMessageBox.StandardButton.Discard
                                        )
        if tlacitko == QMessageBox.StandardButton.Discard:
            print('NEULOZ ZMENY')
        elif tlacitko == QMessageBox.StandardButton.NoToAll:
            print('NIE VSETKYM ZMENAM')
        else:
            print('IGNORUJ A POKRACUJ V PRACI')

app = QApplication(sys.argv)
window = MainWindow()
window.show()

app.exec()