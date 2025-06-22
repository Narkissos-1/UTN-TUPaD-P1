# %% [markdown]
# 1) Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100
# (incluyendo ambos extremos), en orden creciente, mostrando un número por línea.

# %%

for i in range(0, 101):
    print(i, end=", ")


# %% [markdown]
# 2) Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de
# dígitos que contiene.

# %%
entero = int(input('Ingrese un número: '))
cantidad_digitos = len(str(entero))
print(f'Tiene {cantidad_digitos} dígitos')


# %% [markdown]
# 3) Escribe un programa que sume todos los números enteros comprendidos entre dos valores
# dados por el usuario, excluyendo esos dos valores.

# %%
# Paso 1: Pedimos los dos números al usuario
a = int(input("Ingrese el primer número: "))
b = int(input("Ingrese el segundo número: "))

# Paso 2: Aseguramos que 'a' sea el menor y 'b' el mayor (los ordenamos)
if a > b:
    a, b = b, a  # intercambiamos los valores

# Paso 3: Usamos un rango que empiece en a+1 y termine en b (excluye b automáticamente)
suma = 0
for i in range(a + 1, b):
    suma += i  # vamos sumando cada número

# Paso 4: Mostramos el resultado
print(f"La suma de los enteros entre {a} y {b} es: {suma}")



# %% [markdown]
# 4) Elabora un programa que permita al usuario ingresar números enteros y los sume en
# secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese
# un 0.

# %%
total = 0
while True:
    numero = int(input("Ingrese un número (0 para terminar): "))
    if numero == 0:
        break
    total += numero
print("Total acumulado:", total)

# %% [markdown]
# 5) Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el
# programa debe mostrar cuántos intentos fueron necesarios para acertar el número.

# %%
import random

secreto = random.randint(0, 9)
intentos = 0

while True:
    intento = int(input("Adivine el número (0 a 9): "))
    intentos += 1
    if intento == secreto:
        break
print("¡Adivinaste en", intentos, "intentos!")

# %% [markdown]
# 6) Desarrolla un programa que imprima en pantalla todos los números pares comprendidos
# entre 0 y 100, en orden decreciente.

# %%
for i in range(100, -1, -1):
    if i % 2 == 0:
        print(i)

# %% [markdown]
# 7) Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un
# número entero positivo indicado por el usuario.

# %%
n = int(input("Ingrese un número positivo: "))
suma = sum(range(n + 1))
print("La suma es:", suma)

# %% [markdown]
# 8) Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el
# programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son
# negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad
# menor, pero debe estar preparado para procesar 100 números con un solo cambio).

# %%
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

# %% [markdown]
# 9) Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la
# media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe
# poder procesar 100 números cambiando solo un valor).

# %%
suma = 0
cantidad = 100

for _ in range(cantidad):
    num = int(input("Ingrese un número: "))
    suma += num

media = suma / cantidad
print("Media:", media)

# %% [markdown]
# 10) Escribe un programa que invierta el orden de los dígitos de un número ingresado por el
# usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745.

# %%
numero = input("Ingrese un número: ")
invertido = numero[::-1]
print("Número invertido:", invertido)