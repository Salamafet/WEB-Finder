# -*- coding: utf-8 -*-
from PySide import QtGui, QtCore
from threading import Thread
import socket

class WEBFinder(QtGui.QWidget):
    def __init__(self):
        super(WEBFinder, self).__init__()

        self.setWindowTitle("WEB Finder")

        self.Ui()

    def Ui(self):
        layout = QtGui.QGridLayout(self)

        self.scan_ip = QtGui.QLineEdit(self)
        self.scan_ip.setPlaceholderText("IP address")
        self.scan_ip.clearFocus()

        self.liste_ip = QtGui.QListWidget(self)
        self.liste_ip.addItem("IP N°1")
        self.liste_ip.addItem("IP N°2")

        self.btn_start = QtGui.QPushButton("START SCAN", self)
        self.btn_reset = QtGui.QPushButton("RESET", self)

        self.prg_etat = QtGui.QProgressBar()
        self.prg_etat.setRange(0, 255)
        self.prg_etat.setTextVisible(False)
        self.prg_etat.hide()


        layout.addWidget(self.scan_ip, 0,0,1,2)
        layout.addWidget(self.liste_ip, 1,0,1,2)
        layout.addWidget(self.btn_start, 2,0,1,1)
        layout.addWidget(self.btn_reset, 2,1,1,1)
        layout.addWidget(self.prg_etat, 2,0,1,2)

        # self.resize(500, 200)

        self.btn_start.clicked.connect(self.start)
        self.btn_reset.clicked.connect(self.reset)
        self.liste_ip.itemDoubleClicked.connect(self.start)

    def start(self):
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
                self.liste_ip.addItem(adresse)

        while digit_to_scan < 255:
            current_ip = reseau + str(digit_to_scan)
            t = Thread(target=scan, args=(current_ip,))
            t.start()
            digit_to_scan += 1

        t.join()
        print("Finish !")

    def reset(self):
        self.liste_ip.clear()
        self.scan_ip.clear()

def main():
    app = QtGui.QApplication([])
    fenetre = WEBFinder()
    fenetre.show()
    app.exec_()

if __name__ == "__main__":
    main()
