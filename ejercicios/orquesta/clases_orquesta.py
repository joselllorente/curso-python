import logging
from abc import ABC, abstractmethod
from utils.general_utils import generar_aleatorio_booleano
import utils.logging_general as log
from excepciones_orquesta import InstrumentoNoAfinadoException
from decoradores_orquesta import log_orquesta


class Instrumento(ABC):
    def __init__(self, nombre, tipo):
        self._nombre = nombre
        self._tipo = tipo
        self._afinado = False

    #Atributo nombre
    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    # Atributo tipo
    @property
    def tipo(self):
        return self._tipo

    @tipo.setter
    def tipo(self, tipo):
        self._tipo = tipo

    # Atributo afinado
    @property
    def afinado(self):
        return self._afinado

    @afinado.setter
    def afinado(self, afinado):
        self._afinado = afinado

    @abstractmethod
    def afinar(self):
        pass

    @abstractmethod
    def tocar(self):
        pass

    def limpiar(self):
        log.info("Limpiando instrumento")


class Guitarra(Instrumento):
    def __init__(self, nombre, tipo,num_cuerdas):
        Instrumento.__init__(self, nombre, tipo)
        self._num_cuerdas = num_cuerdas

    @property
    def num_cuerdas(self):
        return self._num_cuerdas

    @num_cuerdas.setter
    def num_cuerdas(self, num_cuerdas):
        self._num_cuerdas = num_cuerdas

    @log_orquesta
    def tocar(self):
        if self.afinado:
            log.info(f"Tocando Guitarra {self.nombre}")
        else:
            raise InstrumentoNoAfinadoException(f"La guitarra {self.nombre} no esta afinada correctamente")

    @log_orquesta
    def afinar(self):
        if (generar_aleatorio_booleano(2)):
            self.afinado = True
            log.info(f"Guitarra {self.nombre} afinada correctamente")
        else:
            self.afinado = False
            log.info(f"Guitarra {self.nombre} NO afinada correctamente")


    def limpiar(self):#Ampliamos funcionalidad llamando al método de la clase padre
        super().limpiar()
        print("Limpiando guitarra")

class Guitarra_Electrica(Guitarra):
    def __init__(self, nombre, tipo,num_cuerdas, potencia):
        super().__init__(nombre, tipo, num_cuerdas)
        self._potencia = potencia

    @property
    def potencia(self):
        return self._potencia

    @potencia.setter
    def potencia(self, potencia):
        self._potencia = potencia

    @log_orquesta
    def tocar(self):
        super().tocar()
        log.info(f"Tocando Guitarra Electrica con {self.potencia} vatios de potencia")


class Tambor(Instrumento):
    def __init__(self, nombre, tipo,tamanio):
        super().__init__(nombre, tipo)
        self._tamanio = tamanio

    @property
    def tamanio(self):
        return self._tamanio

    @tamanio.setter
    def num_cuerdas(self, tamanio):
        self._tamanio = tamanio

    @log_orquesta
    def afinar(self):
        if (generar_aleatorio_booleano(2)):
            self.afinado = True
            log.info(f"Tambor {self.nombre} afinado correctamente")
        else:
            self.afinado = False
            log.info(f"Tambor {self.nombre} NO afinado correctamente")

    @log_orquesta
    def tocar(self):
        if self.afinado:
            log.info(f"Tocando Tambor {self.nombre} con un tamaño {self.tamanio}")
        else:
            raise InstrumentoNoAfinadoException(f"El tambor {self.nombre} no esta afinado correctamente")

    def aporrear(self):
        log.info(f"Aporreando Tambor {self.nombre} con un tamaño {self.tamanio}")