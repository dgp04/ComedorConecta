# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'cursoMadre.ui'
##
## Created by: Qt User Interface Compiler version 6.6.3
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
from Connector.MadreConnector import *
from editarMadre import *
from eliminarMadres import *
from anadirMadre import *

class Ui_Dialog_listado_padres(QDialog, object):
    def setupUi(self, Dialog_listadp_padres):
        if not Dialog_listadp_padres.objectName():
            Dialog_listadp_padres.setObjectName(u"Dialog_listadp_padres")
        Dialog_listadp_padres.resize(842, 615)
        icon = QIcon()
        icon.addFile(u":/logo/iconoProyecto.png", QSize(), QIcon.Normal, QIcon.Off)
        Dialog_listadp_padres.setWindowIcon(icon)
        self.verticalLayout_2 = QVBoxLayout(Dialog_listadp_padres)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame_superior = QFrame(Dialog_listadp_padres)
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

        self.label = QLabel(Dialog_listadp_padres)
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
        self.btn_volver_atras = QPushButton(Dialog_listadp_padres)
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

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.btn_anadir_padres = QPushButton(Dialog_listadp_padres)
        self.btn_anadir_padres.clicked.connect(self.abrir_anadir_madre)
        self.btn_anadir_padres.setObjectName(u"btn_anadir_padres")
        sizePolicy.setHeightForWidth(self.btn_anadir_padres.sizePolicy().hasHeightForWidth())
        self.btn_anadir_padres.setSizePolicy(sizePolicy)
        self.btn_anadir_padres.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_anadir_padres.setStyleSheet(u"QPushButton{\n"
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
        self.btn_anadir_padres.setIcon(icon1)

        self.horizontalLayout_2.addWidget(self.btn_anadir_padres)

        self.btn_editar_padres = QPushButton(Dialog_listadp_padres)
        self.btn_editar_padres.clicked.connect(self.abrir_editar_madre)
        self.btn_editar_padres.setObjectName(u"btn_editar_padres")
        sizePolicy.setHeightForWidth(self.btn_editar_padres.sizePolicy().hasHeightForWidth())
        self.btn_editar_padres.setSizePolicy(sizePolicy)
        self.btn_editar_padres.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_editar_padres.setStyleSheet(u"QPushButton{\n"
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
        self.btn_editar_padres.setIcon(icon2)

        self.horizontalLayout_2.addWidget(self.btn_editar_padres)

        self.btn_eliminar_padres = QPushButton(Dialog_listadp_padres)
        self.btn_eliminar_padres.clicked.connect(self.abrir_eliminar_padres)
        self.btn_eliminar_padres.setObjectName(u"btn_eliminar_padres")
        sizePolicy.setHeightForWidth(self.btn_eliminar_padres.sizePolicy().hasHeightForWidth())
        self.btn_eliminar_padres.setSizePolicy(sizePolicy)
        self.btn_eliminar_padres.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_eliminar_padres.setStyleSheet(u"QPushButton{\n"
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
        self.btn_eliminar_padres.setIcon(icon3)

        self.horizontalLayout_2.addWidget(self.btn_eliminar_padres)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.tableWidget = QTableWidget(Dialog_listadp_padres)
        if (self.tableWidget.columnCount() < 5):
            self.tableWidget.setColumnCount(5)
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
        
        self.actualiza_madres()
        
        # Ajustar el ancho de la última columna para llenar el espacio restante
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)


        self.verticalLayout.addWidget(self.tableWidget)


        self.verticalLayout_2.addLayout(self.verticalLayout)


        self.retranslateUi(Dialog_listadp_padres)

        QMetaObject.connectSlotsByName(Dialog_listadp_padres)
    # setupUi

    def retranslateUi(self, Dialog_listadp_padres):
        Dialog_listadp_padres.setWindowTitle(QCoreApplication.translate("Dialog_listadp_padres", u"Listado de padres y madres", None))
        self.label_logo.setText("")
        self.label.setText(QCoreApplication.translate("Dialog_listadp_padres", u"Listado de padres y madres", None))
        self.btn_volver_atras.setText(QCoreApplication.translate("Dialog_listadp_padres", u"Volver atr\u00e1s", None))
        self.btn_anadir_padres.setText(QCoreApplication.translate("Dialog_listadp_padres", u"A\u00f1adir madre", None))
        self.btn_editar_padres.setText(QCoreApplication.translate("Dialog_listadp_padres", u"Editar madre", None))
        self.btn_eliminar_padres.setText(QCoreApplication.translate("Dialog_listadp_padres", u"Eliminar madre", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Dialog_listadp_padres", u"ID", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Dialog_listadp_padres", u"Nombre", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Dialog_listadp_padres", u"Nº Hijo", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Dialog_listadp_padres", u"Email", None));
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("Dialog_listadp_padres", u"Direcci\u00f3n", None));
    # retranslateUi

    def abrir_anadir_madre(self):
        self.ventana_anadir_madre = VentanaAnadirMadre()
        self.ventana_anadir_madre.show()
        self.ventana_anadir_madre.exec_()
        self.actualiza_madres()
    
    def abrir_editar_madre(self):
        self.ventana_editar_madre = VentanaEditarMadre()
        self.ventana_editar_madre.show()
        self.ventana_editar_madre.exec_()
        self.actualiza_madres()
    
    def abrir_eliminar_padres(self):
        self.ventana_eliminar_padres = VentanaEliminarMadre()
        self.ventana_eliminar_padres.show()
        self.ventana_eliminar_padres.exec_()
        self.actualiza_madres()
        
    def actualiza_madres(self):
        # Obtener datos de madres del curso actual
        madre_connector = MadreConnector()
        madres_curso = madre_connector.devuelveTodos()
        # Configurar el número de filas en la tabla
        self.tableWidget.setRowCount(len(madres_curso))
        # Llenar la tabla con los datos de los alumnos
        for row, madre in enumerate(madres_curso):
            for col, data in enumerate(madre):
                item = QTableWidgetItem(str(data))
                self.tableWidget.setItem(row, col, item)
                item.setTextAlignment(Qt.AlignCenter)
 
class VentanaAnadirMadre(Ui_Dialog_anadir_padres, QDialog):
    def __init__(self):
        super(VentanaAnadirMadre, self).__init__()
        self.setupUi(self)

class VentanaEditarMadre(Ui_Dialog_editar_padres, QDialog):
    def __init__(self):
        super(VentanaEditarMadre, self).__init__()
        self.setupUi(self)

class VentanaEliminarMadre(Ui_Dialog_eliminar_padres, QDialog):
    def __init__(self):
        super(VentanaEliminarMadre, self).__init__()
        self.setupUi(self)