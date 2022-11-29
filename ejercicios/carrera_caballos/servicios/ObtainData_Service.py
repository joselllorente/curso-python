from ejercicios.carrera_caballos.servicios.Loggin_Service import log, setupLogging
import ejercicios.carrera_caballos.dao.CaballoDAO as dao_caballos
import ejercicios.carrera_caballos.dao.GranPremioDAO as dao_granpremio
import ejercicios.carrera_caballos.dao.ApostantesDAO as dao_apostante
from ejercicios.carrera_caballos.servicios.DB_Service import DBServices

setupLogging(log.DEBUG, "../logs/carrera.log")


def obtener_todos_datos():
    """ Obtenemos los datos de todas las tablas  """
    log.info("Obteniendo los datos de la base de datos")
    try:
        connection = DBServices.get_connection()
        cursor = connection.cursor()

        listado_caballos = obtener_datos_caballos(cursor)
        listado_grandespremios = obtener_datos_grandes_premios(cursor)
        listado_apostantes = obtener_datos_apostantes(cursor)

    except Exception as e:
        log.error("Error al acceder a los datos de la base de datos")
    finally:
        cursor.close()
        DBServices.close_connection()

    return listado_caballos, listado_grandespremios, listado_apostantes


def obtener_datos_grandes_premios(cursor):
    return dao_granpremio.GranPremioDAO.seleccionar(cursor)


def obtener_datos_caballos(cursor):
    return dao_caballos.CaballoDAO.seleccionar(cursor)


def obtener_datos_apostantes(cursor):
    return dao_apostante.ApostanteDAO.seleccionar(cursor)
