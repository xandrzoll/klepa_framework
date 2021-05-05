# Klepa
Учебный web-фреймворк

## Установка
Установка и обновление с помощью pip:

.. code-block:: text
    $ pip install klepa_framework

## Использование

.. code-block:: python

    from klepa_framework import Klepa
    from urls import routes, fronts


    app = Klepa(routes, fronts)


    if __name__ == '__main__':
        app.run()

.. code-block:: text

    Run on 127.0.0.1:8080
