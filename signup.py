# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'signup.ui'
##
## Created by: Qt User Interface Compiler version 6.6.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt, Signal)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform, QDoubleValidator)
from PySide6.QtWidgets import (QApplication, QDialog, QFormLayout, QHBoxLayout,
    QLabel, QLayout, QLineEdit, QPushButton,
    QSizePolicy, QVBoxLayout, QWidget, QMessageBox)
from src.resources import *
from Connector.ConnectorUsuarios import *
import bcrypt

class DialogSignup(QDialog, object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(572, 444)
        
        double_validator = QDoubleValidator(self)
        double_validator.setDecimals(2)
        
        icon = QIcon()
        icon.addFile(u":/logo/iconoProyecto.png", QSize(), QIcon.Normal, QIcon.Off)
        Dialog.setWindowIcon(icon)
        self.verticalLayout_3 = QVBoxLayout(Dialog)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.logo = QLabel(Dialog)
        self.logo.setObjectName(u"logo")
        sizePolicy = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.logo.sizePolicy().hasHeightForWidth())
        self.logo.setSizePolicy(sizePolicy)
        self.logo.setMinimumSize(QSize(550, 100))
        self.logo.setMaximumSize(QSize(200, 250))
        self.logo.setStyleSheet(u"")
        self.logo.setScaledContents(True)
        self.logo.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.logo)


        self.verticalLayout.addLayout(self.verticalLayout_2)

        self.formLayout_3 = QFormLayout()
        self.formLayout_3.setObjectName(u"formLayout_3")
        self.formLayout_3.setContentsMargins(160, -1, -1, -1)
        self.label_username = QLabel(Dialog)
        self.label_username.setObjectName(u"label_username")
        font = QFont()
        font.setPointSize(13)
        self.label_username.setFont(font)

        self.formLayout_3.setWidget(0, QFormLayout.LabelRole, self.label_username)

        self.lineEdit_username = QLineEdit(Dialog)
        self.lineEdit_username.setObjectName(u"lineEdit_username")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.lineEdit_username.sizePolicy().hasHeightForWidth())
        self.lineEdit_username.setSizePolicy(sizePolicy1)
        self.lineEdit_username.setMaximumSize(QSize(200, 16777215))
        self.lineEdit_username.setStyleSheet(u"QLineEdit{\n"
"border: 0px;\n"
"border-bottom: 1px solid black;\n"
"background-color: transparent;\n"
"}")

        self.formLayout_3.setWidget(0, QFormLayout.FieldRole, self.lineEdit_username)

        self.label_email = QLabel(Dialog)
        self.label_email.setObjectName(u"label_email")
        font1 = QFont()
        font1.setPointSize(14)
        self.label_email.setFont(font1)

        self.formLayout_3.setWidget(1, QFormLayout.LabelRole, self.label_email)

        self.lineEdit_email = QLineEdit(Dialog)
        self.lineEdit_email.setObjectName(u"lineEdit_email")
        sizePolicy1.setHeightForWidth(self.lineEdit_email.sizePolicy().hasHeightForWidth())
        self.lineEdit_email.setSizePolicy(sizePolicy1)
        self.lineEdit_email.setMaximumSize(QSize(200, 16777215))
        self.lineEdit_email.setStyleSheet(u"QLineEdit{\n"
"border: 0px;\n"
"border-bottom: 1px solid black;\n"
"background-color: transparent;\n"
"}")

        self.formLayout_3.setWidget(1, QFormLayout.FieldRole, self.lineEdit_email)

        self.label_passwd = QLabel(Dialog)
        self.label_passwd.setObjectName(u"label_passwd")
        self.label_passwd.setFont(font)

        self.formLayout_3.setWidget(2, QFormLayout.LabelRole, self.label_passwd)

        self.lineEdit_passwd = QLineEdit(Dialog)
        self.lineEdit_passwd.setObjectName(u"lineEdit_passwd")
        sizePolicy1.setHeightForWidth(self.lineEdit_passwd.sizePolicy().hasHeightForWidth())
        self.lineEdit_passwd.setSizePolicy(sizePolicy1)
        self.lineEdit_passwd.setMaximumSize(QSize(200, 16777215))
        self.lineEdit_passwd.setStyleSheet(u"QLineEdit{\n"
"border: 0px;\n"
"border-bottom: 1px solid black;\n"
"background-color: transparent;\n"
"}")
        self.lineEdit_passwd.setEchoMode(QLineEdit.Password)

        self.formLayout_3.setWidget(2, QFormLayout.FieldRole, self.lineEdit_passwd)

        self.label_centro = QLabel(Dialog)
        self.label_centro.setObjectName(u"label_centro")
        font2 = QFont()
        font2.setPointSize(12)
        self.label_centro.setFont(font2)

        self.formLayout_3.setWidget(3, QFormLayout.LabelRole, self.label_centro)

        self.lineEdit_centro = QLineEdit(Dialog)
        self.lineEdit_centro.setObjectName(u"lineEdit_centro")
        self.lineEdit_centro.setMaximumSize(QSize(200, 16777215))
        self.lineEdit_centro.setStyleSheet(u"QLineEdit{\n"
"border: 0px;\n"
"border-bottom: 1px solid black;\n"
"background-color: transparent;\n"
"}")

        self.formLayout_3.setWidget(3, QFormLayout.FieldRole, self.lineEdit_centro)

        self.label_telefono = QLabel(Dialog)
        self.label_telefono.setObjectName(u"label_telefono")
        self.label_telefono.setFont(font1)

        self.formLayout_3.setWidget(4, QFormLayout.LabelRole, self.label_telefono)

        self.lineEdit_telefono = QLineEdit(Dialog)
        self.lineEdit_telefono.setObjectName(u"lineEdit_telefono")
        self.lineEdit_telefono.setMaximumSize(QSize(200, 16777215))
        self.lineEdit_telefono.setValidator(double_validator)
        self.lineEdit_telefono.setStyleSheet(u"QLineEdit{\n"
"border: 0px;\n"
"border-bottom: 1px solid black;\n"
"background-color: transparent;\n"
"}")

        self.formLayout_3.setWidget(4, QFormLayout.FieldRole, self.lineEdit_telefono)


        self.verticalLayout.addLayout(self.formLayout_3)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.btn_signup = QPushButton(Dialog)
        self.btn_signup.setObjectName(u"btn_signup")
        sizePolicy1.setHeightForWidth(self.btn_signup.sizePolicy().hasHeightForWidth())
        self.btn_signup.setSizePolicy(sizePolicy1)
        font3 = QFont()
        font3.setPointSize(15)
        self.btn_signup.setFont(font3)
        self.btn_signup.clicked.connect(self.altaUsuario)
        self.btn_signup.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_signup.setStyleSheet(u"QPushButton{\n"
"background-color: #2a5c94;\n"
"color: white;\n"
"border-radius: 10px;\n"
"padding: 5px 35px 5px 35px;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(62, 62, 255)\n"
"}")

        self.horizontalLayout.addWidget(self.btn_signup)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.verticalLayout_3.addLayout(self.verticalLayout)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Sign up", None))
        self.logo.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><img src=\":/logo/logoProyecto.png\"/></p></body></html>", None))
        self.label_username.setText(QCoreApplication.translate("Dialog", u"Username* :", None))
        self.lineEdit_username.setPlaceholderText(QCoreApplication.translate("Dialog", u"Introduzca su nombre de usuario...", None))
        self.label_email.setText(QCoreApplication.translate("Dialog", u"Email* :", None))
        self.lineEdit_email.setPlaceholderText(QCoreApplication.translate("Dialog", u"Introduzca su correo electr\u00f3nico...", None))
        self.label_passwd.setText(QCoreApplication.translate("Dialog", u"Password* :", None))
        self.lineEdit_passwd.setPlaceholderText(QCoreApplication.translate("Dialog", u"Introduzca su contrase\u00f1a...", None))
        self.label_centro.setText(QCoreApplication.translate("Dialog", u"Centro educativo* :", None))
        self.lineEdit_centro.setPlaceholderText(QCoreApplication.translate("Dialog", u"Introduzca el nombre de su centro...", None))
        self.label_telefono.setText(QCoreApplication.translate("Dialog", u"N\u00ba tel\u00e9fono:", None))
        self.lineEdit_telefono.setPlaceholderText(QCoreApplication.translate("Dialog", u"Introduzca su n\u00ba de tel\u00e9fono...", None))
        self.btn_signup.setText(QCoreApplication.translate("Dialog", u"Sign up", None))
    # retranslateUi

    def altaUsuario(self):
        username = self.lineEdit_username.text()
        email = self.lineEdit_email.text()
        password = self.lineEdit_passwd.text()
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
        hashed_password = hashed_password.decode('utf-8')
        centro = self.lineEdit_centro.text()
        telefono = self.lineEdit_telefono.text()
        
        try:
            conector = ConnectorUsuarios()
            usuario = conector.devuelvePorUsuario(username)
            
            if usuario is not None:
                QMessageBox.critical(self, 'Error', 'Nombre de usuario no válido. Ya hay un usuario con ese nombre registrado.')
                self.reiniciar()
            elif '@' not in email or not (email.endswith('.com') or email.endswith('.es')):
                QMessageBox.warning(self, 'Error', 'Correo electrónico introducido no válido.')
                self.reiniciar()
            else: 
                conector.insertar(username, email, hashed_password, centro, telefono)
                QMessageBox.information(self.btn_signup, "Éxito", "Usuario creado con éxito.")
                self.accept()

        except Exception as e:
            QMessageBox.critical(self.btn_signup, "Error", f"Error al insertar datos en la base de datos: {str(e)}")
    
    def reiniciar(self):
        self.lineEdit_username.clear()
        self.lineEdit_email.clear()
        self.lineEdit_passwd.clear()
        self.lineEdit_centro.clear()
        self.lineEdit_telefono.clear()
        self.lineEdit_username.setFocus()