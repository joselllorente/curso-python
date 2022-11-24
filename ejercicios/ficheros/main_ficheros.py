from Tools.scripts.var_access_benchmark import A

import utils.logging_general as log
import logging
from clases_colegio import Colegio, Alumno

COLEGIO = 0
NOMBRE_ALUMNO = 1
APELLIDOS_ALUMNO = 2
DNI_ALUMNO = 3
ASIGNATURAS_ALUMNO = 4
SEPARADOR_DATOS = "|"
SEPARADOR_ASIGNATURAS = ";"

if __name__ == "__main__":
    log.setupLogging(logging.DEBUG, "../logs/ficheros_colegio.log")

    colegios = {}
    log.debug("Empezando a leer el archivo")
    # print("Empezando a leer el archivo")
    with open('alumnos-colegio.txt', 'r', encoding='utf8') as archivo:
        for linea in archivo:
            # print(linea)
            log.debug(linea)
            datos = linea.split(SEPARADOR_DATOS)
            log.debug(datos)
            nombre_colegio = datos[COLEGIO]
            alumno = Alumno(datos[NOMBRE_ALUMNO], datos[APELLIDOS_ALUMNO], datos[DNI_ALUMNO],
                            datos[ASIGNATURAS_ALUMNO].split(SEPARADOR_ASIGNATURAS))
            log.debug("Asignaturas:", alumno.asignaturas)
            if not nombre_colegio in colegios:
                colegios[nombre_colegio] = [alumno]
            else:
                colegios[nombre_colegio].append(alumno)
            # colegios[colegio.nombre] += [alumno]
            # colegios.update(colegios)
            # colegios[colegio.nombre].append(alumno)

    for colegio, alumnos in colegios.items():
        log.debug(colegio)
        archivo_escritura = open(f'{colegio}.txt', "w", encoding="UTF-8")
        for alumno in alumnos:
            log.debug(alumno.asignaturas)
            archivo_escritura.write(str(alumno))
