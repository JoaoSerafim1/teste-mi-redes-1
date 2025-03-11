import socket

socket_receiver = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket_sender = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

HOSTNAME1 = socket.gethostbyname('sid1')
socket_sender.connect((HOSTNAME1, 8001))
socket_sender.send(bytes('V01D', 'UTF-8'))

HOSTNAME2 = socket.gethostbyname('sid2')
socket_receiver.bind((HOSTNAME2, 8002))
socket_receiver.listen(2)
conn, add = socket_receiver.accept()
msg = conn.recv(64)

while len(msg) <= 0:
    conn, add = socket_receiver.accept()
    msg = conn.recv(64)

print(msg.decode('UTF-8'))