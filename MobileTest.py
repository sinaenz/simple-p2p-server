import socket

while True:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        message = input('please enter the message : \n')
        sock.connect(('localhost', 8080))
        sock.sendall(bytes('GM,g3,m3,' + message, 'ascii'))
        print(sock.recv(1024))
        sock.close()

