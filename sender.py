import socket

HOST = input("IP del receptor: ")
PORT = 5001

client = socket.socket()
client.connect((HOST, PORT))

archivo = input("Ruta del archivo: ")

with open(archivo, "rb") as f:
    while True:
        data = f.read(1024)
        if not data:
            break
        client.send(data)

client.close()

print("📁 Archivo enviado")
