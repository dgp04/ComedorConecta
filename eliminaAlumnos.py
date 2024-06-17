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
from Connector.AlumnoConnector import *
import json 

class Ui_Dialog_eliminaAlumnos(QDialog, object):
    def setupUi(self, Dialog, origen):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(858, 416)
        
        with open('config.json', 'r')as json_file:
            data = json.load(json_file)
         
        self.curso = data['curso'] 
        
        self.origen = origen
        
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
"font-size: 16px;\n"
"font-weight: bold;\n"
"color: #2a5c94;\n"
"}")

        self.verticalLayout.addWidget(self.label)

        self.tableWidget = QTableWidget(Dialog)
        if (self.tableWidget.columnCount() < 8):
            self.tableWidget.setColumnCount(8)
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
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setStyleSheet(u"QTableWidget, QHeaderView::section{\n"
"background-color: transparent;\n"
"}\n"
"")
        self.tableWidget.horizontalHeader().setDefaultSectionSize(163)
        self.mostrar_alumnos()
        
        # Ajustar el ancho de la última columna para llenar el espacio restante
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.setColumnWidth(7, 2)  # Ajusta según el tamaño necesario para el checkbox
        
        self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Interactive)  # Permite ajustar manualmente
        self.tableWidget.horizontalHeader().setSectionResizeMode(0, QHeaderView.Stretch)  # NRE
        self.tableWidget.horizontalHeader().setSectionResizeMode(1, QHeaderView.Stretch)  # Nombre
        self.tableWidget.horizontalHeader().setSectionResizeMode(2, QHeaderView.Stretch)  # Curso
        self.tableWidget.horizontalHeader().setSectionResizeMode(3, QHeaderView.Stretch)  # Clase
        self.tableWidget.horizontalHeader().setSectionResizeMode(4, QHeaderView.Stretch)
        self.tableWidget.horizontalHeader().setSectionResizeMode(5, QHeaderView.Stretch)
        self.tableWidget.horizontalHeader().setSectionResizeMode(6, QHeaderView.Stretch)
        self.tableWidget.horizontalHeader().setSectionResizeMode(7, QHeaderView.ResizeToContents)  # Seleccionar
        
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
            self.tableWidget.setItem(row, 7, checkbox_item)  # La columna 5 es para los checkboxes

        self.verticalLayout.addWidget(self.tableWidget)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(-1, 5, -1, 5)
        self.pushButton = QPushButton(Dialog)
        self.pushButton.clicked.connect(self.eliminarAlumnos)
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
"padding: 5px 15px;\n"
"border: 2px solid #2a5c94;\n"
"border-radius: 5px;\n"
"font-size: 16px;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: #2a5c94;\n"
"color: white;\n"
"}")

        self.horizontalLayout_2.addWidget(self.pushButton)


        self.verticalLayout.addLayout(self.horizontalLayout_2)


        self.verticalLayout_2.addLayout(self.verticalLayout)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Eliminar alumnos", None))
        self.label_logo.setText("")
        self.label.setText(QCoreApplication.translate("Dialog", u"Selecciona los alumnos que desea eliminar:", None))
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
        ___qtablewidgetitem7 = self.tableWidget.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("Dialog", u"", None));
        self.pushButton.setText(QCoreApplication.translate("Dialog", u"Eliminar alumno/s", None))
    # retranslateUi

    def mostrar_alumnos(self):
        conector = AlumnoConnector()
        if self.origen == 'curso':
            # Obtener datos de alumnos del curso actual
            alumnos_curso = conector.devuelvePorCurso(self.curso)
            # Configurar el número de filas en la tabla
            self.tableWidget.setRowCount(len(alumnos_curso))
            # Llenar la tabla con los datos de los alumnos
            for row, alumno in enumerate(alumnos_curso):
                for col, data in enumerate(alumno):
                    item = QTableWidgetItem(str(data))
                    self.tableWidget.setItem(row, col, item)
                    item.setTextAlignment(Qt.AlignCenter)
        elif self.origen == 'listado':
            alumnos = conector.devuelveTodos()
            # Configurar el número de filas en la tabla
            self.tableWidget.setRowCount(len(alumnos))
            # Llenar la tabla con los datos de los alumnos
            for row, alumno in enumerate(alumnos):
                for col, data in enumerate(alumno):
                    item = QTableWidgetItem(str(data))
                    self.tableWidget.setItem(row, col, item)
                    item.setTextAlignment(Qt.AlignCenter)

    def eliminarAlumnos(self):
        try:
            numeros = self.obtener_alumnos_seleccionados()
            conector = AlumnoConnector()
            conector.eliminar_alumnos_seleccionados(numeros)
            
            # Eliminar filas de la tabla correspondientes a los alumnos eliminados
            for row in range(self.tableWidget.rowCount()):
                num_actual = self.tableWidget.item(row, 1).text()  # NRE en la columna 1
                if num_actual in numeros:
                    self.tableWidget.removeRow(row)
            QMessageBox.information(self, 'Éxito', 'Los alumnos han sido eliminados correctamente.')
            self.close()
        except Exception as e:
            QMessageBox.critical(self, 'Error', f'Error al eliminar los alumnos: {str(e)}')
            self.close()
        
    def obtener_alumnos_seleccionados(self):
        nres = []
        for row in range(self.tableWidget.rowCount()):
            checkbox_item = self.tableWidget.item(row, 7)  # Obtener el ítem del checkbox
            if checkbox_item and checkbox_item.checkState() == Qt.Checked:
                nre = self.tableWidget.item(row, 0).text()  # Suponiendo que la columna 1 tiene el NRE
                nres.append(nre)
        return nres