from typing import Self 

class Controller:
    
    # Class constructor

    def __init__(Self):
        routes = {}

    # Function to add a new route to our overall list of routes.

    @staticmethod
    def add_route(Self, path, rhandler):
        Self.routes[path] = rhandler

    # method to handle all user requests.

    @staticmethod
    def handle_request(Self, client, request):
        req_query = request.split('\r\n')
        # Check request length.
        if len(req_query) > 0:
            # create new array of lines for processing.
            req_line = req_lines[0]
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
                    rhandler = Self.routes.get(path)

                if rhandler:
                    rhandler(client)
                # Otherwise, inform the user that the page has not been found (404)
                else:
                    Self.send_not_found(client)
            else:
                Self.send_bad_request(client)


    @staticmethod
    def send_not_found(Self, client):
        not_found_response = "HTTP/1.1 404 Not Found\r\nContent-Length: 0\r\n\r\n"
        client_socket.sendall(not_found_response.encode('utf-8'))

    @staticmethod
    def send_bad_request():
        pass
