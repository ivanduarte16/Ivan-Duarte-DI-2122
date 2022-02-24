import csv
import sys
from PySide6.QtCore import QSize
from PySide6.QtGui import QScreen, QAction, QIcon
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox
from pandas import DataFrame
from ui_login import Ui_MainWindow
from ui_main import Ui_buscar
import pandas as pd
import matplotlib.pyplot as plt
from BaseDatos import *
import hashlib

# Redimensionamos la ventana del grafico
plt.rcParams["figure.figsize"] = (15, 8)


class Login(QMainWindow):
  def __init__(self):
    """
    Esta funcion se encarga de importar el login de PQtdesign y mostrarlo
    """
    super(Login, self).__init__()

    # Importamos el la ventana del login del archivo .ui que hemos creado con pqt design
    self.ui = Ui_MainWindow()
    self.ui.setupUi(self)

    # Conectamos con la funcion para verificar la informacion
    self.ui.btn_login.clicked.connect(self.Loguearte)

    # Establecemos un tamaño fijo
    self.setFixedSize(QSize(385, 428))

  def Loguearte(self):
    """
    Esta funcion se encarga de verificar la informacion del login
    """
    con = crear_conexion('Login.db')
    md5 = hashlib.md5(self.ui.password.text().encode('utf-8')).hexdigest()
    print(md5)
    if recuperar_user(con)[0][0] == self.ui.username.text() and recuperar_user(con)[0][1] == self.ui.password.text():
      self.estadisticWindow = EstadisticWindow()
      self.estadisticWindow.show()
      self.close()
    else:
      dialogo = QMessageBox.critical(self, "Ha ocurrido algo inesperado", "Contraseña o usuario incorrecto")
      print(dialogo)
      self.ui.username.clear()
      self.ui.password.clear()


class EstadisticWindow(QMainWindow):
  def __init__(self):
    """
   Ventana donde se mostraran los datos
    """
    super(EstadisticWindow, self).__init__()
    self.setWindowTitle("ESTADISTICAS")
    self.setFixedSize(QSize(441, 332))

    # Importamos el la ventana principal del archivo .ui que hemos creado con pqt design
    self.ui_main = Ui_buscar()
    self.ui_main.setupUi(self)

    # Creamos el boton de cerrar sesion
    cerrar = QAction(QIcon("exit.png"), "&Logout", self)
    cerrar.triggered.connect(self.cerrarSesion)
    self.ui_main.menuFile.addAction(cerrar)

    # Creamos el boton de salir de la app
    salir = QAction(QIcon("salir.png"), "&Exit", self)
    salir.triggered.connect(self.salirApp)
    self.ui_main.menuFile.addAction(salir)

    # Nos conectamos con las funciones
    self.ui_main.pushButton.clicked.connect(self.graficos)

    with open('CSV/Ciudades.csv') as f:
      reader = csv.reader(f)
      for line in reader:
        self.ui_main.comboBox_provincias.addItem(line[0])
    self.ui_main.comboBox_provincias.setEditable(True)
    self.ui_main.comboBox_provincias.setMaxVisibleItems(10)
    self.ui_main.comboBox_datos.setEditable(True)
    self.ui_main.comboBox_datos.setMaxVisibleItems(6)

  def graficos(self):
    """
    Funcion que pintará el grafico de las ciudades de Valencia
    """
    if self.ui_main.comboBox_datos.currentText() == "Casos PCR+":
      plt.close()
      csv = pd.read_csv('CSV/Casos-PCR+-Povincias.csv')
      df = DataFrame(csv, columns=['Fecha', self.ui_main.comboBox_provincias.currentText()])
      df.plot.bar(x='Fecha', y=self.ui_main.comboBox_provincias.currentText())
      plt.xticks(rotation=45),
      plt.title('Casos PCR acumulados en ' + self.ui_main.comboBox_provincias.currentText())
      plt.show()
    elif self.ui_main.comboBox_datos.currentText() == "Casos PCR+ 14 dies":
      plt.close()
      csv = pd.read_csv('CSV/Casos-PCR+-14.csv')
      df = DataFrame(csv, columns=['Fecha', self.ui_main.comboBox_provincias.currentText()])
      df.plot.bar(x='Fecha', y=self.ui_main.comboBox_provincias.currentText())
      plt.xticks(rotation=45),
      plt.title('Casos PCR en los ultimos 14 dias ' + self.ui_main.comboBox_provincias.currentText())
      plt.show()
    elif self.ui_main.comboBox_datos.currentText() == "Muertes":
      plt.close()
      csv = pd.read_csv('CSV/Fallecidos-Ciudades.csv')
      df = DataFrame(csv, columns=['Fecha', self.ui_main.comboBox_provincias.currentText()])
      df.plot.bar(x='Fecha', y=self.ui_main.comboBox_provincias.currentText())
      plt.xticks(rotation=45),
      plt.title('Fallecidos desde enero en ' + self.ui_main.comboBox_provincias.currentText())
      plt.show()
    elif self.ui_main.comboBox_datos.currentText() == "Incidencia acumulada PCR+14":
      plt.close()
      csv = pd.read_csv('CSV/IncidenciasAcumuladasPCR+14.csv')
      df = DataFrame(csv, columns=['Fecha', self.ui_main.comboBox_provincias.currentText()])
      df.plot.bar(x='Fecha', y=self.ui_main.comboBox_provincias.currentText())
      plt.xticks(rotation=45),
      plt.title('Incidencias acumuladas en los ultimos 14 dias en ' + self.ui_main.comboBox_provincias.currentText())
      plt.show()
    elif self.ui_main.comboBox_datos.currentText() == "Incidencia acumulada PCR+":
      plt.close()
      csv = pd.read_csv('CSV/IncidenciasAcumuladaPCR+.csv')
      df = DataFrame(csv, columns=['Fecha', self.ui_main.comboBox_provincias.currentText()])
      df.plot.bar(x='Fecha', y=self.ui_main.comboBox_provincias.currentText())
      plt.xticks(rotation=45),
      plt.title('Incidencias acumuladas en ' + self.ui_main.comboBox_provincias.currentText())
      plt.show()
    elif self.ui_main.comboBox_datos.currentText() == "Taxa de defunció":
      plt.close()
      csv = pd.read_csv('CSV/TaxaDefuncions.csv')
      df = DataFrame(csv, columns=['Fecha', self.ui_main.comboBox_provincias.currentText()])
      df.plot.bar(x='Fecha', y=self.ui_main.comboBox_provincias.currentText())
      plt.xticks(rotation=45),
      plt.title('Incidencias acumuladas en ' + self.ui_main.comboBox_provincias.currentText())
      plt.show()

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
      self.login = Login()
      self.login.show()
      self.close()

  def salirApp(self):
    """
   Funcion que muestra un dialogo para confirmar si quieres salir de la sesion
   """
    dlg = QMessageBox(self)
    dlg.setWindowTitle("Confirmacion")
    dlg.setText("Estas seguro de que quieres cerrar la aplicacion?")
    dlg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
    button = dlg.exec_()
    if button == QMessageBox.Yes:
      self.close()


if __name__ == '__main__':
  app = QApplication(sys.argv)
  mainwindow = Login()
  mainwindow.setGeometry(0, 0, 800, 600)
  mainwindow.show()
  center = QScreen.availableGeometry(QApplication.primaryScreen()).center()
  geo = mainwindow.frameGeometry()
  geo.moveCenter(center)
  mainwindow.move(geo.topLeft())
  sys.exit(app.exec_())
