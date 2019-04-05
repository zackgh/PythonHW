# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from PyQt5.QtCore import QDate, QTime, QDateTime, Qt 
now = QDate.currentDate()
print(now)

print(now.toString(Qt.ISODate))
print(now.toString(Qt.DefaultLocaleLongDate))
print('')

dateTime = QDateTime.currentDateTime()
print(dateTime.toString())
print('Prin the month:')
getTimeStr = dateTime.toString()
print(getTimeStr[4:7])
print('')

#Days in month/year
d = QDate(1945,5,7)
print("Days in month: %s" % d.daysInMonth())
print("Days in year: %s" % d.daysInYear())

xmas1 = QDate(2019,12,24)
xmas2 = QDate(2018,12,24)

now = QDate.currentDate()
daysPassed = xmas2.daysTo(now)
print("%s days passed since last XMas" % daysPassed)


# datetime arothmatic 
now = QDateTime.currentDateTime()
print("Today: %s" % now.toString(Qt.ISODate))
print("Adding 12 days: %s" % now.addDays(12).toString(Qt.ISODate))
print("Subtracting 22 days: %s" % now.addDays(-22).toString(Qt.ISODate))
print("Adding 55 seconds: %s" % now.addSecs(55).toString(Qt.ISODate))
print("Adding 3 months: %s" % now.addMonths(3).toString(Qt.ISODate))
print("Adding 12 years: %s" % now.addYears(12).toString(Qt.ISODate))

# daylight savings time (DST)
from PyQt5.QtCore import QTimeZone
now = QDateTime.currentDateTime()
print("Time Zone: %s" % now.timeZoneAbbreviation())

if now.isDaylightTime():
    print("The current date falls into DST time")
else:
    print("The current date does not fall into DST time")
    
    
    
"""
windows and widgets 
"""

#import sys
#from PyQt5.QtWidgets import QApplication,QWidget
#from PyQt5.QtGui import QIcon
#
#class Example(QWidget):
#    def __init__(self):
#        super().__init__()
#        self.initUI()
#    def initUI(self):
#        self.setGeometry(300,300,300,220)
#        self.setWindowTitle('Icon')
#        self.setWindowIcon(QIcon('web.png'))
#        
#        self.show()
#        
#app = QApplication(sys.argv)
#ex = Example()
#sys.exit(app.exec_())
#    
#app = QApplication(sys.argv)
#w=QWidget()
#w.resize(350,150)
#w.move(300,300)
#w.setWindowTitle('Simple')
#w.show()
#
#sys.exit(app.exec_())
#quit


## a push button 

import sys
from PyQt5.QtWidgets import QWidget, QPushButton, QApplication

class Example(QWidget):
    
    def __init__(self):
        super().__init__()
        
        self.initUI()
        
        
    def initUI(self):               
        
        qbtn = QPushButton('Quit', self)
        qbtn.clicked.connect(QApplication.instance().quit)
        qbtn.resize(qbtn.sizeHint())
        qbtn.move(50, 50)       
        
        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Quit button')    
        self.show()
        
  
      
   
app = QApplication(sys.argv)
ex = Example()
sys.exit(app.exec_())



import sys
from PyQt5.QtWidgets import QWidget, QMessageBox, QApplication


class Example(QWidget):
    
    def __init__(self):
        super().__init__()
        
        self.initUI()
        
        
    def initUI(self):               
        
        self.setGeometry(300, 300, 250, 150)        
        self.setWindowTitle('Message box')    
        self.show()
        
        
    def closeEvent(self, event):
        
        reply = QMessageBox.question(self, 'Message',
            "Are you sure to quit?", QMessageBox.Yes | 
            QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()        
        
        

    
app = QApplication(sys.argv)
ex = Example()
sys.exit(app.exec_())



import sys
from PyQt5.QtWidgets import QWidget, QDesktopWidget, QApplication

class Example(QWidget):
    
    def __init__(self):
        super().__init__()
        
        self.initUI()
        
        
    def initUI(self):               
        
        self.resize(250, 150)
        self.center()
        
        self.setWindowTitle('Center')    
        self.show()
        
        
    def center(self):
        
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
        



app = QApplication(sys.argv)
ex = Example()
sys.exit(app.exec_())











