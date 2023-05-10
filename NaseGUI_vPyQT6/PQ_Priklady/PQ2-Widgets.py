import sys
from PyQt6.QtCore import QSize, Qt, QDate, QTime
from PyQt6.QtWidgets import *


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle('Widgety')

        layout = QVBoxLayout()  # Vertikalna skatulka
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

        for w in widgets:
            layout.addWidget(w())
        today = QDate.currentDate()
        print(today)
        ti = QTime.currentTime()
        print(ti)

        date_label = QLabel(today.toString())
        time_label = QLabel(ti.toString())
        layout.addWidget(date_label)
        layout.addWidget(time_label)

        widget = QWidget()
        widget.setLayout(layout)

        self.setCentralWidget(widget)

app = QApplication(sys.argv)
window = MainWindow()
window.show()

app.exec()