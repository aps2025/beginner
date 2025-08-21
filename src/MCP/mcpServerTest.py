import socket
import threading

class MCPServer:
    def __init__(self, host='localhost', port=5200, name='vnk1'):
        self.host = host
        self.port = port
        self.name = name
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind((self.host, self.port))
        self.server_socket.listen(5)
        print(f"MCP Server '{self.name}' started on {self.host}:{self.port}")

    def handle_client(self, client_socket, address):
        print(f"Connection from {address}")
        try:
            while True:
                data = client_socket.recv(1024)
                if not data:
                    break
                print(f"Received from {address}: {data.decode()}")
                response = f"Server '{self.name}' received: {data.decode()}"
                client_socket.sendall(response.encode())
        finally:
            client_socket.close()
            print(f"Connection closed: {address}")

    def start(self):
        try:
            while True:
                client_socket, address = self.server_socket.accept()
                client_thread = threading.Thread(target=self.handle_client, args=(client_socket, address))
                client_thread.start()
        except KeyboardInterrupt:
            print("Server shutting down.")
        finally:
            self.server_socket.close()

if __name__ == "__main__":
    server = MCPServer(name='vnk1')
    print("Starting MCP Server...")
    server.start()
    print("MCP Server stopped.")