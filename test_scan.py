import socket
from threading import Thread

reseau = "192.168.10."
digit_to_scan = 0
current_ip_scanned = 0

def scan(adresse):
    global current_ip_scanned
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(5)
    try:
        s.connect((adresse, 80))
    except socket.error:
        pass
    else:
        print(adresse + " ouvert !")

while digit_to_scan < 255:
    current_ip = reseau + str(digit_to_scan)
    t = Thread(target=scan, args=(current_ip,))
    t.start()
    digit_to_scan += 1

t.join()
print("Finish !")
