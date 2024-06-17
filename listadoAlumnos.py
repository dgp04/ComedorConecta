# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'listadoAlumnos.ui'
##
## Created by: Qt User Interface Compiler version 6.6.2
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
from anadir import *
from editar import *
from eliminaAlumnos import *
from importar import *
from mandarMensaje import *
from Connector.AlumnoConnector import *

class Ui_Dialog_listadoAlumnos(QDialog, object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(1104, 886)
        icon = QIcon()
        icon.addFile(u":/logo/iconoProyecto.png", QSize(), QIcon.Normal, QIcon.Off)
        Dialog.setWindowIcon(icon)
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
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"QLabel{\n"
"font-size: 25px;\n"
"font-weight: bold;\n"
"color: #2a5c94;\n"
"}")

        self.verticalLayout.addWidget(self.label)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(-1, 10, -1, 10)
        self.btn_volver_atras = QPushButton(Dialog)
        self.btn_volver_atras.clicked.connect(self.close)
        self.btn_volver_atras.setObjectName(u"btn_volver_atras")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_volver_atras.sizePolicy().hasHeightForWidth())
        self.btn_volver_atras.setSizePolicy(sizePolicy)
        self.btn_volver_atras.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_volver_atras.setStyleSheet(u"QPushButton{\n"
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

        self.horizontalLayout_2.addWidget(self.btn_volver_atras)

        self.horizontalSpacer = QSpacerItem(350, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.pushButton = QPushButton(Dialog)
        self.pushButton.clicked.connect(self.abrir_ventana_importar)
        self.pushButton.setObjectName(u"pushButton")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
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

        self.btn_enviar_mensaje = QPushButton(Dialog)
        self.btn_enviar_mensaje.clicked.connect(self.abrir_ventana_enviar_mensaje)
        self.btn_enviar_mensaje.setObjectName(u"btn_enviar_mensaje")
        sizePolicy.setHeightForWidth(self.btn_enviar_mensaje.sizePolicy().hasHeightForWidth())
        self.btn_enviar_mensaje.setSizePolicy(sizePolicy)
        self.btn_enviar_mensaje.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_enviar_mensaje.setStyleSheet(u"QPushButton{\n"
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
        self.btn_enviar_mensaje.setIcon(icon1)

        self.horizontalLayout_2.addWidget(self.btn_enviar_mensaje)

        self.btn_anadir = QPushButton(Dialog)
        self.btn_anadir.clicked.connect(self.abrir_ventana_anadir)
        self.btn_anadir.setObjectName(u"btn_anadir")
        sizePolicy.setHeightForWidth(self.btn_anadir.sizePolicy().hasHeightForWidth())
        self.btn_anadir.setSizePolicy(sizePolicy)
        self.btn_anadir.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_anadir.setStyleSheet(u"QPushButton{\n"
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
        icon2.addFile(u":/iconosLaterales/anadir.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_anadir.setIcon(icon2)

        self.horizontalLayout_2.addWidget(self.btn_anadir)

        self.btn_editar = QPushButton(Dialog)
        self.btn_editar.clicked.connect(self.abrir_ventana_editar)
        self.btn_editar.setObjectName(u"btn_editar")
        sizePolicy.setHeightForWidth(self.btn_editar.sizePolicy().hasHeightForWidth())
        self.btn_editar.setSizePolicy(sizePolicy)
        self.btn_editar.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_editar.setStyleSheet(u"QPushButton{\n"
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
        icon3.addFile(u":/iconosLaterales/editar.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_editar.setIcon(icon3)

        self.horizontalLayout_2.addWidget(self.btn_editar)

        self.btn_eliminar = QPushButton(Dialog)
        self.btn_eliminar.clicked.connect(self.abrir_ventana_eliminar)
        self.btn_eliminar.setObjectName(u"btn_eliminar")
        sizePolicy.setHeightForWidth(self.btn_eliminar.sizePolicy().hasHeightForWidth())
        self.btn_eliminar.setSizePolicy(sizePolicy)
        self.btn_eliminar.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_eliminar.setStyleSheet(u"QPushButton{\n"
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
        icon4 = QIcon()
        icon4.addFile(u":/iconosLaterales/eliminar.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_eliminar.setIcon(icon4)

        self.horizontalLayout_2.addWidget(self.btn_eliminar)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.label_sexto = QLabel(Dialog)
        self.label_sexto.setObjectName(u"label_sexto")
        self.label_sexto.setStyleSheet(u"QLabel{\n"
"font-size: 16px;\n"
"font-weight: bold;\n"
"color: #2a5c94;\n"
"}")

        self.verticalLayout.addWidget(self.label_sexto)

        self.tabla_sexto = QTableWidget(Dialog)
        if (self.tabla_sexto.columnCount() < 7):
            self.tabla_sexto.setColumnCount(7)
        __qtablewidgetitem = QTableWidgetItem()
        self.tabla_sexto.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tabla_sexto.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tabla_sexto.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tabla_sexto.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tabla_sexto.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tabla_sexto.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tabla_sexto.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        self.tabla_sexto.setObjectName(u"tabla_sexto")
        self.tabla_sexto.setStyleSheet(u"QTableWidget, QHeaderView::section{\n"
"background-color: transparent;\n"
"}\n"
"")
        self.tabla_sexto.horizontalHeader().setDefaultSectionSize(163)

        # Ajustar el ancho de la última columna para llenar el espacio restante
        self.tabla_sexto.horizontalHeader().setStretchLastSection(True)
        self.tabla_sexto.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        
        self.verticalLayout.addWidget(self.tabla_sexto)

        self.label_quinto = QLabel(Dialog)
        self.label_quinto.setObjectName(u"label_quinto")
        self.label_quinto.setStyleSheet(u"QLabel{\n"
"font-size: 16px;\n"
"font-weight: bold;\n"
"color: #2a5c94;\n"
"}")

        self.verticalLayout.addWidget(self.label_quinto)

        self.tabla_sexto_2 = QTableWidget(Dialog)
        if (self.tabla_sexto_2.columnCount() < 7):
            self.tabla_sexto_2.setColumnCount(7)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tabla_sexto_2.setHorizontalHeaderItem(0, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tabla_sexto_2.setHorizontalHeaderItem(1, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tabla_sexto_2.setHorizontalHeaderItem(2, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tabla_sexto_2.setHorizontalHeaderItem(3, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.tabla_sexto_2.setHorizontalHeaderItem(4, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.tabla_sexto_2.setHorizontalHeaderItem(5, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.tabla_sexto_2.setHorizontalHeaderItem(6, __qtablewidgetitem13)
        self.tabla_sexto_2.setObjectName(u"tabla_sexto_2")
        self.tabla_sexto_2.setStyleSheet(u"QTableWidget, QHeaderView::section{\n"
"background-color: transparent;\n"
"}\n"
"")
        self.tabla_sexto_2.horizontalHeader().setDefaultSectionSize(163)

        # Ajustar el ancho de la última columna para llenar el espacio restante
        self.tabla_sexto_2.horizontalHeader().setStretchLastSection(True)
        self.tabla_sexto_2.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        self.verticalLayout.addWidget(self.tabla_sexto_2)

        self.label_cuarto = QLabel(Dialog)
        self.label_cuarto.setObjectName(u"label_cuarto")
        self.label_cuarto.setStyleSheet(u"QLabel{\n"
"font-size: 16px;\n"
"font-weight: bold;\n"
"color: #2a5c94;\n"
"}")

        self.verticalLayout.addWidget(self.label_cuarto)

        self.tabla_sexto_3 = QTableWidget(Dialog)
        if (self.tabla_sexto_3.columnCount() < 7):
            self.tabla_sexto_3.setColumnCount(7)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.tabla_sexto_3.setHorizontalHeaderItem(0, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.tabla_sexto_3.setHorizontalHeaderItem(1, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.tabla_sexto_3.setHorizontalHeaderItem(2, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.tabla_sexto_3.setHorizontalHeaderItem(3, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.tabla_sexto_3.setHorizontalHeaderItem(4, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        self.tabla_sexto_3.setHorizontalHeaderItem(5, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        self.tabla_sexto_3.setHorizontalHeaderItem(6, __qtablewidgetitem20)
        self.tabla_sexto_3.setObjectName(u"tabla_sexto_3")
        self.tabla_sexto_3.setStyleSheet(u"QTableWidget, QHeaderView::section{\n"
"background-color: transparent;\n"
"}\n"
"")
        self.tabla_sexto_3.horizontalHeader().setDefaultSectionSize(163)

        # Ajustar el ancho de la última columna para llenar el espacio restante
        self.tabla_sexto_3.horizontalHeader().setStretchLastSection(True)
        self.tabla_sexto_3.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        self.verticalLayout.addWidget(self.tabla_sexto_3)

        self.label_tercero = QLabel(Dialog)
        self.label_tercero.setObjectName(u"label_tercero")
        self.label_tercero.setStyleSheet(u"QLabel{\n"
"font-size: 16px;\n"
"font-weight: bold;\n"
"color: #2a5c94;\n"
"}")

        self.verticalLayout.addWidget(self.label_tercero)

        self.tabla_sexto_4 = QTableWidget(Dialog)
        if (self.tabla_sexto_4.columnCount() < 7):
            self.tabla_sexto_4.setColumnCount(7)
        __qtablewidgetitem21 = QTableWidgetItem()
        self.tabla_sexto_4.setHorizontalHeaderItem(0, __qtablewidgetitem21)
        __qtablewidgetitem22 = QTableWidgetItem()
        self.tabla_sexto_4.setHorizontalHeaderItem(1, __qtablewidgetitem22)
        __qtablewidgetitem23 = QTableWidgetItem()
        self.tabla_sexto_4.setHorizontalHeaderItem(2, __qtablewidgetitem23)
        __qtablewidgetitem24 = QTableWidgetItem()
        self.tabla_sexto_4.setHorizontalHeaderItem(3, __qtablewidgetitem24)
        __qtablewidgetitem25 = QTableWidgetItem()
        self.tabla_sexto_4.setHorizontalHeaderItem(4, __qtablewidgetitem25)
        __qtablewidgetitem26 = QTableWidgetItem()
        self.tabla_sexto_4.setHorizontalHeaderItem(5, __qtablewidgetitem26)
        __qtablewidgetitem27 = QTableWidgetItem()
        self.tabla_sexto_4.setHorizontalHeaderItem(6, __qtablewidgetitem27)
        self.tabla_sexto_4.setObjectName(u"tabla_sexto_4")
        self.tabla_sexto_4.setStyleSheet(u"QTableWidget, QHeaderView::section{\n"
"background-color: transparent;\n"
"}\n"
"")
        self.tabla_sexto_4.horizontalHeader().setDefaultSectionSize(163)

        # Ajustar el ancho de la última columna para llenar el espacio restante
        self.tabla_sexto_4.horizontalHeader().setStretchLastSection(True)
        self.tabla_sexto_4.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        self.verticalLayout.addWidget(self.tabla_sexto_4)

        self.label_segundo = QLabel(Dialog)
        self.label_segundo.setObjectName(u"label_segundo")
        self.label_segundo.setStyleSheet(u"QLabel{\n"
"font-size: 16px;\n"
"font-weight: bold;\n"
"color: #2a5c94;\n"
"}")

        self.verticalLayout.addWidget(self.label_segundo)

        self.tabla_sexto_5 = QTableWidget(Dialog)
        if (self.tabla_sexto_5.columnCount() < 7):
            self.tabla_sexto_5.setColumnCount(7)
        __qtablewidgetitem28 = QTableWidgetItem()
        self.tabla_sexto_5.setHorizontalHeaderItem(0, __qtablewidgetitem28)
        __qtablewidgetitem29 = QTableWidgetItem()
        self.tabla_sexto_5.setHorizontalHeaderItem(1, __qtablewidgetitem29)
        __qtablewidgetitem30 = QTableWidgetItem()
        self.tabla_sexto_5.setHorizontalHeaderItem(2, __qtablewidgetitem30)
        __qtablewidgetitem31 = QTableWidgetItem()
        self.tabla_sexto_5.setHorizontalHeaderItem(3, __qtablewidgetitem31)
        __qtablewidgetitem32 = QTableWidgetItem()
        self.tabla_sexto_5.setHorizontalHeaderItem(4, __qtablewidgetitem32)
        __qtablewidgetitem33 = QTableWidgetItem()
        self.tabla_sexto_5.setHorizontalHeaderItem(5, __qtablewidgetitem33)
        __qtablewidgetitem34 = QTableWidgetItem()
        self.tabla_sexto_5.setHorizontalHeaderItem(6, __qtablewidgetitem34)
        self.tabla_sexto_5.setObjectName(u"tabla_sexto_5")
        self.tabla_sexto_5.setStyleSheet(u"QTableWidget, QHeaderView::section{\n"
"background-color: transparent;\n"
"}\n"
"")
        self.tabla_sexto_5.horizontalHeader().setDefaultSectionSize(163)

        # Ajustar el ancho de la última columna para llenar el espacio restante
        self.tabla_sexto_5.horizontalHeader().setStretchLastSection(True)
        self.tabla_sexto_5.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        self.verticalLayout.addWidget(self.tabla_sexto_5)

        self.label_primero = QLabel(Dialog)
        self.label_primero.setObjectName(u"label_primero")
        self.label_primero.setStyleSheet(u"QLabel{\n"
"font-size: 16px;\n"
"font-weight: bold;\n"
"color: #2a5c94;\n"
"}")

        self.verticalLayout.addWidget(self.label_primero)

        self.tabla_sexto_6 = QTableWidget(Dialog)
        if (self.tabla_sexto_6.columnCount() < 7):
            self.tabla_sexto_6.setColumnCount(7)
        __qtablewidgetitem35 = QTableWidgetItem()
        self.tabla_sexto_6.setHorizontalHeaderItem(0, __qtablewidgetitem35)
        __qtablewidgetitem36 = QTableWidgetItem()
        self.tabla_sexto_6.setHorizontalHeaderItem(1, __qtablewidgetitem36)
        __qtablewidgetitem37 = QTableWidgetItem()
        self.tabla_sexto_6.setHorizontalHeaderItem(2, __qtablewidgetitem37)
        __qtablewidgetitem38 = QTableWidgetItem()
        self.tabla_sexto_6.setHorizontalHeaderItem(3, __qtablewidgetitem38)
        __qtablewidgetitem39 = QTableWidgetItem()
        self.tabla_sexto_6.setHorizontalHeaderItem(4, __qtablewidgetitem39)
        __qtablewidgetitem40 = QTableWidgetItem()
        self.tabla_sexto_6.setHorizontalHeaderItem(5, __qtablewidgetitem40)
        __qtablewidgetitem41 = QTableWidgetItem()
        self.tabla_sexto_6.setHorizontalHeaderItem(6, __qtablewidgetitem41)
        self.tabla_sexto_6.setObjectName(u"tabla_sexto_6")
        self.tabla_sexto_6.setStyleSheet(u"QTableWidget, QHeaderView::section{\n"
"background-color: transparent;\n"
"}\n"
"")
        self.tabla_sexto_6.horizontalHeader().setDefaultSectionSize(163)

        # Ajustar el ancho de la última columna para llenar el espacio restante
        self.tabla_sexto_6.horizontalHeader().setStretchLastSection(True)
        self.tabla_sexto_6.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        self.verticalLayout.addWidget(self.tabla_sexto_6)


        self.verticalLayout_2.addLayout(self.verticalLayout)
        
        self.tablas = [self.tabla_sexto_6, self.tabla_sexto_5, self.tabla_sexto_4, self.tabla_sexto_3, self.tabla_sexto_2, self.tabla_sexto]
        self.actualiza_todos_alumnos()


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Listado de alumnos del centro", None))
        self.label_logo.setText("")
        self.label.setText(QCoreApplication.translate("Dialog", u"Listado de alumnos del centro:", None))
        self.btn_volver_atras.setText(QCoreApplication.translate("Dialog", u"Volver atr\u00e1s", None))
        self.pushButton.setText(QCoreApplication.translate("Dialog", u"Importar alumnos", None))
        self.btn_enviar_mensaje.setText(QCoreApplication.translate("Dialog", u"Enviar mensaje", None))
        self.btn_anadir.setText(QCoreApplication.translate("Dialog", u"A\u00f1adir alumno", None))
        self.btn_editar.setText(QCoreApplication.translate("Dialog", u"Editar alumno", None))
        self.btn_eliminar.setText(QCoreApplication.translate("Dialog", u"Eliminar alumno", None))
        self.label_sexto.setText(QCoreApplication.translate("Dialog", u"Curso 6\u00ba:", None))
        ___qtablewidgetitem = self.tabla_sexto.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Dialog", u"N\u00famero", None));
        ___qtablewidgetitem1 = self.tabla_sexto.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Dialog", u"Primer Apellido", None));
        ___qtablewidgetitem2 = self.tabla_sexto.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Dialog", u"Segundo Apellido", None));
        ___qtablewidgetitem3 = self.tabla_sexto.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Dialog", u"Curso", None));
        ___qtablewidgetitem4 = self.tabla_sexto.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("Dialog", u"Ense\u00f1anza", None));
        ___qtablewidgetitem5 = self.tabla_sexto.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("Dialog", u"Grupo", None));
        ___qtablewidgetitem6 = self.tabla_sexto.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("Dialog", u"Nombre", None));
        self.label_quinto.setText(QCoreApplication.translate("Dialog", u"Curso 5\u00ba:", None))
        ___qtablewidgetitem7 = self.tabla_sexto_2.horizontalHeaderItem(0)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("Dialog", u"N\u00famero", None));
        ___qtablewidgetitem8 = self.tabla_sexto_2.horizontalHeaderItem(1)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("Dialog", u"Primer Apellido", None));
        ___qtablewidgetitem9 = self.tabla_sexto_2.horizontalHeaderItem(2)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("Dialog", u"Segundo Apellido", None));
        ___qtablewidgetitem10 = self.tabla_sexto_2.horizontalHeaderItem(3)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("Dialog", u"Curso", None));
        ___qtablewidgetitem11 = self.tabla_sexto_2.horizontalHeaderItem(4)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("Dialog", u"Ense\u00f1anza", None));
        ___qtablewidgetitem12 = self.tabla_sexto_2.horizontalHeaderItem(5)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("Dialog", u"Grupo", None));
        ___qtablewidgetitem13 = self.tabla_sexto_2.horizontalHeaderItem(6)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("Dialog", u"Nombre", None));
        self.label_cuarto.setText(QCoreApplication.translate("Dialog", u"Curso 4\u00ba:", None))
        ___qtablewidgetitem14 = self.tabla_sexto_3.horizontalHeaderItem(0)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("Dialog", u"N\u00famero", None));
        ___qtablewidgetitem15 = self.tabla_sexto_3.horizontalHeaderItem(1)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("Dialog", u"Primer Apellido", None));
        ___qtablewidgetitem16 = self.tabla_sexto_3.horizontalHeaderItem(2)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("Dialog", u"Segundo Apellido", None));
        ___qtablewidgetitem17 = self.tabla_sexto_3.horizontalHeaderItem(3)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("Dialog", u"Curso", None));
        ___qtablewidgetitem18 = self.tabla_sexto_3.horizontalHeaderItem(4)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("Dialog", u"Ense\u00f1anza", None));
        ___qtablewidgetitem19 = self.tabla_sexto_3.horizontalHeaderItem(5)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("Dialog", u"Grupo", None));
        ___qtablewidgetitem20 = self.tabla_sexto_3.horizontalHeaderItem(6)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("Dialog", u"Nombre", None));
        self.label_tercero.setText(QCoreApplication.translate("Dialog", u"Curso 3\u00ba:", None))
        ___qtablewidgetitem21 = self.tabla_sexto_4.horizontalHeaderItem(0)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("Dialog", u"N\u00famero", None));
        ___qtablewidgetitem22 = self.tabla_sexto_4.horizontalHeaderItem(1)
        ___qtablewidgetitem22.setText(QCoreApplication.translate("Dialog", u"Primer Apellido", None));
        ___qtablewidgetitem23 = self.tabla_sexto_4.horizontalHeaderItem(2)
        ___qtablewidgetitem23.setText(QCoreApplication.translate("Dialog", u"Segundo Apellido", None));
        ___qtablewidgetitem24 = self.tabla_sexto_4.horizontalHeaderItem(3)
        ___qtablewidgetitem24.setText(QCoreApplication.translate("Dialog", u"Curso", None));
        ___qtablewidgetitem25 = self.tabla_sexto_4.horizontalHeaderItem(4)
        ___qtablewidgetitem25.setText(QCoreApplication.translate("Dialog", u"Ense\u00f1anza", None));
        ___qtablewidgetitem26 = self.tabla_sexto_4.horizontalHeaderItem(5)
        ___qtablewidgetitem26.setText(QCoreApplication.translate("Dialog", u"Grupo", None));
        ___qtablewidgetitem27 = self.tabla_sexto_4.horizontalHeaderItem(6)
        ___qtablewidgetitem27.setText(QCoreApplication.translate("Dialog", u"Nombre", None));
        self.label_segundo.setText(QCoreApplication.translate("Dialog", u"Curso 2\u00ba:", None))
        ___qtablewidgetitem28 = self.tabla_sexto_5.horizontalHeaderItem(0)
        ___qtablewidgetitem28.setText(QCoreApplication.translate("Dialog", u"N\u00famero", None));
        ___qtablewidgetitem29 = self.tabla_sexto_5.horizontalHeaderItem(1)
        ___qtablewidgetitem29.setText(QCoreApplication.translate("Dialog", u"Primer Apellido", None));
        ___qtablewidgetitem30 = self.tabla_sexto_5.horizontalHeaderItem(2)
        ___qtablewidgetitem30.setText(QCoreApplication.translate("Dialog", u"Segundo Apellido", None));
        ___qtablewidgetitem31 = self.tabla_sexto_5.horizontalHeaderItem(3)
        ___qtablewidgetitem31.setText(QCoreApplication.translate("Dialog", u"Curso", None));
        ___qtablewidgetitem32 = self.tabla_sexto_5.horizontalHeaderItem(4)
        ___qtablewidgetitem32.setText(QCoreApplication.translate("Dialog", u"Ense\u00f1anza", None));
        ___qtablewidgetitem33 = self.tabla_sexto_5.horizontalHeaderItem(5)
        ___qtablewidgetitem33.setText(QCoreApplication.translate("Dialog", u"Grupo", None));
        ___qtablewidgetitem34 = self.tabla_sexto_5.horizontalHeaderItem(6)
        ___qtablewidgetitem34.setText(QCoreApplication.translate("Dialog", u"Nombre", None));
        self.label_primero.setText(QCoreApplication.translate("Dialog", u"Curso 1\u00ba:", None))
        ___qtablewidgetitem35 = self.tabla_sexto_6.horizontalHeaderItem(0)
        ___qtablewidgetitem35.setText(QCoreApplication.translate("Dialog", u"N\u00famero", None));
        ___qtablewidgetitem36 = self.tabla_sexto_6.horizontalHeaderItem(1)
        ___qtablewidgetitem36.setText(QCoreApplication.translate("Dialog", u"Primer Apellido", None));
        ___qtablewidgetitem37 = self.tabla_sexto_6.horizontalHeaderItem(2)
        ___qtablewidgetitem37.setText(QCoreApplication.translate("Dialog", u"Segundo Apellido", None));
        ___qtablewidgetitem38 = self.tabla_sexto_6.horizontalHeaderItem(3)
        ___qtablewidgetitem38.setText(QCoreApplication.translate("Dialog", u"Curso", None));
        ___qtablewidgetitem39 = self.tabla_sexto_6.horizontalHeaderItem(4)
        ___qtablewidgetitem39.setText(QCoreApplication.translate("Dialog", u"Ense\u00f1anza", None));
        ___qtablewidgetitem40 = self.tabla_sexto_6.horizontalHeaderItem(5)
        ___qtablewidgetitem40.setText(QCoreApplication.translate("Dialog", u"Grupo", None));
        ___qtablewidgetitem41 = self.tabla_sexto_6.horizontalHeaderItem(6)
        ___qtablewidgetitem41.setText(QCoreApplication.translate("Dialog", u"Nombre", None));
    # retranslateUi

    def abrir_ventana_anadir(self):
        self.ventana_anadir_alumnos = VentanaAnadirAlumno()
        self.ventana_anadir_alumnos.show()
        self.ventana_anadir_alumnos.exec_()
        self.limpiar_tablas()
        self.actualiza_todos_alumnos()

    def abrir_ventana_editar(self):
        self.ventana_editar_alumnos = VentanaEditarAlumno()
        self.ventana_editar_alumnos.show()
        self.ventana_editar_alumnos.exec_()
        self.limpiar_tablas()
        self.actualiza_todos_alumnos()

    def abrir_ventana_eliminar(self):
        self.ventana_eliminar_alumnos = VentanaEliminaAlumnos()
        self.ventana_eliminar_alumnos.show()
        self.ventana_eliminar_alumnos.exec_()
        self.limpiar_tablas()
        self.actualiza_todos_alumnos()

    def abrir_ventana_enviar_mensaje(self):
        self.ventana_enviar_mensaje = VentanaMandarMensajeCurso()
        self.ventana_enviar_mensaje.show()
        self.ventana_enviar_mensaje.exec_()
        
    def abrir_ventana_importar(self):
        self.ventana_importar_alumnos = VentanaImportarAlumnos()
        self.ventana_importar_alumnos.show()
        self.ventana_importar_alumnos.exec_()
        self.limpiar_tablas()
        self.actualiza_todos_alumnos()
        
    def actualiza_todos_alumnos(self):
        conector = AlumnoConnector()
        # Primero limpia todas las tablas
        for tabla in self.tablas:
            tabla.setRowCount(0)

        # Conectar a la base de datos y obtener los datos de los alumnos
        alumnos = conector.devuelveTodos()  # Supongamos que esto retorna una lista de diccionarios con los datos de los alumnos
        
        for alumno in alumnos:
            curso = alumno[3]
            if curso == "1":
                self.anadir_fila(self.tabla_sexto_6, alumno)
            elif curso == "2":
                self.anadir_fila(self.tabla_sexto_5, alumno)
            elif curso == "3":
                self.anadir_fila(self.tabla_sexto_4, alumno)
            elif curso == "4":
                self.anadir_fila(self.tabla_sexto_3, alumno)
            elif curso == "5":
                self.anadir_fila(self.tabla_sexto_2, alumno)
            elif curso == "6":
                self.anadir_fila(self.tabla_sexto, alumno)
    
    def anadir_fila(self, tabla, alumno):
        rowPosition = tabla.rowCount()
        tabla.insertRow(rowPosition)
        items = [QTableWidgetItem(str(alumno[0])), QTableWidgetItem(alumno[1]),
                 QTableWidgetItem(alumno[2]), QTableWidgetItem(alumno[3]),
                 QTableWidgetItem(alumno[4]), QTableWidgetItem(alumno[5]),
                 QTableWidgetItem(alumno[6])]
        for col, item in enumerate(items):
            item.setTextAlignment(Qt.AlignCenter)
            tabla.setItem(rowPosition, col, item)

    def actualiza_alumnos(self, curso_alumno):
        # Convertir el curso de string a número entero
        curso_alumno_int = int(curso_alumno[:-1])    
        
        # Limpia la tabla del curso antes de actualizarla
        tabla = self.tablas[curso_alumno_int - 1]
        
        # Obtener datos de alumnos del curso actual
        alumno_connector = AlumnoConnector()
        alumnos_curso = alumno_connector.devuelvePorCurso(curso_alumno)
        
        for alumno in alumnos_curso:
                numero, primerApellido, segundoApellido, curso, ensenanza, grupo, nombre = alumno
                # Agregar alumno solo si pertenece al curso
                if alumno[3] == curso_alumno:
                        # Configurar el número de filas en la tabla
                        tabla.setRowCount(tabla.rowCount() + 1)
                        # Llenar la tabla con los datos del alumno
                        row = tabla.rowCount() - 1
                        for col, data in enumerate(alumno):
                                item = QTableWidgetItem(str(data))
                                tabla.setItem(row, col, item)
                                item.setTextAlignment(Qt.AlignCenter)

    # Función para limpiar todas las tablas
    def limpiar_tablas(self):
        for tabla in self.tablas:
            tabla.clearContents()
            tabla.setRowCount(0)
    
class VentanaAnadirAlumno(Ui_Dialog_anadir_alumno, QDialog):
        def __init__(self):
                super(VentanaAnadirAlumno, self).__init__()
                self.setupUi(self, origen='listado')

class VentanaEditarAlumno(Ui_Dialog_editar_alumno, QDialog):
        def __init__(self):
                super(VentanaEditarAlumno, self).__init__()
                self.setupUi(self, origen='listado')
                
class VentanaEliminaAlumnos(Ui_Dialog_eliminaAlumnos, QDialog):
        def __init__(self):
                super(VentanaEliminaAlumnos, self).__init__()
                self.setupUi(self, origen='listado')

class VentanaMandarMensajeCurso(Ui_Dialog_mensaje, QDialog):
    def __init__(self):
        super(VentanaMandarMensajeCurso, self).__init__()
        self.setupUi(self, origen='listado')

class VentanaImportarAlumnos(Ui_Dialog_importar, QDialog):
    def __init__(self):
        super(VentanaImportarAlumnos, self).__init__()
        self.setupUi(self)