import sys
from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import *
from PyQt6.QtGui import QPalette, QColor


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle('Moja Appka')

        layout = QGridLayout()
        layout.addWidget(Color('red'), 0,0)
        layout.addWidget(Color('green'), 1,1)
        layout.addWidget(Color('blue'), 2, 2)

        layout.addWidget(Color('cyan'), 0,2)
        layout.addWidget(Color('green'), 1, 0)

        layout.addWidget(QLabel('NADPIS'), 0,1)
        layout.addWidget(QPushButton('OK'), 3,0)

        widget = QWidget()
        widget.setLayout(layout)



        # Nastav Centralny Widget
        self.setCentralWidget(widget)

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

# TODO Prestavka do 20:12