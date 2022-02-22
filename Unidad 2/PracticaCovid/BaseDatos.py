import sqlite3


def crear_conexion(base_datos):
  """
  Funcion para conectarnos a la base de datos
  :param base_datos que le pasaremos como argumento:
  :return devuelve la conexion si es valida:
  """
  conexion = None
  try:
    conexion = sqlite3.connect(base_datos)
    c = conexion.cursor()
    c.execute("CREATE TABLE IF NOT EXISTS Login(username TEXT NOT NULL UNIQUE PRIMARY KEY, password TEXT NOT NULL)")
    datos = c.execute("SELECT * FROM puntuacion").fetchall()
    if len(datos) == 0:
      c.execute("INSERT INTO puntuacion VALUES (0)")
  except sqlite3.Error as error:
    print()
  return conexion


def recuperar_user(conexion):
  """
  Funcion para recuperar el usuario y la contraseña
  :param conexion:
  :return devuelve una lista con el usuario y la contraseña:
  """
  sql = "SELECT username, password FROM Login;"
  cursor = conexion.cursor()
  cursor.execute(sql)
  user = cursor.fetchall()
  return user
