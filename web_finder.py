# -*- coding: utf-8 -*-
from PySide import QtGui, QtCore
from threading import Thread
#from functools import partial
import socket, re, webbrowser

class WEBFinder(QtGui.QWidget):

    def __init__(self):
        super(WEBFinder, self).__init__()

        self.setWindowTitle("WEB Finder")
        self.setWindowIcon(QtGui.QIcon("logo.ico"))
        self.setFocus()
        self.Ui()

    def Ui(self):
        layout = QtGui.QGridLayout(self)

        self.lbl_instruction = QtGui.QLabel("Sub network to scan:")

        self.scan_ip = QtGui.QLineEdit(self)
        self.scan_ip.setPlaceholderText("Example: 192.168.1.0")
        self.scan_ip.textChanged.connect(self.enableStart)

        self.liste_ip = QtGui.QListWidget(self)
        #self.liste_ip.itemDoubleClicked.connect(partial(self.browse, self.liste_ip.currentItem()))
        self.liste_ip.itemDoubleClicked.connect(self.browse)
        # self.liste_ip.addItem("10.0.0.200 (80)")
        # self.liste_ip.addItem("192.168.150.13 (443)")

        self.btn_start = QtGui.QPushButton("START SCAN", self)
        self.btn_start.setDisabled(True)
        self.btn_reset = QtGui.QPushButton("CLEAR", self)

        self.prg_etat = QtGui.QProgressBar()
        self.prg_etat.setRange(0, 255)
        self.prg_etat.setTextVisible(False)
        self.prg_etat.hide()

        layout.addWidget(self.lbl_instruction, 0,0,1,1)
        layout.addWidget(self.scan_ip, 0,1,1,1)
        layout.addWidget(self.liste_ip, 1,0,1,2)
        layout.addWidget(self.btn_start, 2,0,1,1)
        layout.addWidget(self.btn_reset, 2,1,1,1)
        layout.addWidget(self.prg_etat, 2,0,1,2)

        # self.resize(500, 200)

        self.btn_start.clicked.connect(self.start)
        self.btn_reset.clicked.connect(self.reset)

    def start(self):
        self.btn_start.setVisible(False)
        self.btn_reset.setVisible(False)
        self.prg_etat.setVisible(True)

        sub_network = self.scan_ip.text()
        if(not re.match(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$", sub_network)):
            msgbox = QtGui.QMessageBox()
            msgbox.setWindowTitle("WEB Finder")
            msgbox.setText("You must enter a sub network address")
            msgbox.setStandardButtons(QtGui.QMessageBox.Ok)
            msgbox.exec_()
        else:
            sub_network = sub_network.split(".")
            sub_network = sub_network[0] + "." + sub_network[1] + "." + sub_network[2] + "."
            digit_to_scan = 0
            global total_ip_found
            total_ip_found = 0

            def scan(adresse):
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.settimeout(5)
                try:
                    s.connect((adresse, 80))
                except socket.error:
                    pass
                else:
                    print(adresse + " open !")
                    self.liste_ip.addItem(adresse + " (80)")
                    global total_ip_found
                    total_ip_found += 1

            while digit_to_scan < 255:
                current_ip = sub_network + str(digit_to_scan)
                t = Thread(target=scan, args=(current_ip,))
                t.start()
                digit_to_scan += 1

            t.join()
            if(total_ip_found == 0):
                msgbox = QtGui.QMessageBox()
                msgbox.setWindowTitle("WEB Finder")
                msgbox.setText("Noting found on " + self.scan_ip.text() + " !")
                msgbox.setStandardButtons(QtGui.QMessageBox.Ok)
                msgbox.exec_()
            print("Finish !")
            self.btn_start.setVisible(True)
            self.btn_reset.setVisible(True)
            self.prg_etat.setVisible(False)


    def reset(self):
        self.liste_ip.clear()
        #self.scan_ip.clear()

    def enableStart(self):
        if(len(self.scan_ip.text()) > 0):
            self.btn_start.setDisabled(False)

    def browse(self):
        adresse = self.liste_ip.currentItem().text()
        adresse = adresse.split(" ")
        port = adresse[1]
        adresse = adresse[0]
        port = port.split("(")
        port = port[1]
        port = port.split(")")
        port = port[0]
        webbrowser.open('http://' + adresse + ":" + port)


def main():
    app = QtGui.QApplication([])
    fenetre = WEBFinder()
    fenetre.show()
    app.exec_()

if __name__ == "__main__":
    total_ip_found = 0 #Variable défini à cet endroit pour accès global
    main()
