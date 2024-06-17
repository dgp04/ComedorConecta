# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'eliminarMadres.ui'
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
    QHeaderView, QLabel, QPushButton, QSizePolicy, QMessageBox,
    QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget)
from src.resources import *
from Connector.MadreConnector import *

class Ui_Dialog_eliminar_padres(QDialog, object):
    def setupUi(self, Dialog_eliminar_padres):
        if not Dialog_eliminar_padres.objectName():
            Dialog_eliminar_padres.setObjectName(u"Dialog_eliminar_padres")
        Dialog_eliminar_padres.resize(858, 416)
        icon = QIcon()
        icon.addFile(u":/logo/iconoProyecto.png", QSize(), QIcon.Normal, QIcon.Off)
        Dialog_eliminar_padres.setWindowIcon(icon)
        self.verticalLayout_2 = QVBoxLayout(Dialog_eliminar_padres)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame_superior = QFrame(Dialog_eliminar_padres)
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

        self.label = QLabel(Dialog_eliminar_padres)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"QLabel{\n"
"font-size: 16px;\n"
"font-weight: bold;\n"
"color: #2a5c94;\n"
"}")

        self.verticalLayout.addWidget(self.label)

        self.tableWidget = QTableWidget(Dialog_eliminar_padres)
        if (self.tableWidget.columnCount() < 6):
            self.tableWidget.setColumnCount(6)
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
        self.tableWidget.setObjectName(u"tableWidget")
        
        self.tableWidget.horizontalHeader().setDefaultSectionSize(163)
        self.mostrar_madres()
        
        # Ajustar el ancho de la última columna para llenar el espacio restante
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.setColumnWidth(5, 2)  # Ajusta según el tamaño necesario para el checkbox
        
        self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Interactive)  # Permite ajustar manualmente
        self.tableWidget.horizontalHeader().setSectionResizeMode(0, QHeaderView.Stretch)  # NRE
        self.tableWidget.horizontalHeader().setSectionResizeMode(1, QHeaderView.Stretch)  # Nombre
        self.tableWidget.horizontalHeader().setSectionResizeMode(2, QHeaderView.Stretch)  # Curso
        self.tableWidget.horizontalHeader().setSectionResizeMode(3, QHeaderView.Stretch)  # Clase
        self.tableWidget.horizontalHeader().setSectionResizeMode(4, QHeaderView.Stretch)  # Padre/Madre
        self.tableWidget.horizontalHeader().setSectionResizeMode(5, QHeaderView.ResizeToContents)  # Seleccionar
        
        self.tableWidget.setStyleSheet("""
QTableView::item {
    border: none;
}
QHeaderView::section {
    border: 1px solid black;
}
QTableView::item:nth-child(6) {
    border: none;
}
""")

        
        # Supongamos que has llenado la tabla con los datos de los alumnos
        for row in range(self.tableWidget.rowCount()):
            checkbox_item = QTableWidgetItem()
            checkbox_item.setCheckState(Qt.Unchecked)
            self.tableWidget.setItem(row, 5, checkbox_item)  # La columna 5 es para los checkboxes

        self.verticalLayout.addWidget(self.tableWidget)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(-1, 5, -1, 5)
        self.btn_eliminar = QPushButton(Dialog_eliminar_padres)
        self.btn_eliminar.clicked.connect(self.eliminarPadres)
        self.btn_eliminar.setObjectName(u"btn_eliminar")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_eliminar.sizePolicy().hasHeightForWidth())
        self.btn_eliminar.setSizePolicy(sizePolicy)
        self.btn_eliminar.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_eliminar.setStyleSheet(u"QPushButton{\n"
"background-color: #ffffff;\n"
"color: #2a5c94;\n"
"padding: 5px 15px;\n"
"border: 2px solid #2a5c94;\n"
"border-radius: 5px;\n"
"font-size: 16px;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: #2a5c94;\n"
"color: white;\n"
"}")

        self.horizontalLayout_2.addWidget(self.btn_eliminar)


        self.verticalLayout.addLayout(self.horizontalLayout_2)


        self.verticalLayout_2.addLayout(self.verticalLayout)


        self.retranslateUi(Dialog_eliminar_padres)

        QMetaObject.connectSlotsByName(Dialog_eliminar_padres)
    # setupUi

    def retranslateUi(self, Dialog_eliminar_padres):
        Dialog_eliminar_padres.setWindowTitle(QCoreApplication.translate("Dialog_eliminar_padres", u"Eliminar padres/madres", None))
        self.label_logo.setText("")
        self.label.setText(QCoreApplication.translate("Dialog_eliminar_padres", u"Selecciona las madres que desea eliminar:", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Dialog_eliminar_padres", u"ID", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Dialog_eliminar_padres", u"Nombre", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Dialog_eliminar_padres", u"Nº Hijo", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Dialog_eliminar_padres", u"Email", None));
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("Dialog_eliminar_padres", u"Direcci\u00f3n", None));
        ___qtablewidgetitem5 = self.tableWidget.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("Dialog", u"", None));
        self.btn_eliminar.setText(QCoreApplication.translate("Dialog_eliminar_padres", u"Eliminar madre/s", None))
    # retranslateUi

    def mostrar_madres(self):
        conector = MadreConnector()
        madres = conector.devuelveTodos()
        # Configurar el número de filas en la tabla
        self.tableWidget.setRowCount(len(madres))
        # Llenar la tabla con los datos de los alumnos
        for row, madre in enumerate(madres):
            for col, data in enumerate(madre):
                item = QTableWidgetItem(str(data))
                self.tableWidget.setItem(row, col, item)
                item.setTextAlignment(Qt.AlignCenter)
                
    def obtener_padres_seleccionados(self):
        ids = []
        for row in range(self.tableWidget.rowCount()):
            checkbox_item = self.tableWidget.item(row, 5)  # Obtener el ítem del checkbox
            if checkbox_item and checkbox_item.checkState() == Qt.Checked:
                id_padre = self.tableWidget.item(row, 0).text()  # Suponiendo que la columna 1 tiene el NRE
                ids.append(id_padre)
        return ids
    
    def eliminarPadres(self):
        reply = QMessageBox.question(self, 'Error', '¿Está seguro de que desea eliminar los padres seleccionados?', QMessageBox.Yes | QMessageBox.No)
        
        if reply == QMessageBox.Yes:
            try:
                ids = self.obtener_padres_seleccionados()
                conector = MadreConnector()
                conector.eliminar_padres_seleccionados(ids)
                
                # Eliminar filas de la tabla correspondientes a los alumnos eliminados
                for row in range(self.tableWidget.rowCount()):
                    id_actual = self.tableWidget.item(row, 1).text()  # NRE en la columna 1
                    if id_actual in ids:
                        self.tableWidget.removeRow(row)
                QMessageBox.information(self, 'Éxito', 'Los padres seleccionados han sido eliminados correctamente.')
                self.close()
            except Exception as e:
                QMessageBox.critical(self, 'Error', f'Error al eliminar los padres: {str(e)}')
                self.close()
        