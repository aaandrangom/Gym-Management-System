import mysql.connector


class Database:
    def __init__(self, host='localhost', user='tu_usuario', password='tu_contraseña', database='nombre_de_la_base_de_datos'):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.connection = None
        self.cursor = None

    def connect(self):
        try:
            self.connection = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database
            )
            self.cursor = self.connection.cursor()
            return True
        except mysql.connector.Error as e:
            return False

    def close_connection(self):
        if self.connection:
            self.connection.close()
