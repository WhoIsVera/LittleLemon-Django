# Proyecto de Restaurante LittleLemon

Este proyecto implementa una aplicación web para la administración de reservas y menú de un restaurante usando Django y Django REST Framework. El backend se conecta a una base de datos MySQL, y se incluye autenticación de usuario, registro y pruebas unitarias.

## Tabla de Contenidos
- [Descripción del Proyecto](#descripción-del-proyecto)
- [Rutas de la API](#rutas-de-la-api)
- [Instalación y Configuración](#instalación-y-configuración)
- [Ejecución de Pruebas](#ejecución-de-pruebas)
- [Evaluación](#evaluación)

## Descripción del Proyecto
La aplicación de restaurante **LittleLemon** permite a los usuarios:
- Visualizar y gestionar el menú.
- Realizar y administrar reservas de mesas.
- Registrarse e iniciar sesión con autenticación basada en token.

La aplicación está diseñada en Django para servir contenido HTML estático y permite probar la API con herramientas como Insomnia.

## Rutas de la API
Las siguientes rutas están disponibles en la API:

### Menú
- **GET /restaurant/menu/**: Lista de ítems del menú.
- **POST /restaurant/menu/**: Agregar un nuevo ítem al menú.
- **GET /restaurant/menu/<int:pk>/**: Detalles de un ítem específico.
- **PUT /restaurant/menu/<int:pk>/**: Actualizar un ítem específico.
- **DELETE /restaurant/menu/<int:pk>/**: Eliminar un ítem específico.

### Reservas
- **GET /restaurant/tables/**: Lista de reservas.
- **POST /restaurant/tables/**: Agregar una nueva reserva.
- **GET /restaurant/tables/<int:pk>/**: Detalles de una reserva específica.
- **PUT /restaurant/tables/<int:pk>/**: Actualizar una reserva específica.
- **DELETE /restaurant/tables/<int:pk>/**: Eliminar una reserva específica.

### Autenticación y Registro
- **POST /auth/token/login/**: Iniciar sesión y obtener un token de autenticación.
- **POST /auth/token/logout/**: Cerrar sesión.
- **POST /auth/users/**: Registrar un nuevo usuario.

## Instalación y Configuración
1. **Clona el repositorio**:
     ```bash
    git clone https://github.com/WhoIsVera/littlelemon.git
    cd littlelemon

2. **Crear y activar un entorno virtual**:
Es recomendable usar un entorno virtual para instalar las dependencias del proyecto.

    Para **Linux/Mac**:
   ```bash
    python3 -m venv env
    source env/bin/activate

3. **Configurar la base de datos MySQL**:
Crea una base de datos MySQL para el proyecto.
Configura las credenciales de la base de datos en el archivo settings.py, en la sección de DATABASES. Asegúrate de que las credenciales coincidan con las de tu instalación de MySQL.
      ```bash
      DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'nombre_de_tu_bd',
            'USER': 'tu_usuario',
            'PASSWORD': 'tu_contraseña',
            'HOST': 'localhost',
            'PORT': '3306',
        }
      }
  4. **Ejecutar migraciones**:
    Ejecuta las migraciones de Django para crear las tablas en la base de datos.
      ```bash
      python manage.py migrate

  5. **Crear un superusuario (opcional)**:
     Si deseas acceder al panel de administración de Django, crea un superusuario.
       ```bash
       python manage.py createsuperuser
6. **Iniciar el servidor de desarrollo**:
    Inicia el servidor para probar el proyecto.
      ```bash
      python manage.py runserver

     

