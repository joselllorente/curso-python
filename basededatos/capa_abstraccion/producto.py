from datetime import datetime


class Producto:
    def __init__(self, id=None, nombre=None, precio=None, fecha_registro=None):
        self._id = id
        self._nombre = nombre
        self._precio = precio
        self._fecha_registro = fecha_registro

    def __str__(self):
        return

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
    def precio(self):
        return self._precio

    @precio.setter
    def precio(self, precio):
        self._precio = precio

    @property
    def email(self):
        return self._email

    @email.setter
    def fecha_registro(self, fecha_registro):
        self._fecha_registro = fecha_registro


if __name__ == '__main__':
    producto1 = Producto(1, 'Producto1', 50000, datetime.now())
    print(producto1)
    # Simular un insert
    producto1 = Producto(1, 'Producto2', 20000, datetime.now())
    print(producto1)
    # Simular un delete
    producto1 = Producto(id=1)
    print(producto1)
