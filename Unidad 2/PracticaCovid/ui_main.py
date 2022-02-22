# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.2.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QLabel, QMainWindow,
    QMenu, QMenuBar, QPushButton, QSizePolicy,
    QWidget)

class Ui_buscar(object):
    def setupUi(self, buscar):
        if not buscar.objectName():
            buscar.setObjectName(u"buscar")
        buscar.resize(441, 332)
        font = QFont()
        font.setPointSize(11)
        buscar.setFont(font)
        buscar.setStyleSheet(u"")
        self.Menu = QAction(buscar)
        self.Menu.setObjectName(u"Menu")
        self.widget_principal = QWidget(buscar)
        self.widget_principal.setObjectName(u"widget_principal")
        self.widget_principal.setEnabled(True)
        self.pushButton = QPushButton(self.widget_principal)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(40, 250, 371, 41))
        font1 = QFont()
        font1.setFamilies([u"DejaVu Sans"])
        font1.setPointSize(10)
        self.pushButton.setFont(font1)
        self.pushButton.setStyleSheet(u"")
        self.label_region = QLabel(self.widget_principal)
        self.label_region.setObjectName(u"label_region")
        self.label_region.setEnabled(True)
        self.label_region.setGeometry(QRect(40, 90, 151, 31))
        self.label_region.setFont(font1)
        self.label_region.setLayoutDirection(Qt.LeftToRight)
        self.label_region.setStyleSheet(u"")
        self.comboBox_provincias = QComboBox(self.widget_principal)
        self.comboBox_provincias.setObjectName(u"comboBox_provincias")
        self.comboBox_provincias.setEnabled(True)
        self.comboBox_provincias.setGeometry(QRect(220, 90, 181, 31))
        self.comboBox_provincias.setFont(font1)
        self.comboBox_provincias.setStyleSheet(u"")
        self.label = QLabel(self.widget_principal)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(40, 20, 371, 31))
        self.label.setFont(font)
        self.label_2 = QLabel(self.widget_principal)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(40, 170, 151, 17))
        font2 = QFont()
        font2.setPointSize(10)
        self.label_2.setFont(font2)
        self.comboBox_datos = QComboBox(self.widget_principal)
        self.comboBox_datos.addItem("")
        self.comboBox_datos.addItem("")
        self.comboBox_datos.addItem("")
        self.comboBox_datos.addItem("")
        self.comboBox_datos.addItem("")
        self.comboBox_datos.addItem("")
        self.comboBox_datos.addItem("")
        self.comboBox_datos.addItem("")
        self.comboBox_datos.setObjectName(u"comboBox_datos")
        self.comboBox_datos.setGeometry(QRect(220, 160, 181, 31))
        self.comboBox_datos.setFont(font2)
        buscar.setCentralWidget(self.widget_principal)
        self.menubar = QMenuBar(buscar)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 441, 23))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        buscar.setMenuBar(self.menubar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menuFile.addSeparator()

        self.retranslateUi(buscar)

        QMetaObject.connectSlotsByName(buscar)
    # setupUi

    def retranslateUi(self, buscar):
        buscar.setWindowTitle(QCoreApplication.translate("buscar", u"MainWindow", None))
        self.Menu.setText(QCoreApplication.translate("buscar", u"Salir", None))
        self.pushButton.setText(QCoreApplication.translate("buscar", u"Generar Gr\u00e0fico", None))
        self.label_region.setText(QCoreApplication.translate("buscar", u"<html><head/><body><p><span style=\" color:#041c1e;\">Selecciona una ciudad</span></p></body></html>", None))
        self.label.setText(QCoreApplication.translate("buscar", u"<html><head/><body><p><span style=\" color:#041c1e;\">ESTADISTICAS COVID COMUNIDAD VALENCIANA</span></p></body></html>", None))
        self.label_2.setText(QCoreApplication.translate("buscar", u"Que desea mostar?", None))
        self.comboBox_datos.setItemText(0, QCoreApplication.translate("buscar", u"Casos PCR+", None))
        self.comboBox_datos.setItemText(1, QCoreApplication.translate("buscar", u"Incidencia acumulada PCR+14", None))
        self.comboBox_datos.setItemText(2, QCoreApplication.translate("buscar", u"Muertes", None))
        self.comboBox_datos.setItemText(3, QCoreApplication.translate("buscar", u"Taxa de defunci\u00f3", None))
        self.comboBox_datos.setItemText(4, QCoreApplication.translate("buscar", u"Incidencia acumulada PCR+", None))
        self.comboBox_datos.setItemText(5, QCoreApplication.translate("buscar", u"Casos PCR+ 14 dies", None))
        self.comboBox_datos.setItemText(6, "")
        self.comboBox_datos.setItemText(7, "")

        self.menuFile.setTitle(QCoreApplication.translate("buscar", u"Menu", None))
    # retranslateUi

