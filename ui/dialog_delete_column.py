# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\studb\ui\dialog_delete_column.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog_delete_column(object):
    def setupUi(self, Dialog_delete_column):
        Dialog_delete_column.setObjectName("Dialog_delete_column")
        Dialog_delete_column.setWindowModality(QtCore.Qt.ApplicationModal)
        Dialog_delete_column.resize(320, 130)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        Dialog_delete_column.setFont(font)
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog_delete_column)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(Dialog_delete_column)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.comboBox = QtWidgets.QComboBox(Dialog_delete_column)
        self.comboBox.setObjectName("comboBox")
        self.horizontalLayout.addWidget(self.comboBox)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog_delete_column)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(Dialog_delete_column)
        self.buttonBox.accepted.connect(Dialog_delete_column.accept)
        self.buttonBox.rejected.connect(Dialog_delete_column.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog_delete_column)

    def retranslateUi(self, Dialog_delete_column):
        _translate = QtCore.QCoreApplication.translate
        Dialog_delete_column.setWindowTitle(_translate("Dialog_delete_column", "删除列"))
        self.label.setText(_translate("Dialog_delete_column", "请选择要删除的列："))