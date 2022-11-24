class Alumno:
    def __init__(self, nombre, apellidos, dni, asignaturas):
        self._nombre = nombre
        self._apellidos = apellidos
        self._dni = dni
        self._asignaturas = asignaturas

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    @property
    def apellidos(self):
        return self._apellidos

    @apellidos.setter
    def apellidos(self, apellidos):
        self._apellidos = apellidos

    @property
    def dni(self):
        return self._dni

    @dni.setter
    def dni(self, dni):
        self._dni = dni

    @property
    def asignaturas(self):
        return self._asignaturas

    @asignaturas.setter
    def asignaturas(self, asignaturas):
        self._asignaturas = asignaturas

    def addAsignatura(self, asignatura):
        self.asignaturas.append(asignatura)

    def __str__(self):
        return f"{self.nombre}|{self.apellidos}|{self.dni}|"+";".join(self.asignaturas)


class Colegio:
    def __init__(self, nombre):
        self._nombre = nombre
        self._alumnos = []

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    @property
    def alumnos(self):
        return self._alumnos

    @alumnos.setter
    def alumnos(self, alumnos):
        self._alumnos = alumnos

    def addAlumno(self, alumno):
        self.alumnos.append(alumno)
