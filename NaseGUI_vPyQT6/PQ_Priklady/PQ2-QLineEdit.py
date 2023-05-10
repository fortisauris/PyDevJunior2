import sys
from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QLineEdit


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle('Moja Appka')
        self.widget = QLineEdit()
        # self.widget.setEchoMode(QLineEdit.EchoMode.Password)
        self.widget.setMaxLength(17)
        # self.widget.setInputMask('000.000.000,00-EUR')
        self.widget.setInputMask('TEL: 000-000-000')
        self.widget.setPlaceholderText('TU MI TO NAPIS')
        # signaly a sloty
        self.widget.returnPressed.connect(self.stlaceny_return)
        self.widget.selectionChanged.connect(self.selection_changed)
        self.widget.textChanged.connect(self.print_text)
        self.widget.textEdited.connect(self.text_editovany)


        # Nastav Centralny Widget
        self.setCentralWidget(self.widget)

    def stlaceny_return(self):
        # self.centralWidget().setText('DOPLN INFO')
        # print('RETURN BOL STLACENY')
        print(self.widget.text())

    def print_text(self, text):
        print('napisany text :',text)

    def text_editovany(self, text):
        print('text editovany')

    def selection_changed(self):
        print('selection changed', self.centralWidget().selectedText())

app = QApplication(sys.argv)
window = MainWindow()
window.show()

app.exec()