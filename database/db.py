import sqlite3
from sqlite3 import Error
from flask import g



def get_db():
    '''
    Funcion que crea la conexion a la base de datos.

    Paremeters:
    Ninguno

    returns:
    g.db:retorna la conexión a la variable global g de flask

    '''
    try:
        if 'db' not in g:
            g.db = sqlite3.connect('database/inventario.db')
        return g.db
    except Error:
        print("Error en la base de datos: " + Error)

def close_db():
    '''
    Función que cierra conexión a la base de datos.

    Parameters:
    Ninguno

    Returns:
    Nada

   '''
    db = g.pop('db',None)

    if db is not None:
       db.close()