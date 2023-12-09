from database.database import Database


class GestionClases:
    def __init__(self):
        self.db = Database()

    def insert_clase(self, clase_data):
        connected = self.db.connect()

        if connected:
            try:
                sql = '''INSERT INTO clases_gimnasio
                  (nombre, hora_inicio, hora_fin, instructor_id) 
                  VALUES (%s, %s, %s, %s)'''

                values = (clase_data['nombre'],
                          clase_data['hora_inicio'],
                          clase_data['hora_fin'],
                          clase_data['instructor_id'])

                self.db.cursor.execute(sql, values)
                self.db.connection.commit()

                print("\033[92mClase agregada con éxito.\033[0m")
                input('Presione ENTER para continuar.')
            except Exception as e:
                print("\033[91mError al agregar clase: ", e, "\033[0m")
                input('Presione ENTER para continuar.')
            finally:
                self.db.close_connection()

    def buscar_clases_por_nombre(self, nombre_clase):
        connected = self.db.connect()

        if connected:
            try:
                sql = '''
                    SELECT clases_gimnasio.*, CONCAT(personas.nombre, ' ', personas.apellido) as nombre_instructor
                    FROM clases_gimnasio
                    JOIN instructores ON clases_gimnasio.instructor_id = instructores.id
                    JOIN personas ON instructores.id = personas.id
                    WHERE clases_gimnasio.nombre = %s
                '''
                values = (nombre_clase,)
                self.db.cursor.execute(sql, values)
                clases_encontradas = self.db.cursor.fetchall()

                clases_en_diccionarios = []
                for clase in clases_encontradas:
                    clase_dict = {
                        'id': clase[0],
                        'nombre': clase[1],
                        'hora_inicio': str(clase[2])[:-3],
                        'hora_fin': str(clase[3])[:-3],
                        'instructor_id': clase[4],
                        'nombre_instructor': clase[5]
                    }
                    clases_en_diccionarios.append(clase_dict)

                return clases_en_diccionarios
            except Exception as e:
                print("\033[91mError al buscar clases por nombre:",
                      e, "\033[0m")
                return []
            finally:
                self.db.close_connection()

    def buscar_clases_por_instructor(self, instructor_id):
        connected = self.db.connect()

        if connected:
            try:
                sql = '''
                    SELECT clases_gimnasio.*, CONCAT(personas.nombre, ' ', personas.apellido) as nombre_instructor
                    FROM clases_gimnasio
                    JOIN instructores ON clases_gimnasio.instructor_id = instructores.id
                    JOIN personas ON instructores.id = personas.id
                    WHERE clases_gimnasio.instructor_id = %s
                '''

                values = (instructor_id,)
                self.db.cursor.execute(sql, values)

                clases_encontradas = self.db.cursor.fetchall()

                clases_en_diccionarios = []
                for clase in clases_encontradas:
                    clase_dict = {
                        'id': clase[0],
                        'nombre': clase[1],
                        'hora_inicio': str(clase[2])[:-3],
                        'hora_fin': str(clase[3])[:-3],
                        'instructor_id': clase[4],
                        'nombre_instructor': clase[5]
                    }
                    clases_en_diccionarios.append(clase_dict)

                return clases_en_diccionarios
            except Exception as e:
                print(
                    "\033[91mError al buscar clases por instructor: ", e, "\033[0m")
            finally:
                self.db.close_connection()

    def actualizar_informacion_clase(self, id_clase, nueva_informacion):
        connected = self.db.connect()

        if connected:
            try:
                set_clause = ", ".join(
                    [f"{key} = %s" for key in nueva_informacion.keys()])
                sql = f"UPDATE clases_gimnasio SET {set_clause} WHERE id = %s"

                values = list(nueva_informacion.values()) + [id_clase]

                self.db.cursor.execute(sql, values)
                self.db.connection.commit()

                print(
                    "\033[92mInformación de la clase actualizada con éxito.\033[0m")
            except Exception as e:
                print("\033[91mError al actualizar información de la clase: ",
                      e, "\033[0m")
            finally:
                self.db.close_connection()

    def eliminar_clase(self, id_clase):
        connected = self.db.connect()

        if connected:
            try:
                sql = "DELETE FROM clases_gimnasio WHERE id = %s"
                values = (id_clase,)
                self.db.cursor.execute(sql, values)
                self.db.connection.commit()
                print("\033[92mClase eliminada con éxito.\033[0m")
            except Exception as e:
                print("\033[91mError al eliminar clase:", e, "\033[0m")
            finally:
                self.db.close_connection()

    def listar_clases(self):
        connected = self.db.connect()

        if connected:
            try:
                sql = '''SELECT clases_gimnasio.*, CONCAT(personas.nombre, ' ', personas.apellido) as nombre_instructor
                    FROM clases_gimnasio
                    JOIN instructores ON clases_gimnasio.instructor_id = instructores.id
                    JOIN personas ON instructores.id = personas.id'''

                self.db.cursor.execute(sql)
                clases = self.db.cursor.fetchall()

                if clases:
                    lista_clases = []
                    for clase in clases:
                        clase_info = {
                            'id': clase[0],
                            'nombre': clase[1],
                            'hora_inicio': str(clase[2])[:-3],
                            'hora_fin': str(clase[3])[:-3],
                            'instructor_id': clase[4],
                            'nombre_instructor': clase[5]
                        }
                        lista_clases.append(clase_info)

                    return lista_clases
                else:
                    print("No hay clases registradas en la base de datos.")
                    return []
            except Exception as e:
                print(f"Error al listar clases: {e}")
            finally:
                self.db.close_connection()
        else:
            return []
