# GUILLERMO-GRAVINO-TRABAJO-FINAL
Proyecto Final Coder House - Python
Comisión: #48405
Alumno: Guillermo Gravino

# Nombre del Proyecto
NuestroTubo. V.1.0

# Requerimientos
Para poder correr este proyecto es necesario tener instalado python 3.9 o superior. 

# Realizar las migraciones antes de ejecutar el servidor:

Desde la terminal correr los comandos:

```bash
python3 manage.py makemigratios
python3 manage.py migrate
```

## Para poder correr el servidor 

Desde la terminal correr el siguiente comando

```bash
python3 manage.py runserver
```

# Descripción del Proyecto

A través de la página web "NuestroTubo", los usuarios podrán cargar urls de videos subidos a diferentes plataformas de video, especificando a qué usuarios le será permitido acceder a esos videos.

De modo que el sitio web permite compartir videos entre los usuarios.

Para acceder al sistema es necesario iniciar sesión en la página (si ya se hizo una primera registración), o bien registrarse. Los datos requeridos en ambos casos son nombre de usuario y contraseña. Una vez que el usuario ingresa al sistema, en necesario que complete su perfil para lo cual será requerido su nombre completo (campo obligatorio) y una foto de perfil (no obligatoria).

El sistema utilizará el nombre completo del usuario para mostrar los videos que fueron compartidos con él.

Los usuarios pueden realizar las siguientes accciones:

- Publicar videos y compartirlos con los usuarios que elija, especificando sus nombres completos separados por comas. 
- Visualizar los videos publicados por el usuario y los videos que fueron compartidos con él.
- Enviar mensajes a otros usuarios.
- Ver / Eliminar los mensajes que le fueron enviados por otros usuarios.
- Crear / Editar el perfil de usuario
- Ver el detalle de los videos publicados y compartidos con él.
- Editar la información de los videos publicados (solo en el caso de que el video haya sido publicado por el mismo usuario)
- Registrarse - Loguearse - Cerrar Sesión.


# Tecnología Utilizada

Front-End
- HTML 5
- CSS 3
- Javascript ES6
- Bootstrap 5.2

Back-End
- Python 3.10.4
- Django 4.0
- Pruebas Realizadas

Repositorio de GitHub:
https://github.com/willygravino/GUILLERMO-GRAVINO-TRABAJO-FINAL

Video Demostración
https://youtu.be/KjeexzxG0AI



