class Jugador:
    def __init__(self, nombre, diamantes):
        self.nombre = nombre
        self.diamantes = diamantes
    def get_nombre(self):
        return self.nombre
    def get_diamantes(self):
        return self.diamantes
    def set_diamantes(self, diamantes):
        self.diamantes = diamantes
    def stacks_diamantes(self):
        return self.diamantes // 64