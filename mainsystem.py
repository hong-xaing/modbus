from controltc100withpython import Ui_Dialog
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys
from Ver_FakeForUI import settingup,servoOn,servoOff,initial,designatedLocation,readCurrentLocation,closeup

global servostatus,master,clickedtimes
servostatus=0

def servoSwitch():
    print("Switch Servo")
    global servostatus,master
    if servostatus==0:
        servoOn(master)
        servostatus=1
        ui.label.setText("STATUS: ON")
        ui.servoonoff.setText("SERVO OFF")
    else:
        servoOff(master)
        servostatus=0
        ui.label.setText("STATUS: OFF")
        ui.servoonoff.setText("SERVO ON")
def goInitial():
    print("Initial")
    global master
    initial(master)
    messagebox=QMessageBox()
    messagebox.setWindowTitle("通知")
    messagebox.setInformativeText("原點復歸完成")
    messagebox.exec_()
def gotoDesignatedLocation():
    print("Designated")
    global master
    desloc=ui.lineEdit.text()
    check=designatedLocation(master,desloc)
    if check=="error":
        messagebox=QMessageBox()
        messagebox.setWindowTitle("通知")
        messagebox.setInformativeText("輸入有誤！")
        messagebox.exec_()
        return 0
def uselessButton():
    global clickedtimes
    clickedtimes+=1
    if(clickedtimes==5):
        messagebox=QMessageBox()
        messagebox.setWindowTitle("你有事嗎？？？")
        messagebox.setInformativeText("你按這個「只是用來填滿版面的按鈕」五次了欸...")
        messagebox.exec_()
        clickedtimes=0

app=QApplication(sys.argv)
widget=QWidget()
ui=Ui_Dialog()
ui.setupUi(widget)

master=settingup()
clickedtimes=0
ui.servoonoff.clicked.connect(servoSwitch)
ui.initial.clicked.connect(goInitial)
ui.designatedlocation.clicked.connect(gotoDesignatedLocation)
ui.pushButton_4.clicked.connect(uselessButton)

widget.show()
app.exec_()
closeup(master)