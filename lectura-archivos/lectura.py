#Lectura de archivos

#Ruta absoluta del archivo para evitar errores de ruta
import os
ruta_archivo = os.path.join(os.path.dirname(__file__), "datos.txt")

#Abrir el archivo en modo lectura
with open(ruta_archivo, "r", encoding="utf-8") as archivo:
    contenido = archivo.read()

print("Contenido del archivo:", contenido)

#Dividir el contenido en líneas
palabras = contenido.split()

#Contar la cantidad de palabras
cantidad_palabras = len(palabras)

print("Número total de palabras:", cantidad_palabras)