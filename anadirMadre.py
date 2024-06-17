# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'anadirMadre.ui'
##
## Created by: Qt User Interface Compiler version 6.6.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon, QDoubleValidator,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDialog, QFormLayout, QHBoxLayout, QMessageBox,
    QLabel, QLayout, QLineEdit, QPushButton,
    QSizePolicy, QVBoxLayout, QWidget)
from src.resources import *
from Connector.MadreConnector import *
from Connector.AlumnoConnector import *
from anadir import *

class Ui_Dialog_anadir_padres(QDialog, object):
    def setupUi(self, Dialog_anadir_padres):
        if not Dialog_anadir_padres.objectName():
            Dialog_anadir_padres.setObjectName(u"Dialog_anadir_padres")
        Dialog_anadir_padres.resize(572, 446)
        icon = QIcon()
        icon.addFile(u":/logo/iconoProyecto.png", QSize(), QIcon.Normal, QIcon.Off)
        Dialog_anadir_padres.setWindowIcon(icon)
        
        double_validator = QDoubleValidator(self)
        double_validator.setDecimals(2)
        
        self.verticalLayout_3 = QVBoxLayout(Dialog_anadir_padres)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.logo = QLabel(Dialog_anadir_padres)
        self.logo.setObjectName(u"logo")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Maximum)
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
        self.formLayout_3.setContentsMargins(110, -1, -1, -1)
        self.label_nombre = QLabel(Dialog_anadir_padres)
        self.label_nombre.setObjectName(u"label_nombre")
        self.label_nombre.setMaximumSize(QSize(130, 16777215))
        font = QFont()
        font.setPointSize(13)
        font.setBold(True)
        self.label_nombre.setFont(font)
        self.label_nombre.setStyleSheet(u"QLabel{\n"
"color: white;\n"
"font-weight: bold;\n"
"background-color: #2a5c94;\n"
"border: 1px solid black;\n"
"padding: 5px 10px;\n"
"}")

        self.formLayout_3.setWidget(0, QFormLayout.LabelRole, self.label_nombre)

        self.lineEdit_nombre = QLineEdit(Dialog_anadir_padres)
        self.lineEdit_nombre.setObjectName(u"lineEdit_nombre")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.lineEdit_nombre.sizePolicy().hasHeightForWidth())
        self.lineEdit_nombre.setSizePolicy(sizePolicy1)
        self.lineEdit_nombre.setMaximumSize(QSize(200, 16777215))
        self.lineEdit_nombre.setCursor(QCursor(Qt.IBeamCursor))
        self.lineEdit_nombre.setStyleSheet(u"QLineEdit{\n"
"border: 0px;\n"
"border-bottom: 1px solid black;\n"
"background-color: transparent;\n"
"margin-top: 10px;\n"
"}")

        self.formLayout_3.setWidget(0, QFormLayout.FieldRole, self.lineEdit_nombre)

        self.label_nre = QLabel(Dialog_anadir_padres)
        self.label_nre.setObjectName(u"label_nre")
        self.label_nre.setMaximumSize(QSize(130, 16777215))
        self.label_nre.setFont(font)
        self.label_nre.setStyleSheet(u"QLabel{\n"
"color: white;\n"
"font-weight: bold;\n"
"background-color: #2a5c94;\n"
"border: 1px solid black;\n"
"border-top: none;\n"
"padding: 5px 10px;\n"
"margin-top: 0px;\n"
"}")

        self.formLayout_3.setWidget(1, QFormLayout.LabelRole, self.label_nre)

        self.lineEdit_nre = QLineEdit(Dialog_anadir_padres)
        self.lineEdit_nre.setMaxLength(7)
        self.lineEdit_nre.setValidator(double_validator)
        self.lineEdit_nre.setObjectName(u"lineEdit_nre")
        sizePolicy1.setHeightForWidth(self.lineEdit_nre.sizePolicy().hasHeightForWidth())
        self.lineEdit_nre.setSizePolicy(sizePolicy1)
        self.lineEdit_nre.setMaximumSize(QSize(200, 16777215))
        self.lineEdit_nre.setStyleSheet(u"QLineEdit{\n"
"border: 0px;\n"
"border-bottom: 1px solid black;\n"
"background-color: transparent;\n"
"margin-top: 10px;\n"
"}")

        self.formLayout_3.setWidget(1, QFormLayout.FieldRole, self.lineEdit_nre)

        self.label_email = QLabel(Dialog_anadir_padres)
        self.label_email.setObjectName(u"label_email")
        self.label_email.setMaximumSize(QSize(130, 16777215))
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

        self.formLayout_3.setWidget(2, QFormLayout.LabelRole, self.label_email)

        self.lineEdit_email = QLineEdit(Dialog_anadir_padres)
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

        self.formLayout_3.setWidget(2, QFormLayout.FieldRole, self.lineEdit_email)

        self.lineEdit_direccion = QLineEdit(Dialog_anadir_padres)
        self.lineEdit_direccion.setObjectName(u"lineEdit_direccion")
        sizePolicy1.setHeightForWidth(self.lineEdit_direccion.sizePolicy().hasHeightForWidth())
        self.lineEdit_direccion.setSizePolicy(sizePolicy1)
        self.lineEdit_direccion.setMaximumSize(QSize(200, 16777215))
        self.lineEdit_direccion.setStyleSheet(u"QLineEdit{\n"
"border: 0px;\n"
"border-bottom: 1px solid black;\n"
"background-color: transparent;\n"
"margin-top: 10px;\n"
"}")

        self.formLayout_3.setWidget(3, QFormLayout.FieldRole, self.lineEdit_direccion)

        self.label_direccion = QLabel(Dialog_anadir_padres)
        self.label_direccion.setObjectName(u"label_direccion")
        self.label_direccion.setMaximumSize(QSize(130, 16777215))
        self.label_direccion.setFont(font)
        self.label_direccion.setStyleSheet(u"QLabel{\n"
"color: white;\n"
"font-weight: bold;\n"
"background-color: #2a5c94;\n"
"border: 1px solid black;\n"
"border-top: none;\n"
"padding: 5px 10px;\n"
"margin-top: 0px;\n"
"}")

        self.formLayout_3.setWidget(3, QFormLayout.LabelRole, self.label_direccion)


        self.verticalLayout.addLayout(self.formLayout_3)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(-1, 6, -1, -1)
        self.btn_anadir = QPushButton(Dialog_anadir_padres)
        self.btn_anadir.clicked.connect(self.anadir_padres)
        self.btn_anadir.setObjectName(u"btn_anadir")
        sizePolicy1.setHeightForWidth(self.btn_anadir.sizePolicy().hasHeightForWidth())
        self.btn_anadir.setSizePolicy(sizePolicy1)
        font1 = QFont()
        font1.setPointSize(15)
        font1.setBold(True)
        self.btn_anadir.setFont(font1)
        self.btn_anadir.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_anadir.setStyleSheet(u"QPushButton{\n"
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

        self.horizontalLayout.addWidget(self.btn_anadir)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.verticalLayout_3.addLayout(self.verticalLayout)


        self.retranslateUi(Dialog_anadir_padres)

        QMetaObject.connectSlotsByName(Dialog_anadir_padres)
    # setupUi

    def retranslateUi(self, Dialog_anadir_padres):
        Dialog_anadir_padres.setWindowTitle(QCoreApplication.translate("Dialog_anadir_padres", u"A\u00f1adir padre/madre", None))
        self.logo.setText(QCoreApplication.translate("Dialog_anadir_padres", u"<html><head/><body><p><img src=\":/logo/logoProyecto.png\"/></p></body></html>", None))
        self.label_nombre.setText(QCoreApplication.translate("Dialog_anadir_padres", u"Nombre:      ", None))
        self.lineEdit_nombre.setPlaceholderText(QCoreApplication.translate("Dialog_anadir_padres", u"Introduce nombre del padre/madre...", None))
        self.label_nre.setText(QCoreApplication.translate("Dialog_anadir_padres", u"Nº del hijo:    ", None))
        self.lineEdit_nre.setPlaceholderText(QCoreApplication.translate("Dialog_anadir_padres", u"Introduce el número del hijo...", None))
        self.label_email.setText(QCoreApplication.translate("Dialog_anadir_padres", u"Email:          ", None))
        self.lineEdit_email.setPlaceholderText(QCoreApplication.translate("Dialog_anadir_padres", u"Introduce el email del padre/madre...", None))
        self.lineEdit_direccion.setPlaceholderText(QCoreApplication.translate("Dialog_anadir_padres", u"Introduce direcci\u00f3n padre/madre...", None))
        self.label_direccion.setText(QCoreApplication.translate("Dialog_anadir_padres", u"Direcci\u00f3n:    ", None))
        self.btn_anadir.setText(QCoreApplication.translate("Dialog_anadir_padres", u"A\u00f1adir padre/madre", None))
    # retranslateUi

    def anadir_padres(self):
        nombre = self.lineEdit_nombre.text()
        nre = self.lineEdit_nre.text()
        email = self.lineEdit_email.text()
        direccion = self.lineEdit_direccion.text()
        
        try:
            conector_alumno = AlumnoConnector()
            alumno = conector_alumno.devuelvePorNumero(nre)
            
            if alumno:
                conector_madre = MadreConnector()
                
                if '@' not in email or not (email.endswith('.com') or email.endswith('.es')):
                    QMessageBox.warning(self, 'Error', 'Correo electrónico introducido no válido.')
                    self.reiniciar()
                    return
                
                if conector_madre.existeNRE(nre):
                    QMessageBox.critical(self, "Error", "El NRE ya existe. No se puede añadir más de un padre/madre para el mismo alumno.")
                    self.reiniciar()
                    return
                
                conector_madre.insertar(nombre, nre, email, direccion)
                QMessageBox.information(self.btn_anadir, "Éxito", "Padre/Madre añadido/a con éxito.")
                self.accept()
            else: 
                reply = QMessageBox.warning(self, 'Error', 'El alumno no está registrado en la base de datos. Para añadir al padre/madre añada primero al alumno.\n\n¿Desea añadirlo ahora?', QMessageBox.Yes| QMessageBox.No)
                self.reiniciar()
                if reply == QMessageBox.Yes:
                    self.abrir_anadir_alumno()
        except Exception as e:
            QMessageBox.critical(self.btn_anadir, "Error", f"Error al insertar datos en la base de datos: {str(e)}")
            self.reiniciar()
    
    def abrir_anadir_alumno(self):
        self.ventana_anadir_alumno = VentanaAnadirAlumno()
        self.ventana_anadir_alumno.show()
        self.ventana_anadir_alumno.exec_()
    
    def reiniciar(self):
        self.lineEdit_nombre.clear()
        self.lineEdit_nre.clear()
        self.lineEdit_email.clear()
        self.lineEdit_direccion.clear()
        self.lineEdit_nombre.setFocus()
    
class VentanaAnadirAlumno(Ui_Dialog_anadir_alumno, QDialog):
    def __init__(self):
        super(VentanaAnadirAlumno, self).__init__()
        self.setupUi(self, origen='listado')
