# Industrial Plants API

API desarrollada con **FastAPI**, **SQLAlchemy** y **PostgreSQL** para gestionar plantas industriales y sus máquinas.

La API permite:

- Crear plantas industriales
- Listar plantas con conteo de máquinas (`machine_count`)
- Obtener una planta con sus máquinas
- Crear máquinas asociadas a una planta
- Actualizar el estado de una máquina

Todos los endpoints están protegidos mediante **API Key** enviada en el header.

---

# Tecnologías utilizadas

- Python
- FastAPI
- SQLAlchemy
- PostgreSQL
- Uvicorn
- Pydantic

---

# Estructura del proyecto


app/
├── api/
│ ├── plants.py
│ └── machines.py
│
├── core/
│ ├── config.py
│ └── security.py
│
├── db/
│ └── database.py
│
├── dependencies/
│ ├── auth.py
│ └── db.py
│
├── models/
│ ├── plant.py
│ └── machine.py
│
├── schemas/
│ ├── plant.py
│ └── machine.py
│
├── services/
│ ├── plant_service.py
│ └── machine_service.py
│
└── main.py


---

# Requisitos

Antes de ejecutar el proyecto necesitas:

- Python **3.10 o superior**
- PostgreSQL instalado y corriendo

---

# Crear entorno virtual

Desde la carpeta raíz del proyecto ejecutar:


python -m venv venv


Activar el entorno virtual:

### Windows (CMD)


venv\Scripts\activate


### Windows (PowerShell)


venv\Scripts\Activate.ps1


---

# Instalar dependencias

Con el entorno virtual activo ejecutar:


pip install fastapi uvicorn sqlalchemy psycopg python-dotenv pydantic-settings


Opcionalmente puedes generar el archivo de dependencias:


pip freeze > requirements.txt


---

# Configurar variables de entorno

Crear un archivo `.env` en la raíz del proyecto.

Ejemplo:


API_KEY=pruebatecnica

DB_HOST=localhost
DB_PORT=5432
DB_NAME=plants_db
DB_USER=postgres
DB_PASSWORD=tu_password


Asegúrate de que la base de datos **plants_db** exista en PostgreSQL.

---

# Ejecutar la aplicación

Con el entorno virtual activo ejecutar:


uvicorn app.main:app --reload


---

# Acceder a la documentación Swagger

Una vez que el servidor esté corriendo abre:


http://127.0.0.1:8000/docs


Aquí podrás probar todos los endpoints.

---

# Autenticación

Todos los endpoints requieren una **API Key** en el header:


x-api-key: mi_clave_super_segura


La clave debe coincidir con la definida en el archivo `.env`.

---

# Endpoints disponibles

## Crear planta


POST /plants


Body de ejemplo:


{
"name": "Planta Lima",
"location": "Lurín"
}


---

## Listar plantas


GET /plants


Incluye el campo:


machine_count


---

## Obtener planta por ID


GET /plants/{id}


Devuelve la planta junto con sus máquinas asociadas.

---

## Crear máquina


POST /machines


Body de ejemplo:


{
"name": "Compresora 1",
"type": "Compresora",
"status": "operational",
"plant_id": 1
}


Estados permitidos para `status`:

- operational
- maintenance
- offline

---

## Actualizar estado de máquina


PATCH /machines/{id}/status


Body de ejemplo:


{
"status": "maintenance"
}


---

# Pruebas recomendadas

1. Crear una planta
2. Listar plantas
3. Crear una máquina asociada
4. Verificar que `machine_count` se actualice
5. Actualizar el estado de una máquina
6. Obtener la planta por ID y confirmar que aparecen sus máquinas