# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mandarMensaje.ui'
##
## Created by: Qt User Interface Compiler version 6.7.1
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDialog, QFrame,
    QHBoxLayout, QHeaderView, QLabel, QPushButton, QMessageBox,
    QSizePolicy, QSpacerItem, QTableWidget, QTableWidgetItem,
    QVBoxLayout, QWidget)
from src.resources import *
from Connector.AlumnoConnector import *
import json
import base64
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
import os.path
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

class Ui_Dialog_mensaje(QDialog, object):
    def setupUi(self, Dialog, origen):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(870, 446)
        icon = QIcon()
        icon.addFile(u":/logo/iconoProyecto.png", QSize(), QIcon.Normal, QIcon.Off)
        Dialog.setWindowIcon(icon)
        
        with open('config.json', 'r', encoding='utf-8') as json_file:
            data = json.load(json_file)
        
        self.curso = data['curso']
        self.origen = origen
        
        # Archivo JSON de credenciales descargado desde la Consola de Desarrolladores de Google
        self.credenciales_archivo = os.path.join(os.path.dirname(__file__), 'credentials.json')

        # Alcance de la API de Gmail
        self.alcance = ['https://www.googleapis.com/auth/gmail.send']
        
        self.verticalLayout_2 = QVBoxLayout(Dialog)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame_superior = QFrame(Dialog)
        self.frame_superior.setObjectName(u"frame_superior")
        self.frame_superior.setMinimumSize(QSize(0, 60))
        self.frame_superior.setMaximumSize(QSize(16777215, 60))
        self.frame_superior.setStyleSheet(u"")
        self.frame_superior.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_superior.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_superior)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(-1, -1, -1, 0)
        self.label_logo = QLabel(self.frame_superior)
        self.label_logo.setObjectName(u"label_logo")
        self.label_logo.setMaximumSize(QSize(120, 150))
        self.label_logo.setPixmap(QPixmap(u":/logo/logoProyecto.png"))
        self.label_logo.setScaledContents(True)
        self.label_logo.setAlignment(Qt.AlignmentFlag.AlignCenter)

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

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)

        self.box_seleccion_mensaje = QComboBox(Dialog)
        self.box_seleccion_mensaje.addItem("")
        self.box_seleccion_mensaje.addItem("")
        self.box_seleccion_mensaje.addItem("")
        self.box_seleccion_mensaje.addItem("")
        self.box_seleccion_mensaje.addItem("")
        self.box_seleccion_mensaje.addItem("")
        self.box_seleccion_mensaje.addItem("")
        self.box_seleccion_mensaje.setObjectName(u"box_seleccion_mensaje")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.box_seleccion_mensaje.sizePolicy().hasHeightForWidth())
        self.box_seleccion_mensaje.setSizePolicy(sizePolicy)
        font = QFont()
        font.setPointSize(12)
        self.box_seleccion_mensaje.setFont(font)
        self.box_seleccion_mensaje.setCursor(QCursor(Qt.PointingHandCursor))
        self.box_seleccion_mensaje.setStyleSheet(u"QComboBox{\n"
"background-color: transparent;\n"
"color: #2a5c94;\n"
"border: 2px solid #2a5c94;\n"
"border-radius: 5px;\n"
"padding: 5px;\n"
"}\n"
"QComboBox:hover{\n"
"background-color: #2a5c94;\n"
"color: white;\n"
"}")

        self.horizontalLayout_3.addWidget(self.box_seleccion_mensaje)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

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
        self.tableWidget.horizontalHeader().setSectionResizeMode(4, QHeaderView.Stretch)  # Padre/Madre
        self.tableWidget.horizontalHeader().setSectionResizeMode(5, QHeaderView.Stretch)  # Padre/Madre
        self.tableWidget.horizontalHeader().setSectionResizeMode(6, QHeaderView.Stretch)  # Padre/Madre
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

        self.verticalLayout.addWidget(self.tableWidget)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(-1, 5, -1, 5)
        self.btn_enviar_mensaje = QPushButton(Dialog)
        self.btn_enviar_mensaje.clicked.connect(self.enviar_correo)
        self.btn_enviar_mensaje.setObjectName(u"btn_enviar_mensaje")
        sizePolicy.setHeightForWidth(self.btn_enviar_mensaje.sizePolicy().hasHeightForWidth())
        self.btn_enviar_mensaje.setSizePolicy(sizePolicy)
        self.btn_enviar_mensaje.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_enviar_mensaje.setStyleSheet(u"QPushButton{\n"
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

        self.horizontalLayout_2.addWidget(self.btn_enviar_mensaje)


        self.verticalLayout.addLayout(self.horizontalLayout_2)


        self.verticalLayout_2.addLayout(self.verticalLayout)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Enviar mensaje", None))
        self.label_logo.setText("")
        self.label.setText(QCoreApplication.translate("Dialog", u"Seleccione el mensaje y los alumnos a cuyos padres desea mandarlo:", None))
        self.box_seleccion_mensaje.setItemText(0, QCoreApplication.translate("Dialog", u"--Seleccione un mensaje--", None))
        self.box_seleccion_mensaje.setItemText(1, QCoreApplication.translate("Dialog", u"El alumno no ha comido nada", None))
        self.box_seleccion_mensaje.setItemText(2, QCoreApplication.translate("Dialog", u"El alumno se ha comido el primer plato pero no ha querido segundo plato", None))
        self.box_seleccion_mensaje.setItemText(3, QCoreApplication.translate("Dialog", u"El alumno no ha comido primer plato pero ha comido segundo plato y postre", None))
        self.box_seleccion_mensaje.setItemText(4, QCoreApplication.translate("Dialog", u"El alumno se ha comido los tres platos y ha terminado casi todo", None))
        self.box_seleccion_mensaje.setItemText(5, QCoreApplication.translate("Dialog", u"El alumno se ha comido todos los platos", None))
        self.box_seleccion_mensaje.setItemText(6, QCoreApplication.translate("Dialog", u"El alumno se ha comido todos los platos y ha querido repetir plato", None))

#if QT_CONFIG(tooltip)
        self.box_seleccion_mensaje.setToolTip(QCoreApplication.translate("Dialog", u"Seleccione el mensaje que desea enviar", None))
#endif // QT_CONFIG(tooltip)
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
        self.btn_enviar_mensaje.setText(QCoreApplication.translate("Dialog", u"Enviar correo/s", None))
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
                    
    def obtener_padres_seleccionados(self):
        conector = AlumnoConnector()
        padres_seleccionados = []
        emails = []

        for row in range(self.tableWidget.rowCount()):
            checkbox_item = self.tableWidget.item(row, 7)  # La columna 5 es para los checkboxes

            if checkbox_item is not None and checkbox_item.checkState() == Qt.Checked:
                num_alumno = self.tableWidget.item(row, 0).text()  # La columna 0 es para el NRE
                padre = conector.devuelvePadrePorNumeroHijo(num_alumno)  # Suponiendo que hay una función devuelvePadrePorNRE en AlumnoConnector
                if padre:
                    padres_seleccionados.append(padre)
        
        for padre in padres_seleccionados:
            emails.append(padre[3])

        return emails
    
    # Función para enviar un correo electrónico utilizando la API de Gmail
    def enviar_correo(self):
        destinatarios = self.obtener_padres_seleccionados()
        asunto = 'Mensaje del comedor escolar'
        cuerpo = f'Este ha sido hoy el comportamiento de tu hijo/a en el comedor: {self.box_seleccion_mensaje.currentText()}'
        cantidad_correos = 0
        
        for destinatario in destinatarios:
            # Crear mensaje de correo electrónico
            mensaje_correo = MIMEMultipart()
            mensaje_correo['From'] = 'me'
            mensaje_correo['To'] = destinatario
            mensaje_correo['Subject'] = asunto
            mensaje_correo.attach(MIMEText(cuerpo, 'plain'))
            credenciales = self.obtener_credenciales()

            # Construir el servicio de Gmail
            servicio_gmail = build('gmail', 'v1', credentials=credenciales)
            
            mensaje = {'raw': base64.urlsafe_b64encode(mensaje_correo.as_string().encode()).decode()}
            try:
                servicio_gmail.users().messages().send(userId='me', body=mensaje).execute()
                cantidad_correos = cantidad_correos + 1
            except Exception as e:
                QMessageBox.warning(self, 'Error', 'Error al enviar el correo electrónico:', e)
        QMessageBox.information(self, 'Éxito', f'Se han enviado correctamente {cantidad_correos} correos electrónicos.')
        
    
    # Función para obtener credenciales de usuario
    def obtener_credenciales(self):
        credenciales = None

        # Comprobar si ya hay credenciales almacenadas
        if os.path.exists('token.json'):
            credenciales = Credentials.from_authorized_user_file('token.json')

        # Si no hay credenciales válidas disponibles, solicitar al usuario que inicie sesión
        if not credenciales or not credenciales.valid:
            if credenciales and credenciales.expired and credenciales.refresh_token:
                credenciales.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    self.credenciales_archivo, self.alcance)
                credenciales = flow.run_local_server(port=0)

            # Guardar las credenciales para futuros usos
            with open('token.json', 'w') as token:
                token.write(credenciales.to_json())

        return credenciales
