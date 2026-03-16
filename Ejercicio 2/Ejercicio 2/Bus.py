class Bus:
    def __init__(self, capacidad_bus):
        self.capacidad_bus = capacidad_bus
        self.pasajeros_bus = 0
        self.precio = 1.50
    def get_capacidad_bus(self):
        return self.capacidad_bus
    def get_pasajeros_bus(self):
        return self.pasajeros_bus
    def set_capacidad_bus(self, capacidad_bus):
        self.capacidad_bus = capacidad_bus
    def set_pasajeros_bus(self, pasajeros_bus):
        self.pasajeros_bus = pasajeros_bus
    def subir_pasajeros(self, cantidad):
        if self.pasajeros_bus + cantidad <= self.capacidad_bus:
            self.pasajeros_bus += cantidad
            print("Subieron", cantidad, "pasajeros")
        else:
            disponibles = self.capacidad_bus - self.pasajeros_bus
            self.pasajeros_bus = self.capacidad_bus
            print("Subieron", disponibles, "pasajeros. El bus está lleno.")
    def cobrar_pasaje(self):
        if self.pasajeros_bus >= self.capacidad_bus:
            total = self.capacidad_bus * self.precio
        else:
            total = self.pasajeros_bus * self.precio
        return total
    def asientos_disponibles(self):
        return self.capacidad_bus - self.pasajeros_bus
    
bus1 = Bus(50)
bus1.subir_pasajeros(51)
print("Total a cobrar:", bus1.cobrar_pasaje())
print("Asientos disponibles:", bus1.asientos_disponibles())

bus2 = Bus(60)
bus2.subir_pasajeros(26)
print("Total a cobrar:", bus2.cobrar_pasaje())
print("Asientos disponibles:", bus2.asientos_disponibles())