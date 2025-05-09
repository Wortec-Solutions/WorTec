# 🚀 WebApp Boilerplate with React JS and Flask API – by Wortec

Construye aplicaciones web modernas usando **React.js** para el frontend y **Python/Flask** para tu backend API, con integración lista para bases de datos, migraciones, despliegue y más.

---

## 🧱 Stack de Tecnologías

### 🔹 Frontend
- **React.js** – Framework para interfaces interactivas.
- **Tailwind CSS** – Framework de utilidades CSS.
- **JavaScript (ES6+)** – Lenguaje para desarrollo frontend.

### 🔹 Backend
- **Python 3.8+**
- **Flask** – Microframework para APIs.
- **Pipenv** – Para la gestión de entornos virtuales y dependencias.
- **SQLAlchemy** – ORM para manejar bases de datos.
- **Alembic** – Migraciones para SQLAlchemy.
- **PostgreSQL** – Motor de base de datos recomendado.

------------------------------------------------

# **Pasos para Iniciar el Proyecto**

---

### **1. Instalar Dependencias**

- **Abre una terminal** en tu entorno de desarrollo (Codespaces o tu terminal local).
- **Instala las dependencias del backend** con `pipenv`:

    ```bash
    pipenv install
    ```

- **Instala las dependencias del frontend** con `npm`:

    ```bash
    npm install
    ```

---

### **2. Convertir Puertos a Públicos**

- **Abre la terminal** si aún no lo has hecho.
- **Convierte los puertos a públicos** para asegurar que las aplicaciones sean accesibles desde el exterior.  
  Los puertos públicos se muestran en la terminal bajo la sección "ports" o "puertos".

> ⚠️ Nota: Recuerda que los puertos se convierten a privados si se reinicia la ventana de Codespace. Debes realizar esta conversión cada vez que reinicies la ventana.

---

### **3. Copiar las Rutas en el Archivo `.env`**

- **Accede a las rutas de los puertos** que se muestran en la terminal.  
  Por lo general, encontrarás las rutas en la sección "ports" de la terminal.
- **Abre o crea el archivo `.env`** en la raíz de tu proyecto.
- **Configura las variables de entorno** en el archivo `.env` con las siguientes rutas:

    ```env
    BACKEND_URL=http://localhost:3001
    FRONTEND_URL=http://localhost:3000
    ```

> Ajusta los puertos según lo que se muestre en la terminal.

---

### **4. Iniciar las Aplicaciones**

- **Inicia el backend** utilizando `pipenv`:

    ```bash
    pipenv run start
    ```

- **Inicia el frontend** utilizando `npm`:

    ```bash
    npm run start
    ```

---

### ✅ **Resumen**

1. **Instalar Dependencias**:
    - `pipenv install` para el backend.
    - `npm install` para el frontend.
2. **Convertir Puertos a Públicos**:
    - Verificar y convertir los puertos en la terminal.
3. **Copiar Rutas en el Archivo `.env`**:
    - Configurar `BACKEND_URL` y `FRONTEND_URL` con los puertos correspondientes.
4. **Iniciar Aplicaciones**:
    - `pipenv run start` para el backend.
    - `npm run start` para el frontend.

---

¡Tu proyecto estará listo para usarse una vez sigas estos pasos! 🚀



### **Ejecutar Migraciones**

Antes de iniciar el backend por primera vez, debes asegurarte de que la base de datos esté configurada correctamente.

1. Establece la variable `DATABASE_URL` según tu base de datos:

| Motor      | DATABASE_URL                                        |
|------------|-----------------------------------------------------|
| SQLite     | sqlite:///./test.db                                 |
| MySQL      | mysql://username:password@localhost:3306/example    |
| PostgreSQL | postgres://username:password@localhost:5432/example |

> En Codespaces con PostgreSQL puedes conectarte con:  
> `psql -h localhost -U gitpod example`

2. Crea los archivos de migración (si hiciste cambios en `models.py`):

    ```bash
    pipenv run migrate
    ```

3. Aplica las migraciones:

    ```bash
    pipenv run upgrade
    ```

---

### **5. Reiniciar las Aplicaciones**

Cada vez que se modifican los modelos hay que reiniciar las aplicaciones, para parar cada una hay que colocarse en la terminal y presiona ctrl + C, luego:

- **Inicia el backend** utilizando `pipenv`:

    ```bash
    pipenv run start
    ```

- **Inicia el frontend** utilizando `npm`:

    ```bash
    npm run start
    ```

**Extra (Precaución). Resetear la Base de Datos**
En caso de errores graves o si deseas reiniciar el entorno de desarrollo desde cero, puedes ejecutar:

  ```bash
  pipenv run reset_db
  ```
  Este comando:

  1. Elimina todas las tablas actuales.

  2. Aplica nuevamente las migraciones.

  3. Deja la base de datos lista para uso.

  ⚠️ Advertencia: Esto eliminará todos los datos existentes. Úsalo con cuidado.

### ✅ Resumen Rápido de Comandos

