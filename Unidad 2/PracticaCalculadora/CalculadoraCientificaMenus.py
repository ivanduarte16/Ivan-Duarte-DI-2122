import os

from PySide6.QtCore import Qt, QSize
from PySide6.QtGui import QAction, QIcon, QKeySequence
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QGridLayout, QLabel, \
  QPushButton, QLineEdit, QToolBar, QStatusBar, QStackedLayout


class MainWindow(QMainWindow):

  def __init__(self):
    super(MainWindow, self).__init__()

    self.setWindowTitle("Calculadora")
    self.widget = QWidget()

    self.pantalla_numeros = QLineEdit()
    self.pantalla_numeros.setFixedHeight(60)
    fuente = self.pantalla_numeros.font()
    self.stacklayout = QStackedLayout()
    fuente.setPointSize(30)
    self.pantalla_numeros.setFont(fuente)
    self.pantalla_numeros.setAlignment(Qt.AlignRight)

    icon_path = os.path.join(os.path.dirname(__file__), "aceptar.png")

    button_action = QAction(QIcon(icon_path), "Normal", self)
    button_action.setStatusTip("Este es el modo normal")

    button_action2 = QAction(QIcon(icon_path), "Cientifico", self)
    button_action2.setStatusTip("Este es el modo cientifico")

    self.setStatusBar(QStatusBar(self))

    # Menu
    menu = self.menuBar()
    file_menu = menu.addMenu("&Menu")
    file_menu.addSeparator()
    file_submenu = file_menu.addMenu("Modos")

    button_action = QAction("Normal", self)
    button_action.triggered.connect(self.calculadoraNormal)
    file_submenu.addAction(button_action)

    button_action2 = QAction("Cientifica", self)
    button_action2.triggered.connect(self.calculadoraCien)
    file_submenu.addAction(button_action2)

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

    self.numeros2 = ['Rad', 'Deg', 'x!', '(', ')', '%', 'AC',
                     'Inv', 'sin', 'In', "7", '8', '9', '/',
                     'π', 'cos', 'log', '4', '5', '6', '*',
                     'e', 'tan', '√', '1', '2', '3', '-',
                     'Ans', 'EXP', '^', '0', '.', '=', '+']

    self.calculadoraNormal()

  def calculadoraNormal(self):
    self.limpiarPantalla()
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

  def calculadoraCien(self):
    self.limpiarPantalla()

    self.posisiones2 = [(i, j) for i in range(5) for j in range(7)]

    for self.posisiones2, self.numeros2 in zip(self.posisiones2, self.numeros2):
      if self.numeros2 == "":
        continue
      boton = QPushButton(self.numeros2)
      boton.clicked.connect(self.operacion)
      self.grid.addWidget(boton, *self.posisiones2)

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

  def limpiarPantalla(self):
    for i in reversed(range(self.grid.count())):
      self.grid.itemAt(i).widget().setParent(None)


app = QApplication([])
window = MainWindow()
window.show()
app.exec()
