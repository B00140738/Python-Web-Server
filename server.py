import socket
from controller import Controller
from route import Route

class Server:
    def __init__(self, routes):
        self.controller = Controller()
        self.initialise_routes(routes)
    
    def set_routes(self, routes):
        self.controller.set_routes(routes)
    
    def handle_request(self, client, request):
        self.controller.handle_request(client, request)

    def initialise_routes(self, routes):
        for route in routes:
            self.controller.add_route(route.path, route.rhandler)

def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ('', 8000)
    
    # Add the default routes
    routes = [
        Route('/', Controller.handle_root),
        Route('/pages/about', Controller.handle_about)
        # Add more routes as needed
    ]
    
    # Create the server
    server = Server(routes)

    try:
        server_socket.bind(server_address)
        server_socket.listen(10)
        print("Server is listening on http://localhost:8000/")

        while True:
            client_socket, _ = server_socket.accept()
            request = client_socket.recv(1024).decode()
            server.handle_request(client_socket, request)
            client_socket.close()
    except Exception as e:
        print(f"Server error: {e}")
    finally:
        server_socket.close()

if __name__ == "__main__":
    main()
