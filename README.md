# 📡 Proyecto de Redes: Cliente-Servidor y Peer-to-Peer (P2P)

Este proyecto implementa dos modelos fundamentales de comunicación en redes utilizando Python:

- 🖥️ **Cliente-Servidor**
- 🌐 **Peer-to-Peer (P2P)**

Ambos permiten la **transferencia de archivos** y simulan **notificaciones**.

---

## 🚀 Tecnologías utilizadas

- Python 3
- Flask
- Requests
- Sockets
- Git & GitHub

---

## 🖥️ Cliente-Servidor

### 📌 Descripción
En este modelo existe un servidor central que gestiona las solicitudes de los clientes.

### 🔄 Funcionamiento
1. El cliente sube un archivo al servidor
2. El servidor almacena el archivo
3. Los clientes pueden consultar los archivos disponibles
4. Se muestra una notificación al subir archivos

### ▶️ Ejecución

```bash
python server.py
