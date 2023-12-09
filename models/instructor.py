# instructor.py
from persona import Persona  # Asegúrate de importar la clase Persona


class Instructor(Persona):
    def __init__(self, id, nombre, apellido, email, fecha_nacimiento, especialidad, años_experiencia, horario_disponible):
        super().__init__(id, nombre, apellido, email, fecha_nacimiento)
        self.especialidad = especialidad
        self.años_experiencia = años_experiencia
        self.horario_disponible = horario_disponible
