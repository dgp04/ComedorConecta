# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'editarMadre.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QFormLayout, QHBoxLayout,
    QLabel, QLayout, QLineEdit, QPushButton, QMessageBox,
    QSizePolicy, QVBoxLayout, QWidget)
from src.resources import *
from Connector.AlumnoConnector import *
from Connector.MadreConnector import *
from editar import *

class Ui_Dialog_editar_padres(QDialog, object):
    def setupUi(self, Dialog_editar_padres):
        if not Dialog_editar_padres.objectName():
            Dialog_editar_padres.setObjectName(u"Dialog_editar_padres")
        Dialog_editar_padres.resize(572, 472)
        icon = QIcon()
        icon.addFile(u":/logo/iconoProyecto.png", QSize(), QIcon.Normal, QIcon.Off)
        Dialog_editar_padres.setWindowIcon(icon)
        
        double_validator = QDoubleValidator(self)
        double_validator.setDecimals(2)
        
        self.verticalLayout_3 = QVBoxLayout(Dialog_editar_padres)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.logo = QLabel(Dialog_editar_padres)
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
        self.label_id = QLabel(Dialog_editar_padres)
        self.label_id.setObjectName(u"label_id")
        self.label_id.setMaximumSize(QSize(130, 16777215))
        font = QFont()
        font.setPointSize(13)
        font.setBold(True)
        self.label_id.setFont(font)
        self.label_id.setStyleSheet(u"QLabel{\n"
"color: white;\n"
"font-weight: bold;\n"
"background-color: #2a5c94;\n"
"border: 1px solid black;\n"
"padding: 5px 10px;\n"
"}")

        self.formLayout_3.setWidget(0, QFormLayout.LabelRole, self.label_id)

        self.label_nombre = QLabel(Dialog_editar_padres)
        self.label_nombre.setObjectName(u"label_nombre")
        self.label_nombre.setMaximumSize(QSize(130, 16777215))
        self.label_nombre.setFont(font)
        self.label_nombre.setStyleSheet(u"QLabel{\n"
"color: white;\n"
"font-weight: bold;\n"
"background-color: #2a5c94;\n"
"border: 1px solid black;\n"
"border-top: none;\n"
"padding: 5px 10px;\n"
"}")

        self.formLayout_3.setWidget(1, QFormLayout.LabelRole, self.label_nombre)

        self.lineEdit_nombre = QLineEdit(Dialog_editar_padres)
        self.lineEdit_nombre.setObjectName(u"lineEdit_nombre")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.lineEdit_nombre.sizePolicy().hasHeightForWidth())
        self.lineEdit_nombre.setSizePolicy(sizePolicy1)
        self.lineEdit_nombre.setMaximumSize(QSize(200, 16777215))
        self.lineEdit_nombre.setCursor(QCursor(Qt.IBeamCursor))
        self.lineEdit_nombre.setEnabled(False)
        self.lineEdit_nombre.setStyleSheet("background-color: #b5b5b5; border: 0px; border-bottom: 1px solid black; margin-top: 10px;")

        self.formLayout_3.setWidget(1, QFormLayout.FieldRole, self.lineEdit_nombre)

        self.label_nre = QLabel(Dialog_editar_padres)
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

        self.formLayout_3.setWidget(2, QFormLayout.LabelRole, self.label_nre)

        self.lineEdit_nre = QLineEdit(Dialog_editar_padres)
        self.lineEdit_nre.setObjectName(u"lineEdit_nre")
        sizePolicy1.setHeightForWidth(self.lineEdit_nre.sizePolicy().hasHeightForWidth())
        self.lineEdit_nre.setSizePolicy(sizePolicy1)
        self.lineEdit_nre.setMaxLength(7)
        self.lineEdit_nre.setValidator(double_validator)
        self.lineEdit_nre.setMaximumSize(QSize(200, 16777215))
        self.lineEdit_nre.setEnabled(False)
        self.lineEdit_nre.setStyleSheet("background-color: #b5b5b5; border: 0px; border-bottom: 1px solid black; margin-top: 10px;")

        self.formLayout_3.setWidget(2, QFormLayout.FieldRole, self.lineEdit_nre)

        self.label_email = QLabel(Dialog_editar_padres)
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

        self.formLayout_3.setWidget(3, QFormLayout.LabelRole, self.label_email)

        self.lineEdit_email = QLineEdit(Dialog_editar_padres)
        self.lineEdit_email.setObjectName(u"lineEdit_email")
        sizePolicy1.setHeightForWidth(self.lineEdit_email.sizePolicy().hasHeightForWidth())
        self.lineEdit_email.setSizePolicy(sizePolicy1)
        self.lineEdit_email.setMaximumSize(QSize(200, 16777215))
        self.lineEdit_email.setEnabled(False)
        self.lineEdit_email.setStyleSheet("background-color: #b5b5b5; border: 0px; border-bottom: 1px solid black; margin-top: 10px;")
        self.lineEdit_email.setEchoMode(QLineEdit.Normal)

        self.formLayout_3.setWidget(3, QFormLayout.FieldRole, self.lineEdit_email)

        self.label_direccion = QLabel(Dialog_editar_padres)
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

        self.formLayout_3.setWidget(4, QFormLayout.LabelRole, self.label_direccion)

        self.lineEdit_direccion = QLineEdit(Dialog_editar_padres)
        self.lineEdit_direccion.setObjectName(u"lineEdit_direccion")
        sizePolicy1.setHeightForWidth(self.lineEdit_direccion.sizePolicy().hasHeightForWidth())
        self.lineEdit_direccion.setSizePolicy(sizePolicy1)
        self.lineEdit_direccion.setMaximumSize(QSize(200, 16777215))
        self.lineEdit_direccion.setEnabled(False)
        self.lineEdit_direccion.setStyleSheet("background-color: #b5b5b5; border: 0px; border-bottom: 1px solid black; margin-top: 10px;")

        self.formLayout_3.setWidget(4, QFormLayout.FieldRole, self.lineEdit_direccion)

        self.lineEdit_id = QLineEdit(Dialog_editar_padres)
        self.lineEdit_id.textChanged.connect(self.habilitar_campos)
        self.lineEdit_id.setValidator(double_validator)
        self.lineEdit_id.setObjectName(u"lineEdit_id")
        self.lineEdit_id.setMaximumSize(QSize(200, 16777215))
        self.lineEdit_id.setStyleSheet(u"QLineEdit{\n"
"border: 0px;\n"
"border-bottom: 1px solid black;\n"
"background-color: transparent;\n"
"margin-top: 10px;\n"
"}")

        self.formLayout_3.setWidget(0, QFormLayout.FieldRole, self.lineEdit_id)


        self.verticalLayout.addLayout(self.formLayout_3)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(-1, 6, -1, -1)
        self.btn_anadir = QPushButton(Dialog_editar_padres)
        self.btn_anadir.clicked.connect(self.actualizar_padres)
        self.btn_anadir.setEnabled(False)
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


        self.retranslateUi(Dialog_editar_padres)

        QMetaObject.connectSlotsByName(Dialog_editar_padres)
    # setupUi

    def retranslateUi(self, Dialog_editar_padres):
        Dialog_editar_padres.setWindowTitle(QCoreApplication.translate("Dialog_editar_padres", u"Editar padre/madre", None))
        self.logo.setText(QCoreApplication.translate("Dialog_editar_padres", u"<html><head/><body><p><img src=\":/logo/logoProyecto.png\"/></p></body></html>", None))
        self.label_id.setText(QCoreApplication.translate("Dialog_editar_padres", u"ID padre:      ", None))
        self.label_nombre.setText(QCoreApplication.translate("Dialog_editar_padres", u"Nombre:      ", None))
        self.lineEdit_nombre.setPlaceholderText(QCoreApplication.translate("Dialog_editar_padres", u"Introduce nombre del padre/madre...", None))
        self.label_nre.setText(QCoreApplication.translate("Dialog_editar_padres", u"Nº del hijo:    ", None))
        self.lineEdit_nre.setPlaceholderText(QCoreApplication.translate("Dialog_editar_padres", u"Introduce el número del hijo...", None))
        self.label_email.setText(QCoreApplication.translate("Dialog_editar_padres", u"Email:          ", None))
        self.lineEdit_email.setPlaceholderText(QCoreApplication.translate("Dialog_editar_padres", u"Introduce el email del padre/madre...", None))
        self.label_direccion.setText(QCoreApplication.translate("Dialog_editar_padres", u"Direcci\u00f3n:    ", None))
        self.lineEdit_direccion.setPlaceholderText(QCoreApplication.translate("Dialog_editar_padres", u"Introduce direcci\u00f3n padre/madre...", None))
        self.lineEdit_id.setPlaceholderText(QCoreApplication.translate("Dialog_editar_padres", u"Introduzca el ID del padre/madre...", None))
        self.btn_anadir.setText(QCoreApplication.translate("Dialog_editar_padres", u"Confirmar cambios", None))
    # retranslateUi

    def actualizar_padres(self):
        id_padre = self.lineEdit_id.text()
        nombre = self.lineEdit_nombre.text()
        nre_hijo = str(self.lineEdit_nre.text())
        email = self.lineEdit_email.text()
        direccion = self.lineEdit_direccion.text()
        conector = MadreConnector()
        padre = conector.devuelvePorID(id_padre)
        
        try:
            conector_alumno = AlumnoConnector()
            alumno = conector_alumno.devuelvePorNumero(nre_hijo)
            
            if alumno is None:
                QMessageBox.warning(self, 'Error', 'Alumno no registrado en la base de datos')
                return
            else: 
                conector.actualizarMadre(nombre, nre_hijo, email, direccion, id_padre)
                QMessageBox.information(self.btn_anadir, 'Éxito', 'Padre/Madre actualizado/a con éxito.')
                self.accept()
        except Exception as e:
            QMessageBox.critical(self.btn_anadir, "Error", f"Error al insertar datos en la base de datos: {str(e)}")
            self.reiniciar()

    def habilitar_campos(self):
        id_padre = self.lineEdit_id.text()
        conector = MadreConnector()
        madre = conector.devuelvePorID(id_padre)
        
        if madre:
            self.lineEdit_nombre.setEnabled(True)
            self.lineEdit_nre.setEnabled(True)
            self.lineEdit_email.setEnabled(True)
            self.lineEdit_direccion.setEnabled(True)
            self.btn_anadir.setEnabled(True)

            self.lineEdit_nombre.setStyleSheet("background-color: transparent; border: 0px; border-bottom: 1px solid black; margin-top: 10px;")
            self.lineEdit_nre.setStyleSheet("background-color: transparent; border: 0px; border-bottom: 1px solid black; margin-top: 10px;")
            self.lineEdit_email.setStyleSheet("background-color: transparent; border: 0px; border-bottom: 1px solid black; margin-top: 10px;")
            self.lineEdit_direccion.setStyleSheet("background-color: transparent; border: 0px; border-bottom: 1px solid black; margin-top: 10px;")

            # Populate fields with data from the database
            self.lineEdit_nombre.setText(madre[1])
            self.lineEdit_nre.setText(str(madre[2]))
            self.lineEdit_email.setText(madre[3])
            self.lineEdit_direccion.setText(madre[4])
        else:
            self.lineEdit_nombre.setEnabled(True)
            self.lineEdit_nre.setEnabled(False)
            self.lineEdit_email.setEnabled(False)
            self.lineEdit_direccion.setEnabled(False)
            self.btn_anadir.setEnabled(False)

            self.lineEdit_nombre.setStyleSheet("background-color: #b5b5b5; border: 0px; border-bottom: 1px solid black; margin-top: 10px;")
            self.lineEdit_nre.setStyleSheet("background-color: #b5b5b5; border: 0px; border-bottom: 1px solid black; margin-top: 10px;")
            self.lineEdit_email.setStyleSheet("background-color: #b5b5b5; border: 0px; border-bottom: 1px solid black; margin-top: 10px;")
            self.lineEdit_direccion.setStyleSheet("background-color: #b5b5b5; border: 0px; border-bottom: 1px solid black; margin-top: 10px;")

            self.lineEdit_nombre.clear()
            self.lineEdit_nre.clear()
            self.lineEdit_email.clear()
            self.lineEdit_direccion.clear()
    
    def abrir_editar_alumno(self, nre):
        self.dialog_editar_alumno = QDialog(self)
        self.ui_editar_alumno = Ui_Dialog_editar_alumno()
        self.ui_editar_alumno.setupUi(self.dialog_editar_alumno, origen='listado')
        self.ui_editar_alumno.lineEdit_nre.setText(nre)
        self.dialog_editar_alumno.show()
        self.dialog_editar_alumno.exec_()
        self.accept()
                
    def reiniciar(self):
        self.lineEdit_id.clear()
        self.lineEdit_nombre.clear()
        self.lineEdit_nre.clear()
        self.lineEdit_email.clear()
        self.lineEdit_direccion.clear()
        self.lineEdit_id.setFocus()
