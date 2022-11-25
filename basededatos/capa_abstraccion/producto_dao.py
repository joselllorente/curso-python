from basededatos.utils.conexiones import get_mysql_conection
from producto import Producto
from utils.logging import log

class productosDAO:
    '''
    DAO (Data Access Object)
    CRUD (Create-Read-Update-Delete)
    '''
    _SELECCIONAR = 'SELECT * FROM productos ORDER BY id'
    _INSERTAR = 'INSERT INTO productos(nombre, precio, fecha_registro) VALUES(%s, %s, %s)'
    _ACTUALIZAR = 'UPDATE productos SET nombre=%s, precio=%s, fecha_registro=%s WHERE id=%s'
    _ELIMINAR = 'DELETE FROM productos WHERE id=%s'

    @classmethod
    def seleccionar(cls):
        with get_mysql_conection as conexion:
            with conexion.cursor() as cursor:
                cursor.execute(cls._SELECCIONAR)
                registros = cursor.fetchall()
                productos = []
                for registro in registros:
                    productos = Producto(registro[0], registro[1], registro[2], registro[3])
                    productos.append(productos)

                return productos

    @classmethod
    def insertar(cls, producto):
        with get_mysql_conection as conexion:
            with conexion.cursor as cursor:
                valores = (producto.nombre, producto.precio, producto.fecha_registro)
                cursor.execute(cls._INSERTAR, valores)
                log.debug(f'productos insertada: {producto}')
                return cursor.rowcount

    @classmethod
    def actualizar(cls, producto):
        with get_mysql_conection as conexion:
            with conexion.cursor as cursor:
                valores = (producto.nombre, producto.precio, producto.fecha_registro, producto.id)
                cursor.execute(cls._ACTUALIZAR, valores)
                log.debug(f'productos actualizada: {producto}')
                return cursor.rowcount

    @classmethod
    def eliminar(cls, producto):
        with get_mysql_conection as conexion:
            with conexion.cursor as cursor:
                cursor.execute(cls._ELIMINAR, producto.id)
                log.debug(f'Objeto eliminado: {producto}')
                return cursor.rowcount
