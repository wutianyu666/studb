# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\studb\ui\dialog_set_column_name.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog_set_column_name(object):
    def setupUi(self, Dialog_set_column_name):
        Dialog_set_column_name.setObjectName("Dialog_set_column_name")
        Dialog_set_column_name.setWindowModality(QtCore.Qt.ApplicationModal)
        Dialog_set_column_name.resize(320, 130)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        Dialog_set_column_name.setFont(font)
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog_set_column_name)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(Dialog_set_column_name)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.lineEdit = QtWidgets.QLineEdit(Dialog_set_column_name)
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout.addWidget(self.lineEdit)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog_set_column_name)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(Dialog_set_column_name)
        self.buttonBox.rejected.connect(Dialog_set_column_name.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog_set_column_name)

    def retranslateUi(self, Dialog_set_column_name):
        _translate = QtCore.QCoreApplication.translate
        Dialog_set_column_name.setWindowTitle(_translate("Dialog_set_column_name", "设置列名"))
        self.label.setText(_translate("Dialog_set_column_name", "新列的列名："))
