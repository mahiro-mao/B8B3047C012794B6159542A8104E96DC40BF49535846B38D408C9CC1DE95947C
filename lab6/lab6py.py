import socket

HOST = 'localhost'
PORT = 5555 

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
    server_socket.bind((HOST, PORT))
    server_socket.listen(1)
    print(f"Server running on {HOST}:{PORT}\n\n")

    try:
        client_socket, client_address = server_socket.accept()
        with client_socket:
            print(f"Connected by {client_address}\n")

            # take request
            request = client_socket.recv(1024).decode("ASCII")
            print(f"Received request: {request}")

            # Fixa htmlen på sidan
            response_headers = "HTTP/1.1 200 OK\n" \
                               "Content-Type: text/html\n" \
                               "Cache-Control: whatever\n" \
                               "Connection: close\n" \
                               
            response_body = f"""
            <html>
            <body>
                <h1>Your browser sent the following request:</h1>
                <pre>{request}</pre>
            </body>
            </html>
            """

            # Send the response headers and body
            client_socket.sendall(bytearray("HTTP/1.1 200 OK\n", "ASCII"))
            #client_socket.sendall(bytearray(response_headers, "ASCII"))
            client_socket.sendall(bytearray("\n", "ASCII"))  # Blank line
            #client_socket.sendall(bytearray(response_body, "ASCII"))
            print("Sent response to client.\n")
    except Exception as err:
        print(f"Error has occured:  {err}")