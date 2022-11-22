from abc import ABC, abstractmethod
from utils.general_utils import pide_datos
import logging as log
import random
from excepciones import TemperatureException, TooHotTemperatureException, TooColdTemperatureException


class TazaCafe:
    def __init__(self, tipocafe, temperatura):
        self.tipocafe = tipocafe
        self.temperatura = temperatura


class Persona(ABC):
    def __init__(self, nombre):
        self.nombre = nombre


class Cliente(Persona):

    def tomar_taza(self, tazacafe):
        log.info("El cliente {} se está tomado la taza de cafe".format(self.nombre))
        if tazacafe.temperatura > 60:
            # log.info("El cliente {} ha dicho que el cafe estaba muy caliente".format(self.nombre))
            raise TooHotTemperatureException("Cafe muy caliente")
        elif tazacafe.temperatura < 40:
            # log.info("El cliente {} ha dicho que el cafe estaba muy frio".format(self.nombre))
            raise TooColdTemperatureException("Cafe muy frio")


class Camarero(Persona):

    def servir_taza(self):
        log.info("El camarero está poniendo el café")
        taza_cafe = TazaCafe(pide_datos("Cómo desea el café?"), random.randint(0, 100))
        log.debug("Taza de café {} creada a {} grados".format(taza_cafe.tipocafe, taza_cafe.temperatura))

        return taza_cafe


class Bar:
    def __init__(self, camarero):
        self.camarero = camarero

    def atender_cliente(self, cliente):
        try:
            taza_cafe = self.camarero.servir_taza()
            cliente.tomar_taza(taza_cafe)
        except TooHotTemperatureException as thte:
            log.error(thte.message)
            log.error("El camarero le pone un vaso de agua")
        except TooColdTemperatureException as tcte:
            log.error(tcte.message)
            log.error("El camarero le calienta más el café")
        except Exception as e:
            log.error("Al cliente le pasa algo")
        else:
            log.info(
                "El cliente {} se ha tomado el café muy agusto a {} grados".format(cliente.nombre,
                                                                                   taza_cafe.temperatura))


if __name__ == "__main__":
    cliente = Cliente("cliente1")
    camarero = Camarero("camarero1")
    bar = Bar(camarero)
    bar.atender_cliente(cliente)
