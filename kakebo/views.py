from kakebo import app
import sqlite3

@app.route('/')
def index():
    conexion = sqlite3.connect("movimientos.db")
    cur = conexion.cursor()

    cur.execute("SELECT * FROM movimientos;")

    claves = cur.description
    
    filas = cur.fetchall()
    d = {}





    l = []
    for fila in filas:
        d = {}
        for columna in fila:
    conexion.close()

    return "Consulta realizada"
