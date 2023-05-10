import sys
import time
from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QLineEdit, QVBoxLayout, QWidget


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle('Moja Appka')
        self.label = QLabel('KLIKNI NA TOTO OKNO !')  # Nadpis v okne

        # Nastav Centralny Widget
        self.setCentralWidget(self.label)

    def mouseMoveEvent(self, event):
        self.label.setText('MYS SA HYBE')
        pos = event.position()
        print(pos.x(), pos.y())

    def mousePressEvent(self, event):
        self.label.setText('KLIK !')

    def mouseReleaseEvent(self, event):
        self.label.setText('KLIKNI NA TOTO OKNO !')

    def mouseDoubleClickEvent(self, event):
        self.label.setText('DVOJKLIK !')




app = QApplication(sys.argv)
window = MainWindow()
window.show()

app.exec()

# TODO Prestavka 20:10