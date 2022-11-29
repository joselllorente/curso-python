from ejercicios.carrera_caballos.models.Apostante import Apostante


class ApostanteDAO:
    _INSERTAR = "INSERT INTO `apostantes` (`nombre`, `saldo`) " \
                "VALUES (%s, %s)"

    _UPDATE = "UPDATE `apostantes` " \
              "SET `saldo` = %s " \
              "WHERE `apostantes`.`id` = %s"

    _SELECCIONAR = 'SELECT id, nombre, saldo ' \
                   'FROM apostantes ' \
                   'ORDER BY id'

    @classmethod
    def insertar(cls, apostante, cursor):
        valores = (apostante.nombre, apostante.saldo)
        cursor.execute(cls._INSERTAR, valores)

    @classmethod
    def insertar_apostantes(cls, apostantes, cursor):
        for apostante in apostantes:
            cls.insertar(apostante, cursor)

    @classmethod
    def update(cls, apostante, cursor):
        valores = (apostante.saldo, apostante.id)
        cursor.execute(cls._UPDATE, valores)

    @classmethod
    def update_many(cls, apostantes, cursor):
        for apostante in apostantes:
            cls.update(apostante, cursor)

    @classmethod
    def seleccionar(cls, cursor):
        cursor.execute(cls._SELECCIONAR)
        registros = cursor.fetchall()
        list_apostantes = []
        for registro in registros:
            apostante = Apostante(id=registro[0], nombre=registro[1], saldo=registro[2])
            list_apostantes.append(apostante)
        return list_apostantes
