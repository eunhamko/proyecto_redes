import socket

HOST = '0.0.0.0'
PORT = 5001

server = socket.socket()
server.bind((HOST, PORT))
server.listen(1)

print("Esperando conexión...")

conn, addr = server.accept()
print("Conectado con", addr)

file = open("recibido.txt", "wb")

while True:
    data = conn.recv(1024)
    if not data:
        break
    file.write(data)

file.close()
conn.close()

print("📁 Archivo recibido")
