# AI-Enhanced Notes Management System

## Table of Contents

---

- [Versions](#versions)
- [Requirements](#requirements)
    - [Main Env Setup](#env-setup)
    - [Env Setup for Testing](#env-setup-for-testing)
- [Local Development Server](#local-development-server)
- [Copyright](#copyright)

## Versions

---
[Python](https://www.python.org): **3.13**

[FastAPI Framework](https://github.com/fastapi/fastapi): **0.115.11**

[PostgreSQL](https://www.postgresql.org/): **17.2**

## Requirements

---

You must have on your local computer installed Python and PostgreSQL. 

Next, all dependencies are in the **requirements.txt** file. First, you need to create a virtual environment:
```text
python -m venv venv
```

```text
venv\Scripts\activate
```

or if you are using a Linux:

```text
python3 -m venv venv
```

```text
source venv/bin/activate
```

Then, you need to install **requirements.txt**:

```text
pip install -r /path/to/requirements.txt
```

### Env Setup

---

To set up a project, you need a create "**.env**" 
file in main directory and fill it with the following data:
1. Create PostgreSQL database.
2. Set your database settings like this:

```text 
DB_NAME=<your-db-name>
DB_USER=<your-db-user>
DB_PASS=<your-db-password>
DB_HOST=<your-db-host>
DB_PORT=<your-db-port>
```
3. Get **GOOGLE_API_KEY** from https://aistudio.google.com/.
4. Set it in the same file.
5. Your .env file should look like this:

```text 
DB_NAME=<your-db-name>
DB_USER=<your-db-user>
DB_PASS=<your-db-password>
DB_HOST=<your-db-host>
DB_PORT=<your-db-port>
GOOGLE_API_KEY=<your-google-api-key>
```

### Env Setup for Testing

---

You should do:
1. All the previous steps.
2. Create an additional **.env** file, for example **.test.env**.

```text 
DB_NAME=<test-db-name>
DB_USER=<test-db-user>
DB_PASS=<test-db-password>
DB_HOST=<test-db-host>
DB_PORT=<test-db-port>
GOOGLE_API_KEY=<test-google-api-key>
```

3. Uncomment **pytest.ini** file.
4. In the **env_files** variable, specify the name of your file, for example:

```text 
[pytest]
env_files =
    .test.env
```

5. All Done!

## Local Development Server

---

After starting the application, access the site by navigating to:
> <http://localhost:8000>

Swagger is accesible via the following link: 
> <http://localhost:8000/docs>

## Copyright

---

### © Roman Popov, 2025.