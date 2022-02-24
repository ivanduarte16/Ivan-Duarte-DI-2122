# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'login.ui'
##
## Created by: Qt User Interface Compiler version 6.2.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QMainWindow,
    QPushButton, QSizePolicy, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(385, 428)
        MainWindow.setMinimumSize(QSize(385, 428))
        MainWindow.setStyleSheet(u"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setMinimumSize(QSize(385, 428))
        self.centralwidget.setMaximumSize(QSize(385, 428))
        self.username = QLineEdit(self.centralwidget)
        self.username.setObjectName(u"username")
        self.username.setGeometry(QRect(80, 120, 221, 41))
        font = QFont()
        font.setFamilies([u"CaskaydiaCove Nerd Font"])
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(True)
        self.username.setFont(font)
        self.username.setStyleSheet(u"")
        self.username.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.password = QLineEdit(self.centralwidget)
        self.password.setObjectName(u"password")
        self.password.setGeometry(QRect(80, 210, 221, 41))
        self.password.setStyleSheet(u"")
        self.password.setEchoMode(QLineEdit.Password)
        self.btn_login = QPushButton(self.centralwidget)
        self.btn_login.setObjectName(u"btn_login")
        self.btn_login.setGeometry(QRect(80, 300, 221, 41))
        self.btn_login.setStyleSheet(u"")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(120, 40, 141, 41))
        font1 = QFont()
        font1.setPointSize(16)
        font1.setBold(False)
        font1.setItalic(True)
        self.label.setFont(font1)
        self.label.setStyleSheet(u"")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.username.setText("")
        self.username.setPlaceholderText(QCoreApplication.translate("MainWindow", u"    username", None))
        self.password.setText("")
        self.password.setPlaceholderText(QCoreApplication.translate("MainWindow", u"     password", None))
        self.btn_login.setText(QCoreApplication.translate("MainWindow", u"LOGIN", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"BIENVENIDO", None))
    # retranslateUi

