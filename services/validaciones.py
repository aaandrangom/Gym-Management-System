from datetime import date
import re


class ValidadorDatos:

    @staticmethod
    def obtener_fecha_nacimiento_valida(fecha_str):
        while True:
            try:
                fecha = date.fromisoformat(fecha_str)
                if fecha <= date.today():
                    return fecha
                else:
                    print("\033[91mLa fecha no puede ser en el futuro.\033[0m")
            except ValueError:
                print("\033[91mFormato de fecha incorrecto.\033[0m")

            fecha_str = input("Intente de nuevo (formato YYYY-MM-DD): ")

    @staticmethod
    def obtener_fecha_valida(fecha_str):
        while True:
            try:
                fecha = date.fromisoformat(fecha_str)
                return fecha
            except ValueError:
                print("\033[91mFormato de fecha incorrecto.\033[0m")

            fecha_str = input("Intente de nuevo (formato YYYY-MM-DD): ")

    def obtener_fecha_fin_valida(fecha_str, fecha_inicio=None):
        while True:
            try:
                fecha = date.fromisoformat(fecha_str)
                if fecha < fecha_inicio:
                    print(
                        "\033[91mLa fecha no puede ser anterior a la fecha de inicio.\033[0m")
                else:
                    return fecha
            except ValueError:
                print("\033[91mFormato de fecha incorrecto.\033[0m")
            fecha_str = input("Intente de nuevo (formato YYYY-MM-DD): ")

    @staticmethod
    def obtener_entre_limites(limite_inferior, limite_superior):
        while True:
            valor = input(
                f"Ingrese un valor entre {limite_inferior} y {limite_superior}: ")
            try:
                valor_num = int(valor)
                if limite_inferior <= valor_num <= limite_superior:
                    return valor_num
                else:
                    print(
                        "\033[91mEl valor debe estar entre los límites especificados. Intente de nuevo.\033[0m")
            except ValueError:
                print("\033[91mValor no válido. Intente de nuevo.\033[0m")

    @staticmethod
    def obtener_solo_letras_con_espacios(cadena):
        while True:
            if not cadena:
                print(
                    "\033[91mLa cadena no puede estar vacía. Intente de nuevo.\033[0m")
                cadena = input("→ ")
            elif all(char.isalpha() or char.isspace() for char in cadena):
                return cadena
            else:
                print(
                    "\033[91mIngrese solo letras y espacios. Intente de nuevo.\033[0m")
                cadena = input("→ ")

    @staticmethod
    def obtener_solo_numeros(cadena):
        while True:
            if cadena.isdigit():
                return int(cadena)
            else:
                print("\033[91mIngrese solo números. Intente de nuevo.\033[0m")
                cadena = input("→ ")

    @staticmethod
    def obtener_alfanumerico(cadena):
        while True:
            # adena = input("Ingrese solo caracteres alfanuméricos: ")
            if cadena.isalnum():
                return cadena
            else:
                print(
                    "\033[91mIngrese solo caracteres alfanuméricos. Intente de nuevo.\033[0m")
                cadena = input("→ ")

    @staticmethod
    def obtener_email_valido(email):
        while True:
            # email = input(
            #   "Ingrese una dirección de correo electrónico válida: ")
            patron_email = re.compile(
                r'^[\w\.-]+@[a-zA-Z\d\.-]+\.[a-zA-Z]{2,}$')
            if re.match(patron_email, email):
                return email
            else:
                print(
                    "\033[91mFormato de correo electrónico incorrecto. Intente de nuevo.\033[0m")
                email = input("→ ")

    @staticmethod
    def obtener_formato_hora_valido(hora):
        while True:
            patron_hora = re.compile(r'^([01]\d|2[0-3]):[0-5]\d$')
            if re.match(patron_hora, hora):
                return hora
            else:
                print(
                    "\033[91mFormato de hora incorrecto. Intente de nuevo.\033[0m")
                hora = input("→ ")

    @staticmethod
    def obtener_formato_hora_fin_valido(hora_inicio, hora_fin):
        while True:
            patron_hora = re.compile(r'^([01]\d|2[0-3]):[0-5]\d$')
            if not re.match(patron_hora, hora_fin):
                print(
                    "\033[91mFormato de hora incorrecto. Intente de nuevo.\033[0m")
            elif hora_fin <= hora_inicio:
                print(
                    "\033[91mLa hora final debe ser posterior a la hora de inicio. Intente de nuevo.\033[0m")
            else:
                return hora_fin
            hora_fin = input("→ ")

    @staticmethod
    def es_formato_horario_valido(horario):
        while True:
            patron_horario = re.compile(
                r'^([01]\d|2[0-3]):[0-5]\d - ([01]\d|2[0-3]):[0-5]\d$')
            if re.match(patron_horario, horario):
                horas = horario.split(' - ')
                hora_inicio = horas[0]
                hora_fin = horas[1]
                if hora_inicio < hora_fin:
                    return horario
                else:
                    print(
                        "\033[91mLa hora de inicio debe ser menor que la hora de fin. Intente de nuevo.\033[0m")
            else:
                print(
                    "\033[91mFormato de horario incorrecto. Intente de nuevo.\033[0m")

            horario = input("→ ")
