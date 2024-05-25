import socket
from controller import Controller

def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    addr = ('', 8000)

    controller = Controller()
    controller.add_route('/', controller.handle_root)
    controller.add_route('/about', controller.handle_about)

    try:
        s.bind(addr)
        s.listen(10)
        print("Server is listening on port 8000")

        while True:
            client, _ = server_socket.accept()
            request = client.recv(1024).decode()
            controller.handle_request(client, request)
            client.close()
    except Exception as e:
        print(f"Server error: {e}")
    finally:
        s.close()

if __name__ == "__main__":
    main()

