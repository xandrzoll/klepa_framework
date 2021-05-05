from klepa_framework import Klepa
from urls import routes, fronts


app = Klepa(routes, fronts)


if __name__ == '__main__':
    app.run()
