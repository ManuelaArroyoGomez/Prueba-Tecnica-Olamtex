#Manipulación de listas y diccionarios

#Creacion de una lista con números del 1 al 50
numeros = list(range(1, 51))
print("Lista inicial: ", numeros)

#Lista de los numeros pares
num_pares = []
for n in numeros:
    if n % 2 == 0:
        num_pares.append(n)

print("Numeros pares:", num_pares)

#Lista con el cuadrado de cada numero
cuadrados = []
for n in numeros:
    cuadrados.append(n ** 2)

print("Cuadrados:", cuadrados)

#Diccionario con el numero original y sus cuadrados
diccionario = {}
for n in numeros:
    diccionario[n] = n ** 2

print("Diccionario:", diccionario)