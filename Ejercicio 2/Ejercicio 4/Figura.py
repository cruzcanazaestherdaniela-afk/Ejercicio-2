import math
from abc import ABC, abstractmethod

class Figura(ABC):
    def __init__(self, color):
        self.color = color

    @abstractmethod
    def obtenerArea(self):
        pass

class Cuadrado(Figura):
    def __init__(self, lado, color):
        super().__init__(color)
        self.lado = lado

    def obtenerArea(self):
        return self.lado ** 2

class Triangulo(Figura):
    def __init__(self, lado1, lado2, lado3, color):
        super().__init__(color)
        self.l1 = lado1
        self.l2 = lado2
        self.l3 = lado3

    def obtenerArea(self):
        s = (self.l1 + self.l2 + self.l3) / 2
        return math.sqrt(s * (s - self.l1) * (s - self.l2) * (s - self.l3))

class Redondo(Figura):
    def __init__(self, radio, color):
        super().__init__(color)
        self.radio = radio

    def obtenerArea(self):
        return math.pi * self.radio ** 2

if __name__ == "__main__":
    figuras = [
        Cuadrado(6, "Rosado Suave"),
        Cuadrado(8, "Celeste Pastel"),
        Triangulo(2, 4, 6, "Verde Menta"),
        Triangulo(5, 5, 5, "Amarillo Fosforecente"),
        Redondo(3, "Azul Marino"),
        Redondo(7, "Morado Lavanda")
    ]
    print("Áreas:")
    for f in figuras:
        print(f"{type(f).__name__} ({f.color}), y su Area es: {f.obtenerArea():.2f}")

    c = Cuadrado(2, "Rojo Sangriento")
    t = Triangulo(5, 8, 6, "Verde Esmeralda")

    if c.obtenerArea() > t.obtenerArea():
        print("Mayor area es: cuadrado, color:", c.color)
    else:
        print("Mayor area es: triangulo, color:", t.color)