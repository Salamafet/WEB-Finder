from PySide import QtGui, QtCore

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
        print("coucou")

    def reset(self):
        self.liste_ip.clear()
        self.scan_ip.clear()

app = QtGui.QApplication([])
fenetre = WEBFinder()
fenetre.show()
app.exec_()
