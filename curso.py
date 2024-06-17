# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'curso.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QFrame, QHBoxLayout,
    QHeaderView, QLabel, QPushButton, QSizePolicy,
    QSpacerItem, QTableWidget, QTableWidgetItem, QVBoxLayout,
    QWidget)
from src.resources import *
from editar import *
from importar import *
from anadir import *
from eliminaAlumnos import *
from mandarMensaje import *
import json


class Ui_Dialog_curso(QDialog, object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(842, 616)
        icon = QIcon()
        icon.addFile(u":/logo/iconoProyecto.png", QSize(), QIcon.Normal, QIcon.Off)
        Dialog.setWindowIcon(icon)
        
        with open('config.json', 'r')as json_file:
            data = json.load(json_file)
         
        self.curso = data['curso'] 
        
        self.verticalLayout_2 = QVBoxLayout(Dialog)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame_superior = QFrame(Dialog)
        self.frame_superior.setObjectName(u"frame_superior")
        self.frame_superior.setMinimumSize(QSize(0, 60))
        self.frame_superior.setMaximumSize(QSize(16777215, 60))
        self.frame_superior.setStyleSheet(u"")
        self.frame_superior.setFrameShape(QFrame.StyledPanel)
        self.frame_superior.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_superior)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(-1, -1, -1, 0)
        self.label_logo = QLabel(self.frame_superior)
        self.label_logo.setObjectName(u"label_logo")
        self.label_logo.setMaximumSize(QSize(120, 150))
        self.label_logo.setPixmap(QPixmap(u":/logo/logoProyecto.png"))
        self.label_logo.setScaledContents(True)
        self.label_logo.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.label_logo)


        self.verticalLayout.addWidget(self.frame_superior)

        self.label = QLabel(Dialog)
        self.label.setStyleSheet(u"QLabel{"
"font-size: 30px;\n"
"font-weight: bold;\n"
"color: #2a5c94;\n"
"}")
        self.label.setObjectName(u"label")

        self.verticalLayout.addWidget(self.label)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(-1, 10, -1, 10)
        self.pushButton = QPushButton(Dialog)
        self.pushButton.clicked.connect(self.close)
        self.pushButton.setObjectName(u"pushButton")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        self.pushButton.setCursor(QCursor(Qt.PointingHandCursor))
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

        self.horizontalLayout_2.addWidget(self.pushButton)

        self.horizontalSpacer = QSpacerItem(300, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.pushButton_6 = QPushButton(Dialog)
        self.pushButton_6.clicked.connect(self.abrir_ventana_importar)
        self.pushButton_6.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_6.setObjectName(u"pushButton_6")
        sizePolicy.setHeightForWidth(self.pushButton_6.sizePolicy().hasHeightForWidth())
        self.pushButton_6.setSizePolicy(sizePolicy)
        self.pushButton_6.setStyleSheet(u"QPushButton{\n"
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
        self.horizontalLayout_2.addWidget(self.pushButton_6)

        
        self.pushButton_5 = QPushButton(Dialog)
        self.pushButton_5.clicked.connect(self.abrir_ventana_enviar_mensaje)
        self.pushButton_5.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_5.setObjectName(u"pushButton_5")
        sizePolicy.setHeightForWidth(self.pushButton_5.sizePolicy().hasHeightForWidth())
        self.pushButton_5.setSizePolicy(sizePolicy)
        self.pushButton_5.setStyleSheet(u"QPushButton{\n"
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
        icon1 = QIcon()
        icon1.addFile(u":/iconosLaterales/mensaje.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_5.setIcon(icon1)
        self.horizontalLayout_2.addWidget(self.pushButton_5)

        self.pushButton_2 = QPushButton(Dialog)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.clicked.connect(self.abrir_anadir_alumno)
        sizePolicy.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy)
        self.pushButton_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_2.setStyleSheet(u"QPushButton{\n"
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
        icon1 = QIcon()
        icon1.addFile(u":/iconosLaterales/anadir.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_2.setIcon(icon1)

        self.horizontalLayout_2.addWidget(self.pushButton_2)

        self.pushButton_3 = QPushButton(Dialog)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.clicked.connect(self.abrir_editar_alumno)
        sizePolicy.setHeightForWidth(self.pushButton_3.sizePolicy().hasHeightForWidth())
        self.pushButton_3.setSizePolicy(sizePolicy)
        self.pushButton_3.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_3.setStyleSheet(u"QPushButton{\n"
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
        icon2 = QIcon()
        icon2.addFile(u":/iconosLaterales/editar.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_3.setIcon(icon2)

        self.horizontalLayout_2.addWidget(self.pushButton_3)

        self.pushButton_4 = QPushButton(Dialog)
        self.pushButton_4.clicked.connect(self.abrir_ventana_eliminarAlumnos)
        self.pushButton_4.setObjectName(u"pushButton_4")
        sizePolicy.setHeightForWidth(self.pushButton_4.sizePolicy().hasHeightForWidth())
        self.pushButton_4.setSizePolicy(sizePolicy)
        self.pushButton_4.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_4.setStyleSheet(u"QPushButton{\n"
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
        icon3 = QIcon()
        icon3.addFile(u":/iconosLaterales/eliminar.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_4.setIcon(icon3)

        # Establecer la política de tamaño de los botones para que no se expandan
        for button in (self.pushButton, self.pushButton_2, self.pushButton_3, self.pushButton_4):
            button.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)

        self.horizontalLayout_2.addWidget(self.pushButton_4)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.tableWidget = QTableWidget(Dialog)
        self.tableWidget.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        if (self.tableWidget.columnCount() < 7):
            self.tableWidget.setColumnCount(7)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setStyleSheet("""
QTableView::item {
    border: none;
}
QHeaderView::section {
    border: 1px solid black;
}
""")
        self.tableWidget.horizontalHeader().setDefaultSectionSize(163)
        
        self.actualiza_alumnos()
        
        # Ajustar el ancho de la última columna para llenar el espacio restante
        self.tableWidget.horizontalHeader().setStretchLastSection(True)


        self.verticalLayout.addWidget(self.tableWidget)


        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", f"Datos de los alumnos de {self.curso}", None))
        self.label_logo.setText("")
        self.label.setText(f'Alumnos de {self.curso}º')
        self.pushButton.setText(QCoreApplication.translate("Dialog", u"Volver atr\u00e1s", None))
        self.pushButton_6.setText(QCoreApplication.translate("Dialog", u"Importar alumnos", None))
        self.pushButton_5.setText(QCoreApplication.translate("Dialog", u"Enviar mensaje", None))
        self.pushButton_2.setText(QCoreApplication.translate("Dialog", u"A\u00f1adir alumno", None))
        self.pushButton_3.setText(QCoreApplication.translate("Dialog", u"Editar alumno", None))
        self.pushButton_4.setText(QCoreApplication.translate("Dialog", u"Eliminar alumno", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Dialog", u"Número", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Dialog", u"Primer Apellido", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Dialog", u"Segundo Apellido", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Dialog", u"Curso", None));
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("Dialog", u"Enseñanza", None));
        ___qtablewidgetitem5 = self.tableWidget.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("Dialog", u"Grupo", None));
        ___qtablewidgetitem6 = self.tableWidget.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("Dialog", u"Nombre", None));
    # retranslateUi
    
    def abrir_anadir_alumno(self):
        self.ventana_anadir_alumno = VentanaAnadirAlumno()
        self.ventana_anadir_alumno.show()
        self.ventana_anadir_alumno.exec_()
        self.actualiza_alumnos()
    
    def abrir_editar_alumno(self):
        self.ventana_editar_alumno = VentanaEditarAlumno()
        self.ventana_editar_alumno.show()
        self.ventana_editar_alumno.exec_()
        self.actualiza_alumnos()

    def abrir_ventana_eliminarAlumnos(self):
        self.ventana_eliminar_alumnos = VentanaEliminarAlumnos()
        self.ventana_eliminar_alumnos.show()
        self.ventana_eliminar_alumnos.exec_()
        self.actualiza_alumnos()
        
    def abrir_ventana_enviar_mensaje(self):
        self.ventana_enviar_mensaje = VentanaMandarMensajeCurso()
        self.ventana_enviar_mensaje.show()
        self.ventana_enviar_mensaje.exec_()
        
    def actualiza_alumnos(self):
        # Obtener datos de alumnos del curso actual
        alumno_connector = AlumnoConnector()
        alumnos_curso = alumno_connector.devuelvePorCurso(self.curso)
        # Configurar el número de filas en la tabla
        self.tableWidget.setRowCount(len(alumnos_curso))
        # Llenar la tabla con los datos de los alumnos
        for row, alumno in enumerate(alumnos_curso):
            for col, data in enumerate(alumno):
                item = QTableWidgetItem(str(data))
                self.tableWidget.setItem(row, col, item)
                item.setTextAlignment(Qt.AlignCenter)

    def abrir_ventana_importar(self):
        self.ventana_importar_alumnos = VentanaImportarAlumnos()
        self.ventana_importar_alumnos.show()
        self.ventana_importar_alumnos.exec_()

class VentanaAnadirAlumno(Ui_Dialog_anadir_alumno, QDialog):
    def __init__(self):
        super(VentanaAnadirAlumno, self).__init__()
        self.setupUi(self, origen='curso')

class VentanaEditarAlumno(Ui_Dialog_editar_alumno, QDialog):
    def __init__(self):
        super(VentanaEditarAlumno, self).__init__()
        self.setupUi(self, origen='curso')
        
class VentanaEliminarAlumnos(Ui_Dialog_eliminaAlumnos, QDialog):
    def __init__(self):
        super(VentanaEliminarAlumnos, self).__init__()
        self.setupUi(self, origen='curso')
        
class VentanaMandarMensajeCurso(Ui_Dialog_mensaje, QDialog):
    def __init__(self):
        super(VentanaMandarMensajeCurso, self).__init__()
        self.setupUi(self, origen='curso')

class VentanaImportarAlumnos(Ui_Dialog_importar, QDialog):
    def __init__(self):
        super(VentanaImportarAlumnos, self).__init__()
        self.setupUi(self)