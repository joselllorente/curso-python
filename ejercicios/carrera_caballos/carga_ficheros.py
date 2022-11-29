from ejercicios.carrera_caballos.servicios.Files_Service import obtener_datos_ficheros
from ejercicios.carrera_caballos.servicios.Loggin_Service import log, setupLogging
from ejercicios.carrera_caballos.servicios.LoadData_Service import carga_datos
import os
import sys

setupLogging(log.DEBUG, "./logs/carrera.log")

if __name__ == "__main__":
    log.info("Empezando la carga de ficheros en base de datos")

    if len(sys.argv) > 1:
        ruta = sys.argv[1]
    else:
        ruta = "./resources/"

    nombres_ficheros = os.listdir(ruta)

    ruta_ficheros = list(map(lambda nombre_fichero: ruta + nombre_fichero, nombres_ficheros))
    log.debug(f"Ficheros a tratar: {ruta_ficheros}")

    mapa_datos = obtener_datos_ficheros(ruta_ficheros)

    carga_datos(mapa_datos)


    log.info("Fin de la carga de ficheros en base de datos")

