import socket
import platform

# create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# get local machine name
host = socket.gethostname()

port = 8080

# bind the socket to a public host, and a port
server_socket.bind((host, port))

# become a server socket
server_socket.listen(5)

print('Waiting for client connection...')

while True:
    # accept connections from outside
    (client_socket, client_address) = server_socket.accept()
    
    print('Got connection from', client_address)
    
    # receive the data
    data = client_socket.recv(1024).decode()
    
    # get OS information
    os_info = platform.system() + ' ' + platform.release()
    
    # send the OS information back to the client
    client_socket.send(os_info.encode())
    
    # close the connection
    client_socket.close()