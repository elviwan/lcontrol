

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(402, 300)
        self.LoginButton = QtWidgets.QPushButton(Dialog)
        self.LoginButton.setGeometry(QtCore.QRect(140, 200, 114, 32))
        self.LoginButton.setObjectName("LoginButton")
        self.LabelUserName = QtWidgets.QLabel(Dialog)
        self.LabelUserName.setGeometry(QtCore.QRect(60, 120, 71, 16))
        self.LabelUserName.setObjectName("LabelUserName")
        self.LabelPassword = QtWidgets.QLabel(Dialog)
        self.LabelPassword.setGeometry(QtCore.QRect(60, 160, 71, 16))
        self.LabelPassword.setObjectName("LabelPassword")
        self.UsernameInput = QtWidgets.QLineEdit(Dialog)
        self.UsernameInput.setGeometry(QtCore.QRect(150, 120, 113, 21))
        self.UsernameInput.setObjectName("UsernameInput")
        self.PasswordInput = QtWidgets.QLineEdit(Dialog)
        self.PasswordInput.setGeometry(QtCore.QRect(150, 160, 113, 21))
        self.PasswordInput.setObjectName("PasswordInput")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.LoginButton.setText(_translate("Dialog", "Login"))
        self.LabelUserName.setText(_translate("Dialog", "Username:"))
        self.LabelPassword.setText(_translate("Dialog", "Password:"))



if __name__ == '__main__':
    app = QtWidgets.QApplication( sys.argv )
    ui = QtWidgets.QDialog()
    ui.setupUi(ui)
    ui.show()





