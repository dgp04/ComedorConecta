# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'cursos.ui'
##
## Created by: Qt User Interface Compiler version 6.6.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt, Signal)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QMainWindow, QPushButton, QSizePolicy, QSpacerItem, QDialog, QMessageBox,
    QVBoxLayout, QWidget)
from src.resources import *
from curso import *
from listadoAlumnos import *
from ajustesUsuario import *
from listadoPadres import *
import json

class Ui_MainWindow_cursos(QMainWindow, QDialog, object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(750, 688)
        MainWindow.showMaximized( )
        
        with open("config.json", 'r', encoding='utf-8') as json_file:
                data = json.load(json_file)

        self.usuario = data['usuario']
        self.id_usuario = data['id_usuario']
        
        icon = QIcon()
        icon.addFile(u":/logo/iconoProyecto.png", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, -1, 0)
        self.frame_superior = QFrame(self.centralwidget)
        self.frame_superior.setObjectName(u"frame_superior")
        self.frame_superior.setMinimumSize(QSize(0, 60))
        self.frame_superior.setMaximumSize(QSize(16777215, 60))
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


        self.verticalLayout_2.addWidget(self.frame_superior)

        self.frame_inferior = QFrame(self.centralwidget)
        self.frame_inferior.setObjectName(u"frame_inferior")
        font = QFont()
        font.setKerning(True)
        self.frame_inferior.setFont(font)
        self.frame_inferior.setFrameShape(QFrame.StyledPanel)
        self.frame_inferior.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_inferior)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.frame_inferior)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(160, 0))
        self.frame.setMaximumSize(QSize(160, 16777215))
        self.frame.setStyleSheet(u"background-color: #2a5c94;\n"
"border-top-right-radius: 10px;")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.btn_chat = QPushButton(self.frame)
        self.btn_chat.setObjectName(u"btn_chat")
        font1 = QFont()
        font1.setPointSize(12)
        self.btn_chat.setFont(font1)
        self.btn_chat.setHidden(True)
        self.btn_chat.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_chat.setStyleSheet(u"QPushButton{\n"
"border: none;\n"
"background-color: transparent;\n"
"padding: 10px;\n"
"border-radius: 5px;\n"
"color: white;\n"
"font-weight: bold;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(25, 22, 109);\n"
"text-decoration: underline;\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u":/iconosLaterales/chat.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_chat.setIcon(icon1)
        self.btn_chat.setIconSize(QSize(32, 32))

        self.verticalLayout_3.addWidget(self.btn_chat)

        self.btn_alumnos = QPushButton(self.frame)
        self.btn_alumnos.clicked.connect(self.abrir_listado_alumnos)
        self.btn_alumnos.setObjectName(u"btn_alumnos")
        self.btn_alumnos.setFont(font1)
        self.btn_alumnos.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_alumnos.setStyleSheet(u"QPushButton{\n"
"border: none;\n"
"background-color: transparent;\n"
"padding: 10px;\n"
"border-radius: 5px;\n"
"color: white;\n"
"font-weight: bold;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(25, 22, 109);\n"
"text-decoration: underline;\n"
"}")
        icon2 = QIcon()
        icon2.addFile(u":/iconosLaterales/estudiante-icono-png.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_alumnos.setIcon(icon2)
        self.btn_alumnos.setIconSize(QSize(20, 32))

        self.verticalLayout_3.addWidget(self.btn_alumnos)

        self.btn_padres = QPushButton(self.frame)
        self.btn_padres.clicked.connect(self.abrir_ventana_padres)
        self.btn_padres.setObjectName(u"btn_padres")
        self.btn_padres.setFont(font1)
        self.btn_padres.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_padres.setStyleSheet(u"QPushButton{\n"
"border: none;\n"
"background-color: transparent;\n"
"padding: 10px;\n"
"border-radius: 5px;\n"
"color: white;\n"
"font-weight: bold;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(25, 22, 109);\n"
"text-decoration: underline;}")
        icon3 = QIcon()
        icon3.addFile(u":/iconosLaterales/padres.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_padres.setIcon(icon3)
        self.btn_padres.setIconSize(QSize(32, 32))

        self.verticalLayout_3.addWidget(self.btn_padres)

        self.btn_ajustes = QPushButton(self.frame)
        self.btn_ajustes.clicked.connect(self.abrir_ajustes_usuario)
        self.btn_ajustes.setObjectName(u"btn_ajustes")
        self.btn_ajustes.setFont(font1)
        self.btn_ajustes.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_ajustes.setStyleSheet(u"QPushButton{\n"
"border: none;\n"
"background-color: transparent;\n"
"padding: 10px;\n"
"border-radius: 5px;\n"
"color: white;\n"
"font-weight: bold;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(25, 22, 109);\n"
"text-decoration: underline;}")
        icon4 = QIcon()
        icon4.addFile(u":/iconosLaterales/ajustes.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_ajustes.setIcon(icon4)
        self.btn_ajustes.setIconSize(QSize(32, 32))

        self.verticalLayout_3.addWidget(self.btn_ajustes)

        self.verticalSpacer = QSpacerItem(20, 250, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_3.addItem(self.verticalSpacer)

        self.btn_logout = QPushButton(self.frame)
        self.btn_logout.setObjectName(u"btn_logout")
        self.btn_logout.setFont(font1)
        self.btn_logout.clicked.connect(self.cerrar)
        self.btn_logout.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_logout.setStyleSheet(u"QPushButton{\n"
"border: none;\n"
"background-color: transparent;\n"
"padding: 10px;\n"
"border-radius: 5px;\n"
"color: white;\n"
"font-weight: bold;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(25, 22, 109);\n"
"text-decoration: underline;\n"
"}")
        icon5 = QIcon()
        icon5.addFile(u":/iconosLaterales/cierre.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_logout.setIcon(icon5)
        self.btn_logout.setIconSize(QSize(25, 25))

        self.verticalLayout_3.addWidget(self.btn_logout)


        self.horizontalLayout_2.addWidget(self.frame)

        self.frame_2 = QFrame(self.frame_inferior)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_2)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.btn_sexto = QPushButton(self.frame_2)
        self.btn_sexto.setObjectName(u"btn_sexto")
        self.btn_sexto.clicked.connect(lambda: self.abrir_curso('6'))
        self.btn_sexto.setMaximumSize(QSize(1570, 16777215))
        self.btn_sexto.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_sexto.setStyleSheet(u"QPushButton{\n"
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

        self.verticalLayout_4.addWidget(self.btn_sexto)

        self.btn_quinto = QPushButton(self.frame_2)
        self.btn_quinto.setObjectName(u"btn_quinto")
        self.btn_quinto.clicked.connect(lambda: self.abrir_curso('5'))
        self.btn_quinto.setMaximumSize(QSize(1570, 16777215))
        self.btn_quinto.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_quinto.setStyleSheet(u"QPushButton{\n"
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

        self.verticalLayout_4.addWidget(self.btn_quinto)

        self.btn_cuarto = QPushButton(self.frame_2)
        self.btn_cuarto.setObjectName(u"btn_cuarto")
        self.btn_cuarto.clicked.connect(lambda: self.abrir_curso('4'))
        self.btn_cuarto.setMaximumSize(QSize(1570, 16777215))
        self.btn_cuarto.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_cuarto.setStyleSheet(u"QPushButton{\n"
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

        self.verticalLayout_4.addWidget(self.btn_cuarto)

        self.btn_tercero = QPushButton(self.frame_2)
        self.btn_tercero.clicked.connect(lambda: self.abrir_curso('3'))
        self.btn_tercero.setObjectName(u"btn_tercero")
        self.btn_tercero.setMaximumSize(QSize(1570, 16777215))
        self.btn_tercero.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_tercero.setStyleSheet(u"QPushButton{\n"
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

        self.verticalLayout_4.addWidget(self.btn_tercero)

        self.btn_segundo = QPushButton(self.frame_2)
        self.btn_segundo.setObjectName(u"btn_segundo")
        self.btn_segundo.clicked.connect(lambda: self.abrir_curso('2'))
        self.btn_segundo.setMaximumSize(QSize(1570, 16777215))
        self.btn_segundo.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_segundo.setStyleSheet(u"QPushButton{\n"
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

        self.verticalLayout_4.addWidget(self.btn_segundo)

        self.btn_primero = QPushButton(self.frame_2)
        self.btn_primero.setObjectName(u"btn_primero")
        self.btn_primero.clicked.connect(lambda: self.abrir_curso('1'))
        self.btn_primero.setMaximumSize(QSize(1570, 16777215))
        self.btn_primero.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_primero.setStyleSheet(u"QPushButton{\n"
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

        self.verticalLayout_4.addWidget(self.btn_primero)
       
        self.horizontalLayout_2.addWidget(self.frame_2)

        self.verticalLayout_2.addWidget(self.frame_inferior)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Cursos", None))
        self.label_logo.setText("")
        self.btn_chat.setText(QCoreApplication.translate("MainWindow", u"CHAT", None))
        self.btn_alumnos.setText(QCoreApplication.translate("MainWindow", u"Alumnos", None))
        self.btn_padres.setText(QCoreApplication.translate("MainWindow", u"Padres", None))
        self.btn_ajustes.setText(QCoreApplication.translate("MainWindow", u"Ajustes", None))
        self.btn_logout.setText(QCoreApplication.translate("MainWindow", u"Log out", None))
        self.btn_sexto.setText(QCoreApplication.translate("MainWindow", u"Curso 6\u00ba", None))
        self.btn_quinto.setText(QCoreApplication.translate("MainWindow", u"Curso 5\u00ba", None))
        self.btn_cuarto.setText(QCoreApplication.translate("MainWindow", u"Curso 4\u00ba", None))
        self.btn_tercero.setText(QCoreApplication.translate("MainWindow", u"Curso 3\u00ba", None))
        self.btn_segundo.setText(QCoreApplication.translate("MainWindow", u"Curso 2\u00ba", None))
        self.btn_primero.setText(QCoreApplication.translate("MainWindow", u"Curso 1\u00ba", None))
    # retranslateUi

    def cerrar(self):
        QMessageBox.information(self, 'Cierre de sesión', 'Se ha cerrado sesión. Vuelva a abrir la aplicación si quiere seguir usándola.')
        self.close()
        
    def abrir_curso(self, curso):
        self.hide()
        data = {"id_usuario": self.id_usuario, "usuario": self.usuario, "curso": curso}

        with open("config.json", "w", encoding='utf-8') as json_file:
                json.dump(data, json_file)
        
        self.ventana_curso = VentanaCurso()
        self.ventana_curso.showMaximized()
        self.ventana_curso.exec()
        self.show()

    def abrir_listado_alumnos(self):
        self.ventana_listado_alumnos = VentanaListadoAlumnos()
        self.ventana_listado_alumnos.showMaximized()
        self.ventana_listado_alumnos.exec_()
        self.show()
        
    def abrir_ajustes_usuario(self):
        self.ventana_ajustes_usuario = VentanaAjustesUsuario()
        self.ventana_ajustes_usuario.show()
        self.ventana_ajustes_usuario.exec_()
        self.show()
        
    def abrir_ventana_padres(self):
        self.ventana_listado_padres = VentanaListadoPadres()
        self.ventana_listado_padres.showMaximized()
        self.ventana_listado_padres.exec_()
        self.show()

class VentanaCurso(Ui_Dialog_curso, QDialog):
        def __init__(self):
                super(VentanaCurso, self).__init__()
                self.setupUi(self)

class VentanaListadoAlumnos(Ui_Dialog_listadoAlumnos, QDialog):
        def __init__(self):
                super(VentanaListadoAlumnos, self).__init__()
                self.setupUi(self)

class VentanaAjustesUsuario(Ui_Dialog_ajustes, QDialog):
        def __init__(self):
                super(VentanaAjustesUsuario, self).__init__()
                self.setupUi(self)

class VentanaListadoPadres(Ui_Dialog_listado_padres, QDialog):
        def __init__(self):
                super(VentanaListadoPadres, self).__init__()
                self.setupUi(self)