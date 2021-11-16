from PySide6.QtCore import QSize
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton

from config import ALTURA, ANCHO, btx, bty


class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setFixedSize(QSize(ALTURA, ANCHO))
        self.setWindowTitle("Exemple signals-slots 1")

        self.pybutton = QPushButton('Normalitza', self)
        self.pybutton2 = QPushButton('Maximitza', self)
        self.pybutton3 = QPushButton('Minimitza', self)

        self.pybutton.clicked.connect(self.normalitza)
        self.pybutton2.clicked.connect(self.maximitza)
        self.pybutton3.clicked.connect(self.minimitza)

        self.pybutton.resize(btx, bty)
        self.pybutton.move((ALTURA - 100) / 2, (ANCHO - 50) / 2)
        self.pybutton2.resize(btx, bty)
        self.pybutton2.move((ALTURA - 100) / 4.25, (ANCHO - 50) / 2)
        self.pybutton3.resize(btx, bty)
        self.pybutton3.move((ALTURA - 100) / 1.3, (ANCHO - 50) / 2)

    def normalitza(self):
        '''
            S'executaà al rebre la notificació de que s'ha apretat el botó:
            - Observeu que la consola imprimirà "Clic rebut!" al fer clic al botó
        '''
        print('Clic rebut!, normalitza')
        self.setFixedSize(QSize(ALTURA, ANCHO))
        self.pybutton.move((ALTURA - 100) / 2, (ANCHO - 50) / 2)
        self.pybutton2.move((ALTURA - 100) / 4.25, (ANCHO - 50) / 2)
        self.pybutton3.move((ALTURA - 100) / 1.3, (ANCHO - 50) / 2)

    def maximitza(self):
        '''
            S'executaà al rebre la notificació de que s'ha apretat el botó:
            - Observeu que la consola imprimirà "Clic rebut!" al fer clic al botó
        '''
        print('Clic rebut!, maximitza')
        self.setFixedSize(QSize(ALTURA + 200, ANCHO + 200))
        self.pybutton.move((ALTURA - 100) / 2, (ANCHO - 50) / 2)
        self.pybutton2.move((ALTURA - 100) / 4.25, (ANCHO - 50) / 2)
        self.pybutton3.move((ALTURA - 100) / 1.3, (ANCHO - 50) / 2)

    def minimitza(self):
        '''
            S'executaà al rebre la notificació de que s'ha apretat el botó:
            - Observeu que la consola imprimirà "Clic rebut!" al fer clic al botó
        '''
        print('Clic rebut!, minimitza')
        self.setFixedSize(QSize(ALTURA - 200, ANCHO - 200))
        self.pybutton.move((ALTURA - 100) / 2, (ANCHO - 50) / 2)
        self.pybutton2.move((ALTURA - 100) / 4.25, (ANCHO - 50) / 2)
        self.pybutton3.move((ALTURA - 100) / 1.3, (ANCHO - 50) / 2)


if __name__ == "__main__":
    app = QApplication([])
    mainWin = MainWindow()
    mainWin.show()
    app.exec()
