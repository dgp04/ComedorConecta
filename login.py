# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'login.ui'
##
## Created by: Qt User Interface Compiler version 6.6.0
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
from PySide6.QtWidgets import (QApplication, QDialog, QFormLayout, QHBoxLayout,
    QLabel, QLayout, QLineEdit, QPushButton,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)
from signup import *
from cursos import *
from src.resources import *
from Connector.ConnectorUsuarios import *
import json
import bcrypt

class Ui_Dialog_login(QDialog, object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(572, 381)
        icon = QIcon()
        icon.addFile(u":/logo/iconoProyecto.png", QSize(), QIcon.Normal, QIcon.Off)
        Dialog.setWindowIcon(icon)
        self.verticalLayout_6 = QVBoxLayout(Dialog)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
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
        self.logo.setCursor(QCursor(Qt.ArrowCursor))
        self.logo.setStyleSheet(u"")
        self.logo.setScaledContents(False)
        self.logo.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.logo)


        self.verticalLayout.addLayout(self.verticalLayout_2)

        self.formLayout_3 = QFormLayout()
        self.formLayout_3.setObjectName(u"formLayout_3")
        self.formLayout_3.setContentsMargins(160, -1, -1, -1)
        self.label_user = QLabel(Dialog)
        self.label_user.setObjectName(u"label_user")
        font = QFont()
        font.setPointSize(13)
        self.label_user.setFont(font)

        self.formLayout_3.setWidget(0, QFormLayout.LabelRole, self.label_user)

        self.lineEdit_user = QLineEdit(Dialog)
        self.lineEdit_user.setObjectName(u"lineEdit_user")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.lineEdit_user.sizePolicy().hasHeightForWidth())
        self.lineEdit_user.setSizePolicy(sizePolicy1)
        self.lineEdit_user.setMaximumSize(QSize(200, 16777215))
        self.lineEdit_user.setStyleSheet(u"QLineEdit{\n"
"border: 0px;\n"
"border-bottom: 1px solid black;\n"
"background-color: transparent;\n"
"}")

        self.formLayout_3.setWidget(0, QFormLayout.FieldRole, self.lineEdit_user)

        self.label_passwd = QLabel(Dialog)
        self.label_passwd.setObjectName(u"label_passwd")
        self.label_passwd.setFont(font)

        self.formLayout_3.setWidget(1, QFormLayout.LabelRole, self.label_passwd)

        self.lineEdit_passwd = QLineEdit(Dialog)
        self.lineEdit_passwd.setObjectName(u"lineEdit_passwd")
        sizePolicy1.setHeightForWidth(self.lineEdit_passwd.sizePolicy().hasHeightForWidth())
        self.lineEdit_passwd.setSizePolicy(sizePolicy1)
        self.lineEdit_passwd.setMaximumSize(QSize(200, 16777215))
        self.lineEdit_passwd.returnPressed.connect(self.iniciarSesion)
        self.lineEdit_passwd.setStyleSheet(u"QLineEdit{\n"
"border: 0px;\n"
"border-bottom: 1px solid black;\n"
"background-color: transparent;\n"
"}")
        self.lineEdit_passwd.setEchoMode(QLineEdit.Password)

        self.formLayout_3.setWidget(1, QFormLayout.FieldRole, self.lineEdit_passwd)


        self.verticalLayout.addLayout(self.formLayout_3)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(160, -1, -1, -1)
        self.label_creaCuenta = QLabel(Dialog)
        self.label_creaCuenta.setObjectName(u"label_creaCuenta")

        self.horizontalLayout_3.addWidget(self.label_creaCuenta)

        self.pushButton_creaCuenta = QPushButton(Dialog)
        self.pushButton_creaCuenta.setObjectName(u"pushButton_creaCuenta")
        sizePolicy1.setHeightForWidth(self.pushButton_creaCuenta.sizePolicy().hasHeightForWidth())
        self.pushButton_creaCuenta.setSizePolicy(sizePolicy1)
        self.pushButton_creaCuenta.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_creaCuenta.clicked.connect(self.ventana_signup)
        self.pushButton_creaCuenta.setStyleSheet(u"QPushButton{\n"
"background-color: transparent;\n"
"border: 0;\n"
"color: blue;\n"
"}\n"
"QPushButton:hover{\n"
"text-decoration: underline;\n"
"}")

        self.horizontalLayout_3.addWidget(self.pushButton_creaCuenta)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.pushButton_login = QPushButton(Dialog)
        self.pushButton_login.setObjectName(u"pushButton_login")
        sizePolicy1.setHeightForWidth(self.pushButton_login.sizePolicy().hasHeightForWidth())
        self.pushButton_login.setSizePolicy(sizePolicy1)
        font1 = QFont()
        font1.setPointSize(15)
        self.pushButton_login.setFont(font1)
        self.pushButton_login.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_login.clicked.connect(self.iniciarSesion)
        self.pushButton_login.setStyleSheet(u"QPushButton{\n"
"background-color: #2a5c94;\n"
"color: white;\n"
"border-radius: 10px;\n"
"padding: 5px 35px 5px 35px;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(62, 62, 255)\n"
"}")

        self.horizontalLayout.addWidget(self.pushButton_login)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.verticalLayout_6.addLayout(self.verticalLayout)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Login", None))
        self.logo.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><img src=\":/logo/logoProyecto.png\"/></p></body></html>", None))
        self.label_user.setText(QCoreApplication.translate("Dialog", u"User:", None))
        self.lineEdit_user.setPlaceholderText(QCoreApplication.translate("Dialog", u"Introduzca su usuario o email...", None))
        self.label_passwd.setText(QCoreApplication.translate("Dialog", u"Password:", None))
        self.lineEdit_passwd.setPlaceholderText(QCoreApplication.translate("Dialog", u"Introduzca su contrase\u00f1a...", None))
        self.label_creaCuenta.setText(QCoreApplication.translate("Dialog", u"\u00bfA\u00fan no te has registrado?", None))
        self.pushButton_creaCuenta.setText(QCoreApplication.translate("Dialog", u"Crear cuenta", None))
        self.pushButton_login.setText(QCoreApplication.translate("Dialog", u"Log in", None))
    # retranslateUi

    def ventana_signup(self):
        self.hide()
        self.ventanaSignUp = VentanaSignUp()
        self.ventanaSignUp.show()
        self.ventanaSignUp.exec_()
        self.show()
    
    def iniciarSesion(self):
        # Obtener el nombre de usuario o correo electrónico y la contraseña ingresados por el usuario
        identificador = self.lineEdit_user.text()
        password = self.lineEdit_passwd.text()

        conector = ConnectorUsuarios()
        
        # Realizar la búsqueda en la base de datos
        usuario = conector.devuelvePorUsuario(identificador)
        
        if usuario is not None and bcrypt.checkpw(password.encode('utf-8'), usuario[3].encode('utf-8')):
            data = {"id_usuario": usuario[0], "usuario": usuario[1], "curso": ''}

            with open("config.json", "w", encoding='utf-8') as json_file:
                json.dump(data, json_file)
            
            # Si se encontró un usuario y la contraseña es correcta, mostrar un mensaje de éxito
            self.cursos = VentanaCursos()
            self.cursos.show()
            self.accept()
        else:
            # Si no se encontró el usuario o la contraseña es incorrecta, mostrar un mensaje de error
            QMessageBox.critical(self, "Error", "Nombre de usuario o contraseña incorrectos.")
    
class VentanaSignUp(DialogSignup, QDialog):
    def __init__(self):
        super(VentanaSignUp, self).__init__()
        self.setupUi(self)
        
class VentanaCursos(Ui_MainWindow_cursos, QMainWindow):
    def __init__(self):
        super(VentanaCursos, self).__init__()
        self.setupUi(self)