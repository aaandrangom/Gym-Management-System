from database.database import Database


class GestionClientes:
    def __init__(self):
        self.db = Database()

    def insert_cliente(self, cliente_data):
        connected = self.db.connect()
        if connected:
            try:
                sql = '''INSERT INTO Clientes 
                (id, membresia, fecha_inicio_membresia, fecha_fin_membresia) 
                VALUES (%s, %s, %s, %s)'''

                values = (cliente_data['id'],
                          cliente_data['membresia'],
                          cliente_data['fecha_inicio_membresia'],
                          cliente_data['fecha_fin_membresia'])

                self.db.cursor.execute(sql, values)
                self.db.connection.commit()

                print("\033[92mCliente agregado con éxito.\033[0m")
                input('Presione ENTER para continuar.')
            except Exception as e:
                print("\033[91mError al agregar cliente:", e, "\033[0m")
                input('Presione ENTER para continuar.')
            finally:
                self.db.close_connection()

    def actualizar_informacion_cliente(self, id_cliente, nueva_informacion):
        connected = self.db.connect()

        if connected:
            try:
                set_clause = ", ".join(
                    [f"{key} = %s" for key in nueva_informacion.keys()])
                sql = f"UPDATE Clientes SET {set_clause} WHERE id = %s"

                values = list(nueva_informacion.values()) + [id_cliente]

                self.db.cursor.execute(sql, values)
                self.db.connection.commit()

                print(
                    "\033[92mInformación del cliente actualizada con éxito.\033[0m")
            except Exception as e:
                print(
                    "\033[91mError al actualizar información del cliente:", e, "\033[0m")
            finally:
                self.db.close_connection()

    def eliminar_cliente(self, id_cliente):
        connected = self.db.connect()

        if connected:
            try:
                sql = "DELETE FROM Clientes WHERE id = %s"
                values = (id_cliente,)
                self.db.cursor.execute(sql, values)
                self.db.connection.commit()
                print("\033[92mCliente eliminado con éxito.\033[0m")
            except Exception as e:
                print("\033[91mError al eliminar cliente:", e, "\033[0m")
            finally:
                self.db.close_connection()

    def listar_id_cliente(self):
        connected = self.db.connect()

        if connected:
            try:
                sql = "SELECT * FROM clientes"
                self.db.cursor.execute(sql)
                personas = self.db.cursor.fetchall()

                if personas:
                    lista_personas = []
                    for persona in personas:
                        persona_info = {
                            'id': persona[0],
                            'membresia': persona[1],
                            'fecha_inicio_membresia': persona[2],
                            'fecha_fin_membresia': persona[3],
                        }
                        lista_personas.append(persona_info)

                    return lista_personas
                else:
                    return []
            except Exception as e:
                print(f"\033[91mError al listar clientes: {e}\033[0m")
                return []
            finally:
                self.db.close_connection()
        else:
            return []
