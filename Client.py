import socket

# create a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# get local machine name
host = socket.gethostname()

port = 8080

# connection to hostname on the port.
client_socket.connect((host, port))

# send a message to the server
client_socket.send('Hello, server!'.encode())

# receive the response
data = client_socket.recv(1024).decode()

print('Received data:', data)

# close the connection
client_socket.close()