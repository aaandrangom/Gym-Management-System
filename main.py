from ui.menu import Menu
from ui.menu import Consola
from services.validaciones import ValidadorDatos
from services.gestion_personas import GestionPersonas
from services.gestion_clientes import GestionClientes
from services.gestion_instructores import GestionInstructores
from services.gestion_clases import GestionClases
from services.gestion_inscripciones import GestionInscripciones


def obtener_personas_por_id(lista_personas, lista_clientes):
    id_clientes = set(cliente['id'] for cliente in lista_clientes)
    personas_filtradas = [
        persona for persona in lista_personas if persona['id'] in id_clientes]
    return personas_filtradas


def obtener_cliente_por_id(lista_clientes, id_cliente):
    for cliente in lista_clientes:
        if cliente['id'] == id_cliente:
            return cliente
    return None


while True:
    try:
        menu = Menu()
        consola = Consola()
        validaciones = ValidadorDatos()
        personas = GestionPersonas()
        clientes = GestionClientes()
        instructores = GestionInstructores()
        clases = GestionClases()
        inscripciones = GestionInscripciones()

        menu.menu()
        opcion_seleccionada = validaciones.obtener_solo_numeros(
            consola.obtener_input("Seleccione una opción"))

        if opcion_seleccionada == 1:
            menu.menu_personas()

            opcion_persona_seleccionada = validaciones.obtener_solo_numeros(
                consola.obtener_input("Seleccione una opción"))

            if opcion_persona_seleccionada == 1:
                info_persona = consola.pedir_datos_persona()
                personas.insert_person(info_persona)
                input("Presione ENTER para continuar.")
            elif opcion_persona_seleccionada == 2:
                lista_personas = personas.listar_personas()
                persona_seleccionada = menu.mostrar_menu_personas(
                    lista_personas)

                personas.eliminar_persona(persona_seleccionada['id'])
                input('Presione ENTER para continuar.')
            elif opcion_persona_seleccionada == 3:
                continue
            else:
                print("\033[91mOpción no válida. Inténtelo de nuevo.\033[0m")
                input('Presione ENTER para continuar.')
        elif opcion_seleccionada == 2:
            menu.menu_clientes()

            opcion_cliente_seleccionado = validaciones.obtener_solo_numeros(
                consola.obtener_input("Seleccione una opción"))

            if opcion_cliente_seleccionado == 1:
                lista_personas = personas.listar_personas()
                a = menu.mostrar_menu_personas(lista_personas)
                if a != None:
                    info_cliente = consola.pedir_datos_cliente(a['id'])
                    clientes.insert_cliente(info_cliente)
            elif opcion_cliente_seleccionado == 2:
                lista_clientes = clientes.listar_id_cliente()
                lista_personas = personas.listar_personas()

                personas_clientes = obtener_personas_por_id(
                    lista_personas, lista_clientes)
                persona_seleccionada = menu.mostrar_menu_personas(
                    personas_clientes)

                id_cliente = obtener_cliente_por_id(
                    lista_clientes, persona_seleccionada['id'])
                menu.mostrar_info_cliente(id_cliente)

                info_nuevo_cliente = consola.pedir_nueva_informacion_cliente()
                clientes.actualizar_informacion_cliente(
                    persona_seleccionada['id'], info_nuevo_cliente)
                input('Presione ENTER para continuar.')
            elif opcion_cliente_seleccionado == 3:
                lista_clientes = clientes.listar_id_cliente()
                lista_personas = personas.listar_personas()
                personas_clientes = obtener_personas_por_id(
                    lista_personas, lista_clientes)
                persona_seleccionada = menu.mostrar_menu_personas(
                    personas_clientes)

                id_cliente = obtener_cliente_por_id(
                    lista_clientes, persona_seleccionada['id'])
                clientes.eliminar_cliente(id_cliente['id'])
                input('Presione ENTER para continuar.')
            elif opcion_cliente_seleccionado == 4:
                continue
            else:
                print("\033[91mOpción no válida. Inténtelo de nuevo.\033[0m")
                input('Presione ENTER para continuar.')
        elif opcion_seleccionada == 3:
            menu.menu_instructores()

            opcion_instructor_seleccionado = validaciones.obtener_solo_numeros(
                consola.obtener_input("Seleccione una opción"))

            if opcion_instructor_seleccionado == 1:
                lista_personas = personas.listar_personas()
                id = menu.mostrar_menu_personas(lista_personas)
                info_instructor = consola.pedir_datos_instructor(id['id'])
                instructores.insert_instructor(info_instructor)
                input("Presione ENTER para continuar.")
            elif opcion_instructor_seleccionado == 2:
                lista_instructores = instructores.listar_instructores()
                lista_personas = personas.listar_personas()

                personas_clientes = obtener_personas_por_id(
                    lista_personas, lista_instructores)
                persona_seleccionada = menu.mostrar_menu_personas(
                    personas_clientes)

                id_instructor = obtener_cliente_por_id(
                    lista_instructores, persona_seleccionada['id'])
                menu.mostrar_info_instructor(id_instructor)

                info_nuevo_instructor = consola.pedir_datos_actualizacion_instructor()
                instructores.actualizar_informacion_instructor(
                    persona_seleccionada['id'], info_nuevo_instructor)
                input('Presione ENTER para continuar.')
            elif opcion_instructor_seleccionado == 3:
                lista_instructores = instructores.listar_instructores()
                lista_personas = personas.listar_personas()
                personas_clientes = obtener_personas_por_id(
                    lista_personas, lista_instructores)
                persona_seleccionada = menu.mostrar_menu_personas(
                    personas_clientes)

                id_instructor = obtener_cliente_por_id(
                    lista_instructores, persona_seleccionada['id'])
                instructores.eliminar_instructor(id_instructor['id'])
                input('Presione ENTER para continuar.')
            elif opcion_instructor_seleccionado == 4:
                continue
            else:
                print("\033[91mOpción no válida. Inténtelo de nuevo.\033[0m")
                input('Presione ENTER para continuar.')
        elif opcion_seleccionada == 4:
            menu.menu_clases()

            opcion_clase_seleccionado = validaciones.obtener_solo_numeros(
                consola.obtener_input("Seleccione una opción"))

            if opcion_clase_seleccionado == 1:
                lista_instructores = instructores.listar_instructores()

                if len(lista_instructores) != 0:
                    lista_personas = personas.listar_personas()

                    personas_clientes = obtener_personas_por_id(
                        lista_personas, lista_instructores)
                    persona_seleccionada = menu.mostrar_menu_personas(
                        personas_clientes)
                    menu.mostrar_menu_personas

                    info_clase = consola.pedir_datos_clase(
                        persona_seleccionada['id'])
                    clases.insert_clase(info_clase)
                else:
                    print("\033[91mNo hay instructores registrados.\033[0m")
                    input('Presione ENTER para continuar.')
            elif opcion_clase_seleccionado == 2:
                menu.encabezado_personalizado('BUSCAR CLASE POR NOMBRE')
                nombre_clase = validaciones.obtener_solo_letras_con_espacios(
                    consola.obtener_input("Nombre de la clase"))

                clase_encontrada = clases.buscar_clases_por_nombre(
                    nombre_clase)
                if len(clase_encontrada) == 0:
                    print("\033[91mClase no encontrada.\033[0m")
                    input('Presione ENTER para continuar.')
                else:
                    menu.mostrar_info_clases(clase_encontrada)
                    input('Presione ENTER para continuar.')
            elif opcion_clase_seleccionado == 3:
                menu.encabezado_personalizado('BUSCAR CLASE POR INSTRUCTOR')
                lista_instructores = instructores.listar_instructores()
                lista_personas = personas.listar_personas()

                personas_clientes = obtener_personas_por_id(
                    lista_personas, lista_instructores)
                persona_seleccionada = menu.mostrar_menu_personas(
                    personas_clientes)

                instructor_id = persona_seleccionada['id']

                clase_encontrada = clases.buscar_clases_por_instructor(
                    instructor_id)

                if len(clase_encontrada) == 0:
                    print("\033[91mClase no encontrada.\033[0m")
                    input('Presione ENTER para continuar.')
                else:
                    menu.mostrar_info_clases(clase_encontrada)
                    input('Presione ENTER para continuar.')
            elif opcion_clase_seleccionado == 4:
                menu.encabezado_personalizado(
                    'ACTUALIZAR INFORMACIÓN DE LA CLASE')
                lista_clases = clases.listar_clases()
                menu.mostrar_info_clases(lista_clases)

                lista_instructores = instructores.listar_instructores()
                lista_personas = personas.listar_personas()

                personas_clientes = obtener_personas_por_id(
                    lista_personas, lista_instructores)

                a = menu.mostrar_menu_personas_instructores(
                    personas_clientes)

                if a != None:
                    print("Ingrese los nuevos datos de la clase:")
                    id = ValidadorDatos.obtener_solo_numeros(
                        Consola.obtener_input("ID Clase: "))
                    nueva_clase = consola.pedir_datos_actualizacion_clase()
                    clases.actualizar_informacion_clase(
                        id, nueva_clase)
                input('Presione ENTER para continuar.')
            elif opcion_clase_seleccionado == 5:
                menu.encabezado_personalizado(
                    'ELIMINAR UNA CLASE')
                lista_clases = clases.listar_clases()
                a = menu.mostrar_info_clases(lista_clases)

                if a != None:
                    id = ValidadorDatos.obtener_solo_numeros(
                        Consola.obtener_input("ID Clase: "))
                    clases.eliminar_clase(id)

                input('Presione ENTER para continuar.')
            elif opcion_clase_seleccionado == 6:
                continue
            else:
                print("\033[91mOpción no válida. Inténtelo de nuevo.\033[0m")
                input('Presione ENTER para continuar.')
        elif opcion_seleccionada == 5:
            menu.menu_inscripciones()
            opcion_inscripcion_seleccionado = validaciones.obtener_solo_numeros(
                consola.obtener_input("Seleccione una opción"))

            if opcion_inscripcion_seleccionado == 1:
                lista_clientes = clientes.listar_id_cliente()
                lista_personas = personas.listar_personas()

                personas_clientes = obtener_personas_por_id(
                    lista_personas, lista_clientes)
                persona_seleccionada = menu.mostrar_menu_personas(
                    personas_clientes)

                if persona_seleccionada != None:
                    lista_clases = clases.listar_clases()
                    menu.mostrar_info_clases(lista_clases)
                    id = ValidadorDatos.obtener_solo_numeros(
                        Consola.obtener_input("ID Clase: "))

                    inscripciones.inscribir_cliente(
                        persona_seleccionada['id'], id)
                    input('Presione ENTER para continuar.')
            elif opcion_inscripcion_seleccionado == 2:
                lista_inscripciones = inscripciones.obtener_inscripciones()
                menu.mostrar_info_inscripciones(lista_inscripciones)

                id_cliente = ValidadorDatos.obtener_solo_numeros(
                    Consola.obtener_input("ID Cliente"))
                id_clase = ValidadorDatos.obtener_solo_numeros(
                    Consola.obtener_input("ID Clase"))
                inscripciones.desinscribir_cliente(id_cliente, id_clase)

                input("Presionar ENTER para continuar")
            elif opcion_inscripcion_seleccionado == 3:
                continue
            else:
                print("\033[91mOpción no válida. Inténtelo de nuevo.\033[0m")
                input('Presione ENTER para continuar.')
        elif opcion_seleccionada == 6:
            break
        else:
            print("\033[91mOpción no válida. Inténtelo de nuevo.\033[0m")
            input('Presione ENTER para continuar.')
    except KeyboardInterrupt:
        print("\nSaliendo del programa.")
        break
    except Exception as e:
        print(f"Error inesperado: {e}")
