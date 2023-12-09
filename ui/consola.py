# ui/consola.py
import os
from services.validaciones import ValidadorDatos

validaciones = ValidadorDatos()


class Consola:
    @staticmethod
    def obtener_input(mensaje):
        print(f"{mensaje} → ", end="")
        return input()

    @staticmethod
    def limpiar_pantalla():
        os.system('cls')

    @staticmethod
    def pedir_datos_persona():
        print("Ingrese los datos de la persona:")
        nombre = validaciones.obtener_solo_letras_con_espacios(
            Consola.obtener_input("Nombres"))

        apellido = validaciones.obtener_solo_letras_con_espacios(
            Consola.obtener_input("Apellidos"))

        email = validaciones.obtener_email_valido(
            Consola.obtener_input("Email"))

        fecha_nacimiento = validaciones.obtener_fecha_nacimiento_valida(
            Consola.obtener_input("Fecha de Nacimiento (formato YYYY-MM-DD)"))

        datos_persona = {
            'nombre': nombre,
            'apellido': apellido,
            'email': email,
            'fecha_nacimiento': fecha_nacimiento
        }

        return datos_persona

    @staticmethod
    def pedir_datos_cliente(id):
        print("Ingrese los datos del cliente:")

        membresia = ValidadorDatos.obtener_alfanumerico(
            Consola.obtener_input("Tipo de membresía"))
        fecha_inicio_membresia = ValidadorDatos.obtener_fecha_valida(
            Consola.obtener_input("Fecha de inicio de membresía (formato YYYY-MM-DD)"))

        fecha_fin_membresia = ValidadorDatos.obtener_fecha_fin_valida(
            Consola.obtener_input(
                "Fecha de fin de membresía (formato YYYY-MM-DD)"),
            fecha_inicio=fecha_inicio_membresia
        )

        datos_cliente = {
            'id': id,
            'membresia': membresia,
            'fecha_inicio_membresia': fecha_inicio_membresia,
            'fecha_fin_membresia': fecha_fin_membresia
        }

        return datos_cliente

    @staticmethod
    def pedir_nueva_informacion_cliente():
        print("Ingrese la nueva información del cliente:")
        membresia = ValidadorDatos.obtener_alfanumerico(Consola.obtener_input(
            "Nuevo tipo de membresía)"))
        fecha_inicio_membresia = ValidadorDatos.obtener_fecha_valida(
            Consola.obtener_input("Nueva fecha de inicio de membresía (YYYY-MM-DD)"))
        fecha_fin_membresia = ValidadorDatos.obtener_fecha_fin_valida(
            Consola.obtener_input(
                "Nueva fecha de fin de membresía (YYYY-MM-DD)"),
            fecha_inicio=fecha_inicio_membresia
        )

        nueva_informacion_cliente = {}
        if membresia:
            nueva_informacion_cliente['membresia'] = membresia
        if fecha_inicio_membresia:
            nueva_informacion_cliente['fecha_inicio_membresia'] = fecha_inicio_membresia
        if fecha_fin_membresia:
            nueva_informacion_cliente['fecha_fin_membresia'] = fecha_fin_membresia

        return nueva_informacion_cliente

    @staticmethod
    def pedir_datos_instructor(id):
        print("Ingrese los datos del instructor:")

        id_persona = id
        especialidad = ValidadorDatos.obtener_solo_letras_con_espacios(
            Consola.obtener_input("Especialidad"))
        años_experiencia = ValidadorDatos.obtener_solo_numeros(
            Consola.obtener_input("Años de experiencia"))
        horario_disponible = ValidadorDatos.es_formato_horario_valido(
            Consola.obtener_input("Horario disponible  (hh:mm - hh:mm)"))

        datos_instructor = {
            'id': id_persona,
            'especialidad': especialidad,
            'años_experiencia': años_experiencia,
            'horario_disponible': horario_disponible
        }

        return datos_instructor

    @staticmethod
    def pedir_datos_actualizacion_instructor():
        print("Ingrese los nuevos datos del instructor:")
        especialidad = ValidadorDatos.obtener_solo_letras_con_espacios(
            Consola.obtener_input("Especialidad"))
        años_experiencia = ValidadorDatos.obtener_solo_numeros(
            Consola.obtener_input("Años de Experiencia: "))
        horario_disponible = ValidadorDatos.es_formato_horario_valido(
            Consola.obtener_input("Horario disponible  (hh:mm - hh:mm)"))

        nuevos_datos = {
            'especialidad': especialidad,
            'años_experiencia': años_experiencia,
            'horario_disponible': horario_disponible
        }

        return nuevos_datos

    @staticmethod
    def pedir_datos_clase(instructor_id):
        print("Ingrese los datos de la clase:")
        nombre = Consola.obtener_input("Nombre de la clase: ")

        hora_inicio = ValidadorDatos.obtener_formato_hora_valido(
            Consola.obtener_input("Hora de inicio (HH:MM): "))

        hora_fin = ValidadorDatos.obtener_formato_hora_fin_valido(hora_inicio,
                                                                  Consola.obtener_input("Hora de fin (HH:MM): "))

        datos_clase = {
            'nombre': nombre,
            'hora_inicio': hora_inicio,
            'hora_fin': hora_fin,
            'instructor_id': instructor_id
        }

        return datos_clase

    @staticmethod
    def pedir_datos_actualizacion_clase():
        nombre = ValidadorDatos.obtener_solo_letras_con_espacios(
            Consola.obtener_input("Nuevo nombre de la clase"))
        hora_inicio = ValidadorDatos.obtener_formato_hora_valido(
            Consola.obtener_input("Nueva hora de inicio (HH:MM): "))
        hora_fin = ValidadorDatos.obtener_formato_hora_fin_valido(hora_inicio,
                                                                  Consola.obtener_input("Nueva hora de fin (HH:MM): "))
        instructor_id = ValidadorDatos.obtener_solo_numeros(
            Consola.obtener_input("Nuevo ID Instructor: "))

        datos_clase = {
            'nombre': nombre,
            'hora_inicio': hora_inicio,
            'hora_fin': hora_fin,
            'instructor_id': instructor_id
        }

        return datos_clase
