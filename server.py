import socket
from controller import Controller
from typing import Self

class Server:

    def __init__(Self, routes):
        Self.controller = Controller()
        # Now initialise the routes
        Self.initialise_routes(routes)
    
    @staticmethod
    def set_routes(Self, routes):
        Self.controller.set_routes(routes)
    
    @staticmethod
    def handle_request(Self, client, request):
        Self.controller.handle_request(client, request)

    @staticmethod
    def initialise_routes(Self, routes):
        for route in routes:
            Self.controller.add_route(route.path, route.rhandler)
        return


def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    addr = ('', 8000)
    
    # Add the default routes
    routes = [
        Route('/', Controller.handle_root),
        Route('/about', Controller.handle_about)
        # Add more routes as you see fit.
    ]
    
    # Create the server.
    server = Server(routes)

    try:
        s.bind(addr)
        s.listen(10)
        print("Server is listening on port http://localhost:8000/")

        while True:
            client, _ = s.accept()
            request = client.recv(1024).decode()
            controller.handle_request(client, request)
            client.close()
    except Exception as e:
        print(f"Server error: {e}")
    finally:
        s.close()

if __name__ == "__main__":
    main()

