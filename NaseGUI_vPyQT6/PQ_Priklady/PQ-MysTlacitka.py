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


    def mousePressEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            self.label.setText('LAVE TLACITKO MYSI JE STLACENE')
        elif event.button() == Qt.MouseButton.RightButton:
            self.label.setText('PRAVE TLACITKO MYSI JE STLACENE')
        elif event.button() == Qt.MouseButton.MiddleButton:
            self.label.setText('STREDNE TLACITKO MYSI JE STLACENE')

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            self.label.setText('LAVE TLACITKO MYSI JE PUSTENE')
        elif event.button() == Qt.MouseButton.RightButton:
            self.label.setText('PRAVE TLACITKO MYSI JE PUSTENE')
        elif event.button() == Qt.MouseButton.MiddleButton:
            self.label.setText('STREDNE TLACITKO MYSI JE PUSTENE')

    def mouseDoubleClickEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            self.label.setText('LAVY DVOJKLIK')
        elif event.button() == Qt.MouseButton.RightButton:
            self.label.setText('PRAVY DVOJKLIK')
        elif event.button() == Qt.MouseButton.MiddleButton:
            self.label.setText('STREDNY DVOJKLIK')



app = QApplication(sys.argv)
window = MainWindow()
window.show()

app.exec()

# TODO Prestavka 20:10