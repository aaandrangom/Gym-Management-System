from database.database import Database


class GestionInscripciones:
    def __init__(self):
        self.db = Database()

    def inscribir_cliente(self, id_cliente, id_clase):
        connected = self.db.connect()

        if connected:
            try:
                sql = '''INSERT INTO inscripciones
                  (id_cliente, id_clase, fecha_inscripcion) 
                  VALUES (%s, %s, NOW())'''

                values = (id_cliente, id_clase)

                self.db.cursor.execute(sql, values)
                self.db.connection.commit()

                print("\033[92mCliente inscrito en la clase con éxito.\033[0m")
            except Exception as e:
                print("\033[91mError al inscribir cliente en la clase: ",
                      e, "\033[0m")
            finally:
                self.db.close_connection()

    def desinscribir_cliente(self, id_cliente, id_clase):
        connected = self.db.connect()

        if connected:
            try:
                sql = "DELETE FROM Inscripciones WHERE id_cliente = %s AND id_clase = %s"
                values = (id_cliente, id_clase)

                self.db.cursor.execute(sql, values)
                self.db.connection.commit()

                print(
                    "\033[92mCliente desinscrito de la clase con éxito.\033[0m")
            except Exception as e:
                print("\033[91mError al desinscribir cliente de la clase: ",
                      e, "\033[0m")
            finally:
                self.db.close_connection()

    def obtener_inscripciones(self):
        connected = self.db.connect()

        if connected:
            try:
                sql = '''
                    SELECT
                        inscripciones.id_cliente,
                        personas.nombre AS nombre_cliente,
                        personas.apellido AS apellido_cliente,
                        inscripciones.id_clase,
                        clases_gimnasio.nombre AS nombre_clase,
                        inscripciones.fecha_inscripcion
                    FROM
                        inscripciones
                    JOIN
                        clientes ON inscripciones.id_cliente = clientes.id
                    JOIN
                        personas ON clientes.id = personas.id
                    JOIN
                        clases_gimnasio ON inscripciones.id_clase = clases_gimnasio.id
                '''

                self.db.cursor.execute(sql)
                inscripciones = self.db.cursor.fetchall()

                inscripciones_info = []
                for inscripcion in inscripciones:
                    inscripcion_info = {
                        'id_cliente': inscripcion[0],
                        'nombre_cliente': inscripcion[1],
                        'apellido_cliente': inscripcion[2],
                        'id_clase': inscripcion[3],
                        'nombre_clase': inscripcion[4],
                        'fecha_inscripcion': inscripcion[5]
                    }
                    inscripciones_info.append(inscripcion_info)

                return inscripciones_info
            except Exception as e:
                print("\033[91mError al obtener inscripciones:", e, "\033[0m")
            finally:
                self.db.close_connection()
