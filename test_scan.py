import socket, os
from threading import Thread
import time

reseau = "192.168.10."
current_ip = 0




while current_ip < 255:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.3)
    try:
        s.connect((reseau + str(current_ip), 80))
    except socket.error:
        pass
    else:
        print(reseau + str(current_ip) + " ouvert !")

    current_ip += 1
