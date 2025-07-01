# Trabajo Práctico 5 - Listas
# Alumno: Valentín Rodríguez
# DNI: 43523626
# Ejercicio 1: Crear una lista con los números del 1 al 100 que sean múltiplos de 4.

multiplos_de_4 = list(range(4, 101, 4))
print("Ejercicio 1 - Múltiplos de 4 del 1 al 100:")
print(multiplos_de_4)

# Ejercicio 2: Crear una lista con cinco elementos y mostrar el penúltimo.

mis_favoritos = ["café", "coca cola", "películas", "viajar", "fútbol"]
penultimo = mis_favoritos[-2]

print("Ejercicio 2 - Penúltimo elemento de la lista:")
print(penultimo)

# Ejercicio 3: Crear una lista vacía y agregar tres palabras usando append.

lista_vacia = [] 

lista_vacia.append("python")
lista_vacia.append("listas")
lista_vacia.append("universidad")

print("Ejercicio 3 - Lista con palabras agregadas:")
print(lista_vacia)

# Ejercicio 4: Reemplazar el segundo y último valor de la lista “animales”.

animales = ["perro", "gato", "conejo", "pez"]

animales[1] = "loro"

animales[-1] = "oso"

print("Ejercicio 4 - Lista modificada de animales:")
print(animales)

# Ejercicio 5 - Análisis del código

# El programa define una lista de números:
numeros = [8, 15, 3, 22, 7]

# se utiliza la función max(numeros) para encontrar el número más grande de la lista. en este caso, el número más grande es 22.
# La función remove() se usa para eliminar ese número de la lista.
numeros.remove(max(numeros))

# Finalmente, se imprime la lista actualizada, que ya no contiene el número 22.
print(numeros)

#este programa elimina el valor máximo de una lista de números.

# Ejercicio 6

numeros = list(range(10, 31, 5))

print("Los dos primeros números son:", numeros[0:2])

# Ejercicio 7

autos = ["sedan", "polo", "suran", "gol"]

autos[1:3] = ["corolla", "civic"]

print("Lista modificada de autos:", autos)

# Ejercicio 8

dobles = []

dobles.append(5 * 2)
dobles.append(10 * 2)
dobles.append(15 * 2)

print("Lista de dobles:", dobles)

# Ejercicio 9

compras = [["pan", "leche"], ["arroz", "fideos", "salsa"], ["agua"]]

compras[2].append("jugo")

compras[1][1] = "tallarines"

compras[0].remove("pan")

print("Lista de compras actualizada:", compras)

# Ejercicio 10

lista_anidada = [
    15,                 # lista_anidada[0]
    True,               # lista_anidada[1]
    [25.5, 57.9, 30.6], # lista_anidada[2][0], [2][1], [2][2]
    False               # lista_anidada[3]
]

print("Lista anidada:", lista_anidada)


