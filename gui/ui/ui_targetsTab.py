# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui/ui/ui_targetsTab.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_TargetsTab(object):
    def setupUi(self, TargetsTab):
        TargetsTab.setObjectName("TargetsTab")
        TargetsTab.resize(1214, 771)
        self.horizontalLayout = QtWidgets.QHBoxLayout(TargetsTab)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.groupBox_5 = QtWidgets.QGroupBox(TargetsTab)
        self.groupBox_5.setObjectName("groupBox_5")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.groupBox_5)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.list_tagFilter = QtWidgets.QListView(self.groupBox_5)
        self.list_tagFilter.setObjectName("list_tagFilter")
        self.verticalLayout_6.addWidget(self.list_tagFilter)
        self.verticalLayout_4.addWidget(self.groupBox_5)
        self.groupBox_4 = QtWidgets.QGroupBox(TargetsTab)
        self.groupBox_4.setObjectName("groupBox_4")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.groupBox_4)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.lineEdit = QtWidgets.QLineEdit(self.groupBox_4)
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout_5.addWidget(self.lineEdit)
        self.list_taggedImages = QtWidgets.QListView(self.groupBox_4)
        self.list_taggedImages.setObjectName("list_taggedImages")
        self.verticalLayout_5.addWidget(self.list_taggedImages)
        self.verticalLayout_4.addWidget(self.groupBox_4)
        self.label_6 = QtWidgets.QLabel(TargetsTab)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_4.addWidget(self.label_6)
        self.horizontalLayout.addLayout(self.verticalLayout_4)
        self.verticalLayout_10 = QtWidgets.QVBoxLayout()
        self.verticalLayout_10.setContentsMargins(-1, -1, 0, -1)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.viewer_targets = PhotoViewer(TargetsTab)
        self.viewer_targets.setObjectName("viewer_targets")
        self.verticalLayout_10.addWidget(self.viewer_targets)
        self.horizontalLayout.addLayout(self.verticalLayout_10)
        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 3)

        self.retranslateUi(TargetsTab)
        QtCore.QMetaObject.connectSlotsByName(TargetsTab)

    def retranslateUi(self, TargetsTab):
        _translate = QtCore.QCoreApplication.translate
        TargetsTab.setWindowTitle(_translate("TargetsTab", "Form"))
        self.groupBox_5.setTitle(_translate("TargetsTab", "Select Tag"))
        self.groupBox_4.setTitle(_translate("TargetsTab", "Images with Selected Tag"))
        self.lineEdit.setText(_translate("TargetsTab", "search image by name"))
        self.label_6.setText(_translate("TargetsTab", "MINIMAP"))

from gui.photoViewer import PhotoViewer