from PyQt5.QtWidgets import * 
from PyQt5.QtGui import * 
from PyQt5.QtCore import * 


class Ui_Dirs(object):
    def setupUi(self,dirs):
        dirs.setObjectName("dirs")
        dirs.resize(513, 113)
        dirs.setStyleSheet("#dirs{background-color: rgb(152, 255, 255);}")
        
        self.loc = QLabel(dirs)
        self.loc.setGeometry(QRect(10, 20, 531, 21))
        self.loc.setObjectName("loc")

        self.retranslateUi(dirs)
        QMetaObject.connectSlotsByName(dirs)
    def provideLoc(self):
        return self.loc

    def retranslateUi(self,dirs):
        _translate = QCoreApplication.translate
        dirs.setWindowTitle(_translate("dirs", "File status"))

