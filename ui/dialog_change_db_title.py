# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\studb\ui\dialog_change_db_title.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog_change_db_title(object):
    def setupUi(self, Dialog_change_db_title):
        Dialog_change_db_title.setObjectName("Dialog_change_db_title")
        Dialog_change_db_title.setWindowModality(QtCore.Qt.ApplicationModal)
        Dialog_change_db_title.resize(320, 130)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        Dialog_change_db_title.setFont(font)
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog_change_db_title)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(Dialog_change_db_title)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.lineEdit = QtWidgets.QLineEdit(Dialog_change_db_title)
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout.addWidget(self.lineEdit)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog_change_db_title)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(Dialog_change_db_title)
        self.buttonBox.rejected.connect(Dialog_change_db_title.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog_change_db_title)

    def retranslateUi(self, Dialog_change_db_title):
        _translate = QtCore.QCoreApplication.translate
        Dialog_change_db_title.setWindowTitle(_translate("Dialog_change_db_title", "修改数据库标题"))
        self.label.setText(_translate("Dialog_change_db_title", "新的数据库标题："))
