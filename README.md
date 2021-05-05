# Klepa
Учебный web-фреймворк

## Установка
Установка и обновление с помощью pip:

.. code-block:: text
    $ pip install klepa_framework

## Использование
----------------

.. code-block:: python

    # save this as app.py
    from flask import Flask

    app = Flask(__name__)

    @app.route("/")
    def hello():
        return "Hello, World!"

.. code-block:: text

    $ flask run
      * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)

