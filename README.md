# 📡 Proyecto de Redes: Cliente-Servidor y Peer-to-Peer (P2P)

Este proyecto implementa dos modelos fundamentales de comunicación en redes utilizando Python:

- 🖥️ Cliente-Servidor
- 🌐 Peer-to-Peer (P2P)

Ambos permiten la transferencia de archivos y simulan notificaciones.

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

En una terminal:
python server.py

En otra terminal:
python client.py

---

## 🌐 Peer-to-Peer (P2P)

### 📌 Descripción
No existe un servidor central. Los usuarios se conectan directamente entre sí.

### 🔄 Funcionamiento
1. Un usuario actúa como receptor
2. Otro usuario envía el archivo directamente
3. Se muestra una notificación al recibir archivos

### ▶️ Ejecución

Terminal 1:
python receiver.py

Terminal 2:
python sender.py

---

## ⚙️ Instalación

Clona el repositorio:
git clone https://github.com/TU_USUARIO/proyecto_redes.git
cd proyecto_redes

Crea entorno virtual:
python3 -m venv venv
source venv/bin/activate

Instala dependencias:
pip install -r requirements.txt

---

## 📁 Estructura del proyecto

proyecto_redes/
│
├── server.py
├── client.py
├── sender.py
├── receiver.py
├── requirements.txt
├── README.md
└── .gitignore

---

## 🔍 Diferencias clave

Cliente-Servidor:
- Tiene servidor central
- Mayor control
- Dependencia del servidor

P2P:
- No hay servidor central
- Comunicación directa
- Más distribuido

---

## 📸 Evidencia

Agregar capturas de:
- Servidor corriendo
- Cliente subiendo archivo
- Lista de archivos
- Envío P2P
- Recepción P2P

---

## 🎯 Conclusión

Este proyecto permitió comprender las diferencias entre los modelos Cliente-Servidor y Peer-to-Peer mediante una implementación práctica.

---


