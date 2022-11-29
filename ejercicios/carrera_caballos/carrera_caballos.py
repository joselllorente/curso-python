from ejercicios.carrera_caballos.servicios.Loggin_Service import log, setupLogging
from ejercicios.carrera_caballos.servicios.ObtainData_Service import obtener_todos_datos
from ejercicios.carrera_caballos.servicios.GrandesPremios_Service import ejecutar_grandes_premios

setupLogging(log.DEBUG, "./logs/carrera.log")

if __name__ == "__main__":

    lista_caballos, listado_grandespremios, listado_apostantes = obtener_todos_datos()
    ejecutar_grandes_premios(lista_caballos, listado_grandespremios, listado_apostantes)
