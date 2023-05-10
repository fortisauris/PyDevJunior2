import sys
from PyQt6.QtWidgets import QApplication, QPushButton

app = QApplication(sys.argv)

window = QPushButton('Stlac')
window.show()

app.exec()  # mainloop
