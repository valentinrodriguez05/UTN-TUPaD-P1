"""
TP3 – Estructuras Condicionales (10 ejercicios)
Autor: Valentín Rodríguez Arce
DNI: 43 523 626
Fecha: 2025-06-29
Descripción: script con la resolución completa de los 10 ejercicios.
"""

import random
from statistics import mean, median, mode
# 1)
edad = int(input("Ingrese su edad: "))
if edad >= 18:
    print("Es mayor de edad")
else:
    print("Es menor de edad")
# 2) 
nota = float(input("Ingrese su nota: "))
if nota >= 6:
    print("Aprobado")
else:
    print("Desaprobado")
# 3)
numero = int(input("Ingrese un número par: "))
if numero % 2 == 0:
    print("Ha ingresado un número par")
else:
    print("Por favor, ingrese un número par")
# 4) 
edad = int(input("Edad: "))
if edad < 12:
    categoria = "Niño/a"
elif edad < 18:        # 12 ≤ edad < 18
    categoria = "Adolescente"
elif edad < 30:        # 18 ≤ edad < 30
    categoria = "Adulto/a joven"
else:                  # edad ≥ 30
    categoria = "Adulto/a"

print(f"Perteneces a la categoría: {categoria}")
# 5)
pwd = input("Ingrese una contraseña (8-14 caracteres): ")

if 8 <= len(pwd) <= 14:
    print("Ha ingresado una contraseña correcta")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")
# 6)
numeros_aleatorios = [random.randint(1, 100) for _ in range(50)]

media   = mean(numeros_aleatorios)
mediana = median(numeros_aleatorios)
moda    = mode(numeros_aleatorios)

print(f"Media   : {media:.2f}")
print(f"Mediana : {mediana}")
print(f"Moda    : {moda}")

if media > mediana > moda:
    sesgo = "positivo (a la derecha)"
elif media < mediana < moda:
    sesgo = "negativo (a la izquierda)"
else:
    sesgo = "sin sesgo"

print("Conclusión:", sesgo)

# 7)
frase = input("Ingrese una frase o palabra: ")

if frase[-1].lower() in "aeiou":
    frase += "!"
print(frase)

# 8)
nombre = input("Ingrese su nombre: ")
opcion = input("Elija 1-MAYUSCULA, 2-miniscula, 3-Título: ")

if opcion == "1":
    print(nombre.upper())
elif opcion == "2":
    print(nombre.lower())
elif opcion == "3":
    print(nombre.title())
else:
    print("Opción inválida")
# 9) 
mag = float(input("Magnitud del terremoto: "))

if mag < 3:
    categoria = "Muy leve (imperceptible)"
elif mag < 4:
    categoria = "Leve (ligeramente perceptible)"
elif mag < 5:
    categoria = "Moderado (sentido por personas, sin daños)"
elif mag < 6:
    categoria = "Fuerte (daños en estructuras débiles)"
elif mag < 7:
    categoria = "Muy fuerte (daños significativos)"
else:
    categoria = "Extremo (graves daños a gran escala)"

print("Categoría:", categoria)
# 10)
dias_mes = [0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334, 365]

def dia_ordinal(mes, dia):
    return dias_mes[mes - 1] + dia  # ej. 1/1 -> 1

hemi = input("Hemisferio (N/S): ").strip().upper()
mes  = int(input("Mes (1-12): "))
dia  = int(input("Día (1-31): "))

orden = dia_ordinal(mes, dia)

inv =  dia_ordinal(12,21) <= orden <= 365 or 1 <= orden < dia_ordinal(3,21)
prim = dia_ordinal(3,21)  <= orden < dia_ordinal(6,21)
ver  = dia_ordinal(6,21)  <= orden < dia_ordinal(9,21)
oto  = dia_ordinal(9,21)  <= orden < dia_ordinal(12,21)

if hemi == "N":
    if inv:  estacion = "Invierno"
    elif prim: estacion = "Primavera"
    elif ver: estacion = "Verano"
    else: estacion = "Otoño"
elif hemi == "S": 
    if inv:  estacion = "Verano"
    elif prim: estacion = "Otoño"
    elif ver: estacion = "Invierno"
    else: estacion = "Primavera"
else:
    estacion = "Hemisferio inválido"

print(f"Estación: {estacion}")
