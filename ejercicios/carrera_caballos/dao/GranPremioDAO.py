from ejercicios.carrera_caballos.models.GranPremio import GranPremio


class GranPremioDAO:
    _INSERTAR = "INSERT INTO `grandes_premios` (`nombre`, `distancia`, `num_carreras`) VALUES (%s, %s, %s)"
    _SELECCIONAR = 'SELECT id,nombre,distancia, num_carreras FROM grandes_premios'

    @classmethod
    def insertar(cls, gran_premio, cursor):
        valores = (gran_premio.nombre, gran_premio.distancia, gran_premio.num_carreras)
        cursor.execute(cls._INSERTAR, valores)

    @classmethod
    def insertar_grandespremios(cls, gran_premios, cursor):
        for gran_premio in gran_premios:
            cls.insertar(gran_premio, cursor)

    @classmethod
    def seleccionar(cls, cursor):
        cursor.execute(cls._SELECCIONAR)
        registros = cursor.fetchall()
        list_gran_premio = []

        for registro in registros:
            gran_premio = GranPremio(id=registro[0], nombre=registro[1], distancia=registro[2], num_carreras= registro[3])
            list_gran_premio.append(gran_premio)

        return list_gran_premio
