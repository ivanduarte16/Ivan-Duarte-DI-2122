import sqlite3

from Constantes import score


def crear_conexion(base_datos):
    conexion = None
    try:
        conexion = sqlite3.connect(base_datos)
        c = conexion.cursor()
        c.execute("CREATE TABLE IF NOT EXISTS puntuacion(score INTERGER NOT NULL)")
        datos = c.execute("SELECT * FROM puntuacion").fetchall()
        if len(datos) == 0:
            c.execute("INSERT INTO puntuacion VALUES (0)")
    except sqlite3.Error as error:
        print()
    return conexion


def insertar_datos():
    conexion = crear_conexion("RegistroPuntuacion.db")
    c = conexion.cursor()
    puntos = str(score.hscore)
    sql = "SELECT * FROM puntuacion;"
    c.execute(sql)
    points = c.fetchall()
    for i in points:
        if score.score > i[0]:
            c.execute("DELETE FROM puntuacion")
            c.execute('INSERT INTO puntuacion(score) values(?)', (puntos,))
    conexion.commit()
    if conexion:
        conexion.close()


def recuperar_datos(conexion):
    sql = "SELECT * FROM puntuacion;"
    puntos = 0
    cursor = conexion.cursor()
    cursor.execute(sql)
    points = cursor.fetchall()
    list(points)
    for i in points:
        puntos = i[0]
    return puntos
