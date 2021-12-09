from PySide6.QtCore import Qt, QSize
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QGridLayout, QLabel, \
  QPushButton, QLineEdit


class MainWindow(QMainWindow):

  def __init__(self):
    super(MainWindow, self).__init__()

    self.setWindowTitle("Calculadora")
    self.widget = QWidget()

    self.pantalla_numeros = QLineEdit()
    self.pantalla_numeros.setFixedHeight(40)
    self.layout_principal = QVBoxLayout()
    self.layout_pantalla = QHBoxLayout()
    self.grid = QGridLayout()
    self.grid.setSpacing(10)

    self.layout_pantalla.addWidget(self.pantalla_numeros)
    self.layout_principal.addLayout(self.layout_pantalla)

    self.cadena = ""
    self.numeros = ['raiz', 'pi', '^', '!',
                    'AC', '(', ')', "/",
                    '7', '8', '9', '*',
                    '4', '5', '6', '+',
                    '1', '2', '3', '-',
                    "0", ".", "<-", "="]

    self.posisiones = [(i, j) for i in range(6) for j in range(4)]

    for self.posisiones, self.numeros in zip(self.posisiones, self.numeros):
      if self.numeros == "":
        continue
      boton = QPushButton(self.numeros)
      boton.clicked.connect(self.operacion)
      self.grid.addWidget(boton, *self.posisiones)

    self.layout_principal.addLayout(self.grid)
    self.widget.setLayout(self.layout_principal)
    self.setCentralWidget(self.widget)

  def operacion(self):
    if self.sender().text() == "<-":
      self.editarTexto(self.cadena[:-1])
      self.cadena = self.cadena[:-1]
    elif self.sender().text() == "=":
      self.result()
    elif self.sender().text() == "AC":
      self.borrar()
    else:
      self.cadena += self.sender().text()
      self.editarTexto(self.cadena)

  def mostrarTexto(self):
    return self.pantalla_numeros.text()

  def result(self):
    self.editarTexto(str(eval(self.cadena)))

  def editarTexto(self, texto):
    self.pantalla_numeros.setText(texto)
    self.pantalla_numeros.setFocus()

  def borrar(self):
    self.editarTexto("")
    self.cadena = ""


app = QApplication([])
window = MainWindow()
window.show()
app.exec()
