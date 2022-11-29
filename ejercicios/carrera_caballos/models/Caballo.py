import random
from datetime import datetime


class Caballo:
    def __init__(self, nombre, fecha_nacimiento, velocidad, experiencia, valor_apuesta, id_granpremio, id=None):
        self._id = id
        self._nombre = nombre
        self._fecha_nacimiento = fecha_nacimiento
        self._velocidad = velocidad
        self._experiencia = experiencia
        self._valor_apuesta = valor_apuesta
        self._id_granpremio = id_granpremio
        self._dist_recorrida = 0

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, id):
        self._id = id

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    @property
    def fecha_nacimiento(self):
        return self._fecha_nacimiento

    @fecha_nacimiento.setter
    def fecha_nacimiento(self, fecha_nacimiento):
        self._fecha_nacimiento = fecha_nacimiento

    @property
    def velocidad(self):
        return self._velocidad

    @velocidad.setter
    def velocidad(self, velocidad):
        self._velocidad = velocidad

    @property
    def experiencia(self):
        return self._experiencia

    @experiencia.setter
    def experiencia(self, experiencia):
        self._experiencia = experiencia

    @property
    def valor_apuesta(self):
        return self._valor_apuesta

    @valor_apuesta.setter
    def valor_apuesta(self, valor_apuesta):
        self._valor_apuesta = valor_apuesta

    @property
    def id_granpremio(self):
        return self._id_granpremio

    @id_granpremio.setter
    def id_granpremio(self, id_granpremio):
        self._id_granpremio = id_granpremio

    @property
    def dist_recorrida(self):
        return self._dist_recorrida

    @dist_recorrida.setter
    def dist_recorrida(self, dist_recorrida):
        self._dist_recorrida = dist_recorrida

    def __str__(self):
        return str(self.id) + " " + str(self.nombre) + " " + str(self.valor_apuesta)
        # return self.nombre + " " + str(self.fecha_nacimiento)+" "+str(self.id_granpremio)

    def correr(self):
        anio_caballo = self.fecha_nacimiento.year
        self.dist_recorrida += self.velocidad + self.experiencia - (
                    datetime.now().year - anio_caballo) + random.randint(1, 50)
