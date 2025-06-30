#1)
for i in range(101):          # range(101) genera 0..100
    print(i)

#2)
n = int(input("Ingrese un número entero: "))
digitos = len(str(abs(n)))
print(f"Cantidad de dígitos: {digitos}")

#3)
a = int(input("Valor 1: "))
b = int(input("Valor 2: "))
if a > b:
    a, b = b, a          # asegura a < b
suma = sum(range(a+1, b))
print(f"Suma entre {a} y {b} (excluidos) = {suma}")

#4)
total = 0
while True:
    n = int(input("Ingrese un número (0 para terminar): "))
    if n == 0:
        break
    total += n
print(f"Suma total: {total}")

#5)
import random
secreto = random.randint(0, 9)
intentos = 0

while True:
    intento = int(input("Adivina el número (0-9): "))
    intentos += 1
    if intento == secreto:
        print(f"¡Correcto! Lo lograste en {intentos} intento(s).")
        break
    print("No, intenta nuevamente...")

#6)
for i in range(100, -1, -2):   
    print(i)

#7)
n = int(input("Ingrese un entero positivo: "))
total = n * (n + 1) // 2       
print(f"Suma de 0 a {n}: {total}")

#8)
CANTIDAD = 5          # cambia aca para probar con menos
pares = impares = pos = neg = 0

for _ in range(CANTIDAD):
    n = int(input("Número: "))
    if n % 2 == 0:
        pares += 1
    else:
        impares += 1
    if n > 0:
        pos += 1
    elif n < 0:
        neg += 1

print(f"Pares: {pares}")
print(f"Impares: {impares}")
print(f"Positivos: {pos}")
print(f"Negativos: {neg}")

#9)
CANTIDAD = 5        # cambia aca para probar con menos
suma = 0
for _ in range(CANTIDAD):
    suma += int(input("Número: "))
media = suma / CANTIDAD
print(f"Media: {media}")

#10)
n = int(input("Ingrese un número: "))
invertido = 0
temp = abs(n)

while temp > 0:
    dig = temp % 10
    invertido = invertido * 10 + dig
    temp //= 10

if n < 0:              # conserva signo
    invertido = -invertido

print(f"Número invertido: {invertido}")

