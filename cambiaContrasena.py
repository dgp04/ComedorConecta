# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'cambiaContrasena.ui'
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
    QLabel, QLineEdit, QPushButton, QSizePolicy, QMessageBox,
    QVBoxLayout, QWidget)
from src.resources import *
from Connector.ConnectorUsuarios import *
import bcrypt

class Ui_Dialog_cambiaContrasena(QDialog, object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(570, 399)
        Dialog.setFixedSize(570, 399)
        
        icon = QIcon()
        icon.addFile(u":/logo/iconoProyecto.png", QSize(), QIcon.Normal, QIcon.Off)
        Dialog.setWindowIcon(icon)
        self.verticalLayout_2 = QVBoxLayout(Dialog)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
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

        self.verticalLayout.addWidget(self.logo)

        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setHorizontalSpacing(15)
        self.formLayout.setVerticalSpacing(0)
        self.formLayout.setContentsMargins(90, -1, -1, -1)
        self.label_email = QLabel(Dialog)
        self.label_email.setObjectName(u"label_email")
        self.label_email.setMaximumSize(QSize(178, 16777215))
        font = QFont()
        font.setPointSize(13)
        font.setBold(True)
        self.label_email.setFont(font)
        self.label_email.setStyleSheet(u"QLabel{\n"
"color: white;\n"
"font-weight: bold;\n"
"background-color: #2a5c94;\n"
"border: 1px solid black;\n"
"padding: 5px 10px;\n"
"}")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label_email)

        self.lineEdit_email = QLineEdit(Dialog)
        self.lineEdit_email.setObjectName(u"lineEdit_email")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.lineEdit_email.sizePolicy().hasHeightForWidth())
        self.lineEdit_email.setSizePolicy(sizePolicy1)
        self.lineEdit_email.setMaximumSize(QSize(200, 16777215))
        self.lineEdit_email.setStyleSheet(u"QLineEdit{\n"
"border: 0px;\n"
"border-bottom: 1px solid black;\n"
"background-color: transparent;\n"
"margin-top: 10px;\n"
"}")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.lineEdit_email)

        self.label_nueva_contrasena = QLabel(Dialog)
        self.label_nueva_contrasena.setObjectName(u"label_nueva_contrasena")
        self.label_nueva_contrasena.setMaximumSize(QSize(178, 16777215))
        self.label_nueva_contrasena.setFont(font)
        self.label_nueva_contrasena.setStyleSheet(u"QLabel{\n"
"color: white;\n"
"font-weight: bold;\n"
"background-color: #2a5c94;\n"
"border: 1px solid black;\n"
"border-top: none;\n"
"padding: 5px 10px;\n"
"}")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_nueva_contrasena)

        self.lineEdit_nueva_contrasena = QLineEdit(Dialog)
        self.lineEdit_nueva_contrasena.setEchoMode(QLineEdit.Password)
        self.lineEdit_nueva_contrasena.setObjectName(u"lineEdit_nueva_contrasena")
        self.lineEdit_nueva_contrasena.setMaximumSize(QSize(200, 16777215))
        self.lineEdit_nueva_contrasena.setStyleSheet(u"QLineEdit{\n"
"border: 0px;\n"
"border-bottom: 1px solid black;\n"
"background-color: transparent;\n"
"margin-top: 10px;\n"
"}")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.lineEdit_nueva_contrasena)

        self.label_repite_contrasena = QLabel(Dialog)
        self.label_repite_contrasena.setObjectName(u"label_repite_contrasena")
        self.label_repite_contrasena.setMaximumSize(QSize(178, 16777215))
        self.label_repite_contrasena.setFont(font)
        self.label_repite_contrasena.setStyleSheet(u"QLabel{\n"
"color: white;\n"
"font-weight: bold;\n"
"background-color: #2a5c94;\n"
"border: 1px solid black;\n"
"border-top: none;\n"
"padding: 5px 10px;\n"
"}")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_repite_contrasena)

        self.lineEdit_repite_contrasena = QLineEdit(Dialog)
        self.lineEdit_repite_contrasena.setEchoMode(QLineEdit.Password)
        self.lineEdit_repite_contrasena.setObjectName(u"lineEdit_repite_contrasena")
        self.lineEdit_repite_contrasena.setMaximumSize(QSize(200, 16777215))
        self.lineEdit_repite_contrasena.setStyleSheet(u"QLineEdit{\n"
"border: 0px;\n"
"border-bottom: 1px solid black;\n"
"background-color: transparent;\n"
"margin-top: 10px;\n"
"}")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.lineEdit_repite_contrasena)


        self.verticalLayout.addLayout(self.formLayout)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(-1, 7, -1, -1)
        self.btn_cambiar_contrasena = QPushButton(Dialog)
        self.btn_cambiar_contrasena.clicked.connect(self.cambiar_contrasena)
        self.btn_cambiar_contrasena.setObjectName(u"btn_cambiar_contrasena")
        self.btn_cambiar_contrasena.setFont(font)
        self.btn_cambiar_contrasena.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_cambiar_contrasena.setStyleSheet(u"QPushButton{\n"
"background-color: #2a5c94;\n"
"color: white;\n"
"border: 1px solid black;\n"
"border-radius: 10px;\n"
"padding: 5px 35px 5px 35px;\n"
"font-weight: bold;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(11, 5, 71)\n"
"}")

        self.horizontalLayout.addWidget(self.btn_cambiar_contrasena)

        self.btn_reiniciar = QPushButton(Dialog)
        self.btn_reiniciar.clicked.connect(self.reiniciar)
        self.btn_reiniciar.setObjectName(u"btn_reiniciar")
        self.btn_reiniciar.setFont(font)
        self.btn_reiniciar.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_reiniciar.setStyleSheet(u"QPushButton{\n"
"background-color: #2a5c94;\n"
"color: white;\n"
"border: 1px solid black;\n"
"border-radius: 10px;\n"
"padding: 5px 35px 5px 35px;\n"
"font-weight: bold;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(11, 5, 71)\n"
"}")

        self.horizontalLayout.addWidget(self.btn_reiniciar)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.verticalLayout_2.addLayout(self.verticalLayout)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Cambiar contrase\u00f1a", None))
        self.logo.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><img src=\":/logo/logoProyecto.png\"/></p></body></html>", None))
        self.label_email.setText(QCoreApplication.translate("Dialog", u"Correo electr\u00f3nico:                ", None))
        self.lineEdit_email.setPlaceholderText(QCoreApplication.translate("Dialog", u"Introduzca su correo electr\u00f3nico...", None))
        self.label_nueva_contrasena.setText(QCoreApplication.translate("Dialog", u"Nueva contrase\u00f1a:                  ", None))
        self.lineEdit_nueva_contrasena.setPlaceholderText(QCoreApplication.translate("Dialog", u"Introduzca la nueva contrase\u00f1a...", None))
        self.label_repite_contrasena.setText(QCoreApplication.translate("Dialog", u"Repita contrase\u00f1a:", None))
        self.lineEdit_repite_contrasena.setPlaceholderText(QCoreApplication.translate("Dialog", u"Repita la nueva contrase\u00f1a...", None))
        self.btn_cambiar_contrasena.setText(QCoreApplication.translate("Dialog", u"Cambiar contrase\u00f1a", None))
        self.btn_reiniciar.setText(QCoreApplication.translate("Dialog", u"Reiniciar", None))
    # retranslateUi

    def cambiar_contrasena(self):
        email = self.lineEdit_email.text()
        
        nueva_contrasena = self.lineEdit_nueva_contrasena.text()
        hashed_nueva_contrasena = bcrypt.hashpw(nueva_contrasena.encode('utf-8'), bcrypt.gensalt())
        hashed_nueva_contrasena = hashed_nueva_contrasena.decode('utf-8')
        
        confirma_contrasena = self.lineEdit_repite_contrasena.text()
        hashed_repite_contrasena = bcrypt.hashpw(confirma_contrasena.encode('utf-8'), bcrypt.gensalt())
        hashed_repite_contrasena = hashed_repite_contrasena.decode('utf-8')
        
        conector = ConnectorUsuarios()
        
        if confirma_contrasena != nueva_contrasena:
            QMessageBox.warning(self, 'Error', 'Las contraseñas no coinciden. Por favor, introduzca en ambos campos la misma contraseña.')
        else:
            usuario = conector.devuelvePorCorreo(email)
            user_id, nombre, email_usuario, contrasena_usuario, centro, telefono = usuario 
            
            if usuario is None:
                QMessageBox.critical(self, 'Error', 'Usuario no registrado en la base de datos.')
                self.reiniciar()
            elif bcrypt.checkpw(nueva_contrasena.encode('utf-8'), contrasena_usuario.encode('utf-8')) == True:
                QMessageBox.warning(self, 'Error', 'La nueva contraseña debe ser diferente a la anterior')
            else:
                print(bcrypt.checkpw(hashed_repite_contrasena.encode('utf-8'), contrasena_usuario.encode('utf-8')))
                conector.cambiaContrasena(hashed_nueva_contrasena, email)
                QMessageBox.information(self, 'Éxito', 'La contraseña se ha cambiado correctamente.')
                self.close()
    
    def reiniciar(self):
        self.lineEdit_email.clear()
        self.lineEdit_nueva_contrasena.clear()
        self.lineEdit_repite_contrasena.clear()
        self.lineEdit_email.setFocus()