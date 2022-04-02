# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/egis/Dropbox/Workspace/PythonProjects/PHOTOELECTRON-YELD-CONTROLLER/GUI/pys_main_window.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_PYSWindow(object):
    def setupUi(self, PYSWindow):
        PYSWindow.setObjectName("PYSWindow")
        PYSWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(PYSWindow)
        self.centralwidget.setObjectName("centralwidget")
        PYSWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(PYSWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 27))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        PYSWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(PYSWindow)
        self.statusbar.setObjectName("statusbar")
        PYSWindow.setStatusBar(self.statusbar)
        self.actionClose = QtWidgets.QAction(PYSWindow)
        self.actionClose.setObjectName("actionClose")
        self.menuFile.addAction(self.actionClose)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(PYSWindow)
        QtCore.QMetaObject.connectSlotsByName(PYSWindow)

    def retranslateUi(self, PYSWindow):
        _translate = QtCore.QCoreApplication.translate
        PYSWindow.setWindowTitle(_translate("PYSWindow", "PYS matavimai"))
        self.menuFile.setTitle(_translate("PYSWindow", "File"))
        self.actionClose.setText(_translate("PYSWindow", "Close"))
