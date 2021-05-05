Klepa
=====

Учебный проект по курсу 'Архитектура и шаблоны проектирования на Python' для `Geekbrains`_

.. _Geekbrains: https://gb.ru/


Установка
----------

Установка с помощью ручной распаковки архива проекта


Пример использования
----------------

.. code-block:: python


    from klepa_framework import Klepa
    from urls import routes, fronts


    app = Klepa(routes, fronts)


    if __name__ == '__main__':
        app.run()


.. code-block:: text

    Run on 127.0.0.1:8080
