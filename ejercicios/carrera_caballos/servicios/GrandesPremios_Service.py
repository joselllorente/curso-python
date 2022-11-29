from ejercicios.carrera_caballos.servicios.Loggin_Service import log, setupLogging
from utils.general_utils import pide_datos
import ejercicios.carrera_caballos.dao.CaballoDAO as dao_caballos
import ejercicios.carrera_caballos.dao.ApostantesDAO as dao_apostante
from ejercicios.carrera_caballos.servicios.DB_Service import DBServices

setupLogging(log.DEBUG, "../logs/carrera.log")


def ejecutar_grandes_premios(lista_caballos, listado_grandespremios, listado_apostantes):
    log.debug(f"Iniciando los grandes premios")
    for gran_premio in listado_grandespremios:
        iniciar_carreras_granpremio(gran_premio, listado_apostantes,
                                    list(filter(lambda caballo: caballo.id_granpremio == gran_premio.id,
                                                lista_caballos)))

        log.info(f"Finalizado el GRAN PREMIO: {gran_premio.nombre}")

    for apostante in listado_apostantes:
        log.info(f"Apostante {apostante.nombre} se queda con un saldo de {apostante.saldo}")

    actualizar_estados_basededatos(lista_caballos, listado_apostantes)

    log.debug(f"Finalizados los grandes premios")

def actualizar_estados_basededatos(lista_caballos, listado_apostantes):

    try:
        connection = DBServices.get_connection()
        cursor = connection.cursor()

        # Actualizamos saldo de los apostantes
        dao_apostante.ApostanteDAO.update_many(listado_apostantes, cursor)
        # Actualizamos experiencia de los caballos
        dao_caballos.CaballoDAO.update_many(lista_caballos, cursor)

        connection.commit()
    except Exception as e:
        log.error(f"Error al guardar los datos en la base de datos {e}")
    finally:
        cursor.close()
        DBServices.close_connection()




def iniciar_carreras_granpremio(gran_premio, listado_apostantes, lista_caballos_gp):
    log.debug(f"Iniciando el GRAN PREMIO: {gran_premio.nombre}")
    for carrera in range(gran_premio.num_carreras):
        log.debug(f"Iniciando la carrera: {carrera + 1} con {gran_premio.distancia} metros".center(50, "-"))
        # Iniciamos apuestas
        realizar_apuestas(carrera, listado_apostantes, lista_caballos_gp)

        # Caballos corren
        caballo_ganador = iniciar_carrera(gran_premio, lista_caballos_gp)

        # Actualizo estado (aumentar experiencia de los caballos, actualizar saldo de los apostantes)
        actualizar_estados(caballo_ganador, listado_apostantes, lista_caballos_gp)

        log.debug(f"Finalizada la carrera: {carrera + 1} ")


def actualizar_estados(caballo_ganador, listado_apostantes, lista_caballos_gp):
    # Actualizo experiencia caballos
    for caballo in lista_caballos_gp:
        if caballo_ganador.id == caballo.id:
            caballo.experiencia += 5
        else:
            caballo.experiencia += 1

    # Actualizo saldo de los apostantes
    for apostante in listado_apostantes:
        if not apostante.caballo_apostado== None and apostante.caballo_apostado.id == caballo_ganador.id:
            saldo_incrementado = apostante.saldo_apostado*caballo_ganador.valor_apuesta
            log.debug(f"Al apostante {apostante.nombre} se le incrementa el saldo en {saldo_incrementado}")
            apostante.saldo += saldo_incrementado



def iniciar_carrera(gran_premio, lista_caballos_gp):
    no_han_llegado_a_meta = True
    caballo_ganador = None

    # Reseteamos la distancia recorrida de los caballos a cero, para iniciar la nueva carrera
    resetea_distancia_caballos(lista_caballos_gp)

    while no_han_llegado_a_meta:
        for caballo in lista_caballos_gp:
            caballo.correr()
            log.debug(f"El caballo {caballo.nombre} lleva recorridos {caballo.dist_recorrida} metros")
            if caballo.dist_recorrida > gran_premio.distancia:
                caballo_ganador = caballo if caballo_ganador == None or caballo.dist_recorrida > caballo_ganador.dist_recorrida else caballo_ganador
                no_han_llegado_a_meta = False

    log.debug(
        f"El caballo ganador ha sido el caballo {caballo_ganador.nombre}")

    return caballo_ganador


def realizar_apuestas(carrera, listado_apostantes, lista_caballos_gp):
    #Reseteamos los caballos apostados de los apostantes
    resetear_apuestas_apostantes(listado_apostantes)

    for apostante in listado_apostantes:
        if apostante.saldo > 0:
            for caballo in lista_caballos_gp:
                print(caballo)

            apostante.saldo_apostado = solicitar_apuesta(apostante)
            apostante.saldo -= apostante.saldo_apostado
            apostante.caballo_apostado = pedir_caballo(lista_caballos_gp)

            log.debug(
                f"El apostante {apostante.nombre} ya ha realizado una apuesta de {apostante.saldo_apostado} "
                f"en la carrera {carrera + 1} sobre el caballo {apostante.caballo_apostado.id}")

        else:
            log.warning(f"El apostante {apostante.nombre} no tiene saldo para poder apostar")


def resetear_apuestas_apostantes(listado_apostantes):
    for apostante in listado_apostantes:
        apostante.caballo_apostado = None
        apostante.saldo_apostado = 0


def pedir_caballo(lista_caballos):
    """Método que devuelve el objeto caballo segun el id de caballo seleccionado por el apostante"""
    caballo_elegido = -1
    while caballo_elegido < 1:
        caballo_elegido = pide_datos("Elige un caballo por el que apostar (Selecciona un número):", "int")
        ids_caballos = list(map(lambda caballo: caballo.id, lista_caballos))
        log.debug(f"ids_caballos de la carrera: {ids_caballos}")
        caballo_elegido = caballo_elegido if caballo_elegido in ids_caballos else 0

    log.debug(f"Caballo seleccionado: {caballo_elegido}")
    return list(filter(lambda caballo: caballo.id == caballo_elegido, lista_caballos))[0]


def solicitar_apuesta(apostante):
    apuesta = -1
    while apuesta < 1:
        apuesta = pide_datos(f"{apostante.nombre} introduce el importe de la apuesta tienes {apostante.saldo} €", "int")
        apuesta = apuesta if apuesta <= apostante.saldo else 0
    log.debug(f"Apuesta de {apuesta} € del apostante {apostante.nombre}")
    return apuesta


def resetea_distancia_caballos(lista_caballos_gp):
    for caballo in lista_caballos_gp:
        caballo.dist_recorrida = 0
