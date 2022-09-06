


class Vehiculo():
    def __init__(self, color, ruedas, puertas):
        self.color = color
        self.ruedas = ruedas
        self.puertas = puertas 

class Coche(Vehiculo):
    def __init__(self,color, ruedas, puertas, velocidad, cilindrada):
        self.color = color
        self.ruedas = ruedas
        self.puertas = puertas 
        self.velocidad = velocidad
        self.cilindrada = cilindrada
    def __str__(self):
        return "Color {}, {} ruedas, {} puertas, {} km/h, {} cc".format(self.color, self.ruedas, self.puertas, self.velocidad, self.cilindrada)



x = Coche("Blanco", 4, 5, 120, 1500)
print(x)


