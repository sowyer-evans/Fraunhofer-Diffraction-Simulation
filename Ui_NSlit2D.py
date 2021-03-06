# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Ui_NSlit2D.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(824, 657)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralWidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.mplwidget2D = MPL_WIDGET_2D(self.centralWidget)
        self.mplwidget2D.setObjectName("mplwidget2D")
        self.horizontalLayout.addWidget(self.mplwidget2D)
        MainWindow.setCentralWidget(self.centralWidget)
        self.dockWidget = QtWidgets.QDockWidget(MainWindow)
        self.dockWidget.setObjectName("dockWidget")
        self.dockWidgetContents_3 = QtWidgets.QWidget()
        self.dockWidgetContents_3.setObjectName("dockWidgetContents_3")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.dockWidgetContents_3)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_lamda = QtWidgets.QLabel(self.dockWidgetContents_3)
        self.label_lamda.setObjectName("label_lamda")
        self.verticalLayout.addWidget(self.label_lamda)
        self.SpinBox_lambda = QtWidgets.QSpinBox(self.dockWidgetContents_3)
        self.SpinBox_lambda.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.SpinBox_lambda.setMinimum(400)
        self.SpinBox_lambda.setMaximum(900)
        self.SpinBox_lambda.setSingleStep(10)
        self.SpinBox_lambda.setProperty("value", 632)
        self.SpinBox_lambda.setObjectName("SpinBox_lambda")
        self.verticalLayout.addWidget(self.SpinBox_lambda)
        self.slider_lambda = QtWidgets.QSlider(self.dockWidgetContents_3)
        self.slider_lambda.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.slider_lambda.setMinimum(400)
        self.slider_lambda.setMaximum(900)
        self.slider_lambda.setSingleStep(10)
        self.slider_lambda.setProperty("value", 632)
        self.slider_lambda.setOrientation(QtCore.Qt.Horizontal)
        self.slider_lambda.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.slider_lambda.setTickInterval(50)
        self.slider_lambda.setObjectName("slider_lambda")
        self.verticalLayout.addWidget(self.slider_lambda)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.label = QtWidgets.QLabel(self.dockWidgetContents_3)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.SpinBox_n = QtWidgets.QDoubleSpinBox(self.dockWidgetContents_3)
        self.SpinBox_n.setDecimals(0)
        self.SpinBox_n.setMinimum(1.0)
        self.SpinBox_n.setMaximum(1000.0)
        self.SpinBox_n.setSingleStep(1.0)
        self.SpinBox_n.setProperty("value", 20.0)
        self.SpinBox_n.setObjectName("SpinBox_n")
        self.verticalLayout.addWidget(self.SpinBox_n)
        self.slider_n = QtWidgets.QSlider(self.dockWidgetContents_3)
        self.slider_n.setMinimum(1)
        self.slider_n.setMaximum(1000)
        self.slider_n.setSingleStep(20)
        self.slider_n.setProperty("value", 20)
        self.slider_n.setOrientation(QtCore.Qt.Horizontal)
        self.slider_n.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.slider_n.setTickInterval(80)
        self.slider_n.setObjectName("slider_n")
        self.verticalLayout.addWidget(self.slider_n)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.label_b = QtWidgets.QLabel(self.dockWidgetContents_3)
        self.label_b.setObjectName("label_b")
        self.verticalLayout.addWidget(self.label_b)
        self.SpinBox_b = QtWidgets.QDoubleSpinBox(self.dockWidgetContents_3)
        self.SpinBox_b.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.SpinBox_b.setDecimals(2)
        self.SpinBox_b.setMinimum(0.1)
        self.SpinBox_b.setMaximum(1000.0)
        self.SpinBox_b.setSingleStep(100.0)
        self.SpinBox_b.setProperty("value", 100.0)
        self.SpinBox_b.setObjectName("SpinBox_b")
        self.verticalLayout.addWidget(self.SpinBox_b)
        self.slider_b = QtWidgets.QSlider(self.dockWidgetContents_3)
        self.slider_b.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.slider_b.setMinimum(1)
        self.slider_b.setMaximum(1000)
        self.slider_b.setSingleStep(100)
        self.slider_b.setPageStep(100)
        self.slider_b.setProperty("value", 100)
        self.slider_b.setOrientation(QtCore.Qt.Horizontal)
        self.slider_b.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.slider_b.setTickInterval(100)
        self.slider_b.setObjectName("slider_b")
        self.verticalLayout.addWidget(self.slider_b)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem2)
        self.label_e = QtWidgets.QLabel(self.dockWidgetContents_3)
        self.label_e.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.label_e.setObjectName("label_e")
        self.verticalLayout.addWidget(self.label_e)
        self.SpinBox_e = QtWidgets.QDoubleSpinBox(self.dockWidgetContents_3)
        self.SpinBox_e.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.SpinBox_e.setDecimals(3)
        self.SpinBox_e.setMinimum(0.0)
        self.SpinBox_e.setMaximum(5000.0)
        self.SpinBox_e.setSingleStep(10.0)
        self.SpinBox_e.setProperty("value", 2400.0)
        self.SpinBox_e.setObjectName("SpinBox_e")
        self.verticalLayout.addWidget(self.SpinBox_e)
        self.slider_e = QtWidgets.QSlider(self.dockWidgetContents_3)
        self.slider_e.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.slider_e.setMaximum(5000)
        self.slider_e.setSingleStep(10)
        self.slider_e.setPageStep(10)
        self.slider_e.setProperty("value", 2400)
        self.slider_e.setOrientation(QtCore.Qt.Horizontal)
        self.slider_e.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.slider_e.setTickInterval(500)
        self.slider_e.setObjectName("slider_e")
        self.verticalLayout.addWidget(self.slider_e)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem3)
        self.label_a = QtWidgets.QLabel(self.dockWidgetContents_3)
        self.label_a.setObjectName("label_a")
        self.verticalLayout.addWidget(self.label_a)
        self.SpinBox_a = QtWidgets.QDoubleSpinBox(self.dockWidgetContents_3)
        self.SpinBox_a.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.SpinBox_a.setDecimals(1)
        self.SpinBox_a.setMinimum(0.1)
        self.SpinBox_a.setSingleStep(1.0)
        self.SpinBox_a.setProperty("value", 15.0)
        self.SpinBox_a.setObjectName("SpinBox_a")
        self.verticalLayout.addWidget(self.SpinBox_a)
        self.slider_a = QtWidgets.QSlider(self.dockWidgetContents_3)
        self.slider_a.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.slider_a.setMinimum(1)
        self.slider_a.setMaximum(100)
        self.slider_a.setProperty("value", 15)
        self.slider_a.setOrientation(QtCore.Qt.Horizontal)
        self.slider_a.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.slider_a.setTickInterval(10)
        self.slider_a.setObjectName("slider_a")
        self.verticalLayout.addWidget(self.slider_a)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem4)
        self.label_f2 = QtWidgets.QLabel(self.dockWidgetContents_3)
        self.label_f2.setObjectName("label_f2")
        self.verticalLayout.addWidget(self.label_f2)
        self.SpinBox_f2 = QtWidgets.QDoubleSpinBox(self.dockWidgetContents_3)
        self.SpinBox_f2.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.SpinBox_f2.setDecimals(1)
        self.SpinBox_f2.setMinimum(0.1)
        self.SpinBox_f2.setMaximum(50.0)
        self.SpinBox_f2.setProperty("value", 1.0)
        self.SpinBox_f2.setObjectName("SpinBox_f2")
        self.verticalLayout.addWidget(self.SpinBox_f2)
        self.slider_f2 = QtWidgets.QSlider(self.dockWidgetContents_3)
        self.slider_f2.setMinimum(1)
        self.slider_f2.setMaximum(50)
        self.slider_f2.setProperty("value", 1)
        self.slider_f2.setOrientation(QtCore.Qt.Horizontal)
        self.slider_f2.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.slider_f2.setTickInterval(5)
        self.slider_f2.setObjectName("slider_f2")
        self.verticalLayout.addWidget(self.slider_f2)
        self.horizontalLayout_4.addLayout(self.verticalLayout)
        self.dockWidget.setWidget(self.dockWidgetContents_3)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(1), self.dockWidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Diffraction - Fraunhofer"))
        self.dockWidget.setWindowTitle(_translate("MainWindow", "Setting"))
        self.label_lamda.setText(_translate("MainWindow", "Wavelength(nm)"))
        self.SpinBox_lambda.setStatusTip(_translate("MainWindow", "Change the wave length of monochromatic light"))
        self.slider_lambda.setStatusTip(_translate("MainWindow", "Change the wave length of monochromatic light"))
        self.label.setText(_translate("MainWindow", "n"))
        self.label_b.setText(_translate("MainWindow", "<html><head/><body><p>b(&mu;m)</p></body></html>"))
        self.SpinBox_b.setStatusTip(_translate("MainWindow", "Change the width of the rectangular aperture"))
        self.slider_b.setStatusTip(_translate("MainWindow", "Change the width of the rectangular aperture"))
        self.label_e.setText(_translate("MainWindow", "<html><head/><body><p>a (&mu;m)</p></body></html>"))
        self.label_a.setText(_translate("MainWindow", "Screen(mm)"))
        self.SpinBox_a.setStatusTip(_translate("MainWindow", "Change the side of the square-shaped screen"))
        self.slider_a.setStatusTip(_translate("MainWindow", "Change the side of the square-shaped screen"))
        self.label_f2.setText(_translate("MainWindow", "f2(m)"))
        self.SpinBox_f2.setStatusTip(_translate("MainWindow", "Change the focal length f2 of the lens L2"))
        self.slider_f2.setStatusTip(_translate("MainWindow", "Change the focal length f2 of the lens L2"))



from mplwidget import MPL_WIDGET_2D

if __name__ == "__main__":

    app = QApplication(sys.argv)
    MyApplication = NSlit2D()
    MyApplication.show()
    sys.exit(app.exec_())

