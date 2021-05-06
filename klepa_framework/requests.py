class Request:
    def __init__(self, environ):
        path = environ.get('PATH_INFO')
        if not path.endswith('/'):
            path = f'{path}/'
        self.path = path
        self.method = environ['REQUEST_METHOD']

        if self.method == 'GET':
            self.request_params = self.parse_input_data(environ.get('QUERY_STRING'))
        if self.method == 'POST':
            self.data = self.post_request(environ.get('CONTENT_LENGTH'), environ.get('wsgi.input'))

    def parse_input_data(self, data):
        result = {}
        if data:
            params = data.split('&')
            for item in params:
                k, v = item.split('=')
                result[k] = v
        return result

    def post_request(self, content_length, data):
        content_length = int(content_length) if content_length else 0
        # считываем данные, если они есть
        data = data.read(content_length) if content_length > 0 else b''
        result = {}
        if data:
            # декодируем данные
            data_str = data.decode(encoding='utf-8')
            # собираем их в словарь
            result = self.parse_input_data(data_str)
        return result
