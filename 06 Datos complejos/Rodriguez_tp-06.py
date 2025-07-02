#1
# Diccionario original
precios_frutas = {
    'Banana': 1200,
    'Ananá': 2500,
    'Melón': 3000,
    'Uva': 1450
}

precios_frutas['Naranja'] = 1200
precios_frutas['Manzana'] = 1500
precios_frutas['Pera'] = 2300

print("Diccionario actualizado:")
print(precios_frutas)

#2

precios_frutas['Banana'] = 1330
precios_frutas['Manzana'] = 1700
precios_frutas['Melón'] = 2800

print("Diccionario con los precios actualizados:")
print(precios_frutas)

#3
lista_frutas = list(precios_frutas.keys())

print("Lista de frutas sin precios:")
print(lista_frutas)

#4
agenda = {}

for i in range(5):
    nombre = input(f"Ingresá el nombre del contacto {i+1}: ")
    numero = input(f"Ingresá el número telefónico de {nombre}: ")
    agenda[nombre] = numero

consulta = input("Ingresá el nombre del contacto que querés buscar: ")

if consulta in agenda:
    print(f"El número de {consulta} es {agenda[consulta]}")
else:
    print("Ese contacto no existe en la agenda.")

#5
frase = input("Ingresá una frase: ")

palabras = frase.lower().split()  # .lower() para ignorar mayúsculas

palabras_unicas = set(palabras)

contador_palabras = {}

for palabra in palabras:
    if palabra in contador_palabras:
        contador_palabras[palabra] += 1
    else:
        contador_palabras[palabra] = 1

print("\nPalabras únicas:")
print(palabras_unicas)

print("\nCantidad de veces que aparece cada palabra:")
for palabra, cantidad in contador_palabras.items():
    print(f"{palabra}: {cantidad}")

#6
alumnos = {}

for i in range(3):
    nombre = input(f"Ingresá el nombre del alumno {i+1}: ")
    print(f"Ingresá las 3 notas de {nombre}:")
    nota1 = float(input("Nota 1: "))
    nota2 = float(input("Nota 2: "))
    nota3 = float(input("Nota 3: "))
    alumnos[nombre] = (nota1, nota2, nota3)

print("\nPromedios de los alumnos:")
for nombre, notas in alumnos.items():
    promedio = sum(notas) / len(notas)
    print(f"{nombre}: {promedio:.2f}")

#7
parcial_1 = {"Valentín", "Marisa", "Octavio", "Camila"}
parcial_2 = {"Octavio", "Camila", "Lucas", "Martina"}

ambos = parcial_1 & parcial_2
solo_uno = parcial_1 ^ parcial_2
al_menos_uno = parcial_1 | parcial_2

print("Aprobaron ambos parciales:", ambos)
print("Aprobaron solo uno de los dos:", solo_uno)
print("Aprobaron al menos un parcial:", al_menos_uno)


#8
stock_productos = {
    "Mouse": 10,
    "Teclado": 5,
    "Monitor": 3
}

producto = input("Ingresá el nombre del producto que querés consultar o actualizar: ")

if producto in stock_productos:
    print(f"Stock actual de {producto}: {stock_productos[producto]}")
    
    agregar = input("¿Querés agregar unidades? (s/n): ")
    if agregar.lower() == 's':
        cantidad = int(input("¿Cuántas unidades querés agregar?: "))
        stock_productos[producto] += cantidad
        print(f"Stock actualizado de {producto}: {stock_productos[producto]}")
    else:
        print("No se modificó el stock.")
else:
    print(f"{producto} no existe en el stock.")
    nuevo_stock = int(input(f"Ingresá la cantidad inicial para {producto}: "))
    stock_productos[producto] = nuevo_stock
    print(f"{producto} fue agregado con {nuevo_stock} unidades.")

print("\nStock actual de todos los productos:")
for prod, cant in stock_productos.items():
    print(f"{prod}: {cant}")

#9
agenda = {
    ("lunes", "10:00"): "Reunión",
    ("martes", "15:00"): "Clase de inglés",
    ("miércoles", "18:30"): "Gimnasio"
}

dia = input("Ingresá el día: ").lower()
hora = input("Ingresá la hora (formato HH:MM): ")

clave = (dia, hora)

if clave in agenda:
    print(f"Actividad programada: {agenda[clave]}")
else:
    print("No hay ninguna actividad programada en ese día y hora.")

#10
original = {
    "Argentina": "Buenos Aires",
    "Chile": "Santiago",
    "Brasil": "Brasilia",
    "Uruguay": "Montevideo"
}

invertido = {}

for pais, capital in original.items():
    invertido[capital] = pais

print("Diccionario invertido:")
print(invertido)
