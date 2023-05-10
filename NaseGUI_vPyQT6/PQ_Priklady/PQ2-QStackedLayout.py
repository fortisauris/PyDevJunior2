import sys
from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import *
from PyQt6.QtGui import QPalette, QColor


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle('Moja Appka')

        # tlacitka
        tlacitko1 = QPushButton("R")
        tlacitko2 = QPushButton("G")
        tlacitko3 = QPushButton("B")

        # signaly a sloty
        tlacitko1.pressed.connect(self.zmen_cervenu)
        tlacitko2.pressed.connect(self.zmen_zelenu)
        tlacitko3.pressed.connect(self.zmen_modru)

        layout = QVBoxLayout()
        layout.addWidget(tlacitko1)
        layout.addWidget(tlacitko2)
        layout.addWidget(tlacitko3)


        self.sublayout = QStackedLayout()
        self.sublayout.addWidget(Color('red'))  # index 0
        self.sublayout.addWidget(Color('green'))  # index 2
        self.sublayout.addWidget(Color('blue'))
        # default value
        self.sublayout.setCurrentIndex(0)

        layout.addLayout(self.sublayout)



        widget = QWidget()
        widget.setLayout(layout)

        # Nastav Centralny Widget
        self.setCentralWidget(widget)

    def zmen_modru(self):
        self.sublayout.setCurrentIndex(2)

    def zmen_zelenu(self):
        self.sublayout.setCurrentIndex(1)

    def zmen_cervenu(self):
        self.sublayout.setCurrentIndex(0)



class Color(QWidget):

    def __init__(self, color):
        super(Color, self).__init__()
        self.setAutoFillBackground(True)

        palette = self.palette()
        palette.setColor(QPalette.ColorRole.Window, QColor(color))
        self.setPalette(palette)


app = QApplication(sys.argv)
window = MainWindow()
window.show()

app.exec()

#  Prestavka do 20:12