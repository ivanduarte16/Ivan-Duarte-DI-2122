from PySide6.QtCore import QSize
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton

from config import *


class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setFixedSize(QSize(ALTURANOR, ANCHONOR))
        self.setWindowTitle("Exemple signals-slots 1")

        self.pybutton = QPushButton('Normalitza', self)
        self.pybutton2 = QPushButton('Maximitza', self)
        self.pybutton3 = QPushButton('Minimitza', self)

        self.pybutton.clicked.connect(self.normalitza)
        self.pybutton2.clicked.connect(self.maximitza)
        self.pybutton3.clicked.connect(self.minimitza)

        self.pybutton.resize(btx, bty)
        self.pybutton.move((ALTURANOR -100) / 2, (ANCHONOR - 50) / 2)
        self.pybutton2.resize(btx, bty)
        self.pybutton2.move((ALTURANOR - 100) / 4.25, (ANCHONOR - 50) / 2)
        self.pybutton3.resize(btx, bty)
        self.pybutton3.move((ALTURANOR - 100) / 1.3, (ANCHONOR - 50) / 2)

    def normalitza(self):
        print('Clic rebut!, normalitza')
        self.setFixedSize(QSize(ALTURANOR, ANCHONOR))
        self.pybutton.move((ALTURANOR - 100) / 2, (ANCHONOR- 50) / 2)
        self.pybutton2.move((ALTURANOR - 100) / 4.25, (ANCHONOR - 50) / 2)
        self.pybutton3.move((ALTURANOR - 100) / 1.3, (ANCHONOR - 50) / 2)

    def maximitza(self):
        print('Clic rebut!, maximitza')
        self.setFixedSize(QSize(ALTURAMAX, ANCHOMAX))
        self.pybutton.move((ALTURAMAX - 100) / 2, (ANCHOMAX - 50) / 2)
        self.pybutton2.move((ALTURAMAX - 100) / 4.25, (ANCHOMAX - 50) / 2)
        self.pybutton3.move((ALTURAMAX - 100) / 1.3, (ANCHOMAX - 50) / 2)

    def minimitza(self):
        print('Clic rebut!, minimitza')
        self.setFixedSize(QSize(ALTURAMIN, ANCHOMIN))
        self.pybutton.move((ALTURAMIN - 100) / 2, (ANCHOMIN - 50) / 2)
        self.pybutton2.move((ALTURAMIN - 100) / 4.25, (ANCHOMIN - 50) / 2)
        self.pybutton3.move((ALTURAMIN - 100) / 1.25, (ANCHOMIN - 50) / 2)


if __name__ == "__main__":
    app = QApplication([])
    mainWin = MainWindow()
    mainWin.show()
    app.exec()
