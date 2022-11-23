archivo = open('prueba.txt', 'r', encoding='utf8')

#r-> read, lo abre para leer, da error so no existe
#a-> append, abre el archivo para añadir mas información, lo crea si no existe
#w-> write. abre archivo para escribir, crea el archivo si no existe
#x-> create, crea el archivo devuelve error si existe
#Se puede indicar si es de texto o binario
#t-> texto(por defecto)
#b-> binario (imagenes)

# print(archivo.read())#Lee todos los caracteres

# leer algunos caracteres
# print(archivo.read(5))
# print(archivo.read(3))

# leer lineas completas
print(archivo.readline())
print(archivo.readline())
