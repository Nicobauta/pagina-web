# Sistema Web de Gestión y Consulta de Películas con AWS y Flask

Este proyecto implementa una **aplicación web desarrollada en Flask** que se conecta a una **base de datos MySQL alojada en AWS RDS**, permitiendo **consultar, almacenar y gestionar información de películas**, clientes y rentas, y mostrar los datos en una **interfaz web dinámica**.

El sistema simula una **plataforma de alquiler de películas**, utilizando como base de datos el esquema **Sakila**.

---

## Características principales

- Aplicación web desarrollada con **Flask**
- Conexión a **AWS RDS (MySQL)**
- Consulta dinámica de datos desde la base de datos
- Búsqueda de películas por:
  - Título
  - Actor
- Visualización de películas y detalles individuales
- Gestión de clientes
- Simulación de renta de películas
- Arquitectura backend + frontend basada en templates HTML
- API REST para comunicación entre frontend y backend

---

## Arquitectura del sistema

Usuario (Navegador)
↓
Templates HTML
↓
Flask (app.py)
↓
MySQL en AWS RDS


---

## Tecnologías utilizadas

- **Python 3**
- **Flask**
- **MySQL**
- **AWS RDS**
- **HTML / CSS / JavaScript**
- **mysql-connector-python**

---

## Estructura del proyecto

.
├── .cache/
├── .ssh/
│ └── authorized_keys
│
├── app/
│ ├── pycache/
│ ├── templates/
│ │ ├── index.html
│ │ ├── movies.html
│ │ ├── movie.html
│ │ ├── login.html
│ │ ├── register.html
│ │ ├── cart.html
│ │ ├── checkout.html
│ │ └── admin_*.html
│ │
│ ├── app.py
│ ├── app.py.save
│ ├── app.py.save.1
│ └── app.py.save.2
│
├── flask/
│
├── pycache/
│
├── .bash_history
├── .bash_logout
├── .bashrc
├── .gitconfig
├── .profile
└── .sudo_as_admin_successful


### Rutas principales

| Ruta | Método | Descripción |
|------|--------|-------------|
| `/` | GET | Página principal |
| `/movies.html` | GET | Listado de películas |
| `/movie/<id>` | GET | Detalle de una película |
| `/search` | GET | Búsqueda por título o actor |
| `/clientes` | GET | Obtiene clientes |
| `/peliculas` | GET | Lista películas con stock |
| `/rentar` | POST | Renta una película |

---


## Funcionalidades del backend (Flask)

### Búsqueda de películas

El sistema permite buscar películas por:

- **Título**
- **Actor (nombre o apellido)**

Los resultados se devuelven en formato **JSON**, lo que facilita su consumo desde JavaScript en el frontend.

---

### Renta de películas

- Verifica la disponibilidad de la película
- Actualiza el stock en la base de datos
- Retorna un mensaje de éxito o error al usuario


## Ejecución del proyecto

```bash
# 1. Acceder al directorio donde se encuentra la aplicación
cd app

# 2. (Opcional) Crear un entorno virtual
python -m venv venv

# 3. Activar el entorno virtual
# Linux / macOS
source venv/bin/activate

# Windows
venv\Scripts\activate

# 4. Instalar las dependencias necesarias
pip install flask mysql-connector-python

# 5. Ejecutar la aplicación Flask
python app.py

# 6. Acceder desde el navegador
# http://localhost:5000
