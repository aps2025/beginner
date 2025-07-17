import socket
import threading

class MCPServer:
    def __init__(self, host='localhost', port=9000):
        self.host = host
        self.port = port
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind((self.host, self.port))
        self.server.listen(5)
        print(f"MCP Server listening on {self.host}:{self.port}")

    def handle_client(self, client_socket, address):
        print(f"Connection from {address}")
        while True:
            try:
                data = client_socket.recv(1024)
                if not data:
                    break
                message = data.decode('utf-8').strip()
                print(f"Received: {message}")
                # Simple MCP echo response
                response = f"MCP-RESPONSE: {message}\n"
                client_socket.sendall(response.encode('utf-8'))
            except ConnectionResetError:
                break
        print(f"Connection closed: {address}")
        client_socket.close()

    def start(self):
        while True:
            client_sock, addr = self.server.accept()
            client_thread = threading.Thread(target=self.handle_client, args=(client_sock, addr))
            client_thread.daemon = True
            client_thread.start()

if __name__ == "__main__":
    server = MCPServer()
    server.start()