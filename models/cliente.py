from persona import Persona


class Cliente(Persona):
    def __init__(self, id, nombre, apellido, email, fecha_nacimiento, membresia, fecha_inicio_membresia, fecha_fin_membresia):
        super().__init__(id, nombre, apellido, email, fecha_nacimiento)
        self.membresia = membresia
        self.fecha_inicio_membresia = fecha_inicio_membresia
        self.fecha_fin_membresia = fecha_fin_membresia
