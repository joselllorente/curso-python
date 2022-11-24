import sys
import MySQLdb
import psycopg2


def get_mysql_conection():
    return get_conection()


def get_conection(db="mysql", maquina="localhost", usuario="root", password="password", base_datos="curso_python",
                  puerto=3306):
    try:
        if db == "mysql":
            conection = MySQLdb.connect(
                host=maquina,
                user=usuario,
                passwd=password,
                db=base_datos,
                port=puerto)
        else:
            conection = psycopg2.connect(
                user=usuario,
                password=password,
                host=maquina,
                port=puerto,
                database=base_datos
            )
    except MySQLdb.Error as mysqle:
        print("No puedo conectar a la base de datos:", mysqle)

    except Exception as e:
        print("No puedo conectar a la base de datos:", e)

    else:
        print("Conexión correcta.")

    return conection
