from PyQt4.QtCore import *
from PyQt4.QtGui import *
from testnewcheckport import Ui_MainWindow
import sys,socket
import threading

saveinglist = []
disablestyle = r'font: 10pt "MS Shell Dlg 2";background-color: rgb(145, 145, 145);color: rgb(0, 0, 0);'
enablestyle = r'font: 10pt "MS Shell Dlg 2";color: rgb(0, 170, 0);'
disablebuttonstyle = "border: 2px solid transpent; border-radius: 5px; border-color: rgb(145, 145, 145);"
enablebuttonstyle = r'QPushButton{border: 2px solid transpent; border-radius: 5px; border-color: rgb(0, 170, 0);} QPushButton:hover{border-color: rgb(0, 255, 0);}'
class main(QMainWindow, Ui_MainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.repaint()
        self.listWidget.setStyleSheet("background-color: rgb(44, 44, 44);")
        self.progressBar.setValue(0)
        self.pushButton_2.setDisabled(True)
        self.pushButton_2.setStyleSheet(disablebuttonstyle)
        self.radioButton.clicked.connect(self.disableonebuttonstyle)
        self.radioButton_2.clicked.connect(self.disableonebuttonstyle)
        self.pushButton.clicked.connect(self.clickrun)
        self.pushButton_3.clicked.connect(exit)
        self.pushButton_2.clicked.connect(self.clickstop)
        self.pushButton_5.clicked.connect(self.savedateils)
    def disableonebuttonstyle(self):
        if self.radioButton.isChecked():
            self.lineEdit_2.setStyleSheet(enablestyle)
            self.lineEdit_4.setStyleSheet(enablestyle)
            self.lineEdit_3.setStyleSheet(disablestyle)
            self.lineEdit_3.clear()
        elif self.radioButton_2.isChecked():
            self.lineEdit_3.setStyleSheet(enablestyle)
            self.lineEdit_2.setStyleSheet(disablestyle)
            self.lineEdit_4.setStyleSheet(disablestyle)
            self.lineEdit_2.clear()
            self.lineEdit_4.clear()

    def clickrun(self):
        try:
            urllist = ["http","www."]
            filterlink = "{0}.".format(str(self.lineEdit.text())[:3])
            filterurl = str(self.lineEdit.text())[:4]
            if (filterlink[:3].isdigit() == True and filterlink == filterurl) or filterurl in urllist:
                if (self.radioButton.isChecked() and str(self.lineEdit_2.text()).isdigit() == True and str(self.lineEdit_4.text()).isdigit() == True) or (self.radioButton_2.isChecked() and str(self.lineEdit_3.text()).isdigit() == True):
                    if self.radioButton.isChecked():
                        if int(self.lineEdit_2.text()) < int(self.lineEdit_4.text()):
                            self.lineEdit.setDisabled(True)
                            self.lineEdit.setStyleSheet(disablestyle)
                            self.pushButton.setDisabled(True)
                            self.pushButton.setStyleSheet(disablebuttonstyle)
                            self.pushButton_2.setEnabled(True)
                            self.pushButton_2.setStyleSheet(enablebuttonstyle)
                            self.radioButton.setDisabled(True)
                            self.radioButton_2.setDisabled(True)
                            self.lineEdit_2.setDisabled(True)
                            self.lineEdit_4.setDisabled(True)
                            self.lineEdit_2.setStyleSheet(disablestyle)
                            self.lineEdit_4.setStyleSheet(disablestyle)                            
                            progressBarvalue1 = (float(self.lineEdit_4.text()) - float(self.lineEdit_2.text()))+1
                            progressBarvalue = 100 / float(progressBarvalue1)
                            progressBarvalue2 = 0

                            for iii in range(int(self.lineEdit_2.text()), int(self.lineEdit_4.text())+1):
                                self.repaint()
                                soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                                ipv4 = socket.gethostbyname(str(self.lineEdit.text()))
                                check = soc.connect_ex((ipv4, iii))
                                if check == 0:
                                    portname = socket.getservbyport(iii)
                                    mssg = "Port {0}, Port_Name {1}, IP: {2} / State Open-{3} is Found <<<<".format(iii,portname,ipv4,check)
                                    saveinglist.append(mssg)
                                    self.listWidget.addItem(mssg)
                                else:
                                    mssg = "Port {0}, IP: {1} / State Close-{2}, Not Found".format(iii, ipv4, check)
                                    saveinglist.append(mssg)
                                    self.listWidget.addItem(mssg)
                                progressBarvalue2 += progressBarvalue
                                self.progressBar.setValue(progressBarvalue2)
                        else:
                            self.listWidget.addItem("We must Port from hight of Port to")
                    elif self.radioButton_2.isChecked():
                        self.lineEdit.setDisabled(True)
                        self.lineEdit.setStyleSheet(disablestyle)
                        self.pushButton.setDisabled(True)
                        self.pushButton.setStyleSheet(disablebuttonstyle)
                        self.pushButton_2.setEnabled(True)
                        self.pushButton_2.setStyleSheet(enablebuttonstyle)
                        self.radioButton.setDisabled(True)
                        self.radioButton_2.setDisabled(True)
                        self.lineEdit_3.setDisabled(True)
                        self.lineEdit_3.setStyleSheet(disablestyle)
                        soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                        ipv4 = socket.gethostbyname(str(self.lineEdit.text()))
                        check = soc.connect_ex((ipv4, int(self.lineEdit_3.text())))
                        self.progressBar.setValue(100)
                        if check == 0:
                            portname = socket.getservbyport(int(self.lineEdit_3.text()))
                            mssg = "Port {0}, Port_Name {1}, IP: {2} / State Open-{3} is Found <<<<".format(self.lineEdit_3.text(),portname,ipv4, check)
                            saveinglist.append(mssg)
                            self.listWidget.addItem(mssg)
                        else:
                            mssg = "Port {0}, IP: {1} / State Close-{2}, Not Found".format(self.lineEdit_3.text(), ipv4, check)
                            saveinglist.append(mssg)
                            self.listWidget.addItem(mssg)
                else:
                    self.listWidget.addItem("Please write Port number and not write letters")
            else:
                self.listWidget.addItem("Enter Website or URL NOTE : We are must link at start www. / http")
        except:
            self.listWidget.addItem("Error...")
    def clickstop(self):
        self.lineEdit.setEnabled(True)
        self.lineEdit.setStyleSheet(enablestyle)
        self.pushButton.setEnabled(True)
        self.pushButton.setStyleSheet(enablebuttonstyle)
        self.progressBar.setValue(0)
        if self.radioButton.isChecked():
            self.radioButton.setEnabled(True)
            self.radioButton_2.setEnabled(True)
            self.lineEdit_2.setEnabled(True)
            self.lineEdit_4.setEnabled(True)
            self.lineEdit_2.setStyleSheet(enablestyle)
            self.lineEdit_4.setStyleSheet(enablestyle)
        elif self.radioButton_2.isChecked():
            self.radioButton_2.setEnabled(True)
            self.radioButton.setEnabled(True)
            self.lineEdit_3.setEnabled(True)
            self.lineEdit_3.setStyleSheet(enablestyle)
        self.pushButton_2.setDisabled(True)
        self.pushButton_2.setStyleSheet(disablebuttonstyle)
    def savedateils(self):
        openfile = open("Dateils.txt","a")
        for oneline in saveinglist:
            openfile.write("{}\n".format(oneline))
        openfile.close()
        self.listWidget.addItem("Successfully Save Dateils.txt")
app = QApplication(sys.argv)
window = main()
window.show()
app.exec_()
