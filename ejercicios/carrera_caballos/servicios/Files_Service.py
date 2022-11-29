from ejercicios.carrera_caballos.models.Apostante import Apostante
from ejercicios.carrera_caballos.models.Caballo import Caballo
from ejercicios.carrera_caballos.models.GranPremio import GranPremio

NOMBRE_FICHERO_GRANPREMIO = "grandes_premios"
NOMBRE_FICHERO_CABALLOS = "caballos"
NOMBRE_FICHERO_APOSTANTES = "apostantes"


def obtener_datos_ficheros(nombres):
    ''' Devolvemos listado de objetos dependiendo del fichero que me manden'''
    listado_objetos = {}
    for nombre_fichero in nombres:
        # Recogemos los datos de los resources
        datos = obtener_datos_fichero(nombre_fichero)

        # Creo una clave con el nombre del fichero eliminando la extension
        clave = nombre_fichero[ : nombre_fichero.rfind(".")]
        listado_objetos[clave] = []
        if NOMBRE_FICHERO_GRANPREMIO in nombre_fichero:
            for linea_datos in datos:
                gran_premio = GranPremio(linea_datos[0], linea_datos[1], linea_datos[2])
                listado_objetos[clave].append(gran_premio)

        elif NOMBRE_FICHERO_CABALLOS in nombre_fichero:
            for linea_datos in datos:
                caballo = Caballo(nombre=linea_datos[0], fecha_nacimiento=linea_datos[1], velocidad=linea_datos[2],
                                  experiencia=linea_datos[3], valor_apuesta=linea_datos[4],
                                  id_granpremio=linea_datos[5])
                listado_objetos[clave].append(caballo)

        elif NOMBRE_FICHERO_APOSTANTES in nombre_fichero:
            for linea_datos in datos:
                apostante = Apostante(linea_datos[0], linea_datos[1])
                listado_objetos[clave].append(apostante)

    return listado_objetos


def leer_fichero(nombre_fichero):
    ''' Devuelve todas las líneas del nombre del fichero que se le pasa '''
    lineas = []
    with open(nombre_fichero, 'r') as fichero:
        for linea in fichero:
            lineas.append(linea)

    return lineas


def obtener_datos_fichero(nombre_fichero, separador="|"):
    ''' Devuelve todos los campos del nombre del fichero que se le pasa
    estableciendo un separador (por defecto es | )'''
    datos_fichero = []
    try:
        for linea in leer_fichero(nombre_fichero):
            datos_linea = linea.split(separador)
            datos_fichero.append(datos_linea)
    except Exception as e:
        print(e)

    return datos_fichero
