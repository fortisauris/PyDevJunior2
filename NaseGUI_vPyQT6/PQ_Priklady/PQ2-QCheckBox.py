import sys
from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QCheckBox


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle('Moja Appka')
        self.widget = QCheckBox('NASTAV VLAJKU')
        self.widget.setTristate(True)
        self.widget.stateChanged.connect(self.print_status)

        # Nastav Centralny Widget
        self.setCentralWidget(self.widget)

    def print_status(self, status):
        # print(Qt.CheckState.Checked)
        print(status)

        if status == 0:
            print('VYPNUTE')
        if status == 1:
            print("POLOZAPNUTE")
        if status == 2:  # ked je 2
            print('ZAPNUTE')

app = QApplication(sys.argv)
window = MainWindow()
window.show()

app.exec()