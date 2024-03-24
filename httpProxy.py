import socket  # Importing the socket module for network communication
from http.server import BaseHTTPRequestHandler, HTTPServer  # Importing specific classes from the http.server module
from urllib.parse import urlparse  # Importing the urlparse function from the urllib.parse module
import chardet  # Importing the chardet module for character encoding detection

def detect_encoding(text):
    # Encode the text to bytes
    encoded_text = text.encode()
    
    # Detect the encoding
    result = chardet.detect(encoded_text)
    
    # Return the encoding
    return result['encoding']

class ProxyHTTPRequestHandler(BaseHTTPRequestHandler):
    # Define a custom HTTP request handler for the proxy server
    def do_GET(self):
        self.handle_request()

    def do_POST(self):
        self.handle_request()

    def handle_request(self):
        # Parse the URL from the client's request
        url = urlparse(self.path)
        destination_host = self.headers['Host']  # Extract the destination host from the request headers
        destination_port = 80  # Assuming default HTTP port
        
        # Establish connection to the destination host
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as destination_socket:
            destination_socket.connect((destination_host, destination_port))
            
            # Print the encoded request as bytes (without decoding)
            encoded_request = self.encode_request()  # Encode the request before forwarding
            print(f"\nClient Request: \n{encoded_request}")
            
            # Forward the request to the destination
            destination_socket.sendall(encoded_request)
            
            # Receive response from the destination (raw bytes)
            response = destination_socket.recv(4096)
            print(f"\nServer Response: \n{response}")
            
            # Send the response back to the client
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.wfile.write(response)

    def encode_request(self):
        # Encode the request from the client
        encoded_request = f"{self.command} {self.path} {self.request_version}\r\n"
        for header, value in self.headers.items():
            encoded_request += f"{header}: {value}\r\n"
        encoded_request += '\r\n'
        
        # Detect encoding of the request
        request_encoding = detect_encoding(encoded_request)
        
        return encoded_request.encode(request_encoding)  # Encode the request using the detected encoding

def proxy_server(listen_host, listen_port):
    # Create the proxy server
    server = HTTPServer((listen_host, listen_port), ProxyHTTPRequestHandler)
    print(f"[*] Listening on {listen_host}:{listen_port}")

    # Start serving requests
    server.serve_forever()

if __name__ == "__main__":
    # Define the proxy server settings
    LISTEN_HOST = '127.0.0.1'
    LISTEN_PORT = 8090

    # Start the proxy server
    proxy_server(LISTEN_HOST, LISTEN_PORT)
