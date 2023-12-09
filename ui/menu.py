
from ui.consola import Consola
from services.validaciones import ValidadorDatos
from ui.consola import Consola


class Menu:
    def __init__(self):
        self.cls = Consola()

    def encabezado(self):
        self.cls.limpiar_pantalla()
        print("")
        print("╔════════════════════════════════════╗")
        print("║       BIENVENIDO AL GIMNASIO       ║")
        print("║════════════════════════════════════║")
        print("║           M-TABOLIC PRO            ║")
        print("╚════════════════════════════════════╝")

    def menu(self):
        self.encabezado()
        print("╔════════════════════════════════════╗")
        print("║           MENÚ DE OPCIONES         ║")
        print("║════════════════════════════════════║")
        print("║ 1. Módulo de Personas              ║")
        print("║ 2. Módulo de Clientes              ║")
        print("║ 3. Módulo de Instructores          ║")
        print("║ 4. Módulo de Clases                ║")
        print("║ 5. Módulo de Inscripciones         ║")
        print("║ 6. Salir                           ║")
        print("╚════════════════════════════════════╝")

    def menu_personas(self):
        self.encabezado()
        print("╔════════════════════════════════════╗")
        print("║       OPCIONES DE PERSONAS         ║")
        print("║════════════════════════════════════║")
        print("║ 1. Ingresar                        ║")
        print("║ 2. Eliminar                        ║")
        print("║ 3. Salir                           ║")
        print("╚════════════════════════════════════╝")

    def mostrar_menu_personas(self, lista_personas):
        self.encabezado()
        print("╔═════════════════════════════════════╗")
        print("║           LISTA DE PERSONAS         ║")
        print("║═════════════════════════════════════║")

        if lista_personas:
            for persona in lista_personas:
                nombre_apellido = f"{persona['nombre']} {persona['apellido']}"
                print(f"║ {persona['id']}. {nombre_apellido.ljust(32)} ║")

            print("║ 0. Volver al menú principal         ║")
            print("╚═════════════════════════════════════╝")

            opcion_seleccionada = ValidadorDatos.obtener_solo_numeros(
                Consola.obtener_input("Seleccione una persona (0 para volver): "))

            if opcion_seleccionada == 0:
                return None
            else:
                persona_seleccionada = next(
                    (persona for persona in lista_personas if persona['id'] == opcion_seleccionada), None)
                if persona_seleccionada:
                    return persona_seleccionada
                else:
                    print(
                        "\033[91mOpción no válida. Inténtelo de nuevo.\033[0m")
                    input('Presione ENTER para continuar')
                    return self.mostrar_menu_personas(lista_personas)
        else:
            print("\033[91mNo hay personas registradas.\033[0m")
            input('Presione ENTER para continuar')
            return None

    def mostrar_menu_personas_instructores(self, lista_personas):
        print("╔═════════════════════════════════════╗")
        print("║         LISTA DE INSTRUCTORES       ║")
        print("║═════════════════════════════════════║")

        if lista_personas:
            for persona in lista_personas:
                nombre_apellido = f"{persona['nombre']} {persona['apellido']}"
                print(f"║ {persona['id']}. {nombre_apellido.ljust(32)} ║")

            print("╚═════════════════════════════════════╝")
            return lista_personas
        else:
            print("\033[91mNo hay personas registradas.\033[0m")
            return None

    def menu_clientes(self):
        self.encabezado()
        print("╔════════════════════════════════════╗")
        print("║       OPCIONES DE CLIENTES         ║")
        print("║════════════════════════════════════║")
        print("║ 1. Ingresar                        ║")
        print("║ 2. Actualizar                      ║")
        print("║ 3. Eliminar                        ║")
        print("║ 4. Salir                           ║")
        print("╚════════════════════════════════════╝")

    def mostrar_info_cliente(self, cliente):
        print("╔═════════════════════════════════════╗")
        print("║        INFORMACIÓN DEL CLIENTE      ║")
        print("║═════════════════════════════════════║")

        if cliente:
            print(f"║ ID: {cliente['id']}".ljust(38) + "║")
            print(f"║ Membresía: {cliente['membresia']}".ljust(38) + "║")
            print(
                f"║ Inicio Membresía: {cliente['fecha_inicio_membresia']}".ljust(38) + "║")
            print(
                f"║ Fin Membresía: {cliente['fecha_fin_membresia']}".ljust(38) + "║")
            print("╚═════════════════════════════════════╝")
        else:
            print("\033[91mNo se proporcionó información del cliente.\033[0m")
            return None

    def menu_instructores(self):
        self.encabezado()
        print("╔════════════════════════════════════╗")
        print("║      OPCIONES DE INSTRUCTORES      ║")
        print("║════════════════════════════════════║")
        print("║ 1. Ingresar                        ║")
        print("║ 2. Actualizar                      ║")
        print("║ 3. Eliminar                        ║")
        print("║ 4. Salir                           ║")
        print("╚════════════════════════════════════╝")

    def mostrar_info_instructor(self, instructor):
        self.encabezado()
        print("╔════════════════════════════════════════════╗")
        print("║           INFORMACIÓN DEL INSTRUCTOR       ║")
        print("║════════════════════════════════════════════║")

        if instructor:
            print(f"║ ID: {instructor['id']}".ljust(45) + "║")
            print(
                f"║ Especialidad: {instructor['especialidad']}".ljust(45) + "║")
            print(
                f"║ Años de Experiencia: {instructor['años_experiencia']}".ljust(45) + "║")
            print(
                f"║ Horario Disponible: {instructor['horario_disponible']}".ljust(45) + "║")
            print("╚════════════════════════════════════════════╝")
        else:
            print("\033[91mNo se encontró información del instructor.\033[0m")
            return None

    def menu_clases(self):
        self.encabezado()
        print("╔════════════════════════════════════╗")
        print("║          OPCIONES DE CLASES        ║")
        print("║════════════════════════════════════║")
        print("║ 1. Ingresar                        ║")
        print("║ 2. Buscar por nombre               ║")
        print("║ 3. Buscar por instructor           ║")
        print("║ 4. Actualizar                      ║")
        print("║ 5. Eliminar                        ║")
        print("║ 6. Salir                           ║")
        print("╚════════════════════════════════════╝")

    def encabezado_personalizado(self, titulo):
        self.encabezado()
        print("╔════════════════════════════════════╗")
        print(f"║{titulo.center(36)}║")
        print("╚════════════════════════════════════╝")

    def mostrar_info_clases(self, lista_clases):
        print("╔═════════════════════════════════════════════════════════╗")
        print("║                      LISTA DE CLASES                    ║")
        print("║═════════════════════════════════════════════════════════║")
        if lista_clases:
            for clase_info in lista_clases:
                print(f"║ ID: {clase_info['id']}".ljust(57), "║")
                print(f"║ Nombre: {clase_info['nombre']}".ljust(57), "║")
                print(
                    f"║ Hora de inicio: {clase_info['hora_inicio']}".ljust(57), "║")
                print(
                    f"║ Hora de fin: {clase_info['hora_fin']}".ljust(57), "║")
                print(
                    f"║ Instructor: {clase_info['nombre_instructor']}".ljust(57), "║")
                print("║".ljust(57), "║")
            print("╚═════════════════════════════════════════════════════════╝")
            return lista_clases
        else:
            print("\033[91mNo hay clases registradas.\033[0m")
            return None

    def menu_inscripciones(self):
        self.encabezado()
        print("╔════════════════════════════════════╗")
        print("║      OPCIONES DE INSTRUCTORES      ║")
        print("║════════════════════════════════════║")
        print("║ 1. Inscribir cliente               ║")
        print("║ 2. Desinscribir cliente            ║")
        print("║ 3. Salir                           ║")
        print("╚════════════════════════════════════╝")

    def mostrar_info_inscripciones(self, lista_inscripciones):
        print("╔═══════════════════════════════════════════════════════╗")
        print("║               LISTA DE INSCRIPCIONES                  ║")
        print("║═══════════════════════════════════════════════════════║")
        if lista_inscripciones:
            for inscripcion_info in lista_inscripciones:
                id_cliente = inscripcion_info['id_cliente']
                id_clase = inscripcion_info['id_clase']
                nombre_cliente = f"{inscripcion_info['nombre_cliente']} {inscripcion_info['apellido_cliente']}"
                nombre_clase = inscripcion_info['nombre_clase']
                fecha_inscripcion = inscripcion_info['fecha_inscripcion']

                print(
                    f"║ ID: {id_cliente} - Cliente: {nombre_cliente.ljust(36)} ║")
                print(f"║ ID: {id_clase} -  Clase: {nombre_clase.ljust(37)} ║")
                print(
                    f"║ Fecha de Inscripción: {str(fecha_inscripcion).ljust(31)} ║")
                print("║".ljust(55), "║")
            print("╚═══════════════════════════════════════════════════════╝")
            return lista_inscripciones
        else:
            print("\033[91mNo hay inscripciones registradas.\033[0m")
            return None
