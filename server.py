import socket
from controller import Controller

def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ('', 8000)

    controller = Controller()
    controller.add_route('/', controller.handle_root)
    controller.add_route('/about', controller.handle_about)

    try:
        server_socket.bind(server_address)
        server_socket.listen(10)
        print("Server is listening on port 8000")

        while True:
            client_socket, _ = server_socket.accept()
            request = client_socket.recv(1024).decode()
            controller.handle_request(client_socket, request)
            client_socket.close()
    except Exception as e:
        print(f"Server error: {e}")
    finally:
        server_socket.close()

if __name__ == "__main__":
    main()

