from database.database import Database


class GestionInstructores:
    def __init__(self):
        self.db = Database()

    def insert_instructor(self, instructor_data):
        connected = self.db.connect()

        if connected:
            try:
                sql = '''INSERT INTO instructores
                  (id, especialidad, años_experiencia, horario_disponible)
                  VALUES (%s, %s, %s, %s)'''

                values = (
                    instructor_data['id'],
                    instructor_data['especialidad'],
                    instructor_data['años_experiencia'],
                    instructor_data['horario_disponible'])

                self.db.cursor.execute(sql, values)
                self.db.connection.commit()

                print("\033[92mInstructor agregado con éxito.\033[0m")
            except Exception as e:
                print("\033[91mError al agregar instructor:", e, "\033[0m")
                input()
            finally:
                self.db.close_connection()

    def actualizar_informacion_instructor(self, id_instructor, nueva_informacion):
        connected = self.db.connect()

        if connected:
            try:
                set_clause = ", ".join(
                    [f"{key} = %s" for key in nueva_informacion.keys()])
                sql = f"UPDATE Instructores SET {set_clause} WHERE id = %s"

                values = list(nueva_informacion.values()) + [id_instructor]

                self.db.cursor.execute(sql, values)
                self.db.connection.commit()

                print(
                    "\033[92mInformación del instructor actualizada con éxito.\033[0m")
            except Exception as e:
                print(
                    "\033[91mError al actualizar información del instructor:", e, "\033[0m")
            finally:
                self.db.close_connection()

    def eliminar_instructor(self, id_instructor):
        connected = self.db.connect()

        if connected:
            try:
                sql = "DELETE FROM Instructores WHERE id = %s"
                values = (id_instructor,)
                self.db.cursor.execute(sql, values)
                self.db.connection.commit()
                print("\033[92mInstructor eliminado con éxito.\033[0m")
            except Exception as e:
                print("\033[91mError al eliminar instructor:", e, "\033[0m")
            finally:
                self.db.close_connection()

    def listar_instructores(self):
        connected = self.db.connect()

        if connected:
            try:
                sql = "SELECT * FROM instructores"
                self.db.cursor.execute(sql)
                personas = self.db.cursor.fetchall()

                if personas:
                    lista_personas = []
                    for persona in personas:
                        persona_info = {
                            'id': persona[0],
                            'especialidad': persona[1],
                            'años_experiencia': persona[2],
                            'horario_disponible': persona[3],
                        }
                        lista_personas.append(persona_info)

                    return lista_personas
                else:
                    return []
            except Exception as e:
                print(f"\033[91mError al listar instructores: {e}\033[0m")
                return []
            finally:
                self.db.close_connection()
        else:
            return []
