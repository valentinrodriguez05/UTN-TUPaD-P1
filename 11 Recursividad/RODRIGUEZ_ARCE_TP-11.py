#1

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

limite = int(input("Ingrese un número entero: "))

print(f"\nFactoriales del 1 al {limite}:\n")
for i in range(1, limite + 1):
    print(f"{i}! = {factorial(i)}")

#2

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

limite = int(input("¿Hasta qué posición mostrar la serie de Fibonacci? "))

print(f"\nSerie de Fibonacci hasta la posición {limite}:\n")
for i in range(limite + 1):
    print(f"F({i}) = {fibonacci(i)}")

#3

def potencia(base, exponente):
    if exponente == 0:
        return 1
    else:
        return base * potencia(base, exponente - 1)

base = int(input("Ingrese la base: "))
exponente = int(input("Ingrese el exponente: "))

resultado = potencia(base, exponente)
print(f"\n{base}^{exponente} = {resultado}")

#4

def convertir_a_binario(n):
    if n == 0:
        return ""
    else:
        return convertir_a_binario(n // 2) + str(n % 2)

numero = int(input("Ingrese un número entero positivo: "))

if numero == 0:
    print("Binario: 0")
else:
    binario = convertir_a_binario(numero)
    print(f"Binario de {numero}: {binario}")

#5

def es_palindromo(palabra):
    if len(palabra) <= 1:
        return True
    elif palabra[0] != palabra[-1]:
        return False
    else:
        return es_palindromo(palabra[1:-1])

texto = input("Ingrese una palabra (sin espacios ni tildes): ")

if es_palindromo(texto):
    print(f"'{texto}' es un palíndromo")
else:
    print(f"'{texto}' no es un palíndromo")

#6

def suma_digitos(n):
    if n < 10:
        return n
    else:
        return (n % 10) + suma_digitos(n // 10)

numero = int(input("Ingrese un número entero positivo: "))
resultado = suma_digitos(numero)
print(f"Suma de los dígitos de {numero} = {resultado}")

#7

def contar_bloques(n):
    if n == 1:
        return 1
    else:
        return n + contar_bloques(n - 1)

nivel_base = int(input("¿Cuántos bloques hay en el nivel más bajo? "))
total = contar_bloques(nivel_base)
print(f"Total de bloques necesarios: {total}")

#8

def contar_digito(numero, digito):
    if numero == 0:
        return 0
    else:
        ultimo = numero % 10
        if ultimo == digito:
            return 1 + contar_digito(numero // 10, digito)
        else:
            return contar_digito(numero // 10, digito)

# Programa principal
numero = int(input("Ingrese un número entero positivo: "))
digito = int(input("¿Qué dígito desea contar (0 a 9)? "))

cantidad = contar_digito(numero, digito)
print(f"El dígito {digito} aparece {cantidad} veces en {numero}.")

