import os

from route import Route

class Controller:
    def __init__(self):
        self.routes = None

    def set_routes(self, routes):
        self.routes = routes

    def add_route(self, path, rhandler):
        if self.routes is None:
            self.routes = Route(path, rhandler)
        else:
            Route.add_route(self.routes, path, rhandler)

    def handle_request(self, client_socket, request):
        request_lines = request.split('\r\n')
        if len(request_lines) > 0:
            request_line = request_lines[0]
            parts = request_line.split(' ')
            if len(parts) >= 2:
                method = parts[0]
                path = parts[1]

                if method == 'GET':
                    handler = self.find_route_handler(path)
                    if handler:
                        handler(client_socket)
                    else:
                        # Try to serve file from 'pages' directory
                        self.serve_file(client_socket, path)
                else:
                    self.send_bad_request(client_socket)

    def find_route_handler(self, path):
        return Route.find_route(self.routes, path)

    @staticmethod
    def send_not_found(client_socket):
        not_found_response = "HTTP/1.1 404 Not Found\r\nContent-Length: 0\r\n\r\n"
        client_socket.sendall(not_found_response.encode('utf-8'))

    @staticmethod
    def send_bad_request(client_socket):
        bad_request_response = "HTTP/1.1 400 Bad Request\r\nContent-Length: 0\r\n\r\n"
        client_socket.sendall(bad_request_response.encode('utf-8'))

    @staticmethod
    def serve_file(client_socket, path):
        try:
            # Check if the path is root or within pages
            if path == '/':
                file_path = 'index.html'
                base_dir = ''
            else:
                file_path = path.lstrip('/') + '.html'
                base_dir = 'pages'
            
            full_path = os.path.join(base_dir, file_path)

            with open(full_path, 'r') as page:
                response_body = page.read()
            response_header = "HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\n"
            client_socket.sendall(response_header.encode('utf-8') + response_body.encode('utf-8'))
        except FileNotFoundError:
            Controller.send_not_found(client_socket)

    @staticmethod
    def handle_root(client_socket):
        Controller.serve_file(client_socket, '/')

    @staticmethod
    def handle_about(client_socket):
        Controller.serve_file(client_socket, '/pages/about')
