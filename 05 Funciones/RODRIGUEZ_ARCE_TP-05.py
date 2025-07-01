#1

def imprimir_hola_mundo():
    print("Hola Mundo!")

imprimir_hola_mundo()

#2
def saludar_usuario(nombre):
    return f"Hola {nombre}!"

nombre_usuario = input("Ingresá tu nombre: ")
saludo = saludar_usuario(nombre_usuario)
print(saludo)

#3
def informacion_personal(nombre, apellido, edad, residencia):
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}.")

nombre = input("Nombre: ")
apellido = input("Apellido: ")
edad = input("Edad: ")
residencia = input("Lugar de residencia: ")

informacion_personal(nombre, apellido, edad, residencia)

#4
import math

def calcular_area_circulo(radio):
    return math.pi * radio ** 2

def calcular_perimetro_circulo(radio):
    return 2 * math.pi * radio

radio = float(input("Ingresá el radio del círculo: "))
area = calcular_area_circulo(radio)
perimetro = calcular_perimetro_circulo(radio)

print(f"Área: {area:.2f}")
print(f"Perímetro: {perimetro:.2f}")

#5
def segundos_a_horas(segundos):
    return segundos / 3600

segundos = int(input("Ingresá una cantidad de segundos: "))
horas = segundos_a_horas(segundos)
print(f"Equivalen a {horas:.2f} horas.")

#6
def tabla_multiplicar(numero):
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")

numero = int(input("Ingresá un número para ver su tabla de multiplicar: "))
tabla_multiplicar(numero)

#7
def operaciones_basicas(a, b):
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    division = a / b if b != 0 else "No se puede dividir por cero"
    return (suma, resta, multiplicacion, division)

a = float(input("Ingresá el primer número: "))
b = float(input("Ingresá el segundo número: "))

resultados = operaciones_basicas(a, b)

print(f"Suma: {resultados[0]}")
print(f"Resta: {resultados[1]}")
print(f"Multiplicación: {resultados[2]}")
print(f"División: {resultados[3]}")

#8
def calcular_imc(peso, altura):
    return peso / (altura ** 2)

peso = float(input("Ingresá tu peso en kg: "))
altura = float(input("Ingresá tu altura en metros: "))

imc = calcular_imc(peso, altura)
print(f"Tu IMC es: {imc:.2f}")

#9
def celsius_a_fahrenheit(celsius):
    return (celsius * 9/5) + 32

celsius = float(input("Ingresá la temperatura en grados Celsius: "))
fahrenheit = celsius_a_fahrenheit(celsius)

print(f"{celsius}°C equivalen a {fahrenheit:.2f}°F")

#10
def calcular_promedio(a, b, c):
    return (a + b + c) / 3

a = float(input("Primer número: "))
b = float(input("Segundo número: "))
c = float(input("Tercer número: "))

promedio = calcular_promedio(a, b, c)
print(f"El promedio es: {promedio:.2f}")

