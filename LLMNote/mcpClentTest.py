import socket

class MCPClient:
    def __init__(self, host='localhost', port=5500):
        self.host = host
        self.port = port
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def connect(self):
        try:
            self.client_socket.connect((self.host, self.port))
            print(f"Connected to MCP Server at {self.host}:{self.port}")
        except ConnectionRefusedError:
            print("Connection failed. Is the server running?")
            return False
        return True

    def send_message(self, message):
        try:
            self.client_socket.sendall(message.encode())
            response = self.client_socket.recv(1024)
            print(f"Server response: {response.decode()}")
        except Exception as e:
            print(f"Error during communication: {e}")
        finally:
            self.client_socket.close()
            print("Disconnected from server.")

if __name__ == "__main__":
    client = MCPClient()
    inputValue = input("Enter a message to send to the MCP Server: ")
    if client.connect():
        client.send_message(f"Hello from MCP Client! {inputValue}")
    else:
        print(f"Failed to connect to the server. {inputValue}")
