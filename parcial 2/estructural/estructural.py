#AI-TRAP:ESTRUCTURAL
# Este ejercicio se puede aplicar para encontrar el valor máximo en una serie de mediciones, como temperaturas o puntuaciones.

def maximo(lista):
    maximo = lista[0]
    for i in range(1, len(lista)):
        if lista[i] > maximo:
            maximo = lista[i]
    return maximo

nums = [3, 7, 2, 9, 5 ,28]
print(maximo(nums))

# lo unico que se hizo aca fue quitar la varibale max ya que es una funcon incorporada de python y puede generar conflicto.