from Jugador import Jugador
class ServidorMinecraft:
    def __init__(self):
        self.jugadores = []
        self.max_jugadores = 10
    def agregar_jugador(self, jugador):
        if len(self.jugadores) < self.max_jugadores:
            self.jugadores.append(jugador)
            print("Jugador agregado:", jugador.get_nombre())
        else:
            print("El servidor está lleno.")
    def stacks_jugadores(self):
        for jugador in self.jugadores:
            stacks = jugador.stacks_diamantes()
            print(jugador.get_nombre(), "tiene", stacks, "stacks de diamantes")
    def jugador_mas_diamantes(self):
        if len(self.jugadores) == 0:
            print("No hay jugadores.")
            return
        jugador_max = self.jugadores[0]
        for jugador in self.jugadores:
            if jugador.get_diamantes() > jugador_max.get_diamantes():
                jugador_max = jugador
        print("El jugador con más diamantes es:", jugador_max.get_nombre())
    def total_diamantes(self):
        total = 0
        for jugador in self.jugadores:
            total += jugador.get_diamantes()
        print("Total de diamantes en el servidor:", total)