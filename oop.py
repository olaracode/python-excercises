# Programacion Orientada a Objetos - OOP(Object Oriented Programming)
# En python cuando se hablan de objetos se habla de Clases

# Es una forma de estructurar datos

class Humanos:
    ## def __init__(instancia, nombre, edad)
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    
    # Metodos de un objeto / una clase
    # un objeto/clase puede tener tantos metodos como necesite
    def presentar(self):
        return f"Hola me llamo {self.nombre} y tengo {self.edad} años"
    

class Perro:
    def __init__(self, name, breed, vaccination, number, owner):
        self.name = name
        self.breed = breed
        self.vaccination = vaccination
        self.number = number
        self.owner = owner # humano_uno = Humanos("Pedro", 35)

    def ladra(self):
        print("wooof")

    def placa_identificacion(self):
        print(f"Nombre: {self.name} - Numero de dueño: {self.numero} - Vaunado: {self.vaccination}")
        print("Por favor llamar en caso de extraviado")

    def get_owner(self):
        print("Dueño:", self.owner.nombre, self.owner.edad)

humano_uno = Humanos("Pedro", 34)
humano_dos = Humanos("Reynaldo", 20)
humano_tres = Humanos("Juan", 18)

perro1 = Perro("Firulais", "Callejero", False, "04141111111", humano_uno)
perro1.get_owner()