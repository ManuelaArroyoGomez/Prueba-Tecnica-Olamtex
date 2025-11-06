#Manipulación de listas y diccionarios

#Creacion de una lista con números del 1 al 100
numeros = list(range(1, 101))
# print(numeros)

#Lista de los numeros pares
num_pares = []

for n in numeros:
    if n % 2 == 0:
        num_pares.append(n)
        
print("Numeros pares:", num_pares)