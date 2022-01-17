
from PySide6.QtGui import QAction
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QLabel, \
  QPushButton, QLineEdit, QMessageBox, QFormLayout


class AnotherWindow(QMainWindow):
  def __init__(self, usuario):
    super().__init__()

    self.statusBar().showMessage("Has iniciado sesion con el ususario " + usuario)

    # Creamos el menu con un separador
    menu = self.menuBar()
    file_menu = menu.addMenu("&Menu")
    file_menu.addSeparator()

    # Creamos el boton de cerrar sesion
    cerrar = QAction("&Logout", self)
    cerrar.triggered.connect(self.cerrarSesion)
    file_menu.addAction(cerrar)

    # Creamos el boton de salir
    salir = QAction("&Salir", self)
    salir.triggered.connect(self.salirVentana)
    file_menu.addAction(salir)

    layout = QVBoxLayout()
    self.label = QLabel("Sesion iniciado como " + usuario)
    layout.addWidget(self.label)
    self.setLayout(layout)

  def cerrarSesion(self):
    """
    Funcion que muestra un dialogo para confirmar si quieres salir de la sesion
    """
    dlg = QMessageBox(self)
    dlg.setWindowTitle("Confirmacion")
    dlg.setText("Estas seguro de que quieres cerrar la sesion?")
    dlg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
    button = dlg.exec_()

    if button == QMessageBox.Yes:
      self.w = MainWindow()
      self.w.show()
      self.close()

  def salirVentana(self):
    """
    Funcion para salir de la aplicacion
    """
    dlg = QMessageBox(self)
    dlg.setWindowTitle("Confirmacion")
    dlg.setText("Estas seguro que quieres salir")
    dlg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
    button = dlg.exec_()

    if button == QMessageBox.Yes:
      self.close()


class MainWindow(QMainWindow):
  def __init__(self):
    super(MainWindow, self).__init__()
    self.setWindowTitle("Login")

    # Definimos el widget principal
    self.widget = QWidget()

    # Definimo el layout que contendrá el login
    self.layout = QVBoxLayout()

    # Definimos un Qformlayout para poner poner informacion al lado de los line edits
    self.formulario = QFormLayout()

    # Definimos el line edit del usuario y se lo añadimos al formulario
    self.line_usuario = QLineEdit()
    self.formulario.addRow("Introduzca su usuario", self.line_usuario)

    # Definimos el line edit de la contraseña y se lo añadimos al formulario
    self.line_contraseña = QLineEdit()

    # Ahora ocultamos el texto de la contraseña
    self.line_contraseña.setEchoMode(QLineEdit.Password)
    self.formulario.addRow("Introduzca la contraseña", self.line_contraseña)

    # Creamos el boton del login
    self.boton_login = QPushButton("Entrar")

    # Conectamos con la funcion para verificar la informacion
    self.boton_login.clicked.connect(self.Loguearte)

    # Añadimos al layour el formulario y el boton
    self.layout.addLayout(self.formulario)
    self.layout.addWidget(self.boton_login)

    # Añadimos al widget el layout
    self.widget.setLayout(self.layout)
    self.setCentralWidget(self.widget)

  def Loguearte(self):
    """
    Esta funcion se encarga de verificar la informacion
    """
    dlg = QMessageBox(self)
    dlg.setWindowTitle("Error al loguearte")

    if self.line_usuario.text() == "admin" and self.line_contraseña.text() == "1234":
      self.window1 = AnotherWindow("admin")
      self.window1.show()
      self.close()

    elif self.line_usuario.text() == "user" and self.line_contraseña.text() == "1234":
      self.window2 = AnotherWindow("user")
      self.window2.show()
      self.close()

    elif self.line_usuario.text() == "admin" and self.line_contraseña.text() != "1234":
      dlg.setText("Contraseña incorrecta")
      button = dlg.exec_()

    elif self.line_usuario.text() == "user" and self.line_contraseña.text() != "1234":
      dlg.setText("Contraseña incorrecta")
      button = dlg.exec_()

    elif self.line_usuario.text() != "user" or self.line_usuario.text() != "admin":
      dlg.setText("Usuario desconocido")
      button = dlg.exec_()


app = QApplication([])
window = MainWindow()
window.show()
app.exec()
