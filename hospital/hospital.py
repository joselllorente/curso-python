
import utils.logging_hospital as log
import clases_hospital as ch

class Hospital:
    def __init__(self, nombre, consultas, sala_espera, enfermeros):
        self.nombre = nombre
        self.consultas = consultas
        self.sala_espera = sala_espera
        self.habitaciones = [None, None, None]
        self.enfermeros = enfermeros

    def arranca_hospital(self):
        log.debug("Arrancando el hospital")
        #Fichan la entrada
        self.fichar_empleados()

        #Empezamos a atender a los pacientes
        while (self.hay_pacientes()):
            self.atender_pacientes_salaespera()
            self.atender_pacientes_consulta()


        # Fichan la salida
        self.fichar_empleados()

    def hay_pacientes(self):
        ''' Método que devuelve si hay pacientes en la sala de espera'''
        return len(self.sala_espera)>0

    def fichar_empleados(self):
        log.debug("Fichando doctores")
        #Pongo a los doctores a fichar
        for consulta in self.consultas:
            consulta.doctor.fichar()

        log.debug("Fichando enfermeros")
        # Pongo a los enfermeros a fichar
        for enfermero in self.enfermeros:
            enfermero.fichar()


    def atender_pacientes_consulta(self):
        '''Los doctores de las consultas que tienen asignado un paciente tratan al paciente'''
        for consulta in self.consultas:
            #Si tiene asignado un paciente
            if (not consulta.paciente == None):
                #El doctor trata al paciente
                enfermo = consulta.doctor.tratar_paciente(consulta.paciente)
                if (not enfermo == None):
                    self.asignar_enfermo_habitacion(enfermo)
                else:
                    log.info("El paciente {} se está despidiendo ".format(consulta.paciente.nombre))
            #Sacamos al paciente de la consulta
            consulta.paciente = None

    def asignar_enfermo_habitacion(self, enfermo_registrado):

        habitacion_asignada = False
        for habitacion, enfermo in enumerate(self.habitaciones):
            if enfermo == None:
                self.habitaciones[habitacion] = enfermo_registrado
                log.info("Enfermo {} asignado a la habitacion {} ".format(enfermo_registrado.nombre,habitacion))
                habitacion_asignada = True
                break

        if (not habitacion_asignada):
            log.warn("No hay habitaciones disponobles se deriva al enfermo a otro Hospital")



    def atender_pacientes_salaespera(self):
        '''Método que recorre todos los enferemeros y por cada uno de ellos obtiene un paciente de la sala de espera
        y lo asigna a una consulta que esté libre'''
        for enfermero in self.enfermeros:
            #Obtenemos paciente
            paciente = self.obtener_paciente()
            # Obtenemos la consulta libre
            consulta = self.obtener_consulta_libre()
            #El enfermero lleva al paciente a la consulta
            if not paciente == None and not consulta == None:
                enfermero.atiende_paciente(paciente, consulta)




    def obtener_paciente(self):
        ''' Obtenemos paciente de la sala de espera, miramos que haya pacientes y se devuelve el primero'''
        paciente = None
        if (len(self.sala_espera)>0):
            paciente = self.sala_espera.pop(0)

        return paciente

    def obtener_consulta_libre(self):
        for consulta in self.consultas:
            if (consulta.paciente==None):
                return consulta

        return None

if __name__ == '__main__':
    #Defino todos los objetos

    #Doctores
    doctor1 = ch.Doctor("Doctor1","apellidos","dni1", "Medicina gneral")
    doctor2 = ch.Doctor("Doctor2", "apellidos2", "dni2", "Cirujia")

    #Consultas
    consulta1 = ch.Consulta("Consulta 1",doctor1)
    consulta2 = ch.Consulta("Consulta 2", doctor2)

    listado_consultas = [consulta1,consulta2]

    #Pacientes
    paciente1 = ch.Paciente("Paciente1","Apellidos1","1111A",["Dolor cabeza","tos"])
    paciente2 = ch.Paciente("Paciente2", "Apellidos2", "2222A", ["Dolor cabeza", "tos"])
    paciente3 = ch.Paciente("Paciente3", "Apellidos3", "3333A", ["Dolor cabeza", "tos"])
    paciente4 = ch.Paciente("Paciente4", "Apellidos4", "44444A", ["Dolor cabeza", "tos"])

    sala_de_espera = [paciente1, paciente2, paciente3, paciente4]

    #Enfermeros
    enfermero1 = ch.Enfermero("Enfermero1","apellidos","dni1", "Planta 1")
    enfermero2 = ch.Enfermero("Enfermero2", "apellidos", "dni1", "Planta 2")

    listado_enfermeros = [enfermero1, enfermero2]

    hospital = Hospital("Hospital 1", listado_consultas, sala_de_espera, listado_enfermeros)
    hospital.arranca_hospital()



