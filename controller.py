from typing import Self 

class Controller:
    
    # Class constructor

    def __init__(Self):
        Self.routes = None
    
    def set_routes(Self, routes):
        Self.routes = routes

    # Function to add a new route to our overall list of routes.

    @staticmethod
    def add_route(Self, path, rhandler):
        if Self.routes is None:
            Self.routes = Route(path, rhandler)
        else:
            # Else, if there are routes add another one
            Route.add_route(Self.routes, path, rhandler)


    # method to handle all user requests.

    @staticmethod
    def handle_request(Self, client, request):
        req_query = request.split('\r\n')
        # Check request length.
        if len(req_query) > 0:
            # create new array of lines for processing.
            req_line = req_query[0]
            # Get individual parts
            parts = req_line.split(' ')
            if len(parts) >= 2:
                method = parts[0]
                # Get the path from the parts array
                # the format is parts[method, path]
                path = parts[1]

                # Now, let's check the method.
                if method == 'GET':
                    # Get/serve the file to the user.
                    rhandler = Self.find_route_handler(path)

                if rhandler:
                    rhandler(client)
                # Otherwise, inform the user that the page has not been found (404)
                else:
                    Self.send_not_found(client)
            else:
                Self.send_bad_request(client)


    @staticmethod
    def find_route_handler(Self, path):
        return Route.find_route(Self.routes, path)

    @staticmethod
    def send_not_found(Self, client):
        not_found_response = "HTTP/1.1 404 Not Found\r\nContent-Length: 0\r\n\r\n"
        client.sendall(not_found_response.encode('utf-8'))

    @staticmethod
    def send_bad_request(Self, client):
        bad_request_response = "HTTP/1.1 400 Bad Request\r\nContent-Length: 0\r\n\r\n"
        client.sendall(bad_request_response.encode('utf-8'))

    @staticmethod
    def serve_file(client, path):
        try:
            with open(file_path, 'r') as page:
                response_body = page.read()
            response_header = "HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\n"
            # Send all of the data off.
            client.sendall(response_header.encode('utf-8') + response_body)
        except FileNotFoundError:
            Self.send_not_found(client)

    # Now, we can add functions to handle each route.

    def handle_root(client):
        Controller.serve_file(client, "index.html")

    def handle_about(client):
        Controller.serve_file(client, "about.html")

