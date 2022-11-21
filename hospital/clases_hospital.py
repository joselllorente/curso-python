import utils.logging_hospital as log
# Abstract Basic Class
from abc import ABC, abstractmethod
import datetime
import random
import utils.utils_hospital as util
from utils.general_utils import generar_aleatorio_booleano


class Persona(ABC):
    def __init__(self, nombre, apellidos, dni):
        self.nombre = nombre
        self.apellidos = apellidos
        self.dni = dni

    def __str__(self):
        return "Dni: {}, nombre: {}, apellidos: {}".format(self.dni, self.nombre, self.apellidos)


class Enfermo(Persona):
    def __init__(self, nombre, apellidos, dni, enfermedad):
        super().__init__(nombre=nombre, apellidos=apellidos, dni=dni)
        self.enfermedad = enfermedad


class Paciente(Persona):
    def __init__(self, nombre, apellidos, dni, sintomas=[]):
        super().__init__(nombre=nombre, apellidos=apellidos, dni=dni)
        self.sintomas = sintomas


class Empleado_Hospital(Persona, ABC):
    def __init__(self, nombre, apellidos, dni):
        super().__init__(nombre, apellidos, dni)
        self.ultimo_fichaje = None
        self.en_servicio = False

    @abstractmethod
    def fichar(self):
        pass


class Doctor(Empleado_Hospital):
    def __init__(self, nombre, apellidos, dni,  especialidad):
        super().__init__(nombre, apellidos, dni)
        self.especialidad = especialidad

    def fichar(self):
        dt = datetime.datetime.now()
        self.ultimo_fichaje = dt
        self.en_servicio = not self.en_servicio
        log.info("El doctor {} esta fichando el día  {}/{}/{} {}:{}:{}".format(self.nombre, self.ultimo_fichaje.day,
                    self.ultimo_fichaje.month, self.ultimo_fichaje.year,
                    self.ultimo_fichaje.hour, self.ultimo_fichaje.minute, self.ultimo_fichaje.second ))

    def tratar_paciente(self, paciente):
        '''El doctor mira si elpaciente está enfermo y si lo está
        crea un objeto de tipo enfermo con una enfermedad aleatoria'''
        log.info("El doctor {} esta tratando al paciente {}".format(self.nombre, paciente.nombre))
        paciente_esta_enfermo = generar_aleatorio_booleano(0)
        enfermedad = random.choice(util.ENFERMEDADES)

        if(paciente_esta_enfermo):
            log.warn("El pacciente {} esta enfermo tiene {}".format(paciente.nombre, enfermedad))
            enfermo = Enfermo(paciente.nombre, paciente.apellidos, paciente.dni, enfermedad)
            return enfermo
        else:
            log.info("El pacciente {} esta sano abandona el hospital".format(paciente.nombre))
            return None



class Enfermero(Empleado_Hospital):
    def __init__(self, nombre, apellidos, dni, planta):
        super().__init__(nombre, apellidos, dni)
        self.enfermedad = planta

    def fichar(self):
        dt = datetime.datetime.now()
        self.ultimo_fichaje = dt
        self.en_servicio = not self.en_servicio
        log.info("El enfermero {} esta fichando el día {}/{}/{} {}:{}:{}".format(self.nombre, self.ultimo_fichaje.day,
                                                                          self.ultimo_fichaje.month,
                                                                          self.ultimo_fichaje.year,
                                                                          self.ultimo_fichaje.hour,
                                                                          self.ultimo_fichaje.minute,
                                                                          self.ultimo_fichaje.second))

    def atiende_paciente(self,paciente, consulta):
        log.info("El enfermero {} esta asignando al paciente {} a la consulta {}".format(self.nombre, paciente.nombre , consulta.nombre))
        consulta.paciente = paciente


class Consulta:
    def __init__(self, nombre, doctor):
        self.nombre = nombre
        self.doctor = doctor
        self.paciente = None

