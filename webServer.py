import socket

HOST = '127.0.0.1'  # localhost
PORT = 13331  # arbitrary non-privileged port

def handle_request(client_socket):
    request_data = client_socket.recv(1024)
    request_text = request_data.decode()
    print(request_text)

    response_headers = 'HTTP/1.1 200 OK\nContent-Type: text/html\n\n'
    with open('index.html', 'r') as f:
        response_body = f.read()
    response = response_headers + response_body
    response_data = response.encode()

    client_socket.sendall(response_data)
    client_socket.close()

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind((HOST, PORT))
    server_socket.listen(1)

    print(f'Serving on port {PORT}...')
    while True:
        client_socket, client_address = server_socket.accept()
        handle_request(client_socket)
