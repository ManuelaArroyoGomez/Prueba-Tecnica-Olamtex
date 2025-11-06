#Lectura de archivos

#Abrir el archivo en modo lectura
archivo = open("datos.txt", "r")
contenido = archivo.read()
archivo.close()

print("Contenido del archivo:", contenido)

#Dividir el contenido en líneas
palabras = contenido.split()

#Contar la cantidad de palabras
cantidad_palabras = len(palabras)

print("Número total de palabras:", cantidad_palabras)