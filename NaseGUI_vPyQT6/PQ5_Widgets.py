import sys
from PyQt6.QtCore import QSize, Qt, QDate, QTime
from PyQt6.QtWidgets import *


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle('Vsetky Widgety')
        layout = QVBoxLayout()  # vertikalna skatulka
        widgets = [
            QCheckBox,
            QComboBox,
            QDateEdit,
            QDateTimeEdit,
            QDial,
            QDoubleSpinBox,
            QLCDNumber,
            QLabel,
            QLineEdit,
            QProgressBar,
            QPushButton,
            QSlider,
            QSpinBox,
            QTimeEdit
        ]

        for w in widgets:   # Cez cyklus nahadzeme widgety do layoutu
            layout.addWidget(w())
        today = QDate.currentDate()
        print(today)
        ti = QTime.currentTime()
        print(ti)

        # skonvertujeme datumy a casy do widgetu QLabel

        self.date_label = QLabel(today.toString())
        self.time_label = QLabel(ti.toString())

        # pridame do layoutu
        layout.addWidget(self.date_label)
        layout.addWidget(self.time_label)
        # self.time_label
        widget = QWidget()
        widget.setLayout(layout)   # definujes

        # Nastav Centralny Widget
        self.setCentralWidget(widget)

    def aktualny(self):
        t = QTime.currentTime()
        print(t)
        self.time_label.setText(t.toString())


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()  # HLAVNY CYKLUS


