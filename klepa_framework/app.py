from wsgiref.simple_server import make_server

from klepa_framework.requests import Request


def PageNotFound404():
    def __call__(self, request):
        return '404 WHAT', '404 PAGE Not Found'


class Klepa:
    def __init__(self, routes_obj, fronts_obj):
        self.routes_lst = routes_obj
        self.fronts_lst = fronts_obj

    def __call__(self, environ, start_response):
        return self.wsgi_app(environ, start_response)

    def wsgi_app(self, environ, start_response):
        rq = Request(environ)

        # отработка паттерна page controller
        view = self.routes_lst.get(rq.path)
        if not view:
            view = PageNotFound404()
        request = {}

        # отработка паттерна front controller
        for front in self.fronts_lst:
            front(request)
        # запуск контроллера с передачей объекта request
        code, body = view(request)
        start_response(code, [('Content-Type', 'text/html')])
        return [body.encode('utf-8')]

    def run(self, host=None, port=None):
        """Runs the app on a dev server

        :param host: hostname. Default is 127.0.0.1
        :param port: port of server. Default is 8080
        """
        _host = '127.0.0.1'
        _port = 8080
        host = host or _host
        port = port or _port
        try:
            with make_server(host, port, self) as httpd:
                print(f'Run on {host}:{port}\nPress Ctrl+C for stop')
                httpd.serve_forever()
        except KeyboardInterrupt:
            print('App stopped')
