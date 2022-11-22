#Decoradores
#Una funcion que recibe una funcion y devuelve una funcion
#Para extender la funcionalidad de una función
#Closure
def funcion_decorador_a (funcion_a_decorar_b):
    def funcion_decorador_c():
        print("Antes de la ejecución de la funcion")
        funcion_a_decorar_b()
        print("Después de la ejecución de la funcion")

    return funcion_decorador_c

def funcion_decorador_param (funcion_a_decorar):
    def funcion_decorador(*args):
        print("Antes de la ejecución de la funcion",type(args))
        resultado = funcion_a_decorar(*args)
        print("Después de la ejecución de la funcion",resultado)
        return resultado

    return funcion_decorador


@funcion_decorador_a
def imprimir ():
    print("Imprimiendo ....")


@funcion_decorador_a
def leer():
    print("Leyendo....")

@funcion_decorador_param
def sumar(num1, num2):
    return num1+num2

@funcion_decorador_param
def multiplicar(num1, num2, num3):
    return num1*num2*num3


imprimir()
leer()
resultado = sumar(7,3)
multiplicar(7,2,5)
print(f'Resultado suma: {resultado}')