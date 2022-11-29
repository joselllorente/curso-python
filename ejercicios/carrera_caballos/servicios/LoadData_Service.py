from ejercicios.carrera_caballos.servicios.Loggin_Service import log, setupLogging
from ejercicios.carrera_caballos.servicios.Files_Service import NOMBRE_FICHERO_CABALLOS, NOMBRE_FICHERO_APOSTANTES, \
    NOMBRE_FICHERO_GRANPREMIO
import ejercicios.carrera_caballos.dao.CaballoDAO as dao_caballos
import ejercicios.carrera_caballos.dao.ApostantesDAO as dao_apostante
import ejercicios.carrera_caballos.dao.GranPremioDAO as dao_granpremio
from ejercicios.carrera_caballos.servicios.DB_Service import DBServices

setupLogging(log.DEBUG, "../logs/carrera.log")


def carga_datos(mapa_datos):

    log.info("Cargado los datos del mapa en la base de datos")

    try:
        connection = DBServices.get_connection()
        cursor = connection.cursor()

        for tipo, objetos in mapa_datos.items():
            if NOMBRE_FICHERO_CABALLOS in tipo:
                dao_caballos.CaballoDAO.insertar_caballos(objetos, cursor)
            elif NOMBRE_FICHERO_APOSTANTES in tipo:
                dao_apostante.ApostanteDAO.insertar_apostantes(objetos, cursor)
            elif NOMBRE_FICHERO_GRANPREMIO in tipo:
                dao_granpremio.GranPremioDAO.insertar_grandespremios(objetos,cursor)

        connection.commit()
    except Exception as e:
        log.error(f"Error al guardar los datos en la base de datos {e}")
    finally:
        cursor.close()
        DBServices.close_connection()
