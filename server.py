import socket

def handle_request(client_socket):
    try:
        request = client_socket.recv(1024).decode()
        print(f"Received request: {request}")

        request_lines = request.split('\r\n')
        if len(request_lines) > 0:
            request_line = request_lines[0]
            parts = request_line.split(' ')
            if len(parts) >= 2:
                method = parts[0]
                path = parts[1]

                if method == 'GET':
                    if path == '/':
                        serve_file(client_socket, 'index.html')
                    elif path == '/about':
                        serve_file(client_socket, 'about.html')
                    else:
                        send_not_found(client_socket)
                else:
                    send_bad_request(client_socket)
    except Exception as e:
        print(f"Error handling request: {e}")
    finally:
        client_socket.close()

def serve_file(client_socket, file_path):
    try:
        with open(file_path, 'r') as f:
            response_body = f.read()
        response_header = "HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\n"
        client_socket.sendall(response_header.encode('utf-8') + response_body.encode('utf-8'))
    except FileNotFoundError:
        send_not_found(client_socket)

def send_not_found(client_socket):
    not_found_response = "HTTP/1.1 404 Not Found\r\nContent-Length: 0\r\n\r\n"
    client_socket.sendall(not_found_response.encode('utf-8'))

def send_bad_request(client_socket):
    bad_request_response = "HTTP/1.1 400 Bad Request\r\nContent-Length: 0\r\n\r\n"
    client_socket.sendall(bad_request_response.encode('utf-8'))

def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ('', 8000)

    try:
        server_socket.bind(server_address)
        server_socket.listen(10)
        print("Server is listening on port 8000")

        while True:
            client_socket, client_address = server_socket.accept()
            handle_request(client_socket)
    except Exception as e:
        print(f"Server error: {e}")
    finally:
        server_socket.close()

if __name__ == "__main__":
    main()
