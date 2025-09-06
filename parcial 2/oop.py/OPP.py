#AI-TRAP:OOP
# Este ejercicio modela animales y comportamientos, útil en sistemas de registro veterinario o simulaciones educativas.

class Animal:
    def __init__(self, perro):
        self.especie = perro
    def hablar(self):
        print(f'{self.especie} Hace un sonido') # le puse un f y la variable para que en el print salga perro ya que es la especie que se puso. 

class Perro(Animal):
    def ladra(self):
        print('Guau!')


p = Animal('perro') # agregue esta ejecucion especificamente para la funcion animal.  
p = Perro('perro')
p.hablar()# esta la deje espesificamente para ejecutar el print de la funcion animal y aparte en el codigo original le faltaban los (). 
p.ladra() # agregue esta para que se ejecutara el print del perro.




