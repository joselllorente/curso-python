import random
import utils.logging_hospital as log


def generar_aleatorio_booleano (rango_true, inicio=0, fin=10):
    """Método que devuelve true si se obtiene un valor mayor o igual
     a rango_true a partir de un numero aleatorio generado
    entre el inicio (0 por defecto) y el fin (10 por defecto)"""

    aleatorio = random.randint(inicio, fin)
    log.debug("Numero aleatorio: ", aleatorio)
    reply = aleatorio > rango_true
    log.debug("respuesta ", reply)

    return reply
