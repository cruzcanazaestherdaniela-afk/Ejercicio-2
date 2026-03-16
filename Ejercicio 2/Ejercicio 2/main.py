from Jugador import Jugador
from ServidorMinecraft import ServidorMinecraft

server = ServidorMinecraft()

j1 = Jugador("Sergio", 128)
j2 = Jugador("Alexa", 100)
j3 = Jugador("Ramiro", 62)
j4 = Jugador("Lucia", 115)

server.agregar_jugador(j1)
server.agregar_jugador(j2)
server.agregar_jugador(j3)
server.agregar_jugador(j4)
server.stacks_jugadores()
server.jugador_mas_diamantes()
server.total_diamantes()