import socket

socket_receiver = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket_sender = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

HOSTNAME1 = socket.gethostbyname('sid1')
socket_receiver.bind((HOSTNAME1, 8001))
socket_receiver.listen(2)
conn, add = socket_receiver.accept()
msg = conn.recv(64)

while len(msg) <= 0:
    conn, add = socket_receiver.accept()
    msg = conn.recv(64)

print(msg)

HOSTNAME2 = socket.gethostbyname('sid2')
socket_sender.connect((HOSTNAME2, 8002))
socket_sender.send(bytes('34SY', 'UTF-8'))