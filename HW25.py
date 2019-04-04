# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 15:48:10 2019

@author: nwkeith
"""
import sys
from PyQt5.QtWidgets import (QApplication, QDesktopWidget, QWidget, QMessageBox, QToolTip, QPushButton, QMainWindow)
from PyQt5.QtGui import (QIcon, QFont)
from PyQt5.QtCore import *
now=QDate.currentDate()
print(now)
print(now.toString(Qt.ISODate))
print(now.toString(Qt.DefaultLocaleLongDate))
print('')

dateTime=QDateTime.currentDateTime()
print(dateTime.toString())

time=QTime.currentTime()
print(time.toString(Qt.DefaultLocaleLongDate))
getTimeStr=dateTime.toString()
print(getTimeStr[4:7])
print('')

#Days in month or year
d=QDate(1945,5,7)
print("Days in month: %s" % d.daysInMonth())
print("Days in year: %s" % d.daysInYear())

onetwofive1=QDate(2019,1,25)
onetwofive2=QDate(2019,12,5)
now=QDate.currentDate()
daysPassed=now.daysTo(onetwofive2)
print('%s days until next 125 day' % daysPassed)

#datetime arithmetic
now=QDateTime.currentDateTime()
print('Today: %s' % now.toString(Qt.ISODate))
print('Adding 246 days: %s' % now.addDays(246).toString(Qt.ISODate))
print('Subtracting 22 days: %s' % now.addDays(-22).toString(Qt.ISODate))
print('Adding 55 seconds: %s' % now.addSecs(55).toString(Qt.ISODate))
print('Adding 3 months: %s' % now.addMonths(3).toString(Qt.ISODate))
print('Adding 12 years: %s' % now.addYears(12).toString(Qt.ISODate))

#Daylight Saving Time
now=QDateTime.currentDateTime()
print('Time Zone: %s' % now.timeZoneAbbreviation())
if now.isDaylightTime():
    print("It's daylight saving time!")
else:
    print("It's not daylight saving time, so sad.")


class mossWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        QToolTip.setFont(QFont('SansSerif',10))
        self.setToolTip('This is one <b>MOSSY</b> widget')
        qbtn=QPushButton("Don't Press",self)
        qbtn.clicked.connect(self.close)
        qbtn.setToolTip('This is one <b>MOSSY</b> button')
        qbtn.resize(qbtn.sizeHint())
        qbtn.move(50,50)
        self.setGeometry(300,300,300,220)
        self.center()
        self.setWindowTitle('Peat Moss')
        self.setWindowIcon(QIcon('bident.png'))
        self.show()
    def center(self):
        qr=self.frameGeometry()
        cp=QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
    def closeEvent(self,event):
        reply=QMessageBox.question(self,'Mossage', "Come on, are you certain?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()
   
       
        
app=QApplication(sys.argv)
ex=mossWidget()
sys.exit(app.exec_())
"""
app=QApplication(sys.argv)
w=QWidget()
w.resize(350,150)
w.move(300,300)
w.setWindowTitle("SimpleMoss")
w.show()
sys.exit(app.exec_())
"""
