from basededatos.utils.conexiones import get_mysql_conection
import utils.logging_general as logs
import logging

logs.setupLogging(logging.DEBUG, "../logs/ejercicio_sql.log")


def insertar_personas():
    try:
        conexion = get_mysql_conection()
        cursor = conexion.cursor()
        sentencia = 'INSERT INTO personas(nombre, apellidos, email) VALUES(%s, %s, %s)'
        valores = (
            ('Nombre1', "Apellidos1", "asdasd@asd.es"),
            ('Nombre2', "Apellidos2", "asdasd@asd.es"),
            ('Nombre3', "Apellidos3", "asdasd@gmail.com")
        )
        cursor.executemany(sentencia, valores)
        conexion.commit()
        registros_insertados = cursor.rowcount
        print(f'Registros Insertados: {registros_insertados}')
    except Exception as e:
        logs.error("Error", e)

    finally:
        cursor.close()
        conexion.close()
        logs.info("Inserts realizados")


def show_names():
    """Muestra solamente los nombres de la tabla personas"""
    try:
        conexion = get_mysql_conection()
        cursor = conexion.cursor()
        sentencia = 'SELECT `nombre`,`apellidos` FROM `personas`'

        cursor.execute(sentencia)
        registros = cursor.fetchall()

        for registro in registros:
            print(registro[1])

    except Exception as e:
        logs.error("Error", e)

    finally:
        cursor.close()
        conexion.close()
        logs.info("Fin")


def show_mail_filter(value):
    """Muestra toda la informacion de las personas cuyo email es igual al valor del parametro 'value'"""
    logs.debug(f"show_mail_filter con parametro {value}")
    new_value = f'%{value}'
    try:
        conexion = get_mysql_conection()
        cursor = conexion.cursor()
        sentencia = 'SELECT * FROM `personas` WHERE `email` LIKE %s'

        cursor.execute(sentencia, [new_value])
        logs.debug(cursor._executed)
        registros = cursor.fetchall()
        logs.debug(registros)

    except Exception as e:
        logs.error("Error", e)

    finally:
        cursor.close()
        conexion.close()
        logs.info("Fin")


def update_email(value):
    """Actualiza todos los email diferentes al parametro 'value' cambiandolos por el mismo"""
    new_value = f'%{value}'
    to_change = f'@{value}'
    try:
        conexion = get_mysql_conection()
        with conexion:
            with conexion.cursor() as cursor:
                sentencia = "UPDATE `personas` " \
                            "SET `email` = CONCAT(left(`personas`.`email`, locate('@', `personas`.`email`) - 1), %s) " \
                            "WHERE `personas`.`email` NOT LIKE %s"
                cursor.execute(sentencia, (to_change, new_value))
                conexion.commit()
                registros_actualizados = cursor.rowcount
                logs.debug(f'Registros Actualizados: {registros_actualizados}')
    except Exception as e:
        logs.error(f'Ocurrió un error: {e}')


if __name__ == "__main__":
    #insertar_personas()
    #show_names()
    #show_mail_filter("gmail.com")
    update_email("gmail.com")