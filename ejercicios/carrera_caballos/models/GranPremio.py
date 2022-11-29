class GranPremio:

    def __init__(self, nombre, distancia, num_carreras, id=None):
        self._id = id
        self._nombre = nombre
        self._distancia = distancia
        self._num_carreras = num_carreras

    def __str__(self):
        return "{}:{}:{}:{}".format(self._id, self._nombre,
                                    self._distancia, self._num_carreras)

    # GranPremio.id
    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value

    # GranPremio.nombre
    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, value):
        self._nombre = value

    # GranPremio.distancia
    @property
    def distancia(self):
        return self._distancia

    @distancia.setter
    def distancia(self, value):
        self._distancia = value

    # GranPremio.num_carreras
    @property
    def num_carreras(self):
        return self._num_carreras

    @num_carreras.setter
    def num_carreras(self, value):
        self._num_carreras