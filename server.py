import socket
import os

def main():
    # Initialize the socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Set up the server address
    server_address = ('', 8000)
    
    # Bind the socket to the address
    try:
        server_socket.bind(server_address)
    except socket.error as e:
        print(f"Bind failed: {e}")
        server_socket.close()
        return
    
    # Start listening for incoming connections
    try:
        server_socket.listen(10)
    except socket.error as e:
        print(f"Listen failed: {e}")
        server_socket.close()
        return
    
    # Inform the user that the server is running
    print("Server is listening on port 8000")
    
    # Accept an incoming connection
    try:
        client_socket, client_address = server_socket.accept()
    except socket.error as e:
        print(f"Accept failed: {e}")
        server_socket.close()
        return

    # Receive data from the client
    try:
        request = client_socket.recv(256).decode()
    except socket.error as e:
        print(f"Receive failed: {e}")
        client_socket.close()
        server_socket.close()
        return
    
    print(f"Received request: {request}")
    
    # Handle the request
    if request.startswith("GET / "):
        try:
            with open("index.html", "r") as f:
                response_body = f.read()
            
            response_header = "HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\n"
            client_socket.sendall(response_header.encode() + response_body.encode())
        except FileNotFoundError:
            print("Failed to open index.html")
            not_found_response = "HTTP/1.1 404 Not Found\r\nContent-Length: 0\r\n\r\n"
            client_socket.sendall(not_found_response.encode())
    else:
        bad_request_response = "HTTP/1.1 400 Bad Request\r\nContent-Length: 0\r\n\r\n"
        client_socket.sendall(bad_request_response.encode())
    
    # Cleanup
    client_socket.close()
    server_socket.close()
    
    # Return 0 to indicate success
    return 0

if __name__ == "__main__":
    main()

