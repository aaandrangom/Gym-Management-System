-- Tabla para personas (Cliente e Instructor heredan de Persona)
CREATE TABLE personas (
    id INT PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(255),
    apellido VARCHAR(255),
    email VARCHAR(255),
    fecha_nacimiento DATE
);

-- Tabla para clientes
CREATE TABLE clientes (
    id INT PRIMARY KEY,
    membresia VARCHAR(255),
    fecha_inicio_membresia DATE,
    fecha_fin_membresia DATE,
    FOREIGN KEY (id) REFERENCES personas(id)
);

-- Tabla para instructores
CREATE TABLE instructores (
    id INT PRIMARY KEY,
    especialidad VARCHAR(255),
    años_experiencia INT,
    horario_disponible VARCHAR(255),
    FOREIGN KEY (id) REFERENCES personas(id)
);

-- Tabla para clases de gimnasio
CREATE TABLE clases_gimnasio (
    id INT PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(255),
    hora_inicio TIME,
    hora_fin TIME,
    instructor_id INT,
    FOREIGN KEY (instructor_id) REFERENCES instructores(id)
);


-- Tabla para inscripciones
CREATE TABLE inscripciones (
    id_cliente INT,
    id_clase INT,
    fecha_inscripcion DATE,
    PRIMARY KEY (id_cliente, id_clase),
    FOREIGN KEY (id_cliente) REFERENCES clientes(id),
    FOREIGN KEY (id_clase) REFERENCES clases_gimnasio(id)
);