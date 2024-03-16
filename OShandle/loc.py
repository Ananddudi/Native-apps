# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'locations.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5.QtWidgets import * 
from PyQt5.QtGui import * 
from PyQt5.QtCore import * 


class Ui_location(object):
    def setupUi(self, location):
        location.setObjectName("location")
        location.resize(253, 113)
        location.setStyleSheet("#location{background-color: rgb(152, 255, 255);}")
        self.buttonBox = QDialogButtonBox(location)
        self.buttonBox.setGeometry(QRect(-50, 60, 341, 32))
        self.buttonBox.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(255, 255, 255, 255), stop:0.495 rgba(255, 255, 255, 255), stop:0.505 rgba(255, 0, 0, 255), stop:1 rgba(255, 0, 0, 255));")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Ok)
        self.buttonBox.setCenterButtons(True)
        self.buttonBox.setObjectName("buttonBox")
        self.loc = QLineEdit(location)
        self.loc.setGeometry(QRect(10, 20, 231, 21))
        self.loc.setText("")
        self.loc.setObjectName("loc")

        self.retranslateUi(location)
        self.buttonBox.accepted.connect(location.accept)
        self.buttonBox.rejected.connect(location.reject)
        QMetaObject.connectSlotsByName(location)

    def getValues(self):
        return self.loc.text()

    def retranslateUi(self, location):
        _translate = QCoreApplication.translate
        location.setWindowTitle(_translate("location", "Dialog"))
        self.loc.setPlaceholderText(_translate("location", "Type the location "))

