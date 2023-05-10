import sys
from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import *


class MainWindow(QMainWindow):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.setWindowTitle('Moja Appka')
        tlacitko = QPushButton('STLAC NA VYVOLANIE DIALOGOVEHO OKNA')
        tlacitko.clicked.connect(self.button_click)

        # Nastav Centralny Widget
        self.setCentralWidget(tlacitko)

    def button_click(self, signal):
        # dlg = QDialog(self)
        # dlg.setWindowTitle('HELLO')
        # dlg.exec()
        dlg = CustomDialog()
        if dlg.exec():
            print('USPECH')
        else:
            print('NEUSPECH')

class CustomDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('HELLO')

        QBtn = QDialogButtonBox.StandardButton.Ok | QDialogButtonBox.StandardButton.Cancel

        self.buttonBox = QDialogButtonBox(QBtn)
        # SIGNALY
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)

        self.layout = QVBoxLayout()
        msg = QLabel('NIECO SA POKAZILO')
        self.layout.addWidget(msg)
        self.layout.addWidget(self.buttonBox)
        self.setLayout(self.layout)


app = QApplication(sys.argv)
window = MainWindow()
window.show()

app.exec()