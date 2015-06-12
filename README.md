OpenFonacide - Contralor de Fonacide
============

[![Build Status](https://travis-ci.org/nemesiscodex/openfonacide.svg?branch=master)](https://travis-ci.org/nemesiscodex/openfonacide) [![Code Climate](https://codeclimate.com/github/nemesiscodex/openfonacide/badges/gpa.svg)](https://codeclimate.com/github/nemesiscodex/openfonacide) [![LGPLv3](https://img.shields.io/badge/license-LGPLv3-blue.svg)](http://opensource.org/licenses/lgpl-3.0.html)  [![Join the chat at https://gitter.im/nemesiscodex/openfonacide](https://badges.gitter.im/Join%20Chat.svg)](https://gitter.im/nemesiscodex/openfonacide?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge) 

http://mecmapi-nemesiscodex.rhcloud.com/

En Desarrollo con el apoyo del Programa de Democracia y Gobernabilidad (USAID-CEAMSO)

#### Requerimientos

* Python 2.7+

#### Instalacion

1. Clonar el repositorio

    ```bash
    git clone https://github.com/nemesiscodex/openfonacide.git
    cd openfonacide
    ```

2. Crear un virtual environment

    ```bash
    sudo apt-get install python-virtualenv # <-- Instala virtualenv
    virtualenv -p /usr/bin/python2.7 venv # Crea el virtualenv
    source venv/bin/activate # Activa el virtualenv
     ```
3. Instala librerias necesarias para conectarse a la base de datos

    ```bash
    sudo apt-get install libpq-dev python-dev
    ```

4. Instala librerias de python con pip

    ```bash
    pip install -r requirements.txt
    ```

5. Instala y configura postgres

    ```bash
    sudo apt-get install postgresql postgresql-contrib # Instalamos postgres
    sudo -i -u postgres # Entramos como usuario postgres
    createuser -P --interactive fonacide # Creamos un usuario(rol). Obs: en password pon "12345" 
    createdb openfonacide -O fonacide # Creamos la base de datos openfonacide para el usuario fonacide
    exit # volvemos atras
    ```

6. Sincronizamos la base de datos e iniciamos el servidor

    ```bash
    python manage.py syncdb # Crea las tablas necesarias
    python manage.py runserver # Inicia el servidor en http://localhost:8000/
    ```

#### Screenshots

![screenshot00](https://github.com/nemesiscodex/openfonacide/raw/master/images/home.png)

![screenshot01](https://github.com/nemesiscodex/openfonacide/raw/master/images/home2.png)

![screenshot02](https://github.com/nemesiscodex/openfonacide/raw/master/images/map.png)
