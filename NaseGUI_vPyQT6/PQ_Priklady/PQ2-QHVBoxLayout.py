import sys
from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import *
from PyQt6.QtGui import QPalette, QColor


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle('Moja Appka')

        layout = QVBoxLayout()
        layout.setSpacing(0)
        layout.setContentsMargins(0,0,0,0)

        sub_layout = QHBoxLayout()
        sub_layout.setSpacing(5)
        sub_layout.setContentsMargins(5, 5, 5, 5)
        sub_layout.addWidget(Color('cyan'))
        sub_layout.addWidget(Color('magenta'))
        sub_layout.addWidget(Color('yellow'))
        sub_layout.addWidget(Color('black'))

        layout.addWidget(Color('red'))
        layout.addLayout(sub_layout)
        layout.addWidget(Color('green'))
        layout.addWidget(Color('blue'))


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