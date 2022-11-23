import utils.logging_general as log
from clases_orquesta import *


class Orquesta:
    def __init__(self,nombre):
        self._nombre = nombre
        self.lista_instrumentos = []

    # Atributo nombre
    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    def crear_orquesta(self):
        log.info(f"Iniciando orquesta {self.nombre}")
        guitarra = Guitarra("Guitarra","Española",5)
        guitarra_electrica = Guitarra_Electrica("Guitarra Electrica", "Española", 5, 150)
        tambor = Tambor("Tambor1","Tipo","Grande")

        self.lista_instrumentos = [guitarra, guitarra_electrica, tambor]

    def iniciar_concierto(self):
        log.info(f"Iniciando Concierto")
        self.afinar_instrumentos()
        self.tocar_instrumentos()


    def afinar_instrumentos(self):
        log.info(f"Afinando Instrumentos:")
        for intrumento in self.lista_instrumentos:
            intrumento.afinar()

    def tocar_instrumentos(self):
        log.info(f"Tocando Instrumentos:")
        try:
            for instrumento in self.lista_instrumentos:
                if isinstance(instrumento, Tambor):
                    instrumento.aporrear()
                else:
                    instrumento.tocar()

        except InstrumentoNoAfinadoException as ine:
            log.error(ine)
            log.info("El concierto se detiene porque un instrumento no está afinado")
            self.iniciar_concierto()


if __name__ == '__main__':
    log.info(f"Empezando")
    orquesta = Orquesta("Orquesta Mondragon")
    orquesta.crear_orquesta()
    orquesta.iniciar_concierto()