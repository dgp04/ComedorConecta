# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'importar.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QHBoxLayout, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QVBoxLayout, QFileDialog, QMessageBox,
    QWidget)
from src.resources import *
from Connector.AlumnoConnector import *
import csv

class Ui_Dialog_importar(QDialog, object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(532, 213)
        icon = QIcon()
        icon.addFile(u":/logo/iconoProyecto.png", QSize(), QIcon.Normal, QIcon.Off)
        Dialog.setWindowIcon(icon)
        self.verticalLayout_2 = QVBoxLayout(Dialog)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setStyleSheet(u"QLabel{\n"
"color: #2a5c94;\n"
"}")

        self.verticalLayout.addWidget(self.label)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.lineEdit = QLineEdit(Dialog)
        self.lineEdit.setObjectName(u"lineEdit")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit.sizePolicy().hasHeightForWidth())
        self.lineEdit.setSizePolicy(sizePolicy)
        self.lineEdit.setStyleSheet(u"QLineEdit{\n"
"border: 0px;\n"
"border-bottom: 1px solid black;\n"
"background-color: transparent;\n"
"margin-top: 10px;\n"
"}")

        self.horizontalLayout.addWidget(self.lineEdit)

        self.pushButton = QPushButton(Dialog)
        self.pushButton.clicked.connect(self.select_file_csv)
        self.pushButton.setObjectName(u"pushButton")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy1)
        self.pushButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet(u"QPushButton{\n"
"background-color: #ffffff;\n"
"color: #2a5c94;\n"
"padding: 10px 20px;\n"
"border: 2px solid #2a5c94;\n"
"border-radius: 5px;\n"
"font-size: 16px;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: #2a5c94;\n"
"color: white;\n"
"}")

        self.horizontalLayout.addWidget(self.pushButton)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.pushButton_2 = QPushButton(Dialog)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setEnabled(True)
        self.pushButton_2.clicked.connect(self.importarAlumnos)
        self.pushButton_2.setCursor(QCursor(Qt.PointingHandCursor))
        sizePolicy.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy)
        self.pushButton_2.setMaximumSize(QSize(799, 16777215))
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet(u"QPushButton{\n"
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

        self.verticalLayout.addWidget(self.pushButton_2)


        self.verticalLayout_2.addLayout(self.verticalLayout)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Importar alumnos", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"Elija el fichero CSV que desea importar:", None))
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("Dialog", u"Seleccione un archivo...", None))
        self.pushButton.setText(QCoreApplication.translate("Dialog", u"Seleccionar archivo", None))
        self.pushButton_2.setText(QCoreApplication.translate("Dialog", u"Importar alumnos", None))
    # retranslateUi

    # Método para elegir la ruta del fichero Manifest.db
    def select_file_csv(self):
        # Abrir el cuadro de diálogo para seleccionar un archivo
        file_dialog = QFileDialog(self)
        file_path, _ = file_dialog.getOpenFileName(self, "Seleccionar Archivo")
        if file_path:
            self.lineEdit.setText(file_path)
            
    # Función para procesar el CSV y limpiar los datos
    def procesar_csv(self):
        alumnos = []
        ruta_archivo = self.lineEdit.text()
        with open(ruta_archivo, newline='', encoding='utf-8') as csvfile:
            csvreader = csv.reader(csvfile)
            for row in csvreader:
                if len(row) > 9:  # Asegurarse de que la fila tenga suficientes columnas
                    alumno = {
                        'numero': row[16],  # Posición de la columna N.
                        'primer_apellido': row[17],  # Posición de la columna 1er. Apellido
                        'segundo_apellido': row[18],  # Posición de la columna 2º Apellido
                        'curso': row[19],  # Posición de la columna Curso
                        'ensenanza': row[20],  # Posición de la columna Enseñanza
                        'grupo': row[21],  # Posición de la columna Grupo
                        'nombre': row[22]  # Posición de la columna Nombre
                    }
                    alumnos.append(alumno)
        return alumnos
    
    def importarAlumnos(self):
        alumnos = self.procesar_csv()
        conector = AlumnoConnector()
        
        try:
            conector.importarAlumnos(alumnos)
            QMessageBox.information(self, 'Éxito', 'Alumnos importados correctamente.')
            self.close()
        except Exception as e:
            QMessageBox.warning(self, 'Error', f'Error al importar los alumnos: {e}')
            self.accept()