| Tarea                           | Comando                                      |
|--------------------------------|----------------------------------------------|
| Instalar backend               | `pipenv install`                             |
| Instalar frontend              | `npm install`                                |
| Ejecutar migraciones           | `pipenv run migrate && pipenv run upgrade`   |
| Iniciar backend                | `pipenv run start`                           |
| Iniciar frontend               | `npm run start`                              |
| Insertar usuarios de prueba    | `flask insert-test-users 5`                  |
| Insertar datos personalizados  | `pipenv run insert-test-data`                |
| Resetear base de datos (**Precaución**) | `pipenv run reset_db`               |
------------------------------------------------
## ☁️ Despliegue Rápido

Este boilerplate está **100% listo para ser desplegado en [Render.com](https://render.com)** o **[Heroku](https://heroku.com)** en minutos.

📄 **Guía de despliegue:** Documentación oficial (puede ajustarse a documentación propia de Wortec más adelante) [official documentation about it](https://start.4geeksacademy.com/deploy)

---

## 🙌 Contribuidores

Este template fue adaptado y mantenido por el equipo de **Wortec**, una empresa dedicada al desarrollo de soluciones tecnológicas: redes, servidores, desarrollo de software, diseño web, y más.

🌐 Visítanos en: [https://wortec.tech](https://wortec.tech)

Inspirado originalmente en recursos educativos de **4Geeks Academy** y ajustado a las necesidades internas de Wortec.









# WebApp boilerplate with React JS and Flask API

Build web applications using React.js for the front end and python/flask for your backend API.

- Documentation can be found here: https://start.4geeksacademy.com/starters/react-flask
- Here is a video on [how to use this template](https://www.loom.com/share/f37c6838b3f1496c95111e515e83dd9b)
- Integrated with Pipenv for package managing.
- Fast deployment to heroku [in just a few steps here](https://start.4geeksacademy.com/backend/deploy-heroku-posgres).
- Use of .env file.
- SQLAlchemy integration for database abstraction.

### 1) Installation:

> If you use Github Codespaces (recommended) or Gitpod this template will already come with Python, Node and the Posgres Database installed. If you are working locally make sure to install Python 3.10, Node 

It is recomended to install the backend first, make sure you have Python 3.8, Pipenv and a database engine (Posgress recomended)

1. Install the python packages: `$ pipenv install`
2. Create a .env file based on the .env.example: `$ cp .env.example .env`
3. Install your database engine and create your database, depending on your database you have to create a DATABASE_URL variable with one of the possible values, make sure you replace the valudes with your database information:

| Engine    | DATABASE_URL                                        |
| --------- | --------------------------------------------------- |
| SQLite    | sqlite:////test.db                                  |
| MySQL     | mysql://username:password@localhost:port/example    |
| Postgress | postgres://username:password@localhost:5432/example |

4. Migrate the migrations: `$ pipenv run migrate` (skip if you have not made changes to the models on the `./src/api/models.py`)
5. Run the migrations: `$ pipenv run upgrade`
6. Run the application: `$ pipenv run start`

> Note: Codespaces users can connect to psql by typing: `psql -h localhost -U gitpod example`

### Undo a migration

You are also able to undo a migration by running

```sh
$ pipenv run downgrade
```

### Backend Populate Table Users

To insert test users in the database execute the following command:

```sh
$ flask insert-test-users 5
```

And you will see the following message:

```
  Creating test users
  test_user1@test.com created.
  test_user2@test.com created.
  test_user3@test.com created.
  test_user4@test.com created.
  test_user5@test.com created.
  Users created successfully!
```

### **Important note for the database and the data inside it**

Every Github codespace environment will have **its own database**, so if you're working with more people eveyone will have a different database and different records inside it. This data **will be lost**, so don't spend too much time manually creating records for testing, instead, you can automate adding records to your database by editing ```commands.py``` file inside ```/src/api``` folder. Edit line 32 function ```insert_test_data``` to insert the data according to your model (use the function ```insert_test_users``` above as an example). Then, all you need to do is run ```pipenv run insert-test-data```.

### Front-End Manual Installation:

-   Make sure you are using node version 14+ and that you have already successfully installed and runned the backend.

1. Install the packages: `$ npm install`
2. Start coding! start the webpack dev server `$ npm run start`

## Publish your website!

This boilerplate it's 100% read to deploy with Render.com and Heroku in a matter of minutes. Please read the [official documentation about it](https://start.4geeksacademy.com/deploy).

### Contributors

This template was built as part of the 4Geeks Academy [Coding Bootcamp](https://4geeksacademy.com/us/coding-bootcamp) by [Alejandro Sanchez](https://twitter.com/alesanchezr) and many other contributors. Find out more about our [Full Stack Developer Course](https://4geeksacademy.com/us/coding-bootcamps/part-time-full-stack-developer), and [Data Science Bootcamp](https://4geeksacademy.com/us/coding-bootcamps/datascience-machine-learning).

You can find other templates and resources like this at the [school github page](https://github.com/4geeksacademy/).
