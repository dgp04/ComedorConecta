# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ajustesUsuario.ui'
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
    QLabel, QLayout, QLineEdit, QPushButton, QMessageBox,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)
from src.resources import *
from cambiaContrasena import *
from Connector.ConnectorUsuarios import *
import json

class Ui_Dialog_ajustes(QDialog, object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(639, 481)
        Dialog.setFixedSize(639, 481)
        
        with open('config.json', 'r', encoding='utf-8')as json_file:
            data = json.load(json_file)
        
        self.nombre_usuario = data['usuario']
        self.id_usuario = data['id_usuario']
        self.curso = data['curso']
        
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
        self.verticalLayout_2.setContentsMargins(20, -1, -1, -1)
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
        self.formLayout_3.setVerticalSpacing(0)
        self.formLayout_3.setContentsMargins(160, -1, -1, -1)
        self.label_usuario = QLabel(Dialog)
        self.label_usuario.setObjectName(u"label_usuario")
        self.label_usuario.setMinimumSize(QSize(102, 0))
        self.label_usuario.setMaximumSize(QSize(150, 16777215))
        font = QFont()
        font.setPointSize(13)
        font.setBold(True)
        self.label_usuario.setFont(font)
        self.label_usuario.setStyleSheet(u"QLabel{\n"
"color: white;\n"
"font-weight: bold;\n"
"background-color: #2a5c94;\n"
"border: 1px solid black;\n"
"padding: 5px 10px;\n"
"}")

        self.formLayout_3.setWidget(0, QFormLayout.LabelRole, self.label_usuario)

        self.lineEdit_usuario = QLineEdit(Dialog)
        self.lineEdit_usuario.setObjectName(u"lineEdit_usuario")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.lineEdit_usuario.sizePolicy().hasHeightForWidth())
        self.lineEdit_usuario.setSizePolicy(sizePolicy1)
        self.lineEdit_usuario.setMaximumSize(QSize(200, 16777215))
        self.lineEdit_usuario.setStyleSheet(u"QLineEdit{\n"
"border: 0px;\n"
"border-bottom: 1px solid black;\n"
"background-color: transparent;\n"
"margin-top: 10px;\n"
"}")

        self.formLayout_3.setWidget(0, QFormLayout.FieldRole, self.lineEdit_usuario)

        self.label_email = QLabel(Dialog)
        self.label_email.setObjectName(u"label_email")
        self.label_email.setMinimumSize(QSize(102, 0))
        self.label_email.setMaximumSize(QSize(102, 16777215))
        self.label_email.setFont(font)
        self.label_email.setStyleSheet(u"QLabel{\n"
"color: white;\n"
"font-weight: bold;\n"
"background-color: #2a5c94;\n"
"border: 1px solid black;\n"
"border-top: none;\n"
"padding: 5px 10px;\n"
"margin-top: 0px;\n"
"}")

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
"margin-top: 10px;\n"
"}")

        self.formLayout_3.setWidget(1, QFormLayout.FieldRole, self.lineEdit_email)

        self.label_centro = QLabel(Dialog)
        self.label_centro.setObjectName(u"label_centro")
        self.label_centro.setMinimumSize(QSize(102, 0))
        self.label_centro.setMaximumSize(QSize(102, 16777215))
        self.label_centro.setFont(font)
        self.label_centro.setStyleSheet(u"QLabel{\n"
"color: white;\n"
"font-weight: bold;\n"
"background-color: #2a5c94;\n"
"border: 1px solid black;\n"
"border-top: none;\n"
"padding: 5px 10px;\n"
"margin-top: 0px;\n"
"}")

        self.formLayout_3.setWidget(2, QFormLayout.LabelRole, self.label_centro)

        self.lineEdit_centro = QLineEdit(Dialog)
        self.lineEdit_centro.setObjectName(u"lineEdit_centro")
        sizePolicy1.setHeightForWidth(self.lineEdit_centro.sizePolicy().hasHeightForWidth())
        self.lineEdit_centro.setSizePolicy(sizePolicy1)
        self.lineEdit_centro.setMaximumSize(QSize(200, 16777215))
        self.lineEdit_centro.setStyleSheet(u"QLineEdit{\n"
"border: 0px;\n"
"border-bottom: 1px solid black;\n"
"background-color: transparent;\n"
"margin-top: 10px;\n"
"}")

        self.formLayout_3.setWidget(2, QFormLayout.FieldRole, self.lineEdit_centro)

        self.label_telefono = QLabel(Dialog)
        self.label_telefono.setObjectName(u"label_telefono")
        self.label_telefono.setMaximumSize(QSize(102, 16777215))
        self.label_telefono.setFont(font)
        self.label_telefono.setStyleSheet(u"QLabel{\n"
"color: white;\n"
"font-weight: bold;\n"
"background-color: #2a5c94;\n"
"border: 1px solid black;\n"
"border-top: none;\n"
"padding: 5px 10px;\n"
"margin-top: 0px;\n"
"}")

        self.formLayout_3.setWidget(3, QFormLayout.LabelRole, self.label_telefono)

        self.lineEdit_telefono = QLineEdit(Dialog)
        self.lineEdit_telefono.setObjectName(u"lineEdit_telefono")
        self.lineEdit_telefono.setMaximumSize(QSize(200, 16777215))
        self.lineEdit_telefono.setStyleSheet(u"QLineEdit{\n"
"border: 0px;\n"
"border-bottom: 1px solid black;\n"
"background-color: transparent;\n"
"margin-top: 10px;\n"
"}")

        self.formLayout_3.setWidget(3, QFormLayout.FieldRole, self.lineEdit_telefono)


        self.verticalLayout.addLayout(self.formLayout_3)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(160, -1, -1, -1)
        self.horizontalSpacer_2 = QSpacerItem(30, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)

        self.label_cambia_contrasena = QLabel(Dialog)
        self.label_cambia_contrasena.setObjectName(u"label_cambia_contrasena")

        self.horizontalLayout_3.addWidget(self.label_cambia_contrasena)

        self.btn_cambia_contrasena = QPushButton(Dialog)
        self.btn_cambia_contrasena.clicked.connect(self.abrir_cambia_contrasena)
        self.btn_cambia_contrasena.setObjectName(u"btn_cambia_contrasena")
        sizePolicy1.setHeightForWidth(self.btn_cambia_contrasena.sizePolicy().hasHeightForWidth())
        self.btn_cambia_contrasena.setSizePolicy(sizePolicy1)
        self.btn_cambia_contrasena.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_cambia_contrasena.setStyleSheet(u"QPushButton{\n"
"background-color: transparent;\n"
"border: 0;\n"
"color: blue;\n"
"}\n"
"QPushButton:hover{\n"
"text-decoration: underline;\n"
"}")

        self.horizontalLayout_3.addWidget(self.btn_cambia_contrasena)

        self.horizontalSpacer = QSpacerItem(180, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(40, 6, -1, -1)
        self.btn_confirmar = QPushButton(Dialog)
        self.btn_confirmar.clicked.connect(self.actualiza_usuario)
        self.btn_confirmar.setObjectName(u"btn_confirmar")
        sizePolicy1.setHeightForWidth(self.btn_confirmar.sizePolicy().hasHeightForWidth())
        self.btn_confirmar.setSizePolicy(sizePolicy1)
        font1 = QFont()
        font1.setPointSize(15)
        font1.setBold(True)
        self.btn_confirmar.setFont(font1)
        self.btn_confirmar.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_confirmar.setStyleSheet(u"QPushButton{\n"
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

        self.horizontalLayout.addWidget(self.btn_confirmar)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.verticalLayout_3.addLayout(self.verticalLayout)

        self.reconoce_usuario()
        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Ajustes de usuario", None))
        self.logo.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><img src=\":/logo/logoProyecto.png\"/></p></body></html>", None))
        self.label_usuario.setText(QCoreApplication.translate("Dialog", u"Usuario:", None))
        self.lineEdit_usuario.setPlaceholderText(QCoreApplication.translate("Dialog", u"Introduzca su nombre de usuario...", None))
        self.label_email.setText(QCoreApplication.translate("Dialog", u"Email:", None))
        self.lineEdit_email.setPlaceholderText(QCoreApplication.translate("Dialog", u"Introduzca su correo electr\u00f3nico...", None))
        self.label_centro.setText(QCoreApplication.translate("Dialog", u"Centro:", None))
        self.lineEdit_centro.setPlaceholderText(QCoreApplication.translate("Dialog", u"Introduzca su centro lectivo...", None))
        self.label_telefono.setText(QCoreApplication.translate("Dialog", u"Tel\u00e9fono:", None))
        self.lineEdit_telefono.setPlaceholderText(QCoreApplication.translate("Dialog", u"Introduzca su n\u00famero de tel\u00e9fono...", None))
        self.label_cambia_contrasena.setText(QCoreApplication.translate("Dialog", u"\u00bfDesea cambiar su contrase\u00f1a?", None))
        self.btn_cambia_contrasena.setText(QCoreApplication.translate("Dialog", u"Cambiar contraseña", None))
        self.btn_confirmar.setText(QCoreApplication.translate("Dialog", u"Confirmar cambios", None))
    # retranslateUi

    def reconoce_usuario(self):
        nombre_usuario = self.nombre_usuario
        conector = ConnectorUsuarios()
        
        try:
            usuario = conector.devuelvePorUsuario(nombre_usuario)
            
            if usuario is not None:
                self.lineEdit_usuario.setText(nombre_usuario)
                self.lineEdit_email.setText(usuario[2])
                self.lineEdit_centro.setText(usuario[4])
                self.lineEdit_telefono.setText(usuario[5])
            else:
                QMessageBox.critical(self.btn_confirmar, 'Error', 'Se ha producido un error inesperado.')
        except Exception as e:
            QMessageBox.critical(self.btn_confirmar, 'Error', f'Se ha producido un error: {str(e)}')
            self.close()

    def actualiza_usuario(self):
        nuevo_nombre_usuario = self.lineEdit_usuario.text()
        nuevo_email = self.lineEdit_email.text()
        nuevo_centro = self.lineEdit_centro.text()
        nuevo_telefono = self.lineEdit_telefono.text()
        conector = ConnectorUsuarios()
        
        try:
            usuario = conector.devuelvePorUsuario(nuevo_nombre_usuario)
            
            id_usuario = self.id_usuario
            conector.actualizarUsuario(id_usuario, nuevo_nombre_usuario, nuevo_email, nuevo_centro, nuevo_telefono)
            QMessageBox.information(self.btn_confirmar, "Éxito", "Inforamción actualizada correctamente.")
                
            data = {"id_usuario": id_usuario, "usuario": nuevo_nombre_usuario, "curso": self.curso}
                
            with open('config.json', 'w', encoding='utf-8')as json_file:
                json.dump(data, json_file)
                
            self.accept()
        except Exception as e:
            QMessageBox.critical(self.btn_confirmar, "Error", f"Error al insertar datos en la base de datos: {str(e)}")
            print(e)
            
    def abrir_cambia_contrasena(self):
        self.ventana_cambia_contrasena = VentanaCambiaContrasena()
        self.ventana_cambia_contrasena.show()
        self.ventana_cambia_contrasena.exec_()

class VentanaCambiaContrasena(Ui_Dialog_cambiaContrasena, QDialog):
    def __init__(self):
        super(VentanaCambiaContrasena, self).__init__()
        self.setupUi(self)