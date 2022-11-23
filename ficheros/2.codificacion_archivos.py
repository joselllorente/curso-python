try:
    archivo = open('prueba.txt', 'w', encoding='utf8')
    archivo.write('Agregamos información al archivo\n')
    archivo.write('Adios')
except Exception as e:
    print(e)
finally:
    archivo.close()
    print('Fin del archivo')
    #Si se hace da error I/O Exception porque el fichero está cerrado
    # archivo.write('nueva info')