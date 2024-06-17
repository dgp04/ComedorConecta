# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'editar.ui'
##
## Created by: Qt User Interface Compiler version 6.6.2
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
import json

class Ui_Dialog_editar_alumno(QDialog, object):
    def setupUi(self, Dialog, origen):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(572, 539)
        icon = QIcon()
        icon.addFile(u":/logo/iconoProyecto.png", QSize(), QIcon.Normal, QIcon.Off)
        Dialog.setWindowIcon(icon)
        
        double_validator = QDoubleValidator(self)
        double_validator.setDecimals(2)
        
        with open('config.json', 'r', encoding='utf-8')as json_file:
            data = json.load(json_file)
        
        self.curso = data['curso'] 
        
        self.origen = origen
        
        self.verticalLayout_3 = QVBoxLayout(Dialog)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.logo = QLabel(Dialog)
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

        self.formLayout_3 = QFormLayout()
        self.formLayout_3.setObjectName(u"formLayout_3")
        self.formLayout_3.setVerticalSpacing(0)
        self.formLayout_3.setContentsMargins(160, -1, -1, -1)
        self.label_numero = QLabel(Dialog)
        self.label_numero.setObjectName(u"label_numero")
        self.label_numero.setMaximumSize(QSize(102, 16777215))
        font = QFont()
        font.setPointSize(13)
        font.setBold(True)
        self.label_numero.setFont(font)
        self.label_numero.setStyleSheet(u"QLabel{\n"
"color: white;\n"
"font-weight: bold;\n"
"background-color: #2a5c94;\n"
"border: 1px solid black;\n"
"padding: 5px 10px;\n"
"}")

        self.formLayout_3.setWidget(0, QFormLayout.LabelRole, self.label_numero)

        self.lineEdit_numero = QLineEdit(Dialog)
        self.lineEdit_numero.textChanged.connect(self.habilitar_campos)
        self.lineEdit_numero.setValidator(double_validator)
        self.lineEdit_numero.setObjectName(u"lineEdit_numero")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.lineEdit_numero.sizePolicy().hasHeightForWidth())
        self.lineEdit_numero.setSizePolicy(sizePolicy1)
        self.lineEdit_numero.setMaximumSize(QSize(200, 16777215))
        self.lineEdit_numero.setStyleSheet(u"QLineEdit{\n"
"border: 0px;\n"
"border-bottom: 1px solid black;\n"
"background-color: transparent;\n"
"margin-top: 10px;\n"
"}")

        self.formLayout_3.setWidget(0, QFormLayout.FieldRole, self.lineEdit_numero)

        self.label_apellido1 = QLabel(Dialog)
        self.label_apellido1.setObjectName(u"label_apellido1")
        self.label_apellido1.setMaximumSize(QSize(102, 16777215))
        font1 = QFont()
        font1.setPointSize(11)
        font1.setBold(True)
        self.label_apellido1.setFont(font1)
        self.label_apellido1.setStyleSheet(u"QLabel{\n"
"color: white;\n"
"font-weight: bold;\n"
"background-color: #2a5c94;\n"
"border: 1px solid black;\n"
"border-top: none;\n"
"padding: 5px 10px;\n"
"margin-top: 0px;\n"
"}")

        self.formLayout_3.setWidget(1, QFormLayout.LabelRole, self.label_apellido1)

        self.lineEdit_apellido1 = QLineEdit(Dialog)
        self.lineEdit_apellido1.setEnabled(False)
        self.lineEdit_apellido1.setObjectName(u"lineEdit_apellido1")
        sizePolicy1.setHeightForWidth(self.lineEdit_apellido1.sizePolicy().hasHeightForWidth())
        self.lineEdit_apellido1.setSizePolicy(sizePolicy1)
        self.lineEdit_apellido1.setMaximumSize(QSize(200, 16777215))
        self.lineEdit_apellido1.setStyleSheet(u"QLineEdit{\n"
"border: 0px;\n"
"border-bottom: 1px solid black;\n"
"background-color: #b5b5b5;\n"
"margin-top: 10px;\n"
"}")

        self.formLayout_3.setWidget(1, QFormLayout.FieldRole, self.lineEdit_apellido1)

        self.label_apellido2 = QLabel(Dialog)
        self.label_apellido2.setObjectName(u"label_apellido2")
        self.label_apellido2.setMaximumSize(QSize(102, 16777215))
        self.label_apellido2.setFont(font1)
        self.label_apellido2.setStyleSheet(u"QLabel{\n"
"color: white;\n"
"font-weight: bold;\n"
"background-color: #2a5c94;\n"
"border: 1px solid black;\n"
"border-top: none;\n"
"padding: 5px 10px;\n"
"margin-top: 0px;\n"
"}")

        self.formLayout_3.setWidget(2, QFormLayout.LabelRole, self.label_apellido2)

        self.lineEdit_apellido2 = QLineEdit(Dialog)
        self.lineEdit_apellido2.setEnabled(False)
        self.lineEdit_apellido2.setObjectName(u"lineEdit_apellido2")
        sizePolicy1.setHeightForWidth(self.lineEdit_apellido2.sizePolicy().hasHeightForWidth())
        self.lineEdit_apellido2.setSizePolicy(sizePolicy1)
        self.lineEdit_apellido2.setMaximumSize(QSize(200, 16777215))
        self.lineEdit_apellido2.setStyleSheet(u"QLineEdit{\n"
"border: 0px;\n"
"border-bottom: 1px solid black;\n"
"background-color: #b5b5b5;\n"
"margin-top: 10px;\n"
"}")

        self.formLayout_3.setWidget(2, QFormLayout.FieldRole, self.lineEdit_apellido2)

        self.label_curso = QLabel(Dialog)
        self.label_curso.setObjectName(u"label_curso")
        self.label_curso.setMaximumSize(QSize(102, 16777215))
        self.label_curso.setFont(font)
        self.label_curso.setStyleSheet(u"QLabel{\n"
"color: white;\n"
"font-weight: bold;\n"
"background-color: #2a5c94;\n"
"border: 1px solid black;\n"
"border-top: none;\n"
"padding: 5px 10px;\n"
"margin-top: 0px;\n"
"}")

        self.formLayout_3.setWidget(3, QFormLayout.LabelRole, self.label_curso)

        self.lineEdit_curso = QLineEdit(Dialog)
        self.lineEdit_curso.setEnabled(False)
        self.lineEdit_curso.setValidator(double_validator)
        self.lineEdit_curso.setObjectName(u"lineEdit_curso")
        self.lineEdit_curso.setMaximumSize(QSize(200, 16777215))
        self.lineEdit_curso.setStyleSheet(u"QLineEdit{\n"
"border: 0px;\n"
"border-bottom: 1px solid black;\n"
"background-color: #b5b5b5;\n"
"margin-top: 10px;\n"
"}")

        self.formLayout_3.setWidget(3, QFormLayout.FieldRole, self.lineEdit_curso)

        self.label_ensenanza = QLabel(Dialog)
        self.label_ensenanza.setObjectName(u"label_ensenanza")
        self.label_ensenanza.setMaximumSize(QSize(102, 16777215))
        self.label_ensenanza.setFont(font1)
        self.label_ensenanza.setStyleSheet(u"QLabel{\n"
"color: white;\n"
"font-weight: bold;\n"
"background-color: #2a5c94;\n"
"border: 1px solid black;\n"
"border-top: none;\n"
"padding: 5px 10px;\n"
"margin-top: 0px;\n"
"}")

        self.formLayout_3.setWidget(4, QFormLayout.LabelRole, self.label_ensenanza)

        self.lineEdit_ensenanza = QLineEdit(Dialog)
        self.lineEdit_ensenanza.setEnabled(False)
        self.lineEdit_ensenanza.setObjectName(u"lineEdit_ensenanza")
        self.lineEdit_ensenanza.setMaximumSize(QSize(200, 16777215))
        self.lineEdit_ensenanza.setStyleSheet(u"QLineEdit{\n"
"border: 0px;\n"
"border-bottom: 1px solid black;\n"
"background-color: #b5b5b5;\n"
"margin-top: 10px;\n"
"}")

        self.formLayout_3.setWidget(4, QFormLayout.FieldRole, self.lineEdit_ensenanza)

        self.lineEdit_grupo = QLineEdit(Dialog)
        self.lineEdit_grupo.setEnabled(False)
        self.lineEdit_grupo.setObjectName(u"lineEdit_grupo")
        self.lineEdit_grupo.setMaximumSize(QSize(200, 16777215))
        self.lineEdit_grupo.setStyleSheet(u"QLineEdit{\n"
"border: 0px;\n"
"border-bottom: 1px solid black;\n"
"background-color: #b5b5b5;\n"
"margin-top: 10px;\n"
"}")

        self.formLayout_3.setWidget(5, QFormLayout.FieldRole, self.lineEdit_grupo)

        self.lineEdit_nombre = QLineEdit(Dialog)
        self.lineEdit_nombre.setEnabled(False)
        self.lineEdit_nombre.setObjectName(u"lineEdit_nombre")
        self.lineEdit_nombre.setMaximumSize(QSize(200, 16777215))
        self.lineEdit_nombre.setStyleSheet(u"QLineEdit{\n"
"border: 0px;\n"
"border-bottom: 1px solid black;\n"
"background-color: #b5b5b5;\n"
"margin-top: 10px;\n"
"}")

        self.formLayout_3.setWidget(6, QFormLayout.FieldRole, self.lineEdit_nombre)

        self.label_grupo = QLabel(Dialog)
        self.label_grupo.setObjectName(u"label_grupo")
        self.label_grupo.setMaximumSize(QSize(102, 16777215))
        self.label_grupo.setFont(font)
        self.label_grupo.setStyleSheet(u"QLabel{\n"
"color: white;\n"
"font-weight: bold;\n"
"background-color: #2a5c94;\n"
"border: 1px solid black;\n"
"border-top: none;\n"
"padding: 5px 10px;\n"
"margin-top: 0px;\n"
"}")

        self.formLayout_3.setWidget(5, QFormLayout.LabelRole, self.label_grupo)

        self.label_nombre = QLabel(Dialog)
        self.label_nombre.setObjectName(u"label_nombre")
        self.label_nombre.setMaximumSize(QSize(102, 16777215))
        self.label_nombre.setFont(font)
        self.label_nombre.setStyleSheet(u"QLabel{\n"
"color: white;\n"
"font-weight: bold;\n"
"background-color: #2a5c94;\n"
"border: 1px solid black;\n"
"border-top: none;\n"
"padding: 5px 10px;\n"
"margin-top: 0px;\n"
"}")

        self.formLayout_3.setWidget(6, QFormLayout.LabelRole, self.label_nombre)


        self.verticalLayout_2.addLayout(self.formLayout_3)


        self.verticalLayout.addLayout(self.verticalLayout_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(-1, 6, -1, -1)
        self.btn_editar = QPushButton(Dialog)
        self.btn_editar.clicked.connect(self.editar_alumno)
        self.btn_editar.setObjectName(u"btn_editar")
        sizePolicy1.setHeightForWidth(self.btn_editar.sizePolicy().hasHeightForWidth())
        self.btn_editar.setSizePolicy(sizePolicy1)
        font2 = QFont()
        font2.setPointSize(15)
        font2.setBold(True)
        self.btn_editar.setFont(font2)
        self.btn_editar.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_editar.setStyleSheet(u"QPushButton{\n"
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

        self.horizontalLayout.addWidget(self.btn_editar)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.verticalLayout_3.addLayout(self.verticalLayout)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Editar alumno", None))
        self.logo.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><img src=\":/logo/logoProyecto.png\"/></p></body></html>", None))
        self.label_numero.setText(QCoreApplication.translate("Dialog", u"N\u00famero:       ", None))
        self.lineEdit_numero.setPlaceholderText(QCoreApplication.translate("Dialog", u"Introduce el n\u00famero del alumno...", None))
        self.label_apellido1.setText(QCoreApplication.translate("Dialog", u"Apellido 1:", None))
        self.lineEdit_apellido1.setPlaceholderText(QCoreApplication.translate("Dialog", u"Introduce 1er apellido del alumno...", None))
        self.label_apellido2.setText(QCoreApplication.translate("Dialog", u"Apellido 2:", None))
        self.lineEdit_apellido2.setPlaceholderText(QCoreApplication.translate("Dialog", u"Introduce 2\u00ba apellido del alumno...", None))
        self.label_curso.setText(QCoreApplication.translate("Dialog", u"Curso:     ", None))
        self.lineEdit_curso.setPlaceholderText(QCoreApplication.translate("Dialog", u"Introduce el curso del alumno...", None))
        self.label_ensenanza.setText(QCoreApplication.translate("Dialog", u"Ense\u00f1anza:", None))
        self.lineEdit_ensenanza.setPlaceholderText(QCoreApplication.translate("Dialog", u"Introduce ense\u00f1anza del alumno...", None))
        self.lineEdit_grupo.setPlaceholderText(QCoreApplication.translate("Dialog", u"Introduce el grupo del alumno...", None))
        self.lineEdit_nombre.setPlaceholderText(QCoreApplication.translate("Dialog", u"Introduce el nombre del alumno...", None))
        self.label_grupo.setText(QCoreApplication.translate("Dialog", u"Grupo:     ", None))
        self.label_nombre.setText(QCoreApplication.translate("Dialog", u"Nombre:", None))
        self.btn_editar.setText(QCoreApplication.translate("Dialog", u"Editar alumno", None))
    # retranslateUi

    def editar_alumno(self):
            numero = self.lineEdit_numero.text()
            primerApellido = self.lineEdit_apellido1.text()
            segundoApellido = self.lineEdit_apellido2.text()
            curso = self.lineEdit_curso.text()
            ensenanza = self.lineEdit_ensenanza.text()
            grupo = self.lineEdit_grupo.text()
            nombre = self.lineEdit_nombre.text()
            conector = AlumnoConnector()

            if self.origen == 'curso':
                try:
                    if curso == self.curso:
                        conector.actualizarAlumno(numero, primerApellido, segundoApellido, curso, ensenanza, grupo, nombre)
                        QMessageBox.information(self, "Éxito", "Alumno editado correctamente")
                        self.close()
                    else:
                        QMessageBox.critical(self, 'Error', 'No se ha podido editar al alumno. Curso introducido incorrecto.')
                        self.reiniciar()
                except Exception as e:
                    QMessageBox.warning(self, "Error", f"No se ha podido editar al alumno: {str(e)}")
                    self.reiniciar()
            elif self.origen == 'listado':
                try:
                    if curso not in ('1', '2', '3', '4', '5', '6'):
                        QMessageBox.warning(self, 'Error', 'Curso introducido no válido. Debe estar entre 1º y 6º.')
                        self.reiniciar()
                        return

                    conector.actualizarAlumno(numero, primerApellido, segundoApellido, curso, ensenanza, grupo, nombre)
                    QMessageBox.information(self, "Éxito", "Alumno editado correctamente")
                    self.close()
                except Exception as e:
                    QMessageBox.warning(self, "Error", f"No se ha podido editar al alumno: {str(e)}") 
                    self.reiniciar()
            
            self.accept()
                
    def habilitar_campos(self):
        numero = str(self.lineEdit_numero.text())
        conector = AlumnoConnector()
        alumno = conector.devuelvePorNumero(numero)
        
        if self.origen == 'curso':
            if alumno:
                self.lineEdit_apellido1.setEnabled(True)
                self.lineEdit_apellido1.setStyleSheet("background-color: transparent; border: 0px; border-bottom: 1px solid black; margin-top: 10px;")
                
                self.lineEdit_apellido2.setEnabled(True)
                self.lineEdit_apellido2.setStyleSheet("background-color: transparent; border: 0px; border-bottom: 1px solid black; margin-top: 10px;")
                
                self.lineEdit_curso.setEnabled(True)
                self.lineEdit_curso.setStyleSheet("background-color: transparent; border: 0px; border-bottom: 1px solid black; margin-top: 10px;")
                
                self.lineEdit_ensenanza.setEnabled(True)
                self.lineEdit_ensenanza.setStyleSheet("background-color: transparent; border: 0px; border-bottom: 1px solid black; margin-top: 10px;")
                
                self.lineEdit_grupo.setEnabled(True)
                self.lineEdit_grupo.setStyleSheet("background-color: transparent; border: 0px; border-bottom: 1px solid black; margin-top: 10px;")
                
                self.lineEdit_nombre.setEnabled(True)
                self.lineEdit_nombre.setStyleSheet("background-color: transparent; border: 0px; border-bottom: 1px solid black; margin-top: 10px;")
                
                if alumno[3] != self.curso:
                    QMessageBox.critical(self, 'Error', 'No se ha podido encontrar al alumno ya que no pertenece a este curso')
                    self.lineEdit_numero.setFocus()
                else:
                    self.lineEdit_apellido1.setText(alumno[1])
                    self.lineEdit_apellido2.setText(alumno[2])
                    self.lineEdit_curso.setText(alumno[3])
                    self.lineEdit_ensenanza.setText(alumno[4])
                    self.lineEdit_grupo.setText(alumno[5])
                    self.lineEdit_nombre.setText(alumno[6])
            else:
                self.lineEdit_apellido1.setEnabled(False)
                self.lineEdit_apellido1.clear()
                self.lineEdit_apellido1.setStyleSheet("background-color: #b5b5b5; border: 0px; border-bottom: 1px solid black; margin-top: 10px;")
                
                self.lineEdit_apellido2.setEnabled(False)
                self.lineEdit_apellido2.clear()
                self.lineEdit_apellido2.setStyleSheet("background-color: #b5b5b5; border: 0px; border-bottom: 1px solid black; margin-top: 10px;")
                
                self.lineEdit_curso.setEnabled(False)
                self.lineEdit_curso.clear()
                self.lineEdit_curso.setStyleSheet("background-color: #b5b5b5; border: 0px; border-bottom: 1px solid black; margin-top: 10px;")
                
                self.lineEdit_ensenanza.setEnabled(False)
                self.lineEdit_ensenanza.clear()
                self.lineEdit_ensenanza.setStyleSheet("background-color: #b5b5b5; border: 0px; border-bottom: 1px solid black; margin-top: 10px;")
                
                self.lineEdit_grupo.setEnabled(False)
                self.lineEdit_grupo.clear()
                self.lineEdit_grupo.setStyleSheet("background-color: #b5b5b5; border: 0px; border-bottom: 1px solid black; margin-top: 10px;")
                
                self.lineEdit_nombre.setEnabled(False)
                self.lineEdit_nombre.clear()
                self.lineEdit_nombre.setStyleSheet("background-color: #b5b5b5; border: 0px; border-bottom: 1px solid black; margin-top: 10px;")
        elif self.origen == 'listado':
            if alumno:
                if not alumno: 
                    QMessageBox.critical(self, 'Error', 'Alumno no encontrado en la base de datos.')
                else:
                    self.lineEdit_apellido1.setEnabled(True)
                    self.lineEdit_apellido1.setStyleSheet("background-color: transparent; border: 0px; border-bottom: 1px solid black; margin-top: 10px;")
                    
                    self.lineEdit_apellido2.setEnabled(True)
                    self.lineEdit_apellido2.setStyleSheet("background-color: transparent; border: 0px; border-bottom: 1px solid black; margin-top: 10px;")
                    
                    self.lineEdit_curso.setEnabled(True)
                    self.lineEdit_curso.setStyleSheet("background-color: transparent; border: 0px; border-bottom: 1px solid black; margin-top: 10px;")
                    
                    self.lineEdit_ensenanza.setEnabled(True)
                    self.lineEdit_ensenanza.setStyleSheet("background-color: transparent; border: 0px; border-bottom: 1px solid black; margin-top: 10px;")
                    
                    self.lineEdit_grupo.setEnabled(True)
                    self.lineEdit_grupo.setStyleSheet("background-color: transparent; border: 0px; border-bottom: 1px solid black; margin-top: 10px;")
                    
                    self.lineEdit_nombre.setEnabled(True)
                    self.lineEdit_nombre.setStyleSheet("background-color: transparent; border: 0px; border-bottom: 1px solid black; margin-top: 10px;")
                    
                    self.lineEdit_apellido1.setText(alumno[1])
                    self.lineEdit_apellido2.setText(alumno[2])
                    self.lineEdit_curso.setText(alumno[3])
                    self.lineEdit_ensenanza.setText(alumno[4])
                    self.lineEdit_grupo.setText(alumno[5])
                    self.lineEdit_nombre.setText(alumno[6])
            else:
                self.lineEdit_apellido1.setEnabled(False)
                self.lineEdit_apellido1.clear()
                self.lineEdit_apellido1.setStyleSheet("background-color: #b5b5b5; border: 0px; border-bottom: 1px solid black; margin-top: 10px;")
                
                self.lineEdit_apellido2.setEnabled(False)
                self.lineEdit_apellido2.clear()
                self.lineEdit_apellido2.setStyleSheet("background-color: #b5b5b5; border: 0px; border-bottom: 1px solid black; margin-top: 10px;")
                
                self.lineEdit_curso.setEnabled(False)
                self.lineEdit_curso.clear()
                self.lineEdit_curso.setStyleSheet("background-color: #b5b5b5; border: 0px; border-bottom: 1px solid black; margin-top: 10px;")
                
                self.lineEdit_ensenanza.setEnabled(False)
                self.lineEdit_ensenanza.clear()
                self.lineEdit_ensenanza.setStyleSheet("background-color: #b5b5b5; border: 0px; border-bottom: 1px solid black; margin-top: 10px;")
                
                self.lineEdit_grupo.setEnabled(False)
                self.lineEdit_grupo.clear()
                self.lineEdit_grupo.setStyleSheet("background-color: #b5b5b5; border: 0px; border-bottom: 1px solid black; margin-top: 10px;")
                
                self.lineEdit_nombre.setEnabled(False)
                self.lineEdit_nombre.clear()
                self.lineEdit_nombre.setStyleSheet("background-color: #b5b5b5; border: 0px; border-bottom: 1px solid black; margin-top: 10px;")
    
    def reiniciar(self):
        self.lineEdit_numero.clear()
        self.lineEdit_apellido1.clear()
        self.lineEdit_apellido2.clear()
        self.lineEdit_curso.clear()
        self.lineEdit_ensenanza.clear()
        self.lineEdit_grupo.clear()
        self.lineEdit_nombre.clear()