from ejercicios.carrera_caballos.models.Caballo import Caballo


class CaballoDAO:
    _INSERTAR = "INSERT INTO `caballos` (`nombre`, `fecha_nacimiento`, `velocidad`, `experiencia`,\
                 `valor_apuesta`, `fk_gran_premio`) VALUES (%s, %s, %s, %s, %s, %s)"

    _UPDATE = "UPDATE `caballos` SET `experiencia` = %s WHERE `id` = %s"

    _SELECCIONAR = 'SELECT id, nombre, fecha_nacimiento, velocidad, ' \
                   'experiencia, valor_apuesta, fk_gran_premio ' \
                   'FROM caballos ' \
                   'ORDER BY id'

    @classmethod
    def insertar(cls, caballo, cursor):
        valores = (caballo.nombre, caballo.fecha_nacimiento, caballo.velocidad, caballo.experiencia,
                   caballo.valor_apuesta, caballo.id_granpremio)
        cursor.execute(cls._INSERTAR, valores)

    @classmethod
    def insertar_caballos(cls, caballos, cursor):
        for caballo in caballos:
            cls.insertar(caballo, cursor)

    @classmethod
    def update(cls, caballo, cursor):
        valores = (caballo.experiencia, caballo.id)
        cursor.execute(cls._UPDATE, valores)

    @classmethod
    def update_many(cls, caballos, cursor):
        for caballo in caballos:
            cls.update(caballo, cursor)

    @classmethod
    def seleccionar(cls, cursor):
        cursor.execute(cls._SELECCIONAR)
        registros = cursor.fetchall()
        list_caballos = []
        for registro in registros:
            caballo = Caballo(id=registro[0], nombre=registro[1], fecha_nacimiento=registro[2], velocidad=registro[3],
                              experiencia=registro[4], valor_apuesta=registro[5],
                              id_granpremio=registro[6])
            list_caballos.append(caballo)
        return list_caballos
