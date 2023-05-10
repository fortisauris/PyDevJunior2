import sys
from PyQt6.QtCore import QSize, Qt
from PyQt6.QtGui import QAction
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QMenu, QPushButton


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.label = QLabel('TEXT')
        # Nastav Centralny Widget
        self.setCentralWidget(self.label)

    def contextMenuEvent(self, event):
        context = QMenu(self)

        # zadefinujeme kontextove akcie
        akcia1 = QAction('ZMEN TEXT', self)
        akcia2 = QAction('OPAKUJ', self)
        akcia3 = QAction('PREPIS', self)

        # pridame akcie do kontextu
        context.addAction(akcia1)
        context.addAction(akcia2)
        context.addAction(akcia3)
        context.addAction(QAction('test', self))

        # odpal funkciu ked ju zavolas
        akcia1.triggered.connect(lambda: self.label.setText('ZMENA TEXTU'))  # 1 signal a 1 SLOT
        akcia2.triggered.connect(lambda: self.label.setText('OPAKUJ'))  # 2 signal a 2 SLOT
        akcia3.triggered.connect(lambda: self.label.setText('PREPIS TEXT'))  # 3 signal a 3 SLOT
        context.exec(event.globalPos())


class CustomButton(QPushButton):
    def mousePressEvent(self, event):
        event.accept()

app = QApplication(sys.argv)
window = MainWindow()
window.show()

app.exec()