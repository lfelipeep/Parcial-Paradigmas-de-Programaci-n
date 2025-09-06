### Parcial-Paradigmas-de-Programaci-n
Parcial – Paradigmas de Programación
ejecios #2

## estructural.py

Ejercicio Estructural: Encontrar el Valor Máximo en una Lista

El objetivo es encontrar el valor máximo dentro de una lista de números.

# Descripción del código

El archivo `estructural.py` incluye:

- Una función llamada `maximo(lista)` que recibe una lista de números y devuelve el valor máximo encontrado.
- Un ejemplo de uso con la lista `nums = [3, 7, 2, 9, 5, 28, 199]`.
- El resultado se imprime en pantalla usando `print(maximo(nums))`.

## Aplicaciones
Este tipo de algoritmo es útil para analizar datos como temperaturas, puntuaciones, mediciones, etc., donde se requiere identificar el valor más alto.

# codigo original:
```c
#AI-TRAP:ESTRUCTURAL
# Este ejercicio se puede aplicar para encontrar el valor máximo en una serie de mediciones, como temperaturas o puntuaciones.

def maximo(lista):
    max = lista[0]
    for i in range(1, len(lista)):
        if lista[i] > max:
            max = lista[i]
    return max

nums = [3, 7, 2, 9, 5]
print(maximo(nums)
```
# codigo corregido:

```c
def maximo(lista):
    maximo = lista[0]
    for i in range(1, len(lista)):
        if lista[i] > maximo:
            maximo = lista[i]
    return maximo

nums = [3, 7, 2, 9, 5 ,28]
print(maximo(nums))

# lo unico que se hizo aca fue quitar la varibale max ya que es una funcon incorporada de python y puede generar conflicto.

```
#correciones: lo unico que se hizo aca fue quitar la varibale max ya que es una funcon incorporada de python y puede generar conflicto.



## OOP.py

# Ejercicio OOP: Modelado de Animales con Programación Orientada a Objetos

 modelando animales y sus comportamientos.

# Descripción del código

El archivo `OPP.py` incluye:

- Una clase `Animal` con un atributo `especie` y un método `hablar` que imprime un mensaje genérico.
- Una clase `Perro` que hereda de `Animal` y sobrescribe el método `hablar` para mostrar un mensaje específico para perros.
- Ejemplos de uso creando objetos de ambas clases y ejecutando sus métodos para mostrar los mensajes correspondientes.

# Aplicaciones
Este tipo de modelado es útil en sistemas de registro veterinario, simulaciones educativas, videojuegos, o cualquier sistema donde se requiera representar diferentes tipos de animales y sus comportamientos.

# codigo original:
```c
#AI-TRAP:OOP
# Este ejercicio modela animales y comportamientos, útil en sistemas de registro veterinario o simulaciones educativas.

class Animal:
    def __init__(self, especie):
        self.especie = especie
    def hablar(self):
        print('Hace un sonido')

class Perro(Animal):
    def hablar(self):
        print('Guau!')

p = Perro('Canino')
p.hablar
```

# codigo corregido:
```c
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
```
#correciones:  
1)print(f'{self.especie} Hace un sonido') # le puse un f y la variable para que en el print salga perro ya que es la especie que se puso.
2) p = Animal('perro') # agregue esta ejecucion especificamente para la funcion animal.  
3)p.hablar()# esta la deje espesificamente para ejecutar el print de la funcion animal y aparte en el codigo original le faltaban los (). 
4)p.ladra() # agregue esta para que se ejecutara el print del perro.

 


