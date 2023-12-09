from database.database import Database


class GestionPersonas:
    def __init__(self):
        self.db = Database()

    def insert_person(self, person_data):
        connected = self.db.connect()
        if connected:
            try:
                sql = "INSERT INTO Personas (nombre, apellido, email, fecha_nacimiento) VALUES (%s, %s, %s, %s)"
                values = (person_data['nombre'], person_data['apellido'],
                          person_data['email'], person_data['fecha_nacimiento'])
                self.db.cursor.execute(sql, values)
                self.db.connection.commit()
                print("\033[92mPersona agregado con éxito.\033[0m")
            except Exception as e:
                print("\033[91mError al agregar persona:", e, "\033[0m")
            finally:
                self.db.close_connection()

    def eliminar_persona(self, id_persona):
        connected = self.db.connect()

        if connected:
            try:
                sql = "DELETE FROM Personas WHERE id = %s"
                values = (id_persona,)

                self.db.cursor.execute(sql, values)
                self.db.connection.commit()

                print("\033[92mPersona eliminada con éxito.\033[0m")
            except Exception as e:
                print("\033[91mError al eliminar persona:", e, "\033[0m")
            finally:
                self.db.close_connection()

    def listar_personas(self):
        connected = self.db.connect()

        if connected:
            try:
                sql = "SELECT * FROM personas"
                self.db.cursor.execute(sql)
                personas = self.db.cursor.fetchall()

                if personas:
                    lista_personas = []
                    for persona in personas:
                        persona_info = {
                            'id': persona[0],
                            'nombre': persona[1],
                            'apellido': persona[2],
                            'email': persona[3],
                            'fecha_nacimiento': persona[4]
                        }
                        lista_personas.append(persona_info)

                    return lista_personas
                else:
                    return []
            except Exception as e:
                print(f"\033[91mError al listar personas: {e}\033[0m")
                return []
            finally:
                self.db.close_connection()
        else:
            return []
