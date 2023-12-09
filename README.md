# SISTEMA DE ADMINISTRACIÓN DE GIMNASIO EN PYTHON CON PROGRAMACIÓN ORIENTADA A OBJETOS

El Sistema de Gestión de Gimnasio es una aplicación de consola diseñada para facilitar la administración integral de un gimnasio.
Proporciona herramientas robustas para controlar a los clientes, monitorear a los instructores y gestionar las clases ofrecidas,
todo respaldado por una base de datos MySQL.

## Instrucciones de Instalación

1. Clonar este repositorio.
2. Instalar las dependencias con `pip install -r requirements.txt`.
3. Crear la base de datos en MySQL utilizando el script `database/schema.sql`.

Asegúrese de reemplazar `tu_usuario`, `tu_contraseña` y `nombre_de_la_base_de_datos` con sus credenciales de MySQL.

5. Abra el archivo `database/database.py`.

6. En `database.py`, busque la sección de configuración de conexión, y actualice las credenciales (`user`, `password`, `host`, `database`) con sus propios valores.

7. Guarde los cambios en `database.py`.

## Cómo Utilizar

```bash
python main.py
```
¡Listo! Ahora su sistema de gestión de gimnasio debería estar configurado con las nuevas credenciales para conectarse a la base de datos.

**Nota:** Asegúrese de tener MySQL instalado y configurado en su máquina antes de ejecutar el script `schema.sql`.
