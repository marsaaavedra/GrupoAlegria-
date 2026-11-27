# Sistema de Inventario de Supermercado

## 1. Descripción del proyecto

El proyecto consiste en el desarrollo de un sistema web para la gestión de inventario de un supermercado. Permite administrar los productos registrados, consultar sus características y realizar operaciones relacionadas con su gestión.

El sistema facilita la búsqueda y organización de productos mediante diferentes criterios, como el nombre, la categoría y el rango de precios.

## 2. Objetivos

- Desarrollar una aplicación web para gestionar productos de un supermercado.
- Implementar operaciones de registro, consulta, modificación y eliminación de productos.
- Permitir la búsqueda de productos por nombre y categoría.
- Incorporar filtros por rango de precios.
- Almacenar la información de los productos utilizando MongoDB.

## 3. Tecnologías utilizadas

- **Python:** lenguaje de programación.
- **Flask:** framework para el desarrollo de la aplicación web.
- **MongoDB:** base de datos NoSQL.
- **PyMongo:** conexión entre Python y MongoDB.
- **HTML y Jinja2:** estructura y presentación de las páginas.
- **Bootstrap:** diseño de la interfaz.
- **Git y GitHub:** control de versiones y trabajo colaborativo.

## 4. Estructura del proyecto

```text
GrupoAlegria-/
│
├── app.py
├── database.py
├── seed_products.py
├── requirements.txt
├── README.md
│
├── models/
│   └── product.py
│
├── routes/
│   └── products.py
│
├── static/
│   ├── img/
│   └── uploads/
│
└── templates/
    ├── base.html
    └── index.html
```
## 5. Funcionalidades del sistema

El sistema contempla las siguientes funcionalidades:

- Registro de productos.
- Visualización del inventario.
- Consulta del detalle de productos.
- Edición de productos.
- Eliminación de productos.
- Carga de imágenes de productos.
- Búsqueda de productos por nombre.
- Filtrado de productos por categoría.
- Filtrado por precio mínimo y máximo.

**Funcionalidades desarrolladas en esta asignación:**
- Búsqueda de productos por nombre y categoría (A10).
- Filtrado de productos por rango de precios (A11).
- Script para registrar 15 productos de ejemplo en MongoDB (A12).
## 6. Instalación y ejecución

### Requisitos previos

- Python instalado.
- MongoDB Atlas o una instancia de MongoDB.
- Git instalado.

### Clonar el repositorio

```bash
git clone https://github.com/marsaaavedra/GrupoAlegria-.git
cd GrupoAlegria-
```

### Crear el entorno virtual

```bash
py -m venv .venv
```

### Instalar las dependencias

```bash
.venv\Scripts\python.exe -m pip install -r requirements.txt
```

### Configurar la base de datos

La aplicación utiliza MongoDB mediante PyMongo. La conexión se configura en el archivo `database.py`.

Se debe disponer de una conexión válida a MongoDB y configurar correctamente el acceso a la base de datos del proyecto.

### Ejecutar la aplicación

```bash
.venv\Scripts\python.exe app.py
```

La aplicación estará disponible en:

```text
http://127.0.0.1:4000
```

## 7. Datos de ejemplo

El proyecto incluye el archivo `seed_products.py`, destinado a registrar 15 productos de ejemplo en la colección `products` de MongoDB.

Para ejecutar la carga de datos:

```bash
.venv\Scripts\python.exe seed_products.py
```

Este procedimiento debe realizarse cuando la conexión con MongoDB esté configurada y disponible.

## 8. Búsqueda y filtros

El sistema permite:

- Buscar productos por coincidencias en su nombre.
- Seleccionar una categoría específica.
- Establecer un precio mínimo.
- Establecer un precio máximo.
- Combinar los diferentes criterios de búsqueda.
- Limpiar los filtros para volver a consultar el inventario completo.

## 9. Repositorio

GitHub: https://github.com/marsaaavedra/GrupoAlegria-

## 10. Demostración

Se incorporará el enlace al video demostrativo del sistema, con una duración máxima de 3 minutos.

