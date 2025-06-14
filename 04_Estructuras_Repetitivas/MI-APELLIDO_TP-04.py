# 1) Imprimir números del 0 al 100 en orden creciente
for i in range(101):
    print(i)

print("\n")

# 2) Contar la cantidad de dígitos de un número ingresado por el usuario
numero = int(input("Ingrese un número entero: "))
print(len(str(abs(numero))))

print("\n")

# 3) Sumar todos los enteros entre dos valores excluyéndolos
a = int(input("Ingrese el primer número: "))
b = int(input("Ingrese el segundo número: "))
menor = min(a, b) + 1
mayor = max(a, b)
suma = sum(range(menor, mayor))
print("La suma es:", suma)

print("\n")

# 4) Sumar números ingresados hasta que el usuario ingrese un 0
total = 0
while True:
    numero = int(input("Ingrese un número (0 para terminar): "))
    if numero == 0:
        break
    total += numero
print("Total acumulado:", total)

print("\n")

# 5) Juego de adivinar un número aleatorio entre 0 y 9
import random
secreto = random.randint(0, 9)
intentos = 0
while True:
    intento = int(input("Adivine el número (0 a 9): "))
    intentos += 1
    if intento == secreto:
        break
print("¡Adivinaste en", intentos, "intentos!")

print("\n")

# 6) Imprimir números pares del 100 al 0 en orden decreciente
for i in range(100, -1, -1):
    if i % 2 == 0:
        print(i)

print("\n")

# 7) Sumar los números entre 0 y un número positivo indicado por el usuario
n = int(input("Ingrese un número positivo: "))
suma = sum(range(n + 1))
print("La suma es:", suma)

print("\n")

# 8) Ingresar 100 números y contar pares, impares, negativos y positivos
pares = impares = negativos = positivos = 0
cantidad = 100
for _ in range(cantidad):
    num = int(input("Ingrese un número: "))
    if num % 2 == 0:
        pares += 1
    else:
        impares += 1
    if num < 0:
        negativos += 1
    elif num > 0:
        positivos += 1
print("Pares:", pares)
print("Impares:", impares)
print("Negativos:", negativos)
print("Positivos:", positivos)

print("\n")

# 9) Ingresar 100 números y calcular la media
suma = 0
cantidad = 100
for _ in range(cantidad):
    num = int(input("Ingrese un número: "))
    suma += num
media = suma / cantidad
print("Media:", media)

print("\n")

# 10) Invertir los dígitos de un número ingresado
numero = input("Ingrese un número: ")
invertido = numero[::-1]
print("Número invertido:", invertido)
