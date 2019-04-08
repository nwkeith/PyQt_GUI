# -*- coding: utf-8 -*-
"""
Created on Sun Apr  7 22:41:10 2019

@author: Nathan Keith
HW26
"""
import sys
from PyQt5.QtWidgets import QMainWindow, QTextEdit, QApplication, QAction, qApp, QMenu
from PyQt5.QtGui import QIcon
#Task 1
"""
class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        self.statusBar().showMessage('Ready')
        self.setGeometry(300,300,450,150)
        self.setWindowTitle('MossBar')
        self.show()
"""

#Task 2
"""
class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        exitAct=QAction(QIcon('exit.png'),'&Exit',self)
        exitAct.setShortcut('Ctrl+Q')
        exitAct.setStatusTip('Exit application')
        exitAct.triggered.connect(qApp.quit)
        
        self.statusBar()
        menubar=self.menuBar()
        fileMenu=menubar.addMenu('&File')
        fileMenu.addAction(exitAct)
        
        self.setGeometry(300,300,300,200)
        self.setWindowTitle('Simple menu')
        self.show()
"""
#Task 3
"""
class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        menubar=self.menuBar()
        fileMenu=menubar.addMenu('File')
        
        impMenu=QMenu('Import',self)
        impAct=QAction('Import mail',self)
        impMenu.addAction(impAct)
        
        newAct=QAction('New',self)
        
        fileMenu.addAction(newAct)
        fileMenu.addMenu(impMenu)
        
        self.setGeometry(300,300,300,200)
        self.setWindowTitle('Submenu')
        self.show()
"""
#Task 4
"""
class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        self.statusbar=self.statusBar()
        self.statusbar.showMessage('Ready')
        menubar=self.menuBar()
        viewMenu=menubar.addMenu('View')
        
        viewStatAct=QAction('View Statusbar', self, checkable=True)
        viewStatAct.setStatusTip('View Statusbar')
        viewStatAct.setChecked(True)
        viewStatAct.triggered.connect(self.toggleMenu)
        
        viewMenu.addAction(viewStatAct)
        
        self.setGeometry(300,300,300,200)
        self.setWindowTitle('Check menu')
        self.show()
    def toggleMenu(self,state):
        if state:
            self.statusbar.show()
        else:
            self.statusbar.hide()
"""
#Task 5
"""
class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        self.setGeometry(300,300,300,200)
        self.setWindowTitle('Check menu')
        self.show()
    def contextMenuEvent(self, event):
        
        cmenu=QMenu(self)
        newAct=cmenu.addAction("New")
        opnAct=cmenu.addAction("Open")
        quitAct=cmenu.addAction("Quit")
        action = cmenu.exec_(self.mapToGlobal(event.pos()))
        
        if action == quitAct:
            qApp.quit()
"""

#Task 6
"""
class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        exitAct=QAction(QIcon('exit.png'),'Exit',self)
        exitAct.setShortcut('Ctrl+Q')
        exitAct.triggered.connect(qApp.quit)
        
        self.toolbar=self.addToolBar('Exit')
        self.toolbar.addAction(exitAct)
        
        self.setGeometry(300,300,400,200)
        self.setWindowTitle('Toolbar')
        self.show()
"""

#Task 7
class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        textEdit=QTextEdit()
        self.setCentralWidget(textEdit)
        
        exitAct=QAction(QIcon('exit.png'),'Exit',self)
        exitAct.setShortcut('Ctrl+Q')
        exitAct.setStatusTip('Exit Application')
        exitAct.triggered.connect(self.close)
        
        self.statusBar()
        
        menubar=self.menuBar()
        fileMenu=menubar.addMenu('&File')
        fileMenu.addAction(exitAct)
        
        self.toolbar=self.addToolBar('Exit')
        self.toolbar.addAction(exitAct)
        
        self.setGeometry(300,300,400,200)
        self.setWindowTitle('Main Moss')
        self.show()
if __name__ == '__main__':

    app=QApplication(sys.argv)
    ex=Example()
    app.exec_()