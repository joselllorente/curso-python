class Apostante:
    def __init__(self, nombre, saldo, id=None):
        self._id = id
        self._nombre = nombre
        self._saldo = saldo
        self._saldo_apostado = 0
        self._caballo_apostado = None

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
    def saldo(self):
        return self._saldo

    @saldo.setter
    def saldo(self, saldo):
        self._saldo = saldo

    @property
    def saldo_apostado(self):
        return self._saldo_apostado

    @saldo_apostado.setter
    def saldo_apostado(self, saldo_apostado):
        self._saldo_apostado = saldo_apostado

    @property
    def caballo_apostado(self):
        return self._caballo_apostado

    @caballo_apostado.setter
    def caballo_apostado(self, caballo_apostado):
        self._caballo_apostado = caballo_apostado

    def __str__(self):
        return self.nombre + " " + str(self.saldo)