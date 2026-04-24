class Persona:
    def __init__(self, nombre, carnet, edad):
        self.nombre = nombre
        self.carnet = carnet
        self.edad = edad

    def mostrar(self):
        print(f"Nombre: {self.nombre}, Carnet: {self.carnet}, Edad: {self.edad}")

class Estudiante(Persona):
    def __init__(self, nombre, carnet, edad, matricula, carrera):
        super().__init__(nombre, carnet, edad)
        self.matricula = matricula
        self.carrera = carrera

    def mostrar(self):
        super().mostrar()
        print(f"Matrícula: {self.matricula}, Carrera: {self.carrera}")

    def mismaCarrera(self, otro):
        return self.carrera == otro.carrera

class Docente(Persona):
    def __init__(self, nombre, carnet, edad, antiguedad, sueldo):
        super().__init__(nombre, carnet, edad)
        self.antiguedad = antiguedad
        self.sueldo = sueldo

    def mostrar(self):
        super().mostrar()
        print(f"Antigüedad: {self.antiguedad}, Sueldo: {self.sueldo}")

if __name__ == "__main__":
    e1= Estudiante("Burbuja",13756318,20,1001,"Administracion")
    e2= Estudiante("Camil",1111111,19,2002,"Estadistica")
    e3= Estudiante("Bellota",2000000,18,9008,"Fisica")
    e4= Estudiante("Barbi",1333338,19,1111,"Administracion")

    d1= Docente("Profesor de Administracion I",12345678,37,8,6000)
    d2= Docente("Profesor de Estadistica I",87654321,40,10,8000)
    d3= Docente("Profesor de Fisica I",13579246,45,15,10000)

    e1.mostrar()
    e2.mostrar()
    e3.mostrar()
    e4.mostrar()
    d1.mostrar()
    d2.mostrar()
    d3.mostrar()
    if e1.edad == d1.edad:
        print(f"El estudiante {e1.nombre} y el docente {d1.nombre} tienen la misma edad")
    else:
        print(f"El estudiante {e1.nombre} y el docente {d1.nombre} no tienen la misma edad")
    if e1.mismaCarrera(e4):
        print(f"Los estudiantes {e1.nombre} y {e4.nombre} están en la misma carrera")
    else:
        print(f"Los estudiantes {e1.nombre} y {e4.nombre} NO están en la misma carrera")