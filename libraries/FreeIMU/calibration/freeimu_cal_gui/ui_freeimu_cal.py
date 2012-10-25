# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'freeimu_cal.ui'
#
# Created: Thu Oct 25 18:40:04 2012
#      by: PyQt4 UI code generator 4.9.5
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_FreeIMUCal(object):
    def setupUi(self, FreeIMUCal):
        FreeIMUCal.setObjectName(_fromUtf8("FreeIMUCal"))
        FreeIMUCal.resize(800, 680)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(FreeIMUCal.sizePolicy().hasHeightForWidth())
        FreeIMUCal.setSizePolicy(sizePolicy)
        FreeIMUCal.setMinimumSize(QtCore.QSize(800, 600))
        FreeIMUCal.setMaximumSize(QtCore.QSize(800, 680))
        FreeIMUCal.setDocumentMode(False)
        self.centralwidget = QtGui.QWidget(FreeIMUCal)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.line = QtGui.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(10, 20, 791, 16))
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.gridLayoutWidget = QtGui.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(0, 0, 801, 25))
        self.gridLayoutWidget.setObjectName(_fromUtf8("gridLayoutWidget"))
        self.gridLayout = QtGui.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setSizeConstraint(QtGui.QLayout.SetDefaultConstraint)
        self.gridLayout.setMargin(0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label = QtGui.QLabel(self.gridLayoutWidget)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 5, 1, 1)
        self.calibrateButton = QtGui.QPushButton(self.gridLayoutWidget)
        self.calibrateButton.setEnabled(False)
        self.calibrateButton.setObjectName(_fromUtf8("calibrateButton"))
        self.gridLayout.addWidget(self.calibrateButton, 0, 8, 1, 1)
        self.serialPortEdit = QtGui.QLineEdit(self.gridLayoutWidget)
        self.serialPortEdit.setObjectName(_fromUtf8("serialPortEdit"))
        self.gridLayout.addWidget(self.serialPortEdit, 0, 1, 1, 1)
        self.samplingToggleButton = QtGui.QPushButton(self.gridLayoutWidget)
        self.samplingToggleButton.setEnabled(False)
        self.samplingToggleButton.setAutoDefault(False)
        self.samplingToggleButton.setDefault(False)
        self.samplingToggleButton.setFlat(False)
        self.samplingToggleButton.setObjectName(_fromUtf8("samplingToggleButton"))
        self.gridLayout.addWidget(self.samplingToggleButton, 0, 6, 1, 1)
        self.connectButton = QtGui.QPushButton(self.gridLayoutWidget)
        self.connectButton.setObjectName(_fromUtf8("connectButton"))
        self.gridLayout.addWidget(self.connectButton, 0, 2, 1, 1)
        self.line_2 = QtGui.QFrame(self.gridLayoutWidget)
        self.line_2.setFrameShape(QtGui.QFrame.VLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.gridLayout.addWidget(self.line_2, 0, 3, 1, 1)
        self.calAlgorithmComboBox = QtGui.QComboBox(self.gridLayoutWidget)
        self.calAlgorithmComboBox.setEnabled(False)
        self.calAlgorithmComboBox.setObjectName(_fromUtf8("calAlgorithmComboBox"))
        self.calAlgorithmComboBox.addItem(_fromUtf8(""))
        self.gridLayout.addWidget(self.calAlgorithmComboBox, 0, 7, 1, 1)
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 30, 801, 631))
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.uncalibratedTab = QtGui.QWidget()
        self.uncalibratedTab.setObjectName(_fromUtf8("uncalibratedTab"))
        self.gridLayoutWidget_4 = QtGui.QWidget(self.uncalibratedTab)
        self.gridLayoutWidget_4.setGeometry(QtCore.QRect(0, 10, 791, 588))
        self.gridLayoutWidget_4.setObjectName(_fromUtf8("gridLayoutWidget_4"))
        self.gridLayout_4 = QtGui.QGridLayout(self.gridLayoutWidget_4)
        self.gridLayout_4.setSizeConstraint(QtGui.QLayout.SetMaximumSize)
        self.gridLayout_4.setMargin(0)
        self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))
        self.gridLayout_5 = QtGui.QGridLayout()
        self.gridLayout_5.setObjectName(_fromUtf8("gridLayout_5"))
        self.label_2 = QtGui.QLabel(self.gridLayoutWidget_4)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout_5.addWidget(self.label_2, 0, 1, 1, 1)
        self.accYZ = PlotWidget(self.gridLayoutWidget_4)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.accYZ.sizePolicy().hasHeightForWidth())
        self.accYZ.setSizePolicy(sizePolicy)
        self.accYZ.setObjectName(_fromUtf8("accYZ"))
        self.gridLayout_5.addWidget(self.accYZ, 1, 0, 1, 1)
        self.accZX = PlotWidget(self.gridLayoutWidget_4)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.accZX.sizePolicy().hasHeightForWidth())
        self.accZX.setSizePolicy(sizePolicy)
        self.accZX.setObjectName(_fromUtf8("accZX"))
        self.gridLayout_5.addWidget(self.accZX, 1, 1, 1, 1)
        self.accXY = PlotWidget(self.gridLayoutWidget_4)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.accXY.sizePolicy().hasHeightForWidth())
        self.accXY.setSizePolicy(sizePolicy)
        self.accXY.setObjectName(_fromUtf8("accXY"))
        self.gridLayout_5.addWidget(self.accXY, 0, 0, 1, 1)
        self.gridLayout_4.addLayout(self.gridLayout_5, 1, 0, 1, 1)
        self.gridLayout_3 = QtGui.QGridLayout()
        self.gridLayout_3.setSizeConstraint(QtGui.QLayout.SetFixedSize)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.magnXY = PlotWidget(self.gridLayoutWidget_4)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.magnXY.sizePolicy().hasHeightForWidth())
        self.magnXY.setSizePolicy(sizePolicy)
        self.magnXY.setObjectName(_fromUtf8("magnXY"))
        self.gridLayout_3.addWidget(self.magnXY, 0, 0, 1, 1)
        self.magnYZ = PlotWidget(self.gridLayoutWidget_4)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.magnYZ.sizePolicy().hasHeightForWidth())
        self.magnYZ.setSizePolicy(sizePolicy)
        self.magnYZ.setObjectName(_fromUtf8("magnYZ"))
        self.gridLayout_3.addWidget(self.magnYZ, 1, 0, 1, 1)
        self.magnZX = PlotWidget(self.gridLayoutWidget_4)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.magnZX.sizePolicy().hasHeightForWidth())
        self.magnZX.setSizePolicy(sizePolicy)
        self.magnZX.setObjectName(_fromUtf8("magnZX"))
        self.gridLayout_3.addWidget(self.magnZX, 1, 1, 1, 1)
        self.label_3 = QtGui.QLabel(self.gridLayoutWidget_4)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout_3.addWidget(self.label_3, 0, 1, 1, 1)
        self.gridLayout_4.addLayout(self.gridLayout_3, 1, 2, 1, 1)
        self.magn3D = GLViewWidget(self.gridLayoutWidget_4)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.magn3D.sizePolicy().hasHeightForWidth())
        self.magn3D.setSizePolicy(sizePolicy)
        self.magn3D.setObjectName(_fromUtf8("magn3D"))
        self.gridLayout_4.addWidget(self.magn3D, 0, 2, 1, 1)
        self.acc3D = GLViewWidget(self.gridLayoutWidget_4)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.acc3D.sizePolicy().hasHeightForWidth())
        self.acc3D.setSizePolicy(sizePolicy)
        self.acc3D.setObjectName(_fromUtf8("acc3D"))
        self.gridLayout_4.addWidget(self.acc3D, 0, 0, 1, 1)
        self.line_3 = QtGui.QFrame(self.gridLayoutWidget_4)
        self.line_3.setLineWidth(1)
        self.line_3.setFrameShape(QtGui.QFrame.VLine)
        self.line_3.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_3.setObjectName(_fromUtf8("line_3"))
        self.gridLayout_4.addWidget(self.line_3, 1, 1, 1, 1)
        self.tabWidget.addTab(self.uncalibratedTab, _fromUtf8(""))
        self.calibratedTab = QtGui.QWidget()
        self.calibratedTab.setObjectName(_fromUtf8("calibratedTab"))
        self.horizontalLayoutWidget = QtGui.QWidget(self.calibratedTab)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(0, 380, 791, 181))
        self.horizontalLayoutWidget.setObjectName(_fromUtf8("horizontalLayoutWidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.groupBox = QtGui.QGroupBox(self.horizontalLayoutWidget)
        self.groupBox.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.groupBox.setFlat(False)
        self.groupBox.setCheckable(False)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.layoutWidget = QtGui.QWidget(self.groupBox)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 20, 381, 154))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.formLayout_3 = QtGui.QFormLayout(self.layoutWidget)
        self.formLayout_3.setSizeConstraint(QtGui.QLayout.SetNoConstraint)
        self.formLayout_3.setFieldGrowthPolicy(QtGui.QFormLayout.ExpandingFieldsGrow)
        self.formLayout_3.setLabelAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.formLayout_3.setMargin(0)
        self.formLayout_3.setObjectName(_fromUtf8("formLayout_3"))
        self.label_14 = QtGui.QLabel(self.layoutWidget)
        self.label_14.setObjectName(_fromUtf8("label_14"))
        self.formLayout_3.setWidget(0, QtGui.QFormLayout.LabelRole, self.label_14)
        self.calRes_acc_OSx = QtGui.QLineEdit(self.layoutWidget)
        self.calRes_acc_OSx.setObjectName(_fromUtf8("calRes_acc_OSx"))
        self.formLayout_3.setWidget(0, QtGui.QFormLayout.FieldRole, self.calRes_acc_OSx)
        self.label_15 = QtGui.QLabel(self.layoutWidget)
        self.label_15.setObjectName(_fromUtf8("label_15"))
        self.formLayout_3.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_15)
        self.calRes_acc_OSy = QtGui.QLineEdit(self.layoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.calRes_acc_OSy.sizePolicy().hasHeightForWidth())
        self.calRes_acc_OSy.setSizePolicy(sizePolicy)
        self.calRes_acc_OSy.setObjectName(_fromUtf8("calRes_acc_OSy"))
        self.formLayout_3.setWidget(1, QtGui.QFormLayout.FieldRole, self.calRes_acc_OSy)
        self.label_16 = QtGui.QLabel(self.layoutWidget)
        self.label_16.setObjectName(_fromUtf8("label_16"))
        self.formLayout_3.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_16)
        self.calRes_acc_OSz = QtGui.QLineEdit(self.layoutWidget)
        self.calRes_acc_OSz.setObjectName(_fromUtf8("calRes_acc_OSz"))
        self.formLayout_3.setWidget(2, QtGui.QFormLayout.FieldRole, self.calRes_acc_OSz)
        self.label_17 = QtGui.QLabel(self.layoutWidget)
        self.label_17.setObjectName(_fromUtf8("label_17"))
        self.formLayout_3.setWidget(3, QtGui.QFormLayout.LabelRole, self.label_17)
        self.calRes_acc_SCx = QtGui.QLineEdit(self.layoutWidget)
        self.calRes_acc_SCx.setObjectName(_fromUtf8("calRes_acc_SCx"))
        self.formLayout_3.setWidget(3, QtGui.QFormLayout.FieldRole, self.calRes_acc_SCx)
        self.label_18 = QtGui.QLabel(self.layoutWidget)
        self.label_18.setObjectName(_fromUtf8("label_18"))
        self.formLayout_3.setWidget(4, QtGui.QFormLayout.LabelRole, self.label_18)
        self.calRes_acc_SCy = QtGui.QLineEdit(self.layoutWidget)
        self.calRes_acc_SCy.setObjectName(_fromUtf8("calRes_acc_SCy"))
        self.formLayout_3.setWidget(4, QtGui.QFormLayout.FieldRole, self.calRes_acc_SCy)
        self.label_19 = QtGui.QLabel(self.layoutWidget)
        self.label_19.setObjectName(_fromUtf8("label_19"))
        self.formLayout_3.setWidget(5, QtGui.QFormLayout.LabelRole, self.label_19)
        self.calRes_acc_SCz = QtGui.QLineEdit(self.layoutWidget)
        self.calRes_acc_SCz.setObjectName(_fromUtf8("calRes_acc_SCz"))
        self.formLayout_3.setWidget(5, QtGui.QFormLayout.FieldRole, self.calRes_acc_SCz)
        self.horizontalLayout.addWidget(self.groupBox)
        self.groupBox_2 = QtGui.QGroupBox(self.horizontalLayoutWidget)
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.layoutWidget_2 = QtGui.QWidget(self.groupBox_2)
        self.layoutWidget_2.setGeometry(QtCore.QRect(10, 20, 381, 154))
        self.layoutWidget_2.setObjectName(_fromUtf8("layoutWidget_2"))
        self.formLayout_5 = QtGui.QFormLayout(self.layoutWidget_2)
        self.formLayout_5.setSizeConstraint(QtGui.QLayout.SetNoConstraint)
        self.formLayout_5.setFieldGrowthPolicy(QtGui.QFormLayout.ExpandingFieldsGrow)
        self.formLayout_5.setLabelAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.formLayout_5.setMargin(0)
        self.formLayout_5.setObjectName(_fromUtf8("formLayout_5"))
        self.label_27 = QtGui.QLabel(self.layoutWidget_2)
        self.label_27.setObjectName(_fromUtf8("label_27"))
        self.formLayout_5.setWidget(0, QtGui.QFormLayout.LabelRole, self.label_27)
        self.calRes_magn_OSx = QtGui.QLineEdit(self.layoutWidget_2)
        self.calRes_magn_OSx.setObjectName(_fromUtf8("calRes_magn_OSx"))
        self.formLayout_5.setWidget(0, QtGui.QFormLayout.FieldRole, self.calRes_magn_OSx)
        self.label_28 = QtGui.QLabel(self.layoutWidget_2)
        self.label_28.setObjectName(_fromUtf8("label_28"))
        self.formLayout_5.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_28)
        self.calRes_magn_OSy = QtGui.QLineEdit(self.layoutWidget_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.calRes_magn_OSy.sizePolicy().hasHeightForWidth())
        self.calRes_magn_OSy.setSizePolicy(sizePolicy)
        self.calRes_magn_OSy.setObjectName(_fromUtf8("calRes_magn_OSy"))
        self.formLayout_5.setWidget(1, QtGui.QFormLayout.FieldRole, self.calRes_magn_OSy)
        self.label_29 = QtGui.QLabel(self.layoutWidget_2)
        self.label_29.setObjectName(_fromUtf8("label_29"))
        self.formLayout_5.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_29)
        self.calRes_magn_OSz = QtGui.QLineEdit(self.layoutWidget_2)
        self.calRes_magn_OSz.setObjectName(_fromUtf8("calRes_magn_OSz"))
        self.formLayout_5.setWidget(2, QtGui.QFormLayout.FieldRole, self.calRes_magn_OSz)
        self.label_30 = QtGui.QLabel(self.layoutWidget_2)
        self.label_30.setObjectName(_fromUtf8("label_30"))
        self.formLayout_5.setWidget(3, QtGui.QFormLayout.LabelRole, self.label_30)
        self.calRes_magn_SCx = QtGui.QLineEdit(self.layoutWidget_2)
        self.calRes_magn_SCx.setObjectName(_fromUtf8("calRes_magn_SCx"))
        self.formLayout_5.setWidget(3, QtGui.QFormLayout.FieldRole, self.calRes_magn_SCx)
        self.label_31 = QtGui.QLabel(self.layoutWidget_2)
        self.label_31.setObjectName(_fromUtf8("label_31"))
        self.formLayout_5.setWidget(4, QtGui.QFormLayout.LabelRole, self.label_31)
        self.calRes_magn_SCy = QtGui.QLineEdit(self.layoutWidget_2)
        self.calRes_magn_SCy.setObjectName(_fromUtf8("calRes_magn_SCy"))
        self.formLayout_5.setWidget(4, QtGui.QFormLayout.FieldRole, self.calRes_magn_SCy)
        self.label_32 = QtGui.QLabel(self.layoutWidget_2)
        self.label_32.setObjectName(_fromUtf8("label_32"))
        self.formLayout_5.setWidget(5, QtGui.QFormLayout.LabelRole, self.label_32)
        self.calRes_magn_SCz = QtGui.QLineEdit(self.layoutWidget_2)
        self.calRes_magn_SCz.setObjectName(_fromUtf8("calRes_magn_SCz"))
        self.formLayout_5.setWidget(5, QtGui.QFormLayout.FieldRole, self.calRes_magn_SCz)
        self.horizontalLayout.addWidget(self.groupBox_2)
        self.horizontalLayoutWidget_2 = QtGui.QWidget(self.calibratedTab)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(500, 560, 289, 31))
        self.horizontalLayoutWidget_2.setObjectName(_fromUtf8("horizontalLayoutWidget_2"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setMargin(0)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.saveCalibrationEEPROMButton = QtGui.QPushButton(self.horizontalLayoutWidget_2)
        self.saveCalibrationEEPROMButton.setEnabled(False)
        self.saveCalibrationEEPROMButton.setObjectName(_fromUtf8("saveCalibrationEEPROMButton"))
        self.horizontalLayout_2.addWidget(self.saveCalibrationEEPROMButton)
        self.saveCalibrationHeaderButton = QtGui.QPushButton(self.horizontalLayoutWidget_2)
        self.saveCalibrationHeaderButton.setEnabled(False)
        self.saveCalibrationHeaderButton.setObjectName(_fromUtf8("saveCalibrationHeaderButton"))
        self.horizontalLayout_2.addWidget(self.saveCalibrationHeaderButton)
        self.horizontalLayoutWidget_3 = QtGui.QWidget(self.calibratedTab)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(0, 0, 791, 381))
        self.horizontalLayoutWidget_3.setObjectName(_fromUtf8("horizontalLayoutWidget_3"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_3.setMargin(0)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.tabWidget_2 = QtGui.QTabWidget(self.horizontalLayoutWidget_3)
        self.tabWidget_2.setTabPosition(QtGui.QTabWidget.South)
        self.tabWidget_2.setTabShape(QtGui.QTabWidget.Rounded)
        self.tabWidget_2.setUsesScrollButtons(True)
        self.tabWidget_2.setDocumentMode(False)
        self.tabWidget_2.setTabsClosable(False)
        self.tabWidget_2.setMovable(False)
        self.tabWidget_2.setObjectName(_fromUtf8("tabWidget_2"))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.accXY_cal = PlotWidget(self.tab)
        self.accXY_cal.setGeometry(QtCore.QRect(0, 0, 781, 351))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.accXY_cal.sizePolicy().hasHeightForWidth())
        self.accXY_cal.setSizePolicy(sizePolicy)
        self.accXY_cal.setObjectName(_fromUtf8("accXY_cal"))
        self.tabWidget_2.addTab(self.tab, _fromUtf8(""))
        self.tab_4 = QtGui.QWidget()
        self.tab_4.setObjectName(_fromUtf8("tab_4"))
        self.accYZ_cal = PlotWidget(self.tab_4)
        self.accYZ_cal.setGeometry(QtCore.QRect(0, 0, 781, 351))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.accYZ_cal.sizePolicy().hasHeightForWidth())
        self.accYZ_cal.setSizePolicy(sizePolicy)
        self.accYZ_cal.setObjectName(_fromUtf8("accYZ_cal"))
        self.tabWidget_2.addTab(self.tab_4, _fromUtf8(""))
        self.tab_3 = QtGui.QWidget()
        self.tab_3.setObjectName(_fromUtf8("tab_3"))
        self.accZX_cal = PlotWidget(self.tab_3)
        self.accZX_cal.setGeometry(QtCore.QRect(0, 0, 781, 351))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.accZX_cal.sizePolicy().hasHeightForWidth())
        self.accZX_cal.setSizePolicy(sizePolicy)
        self.accZX_cal.setObjectName(_fromUtf8("accZX_cal"))
        self.tabWidget_2.addTab(self.tab_3, _fromUtf8(""))
        self.tab_7 = QtGui.QWidget()
        self.tab_7.setObjectName(_fromUtf8("tab_7"))
        self.acc3D_cal = GLViewWidget(self.tab_7)
        self.acc3D_cal.setGeometry(QtCore.QRect(0, 0, 389, 351))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.acc3D_cal.sizePolicy().hasHeightForWidth())
        self.acc3D_cal.setSizePolicy(sizePolicy)
        self.acc3D_cal.setObjectName(_fromUtf8("acc3D_cal"))
        self.tabWidget_2.addTab(self.tab_7, _fromUtf8(""))
        self.horizontalLayout_3.addWidget(self.tabWidget_2)
        self.tabWidget_3 = QtGui.QTabWidget(self.horizontalLayoutWidget_3)
        self.tabWidget_3.setTabPosition(QtGui.QTabWidget.South)
        self.tabWidget_3.setTabShape(QtGui.QTabWidget.Rounded)
        self.tabWidget_3.setUsesScrollButtons(True)
        self.tabWidget_3.setDocumentMode(False)
        self.tabWidget_3.setTabsClosable(False)
        self.tabWidget_3.setMovable(False)
        self.tabWidget_3.setObjectName(_fromUtf8("tabWidget_3"))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.magnXY_cal = PlotWidget(self.tab_2)
        self.magnXY_cal.setGeometry(QtCore.QRect(0, 0, 781, 351))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.magnXY_cal.sizePolicy().hasHeightForWidth())
        self.magnXY_cal.setSizePolicy(sizePolicy)
        self.magnXY_cal.setObjectName(_fromUtf8("magnXY_cal"))
        self.tabWidget_3.addTab(self.tab_2, _fromUtf8(""))
        self.tab_5 = QtGui.QWidget()
        self.tab_5.setObjectName(_fromUtf8("tab_5"))
        self.magnYZ_cal = PlotWidget(self.tab_5)
        self.magnYZ_cal.setGeometry(QtCore.QRect(0, 0, 781, 351))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.magnYZ_cal.sizePolicy().hasHeightForWidth())
        self.magnYZ_cal.setSizePolicy(sizePolicy)
        self.magnYZ_cal.setObjectName(_fromUtf8("magnYZ_cal"))
        self.tabWidget_3.addTab(self.tab_5, _fromUtf8(""))
        self.tab_6 = QtGui.QWidget()
        self.tab_6.setObjectName(_fromUtf8("tab_6"))
        self.magnZX_cal = PlotWidget(self.tab_6)
        self.magnZX_cal.setGeometry(QtCore.QRect(0, 0, 781, 351))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.magnZX_cal.sizePolicy().hasHeightForWidth())
        self.magnZX_cal.setSizePolicy(sizePolicy)
        self.magnZX_cal.setObjectName(_fromUtf8("magnZX_cal"))
        self.tabWidget_3.addTab(self.tab_6, _fromUtf8(""))
        self.tab_8 = QtGui.QWidget()
        self.tab_8.setObjectName(_fromUtf8("tab_8"))
        self.magn3D_cal = GLViewWidget(self.tab_8)
        self.magn3D_cal.setGeometry(QtCore.QRect(0, 0, 389, 351))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.magn3D_cal.sizePolicy().hasHeightForWidth())
        self.magn3D_cal.setSizePolicy(sizePolicy)
        self.magn3D_cal.setObjectName(_fromUtf8("magn3D_cal"))
        self.tabWidget_3.addTab(self.tab_8, _fromUtf8(""))
        self.horizontalLayout_3.addWidget(self.tabWidget_3)
        self.tabWidget.addTab(self.calibratedTab, _fromUtf8(""))
        FreeIMUCal.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(FreeIMUCal)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        FreeIMUCal.setStatusBar(self.statusbar)

        self.retranslateUi(FreeIMUCal)
        self.tabWidget.setCurrentIndex(0)
        self.tabWidget_2.setCurrentIndex(0)
        self.tabWidget_3.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(FreeIMUCal)

    def retranslateUi(self, FreeIMUCal):
        FreeIMUCal.setWindowTitle(QtGui.QApplication.translate("FreeIMUCal", "FreeIMU Calibration Application", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("FreeIMUCal", "Serial Port:", None, QtGui.QApplication.UnicodeUTF8))
        self.calibrateButton.setToolTip(QtGui.QApplication.translate("FreeIMUCal", "Run calibration algorithm over the data collected", None, QtGui.QApplication.UnicodeUTF8))
        self.calibrateButton.setText(QtGui.QApplication.translate("FreeIMUCal", "Calibrate", None, QtGui.QApplication.UnicodeUTF8))
        self.samplingToggleButton.setToolTip(QtGui.QApplication.translate("FreeIMUCal", "Toggle Start/Stop sampling of sensor data from the IMU", None, QtGui.QApplication.UnicodeUTF8))
        self.samplingToggleButton.setText(QtGui.QApplication.translate("FreeIMUCal", "Start Sampling", None, QtGui.QApplication.UnicodeUTF8))
        self.connectButton.setToolTip(QtGui.QApplication.translate("FreeIMUCal", "Connect or Disconnect from the Arduino", None, QtGui.QApplication.UnicodeUTF8))
        self.connectButton.setText(QtGui.QApplication.translate("FreeIMUCal", "Connect", None, QtGui.QApplication.UnicodeUTF8))
        self.calAlgorithmComboBox.setToolTip(QtGui.QApplication.translate("FreeIMUCal", "<html><head/><body><p>Calibration Algorithm used.</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.calAlgorithmComboBox.setItemText(0, QtGui.QApplication.translate("FreeIMUCal", "Ellipsoid to Sphere", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("FreeIMUCal", "Accelerometer", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("FreeIMUCal", "Magnetometer", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.uncalibratedTab), QtGui.QApplication.translate("FreeIMUCal", "Uncalibrated", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("FreeIMUCal", "Accelerometer", None, QtGui.QApplication.UnicodeUTF8))
        self.label_14.setText(QtGui.QApplication.translate("FreeIMUCal", "Offset X", None, QtGui.QApplication.UnicodeUTF8))
        self.label_15.setText(QtGui.QApplication.translate("FreeIMUCal", "Offset Y", None, QtGui.QApplication.UnicodeUTF8))
        self.label_16.setText(QtGui.QApplication.translate("FreeIMUCal", "Offset Z", None, QtGui.QApplication.UnicodeUTF8))
        self.label_17.setText(QtGui.QApplication.translate("FreeIMUCal", "Scale X", None, QtGui.QApplication.UnicodeUTF8))
        self.label_18.setText(QtGui.QApplication.translate("FreeIMUCal", "Scale Y", None, QtGui.QApplication.UnicodeUTF8))
        self.label_19.setText(QtGui.QApplication.translate("FreeIMUCal", "Scale Z", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_2.setTitle(QtGui.QApplication.translate("FreeIMUCal", "Magnetometer", None, QtGui.QApplication.UnicodeUTF8))
        self.label_27.setText(QtGui.QApplication.translate("FreeIMUCal", "Offset X", None, QtGui.QApplication.UnicodeUTF8))
        self.label_28.setText(QtGui.QApplication.translate("FreeIMUCal", "Offset Y", None, QtGui.QApplication.UnicodeUTF8))
        self.label_29.setText(QtGui.QApplication.translate("FreeIMUCal", "Offset Z", None, QtGui.QApplication.UnicodeUTF8))
        self.label_30.setText(QtGui.QApplication.translate("FreeIMUCal", "Scale X", None, QtGui.QApplication.UnicodeUTF8))
        self.label_31.setText(QtGui.QApplication.translate("FreeIMUCal", "Scale Y", None, QtGui.QApplication.UnicodeUTF8))
        self.label_32.setText(QtGui.QApplication.translate("FreeIMUCal", "Scale Z", None, QtGui.QApplication.UnicodeUTF8))
        self.saveCalibrationEEPROMButton.setToolTip(QtGui.QApplication.translate("FreeIMUCal", "Store the calibration parameters to the microcontroller EEPROM", None, QtGui.QApplication.UnicodeUTF8))
        self.saveCalibrationEEPROMButton.setText(QtGui.QApplication.translate("FreeIMUCal", "Save to EEPROM", None, QtGui.QApplication.UnicodeUTF8))
        self.saveCalibrationHeaderButton.setToolTip(QtGui.QApplication.translate("FreeIMUCal", "Store the calibration parameters in an header .h file. When such header is active the EEPROM calibration storage code is disabled thus saving program and data memory.", None, QtGui.QApplication.UnicodeUTF8))
        self.saveCalibrationHeaderButton.setText(QtGui.QApplication.translate("FreeIMUCal", "Save to calibration.h", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab), QtGui.QApplication.translate("FreeIMUCal", "Acc XY", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_4), QtGui.QApplication.translate("FreeIMUCal", "Acc YZ", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_3), QtGui.QApplication.translate("FreeIMUCal", "Acc ZX", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_7), QtGui.QApplication.translate("FreeIMUCal", "Acc 3D", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tab_2), QtGui.QApplication.translate("FreeIMUCal", "Magn XY", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tab_5), QtGui.QApplication.translate("FreeIMUCal", "Magn YZ", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tab_6), QtGui.QApplication.translate("FreeIMUCal", "Magn ZX", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tab_8), QtGui.QApplication.translate("FreeIMUCal", "Magn 3D", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.calibratedTab), QtGui.QApplication.translate("FreeIMUCal", "Calibrated", None, QtGui.QApplication.UnicodeUTF8))

from pyqtgraph import PlotWidget
from pyqtgraph.opengl import GLViewWidget
