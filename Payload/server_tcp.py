import socket

from pynvim import command

class Listener:
	def __init__(self, ip, port):
		listener = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		listener.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
		listener.bind((ip, port))
		listener.listen(0)

		print("[+] Esperando por conexiones")
		self.connection, address = listener.accept()
		print("[+] Tenemos una conexion de " + str(address))


	def ejecutar_remoto(self, command):
		self.connection.send(command)
		return self.connection.recv(1024)

	def run(self):
		while True:
			command = input(">>")
			result = self.ejecutar_remoto(command)
			print(result)

escuchar = Listener("192.168.0.207", 4444)
escuchar.run()