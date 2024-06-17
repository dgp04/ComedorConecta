from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QDialog, QWidget
from login import *

class VentanaPrincipal(Ui_Dialog_login, QDialog):
    def __init__(self):
        super(VentanaPrincipal, self).__init__()
        self.setupUi(self)

app = QApplication([])
ventana = VentanaPrincipal()
ventana.show()
app.exec()  