import requests

SERVER_URL = "http://127.0.0.1:5000"

def subir_archivo():
    ruta = input("Ruta del archivo: ")
    with open(ruta, 'rb') as f:
        files = {'file': f}
        r = requests.post(f"{SERVER_URL}/upload", files=files)
        print(r.json()["message"])
        print("🔔 Notificación: Nuevo archivo subido")

def ver_archivos():
    r = requests.get(f"{SERVER_URL}/files")
    print("📁 Archivos disponibles:")
    for file in r.json():
        print("-", file)

while True:
    print("\n1. Subir archivo")
    print("2. Ver archivos")
    print("3. Salir")
    opcion = input("Opción: ")

    if opcion == "1":
        subir_archivo()
    elif opcion == "2":
        ver_archivos()
    elif opcion == "3":
        break
