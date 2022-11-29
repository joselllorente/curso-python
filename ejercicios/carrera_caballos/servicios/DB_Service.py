import MySQLdb


class DBServices:
    _connection = None

    @classmethod
    def get_connection(cls):
        if cls._connection == None:
            cls._connection = cls.open_connection()

        return cls._connection

    @classmethod
    def open_connection(cls, maquina="localhost", usuario="root", password="password",
                       base_datos="curso_python_carrera",
                       puerto=3306):
        try:
            connection = MySQLdb.connect(
                host=maquina,
                user=usuario,
                passwd=password,
                db=base_datos,
                port=puerto)

        except MySQLdb.Error as mysqle:
            print("No puedo conectar a la base de datos:", mysqle)

        except Exception as e:
            print("No puedo conectar a la base de datos:", e)

        else:
            print("Conexión correcta.")

        return connection

    @classmethod
    def close_connection(cls):
        try:
            cls._connection.close()
            cls._connection = None

        except MySQLdb.Error as mysqle:
            print("No puedo conectar a la base de datos:", mysqle)

        except Exception as e:
            print("No puedo conectar a la base de datos:", e)

        else:
            print("Conexión cerrada.")
