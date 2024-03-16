from PyQt5.QtWidgets import * 
from PyQt5.QtGui import * 
from PyQt5.QtCore import * 


class Ui_confirm(object):
    def setupUi(self, location):
        location.setObjectName("location")
        location.resize(513, 113)
        location.setStyleSheet("#location{background-color: rgb(152, 255, 255);}")
        self.buttonBox = QDialogButtonBox(location)
        self.buttonBox.setGeometry(QRect(-50, 60, 341, 32))
        self.buttonBox.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(255, 255, 255, 255), stop:0.495 rgba(255, 255, 255, 255), stop:0.505 rgba(255, 0, 0, 255), stop:1 rgba(255, 0, 0, 255));")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Ok)
        self.buttonBox.setCenterButtons(True)
        self.buttonBox.setObjectName("buttonBox")
        self.loc = QLabel(location)
        self.loc.setGeometry(QRect(10, 20, 531, 21))
        self.loc.setObjectName("loc")

        self.retranslateUi(location)
        self.buttonBox.accepted.connect(location.accept)
        self.buttonBox.rejected.connect(location.reject)
        QMetaObject.connectSlotsByName(location)

    def retranslateUi(self, location):
        _translate = QCoreApplication.translate
        location.setWindowTitle(_translate("location", "Confirmation"))
        self.loc.setText("It will import only softwares installed in Linux(Ubuntu) or Windows")


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    Dialog = QDialog()
    ui = Ui_confirm()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())