# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'user_pass_messagepoazgr.ui'
##
## Created by: Qt User Interface Compiler version 6.4.3
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
from PySide6.QtWidgets import (QApplication, QComboBox, QLabel, QLineEdit,
    QMainWindow, QPushButton, QSizePolicy, QWidget, QMessageBox)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(297, 150)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(30, 20, 49, 16))
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, 50, 71, 16))
        self.comboBox = QComboBox(self.centralwidget)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setGeometry(QRect(80, 20, 69, 22))
        self.lineEdit = QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(80, 50, 113, 22))
        self.lineEdit.setEchoMode(QLineEdit.Password)
        self.btnEntrar = QPushButton(self.centralwidget)
        self.btnEntrar.setObjectName(u"btnEntrar")
        self.btnEntrar.setGeometry(QRect(60, 80, 75, 24))
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        # Conexión de señal clicked a slot o método
        self.btnEntrar.clicked.connect(self.mensajeBienvenida)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    # Desarrollo del método que maneja el evento
    def mensajeBienvenida(self):
        if self.comboBox.currentText() == "Lara" and self.lineEdit.text() == "abc123.":
            QMessageBox.information(MainWindow, 'Bienvenido', 'El usuario y contraseña son válidos')
        else:
            QMessageBox.information(MainWindow, 'Rechazado', 'Prueba con "Lara" y "abc123."')

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Login", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Usuario:", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Contrase\u00f1a:", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Luis", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Marta", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"Mar\u00eda", None))
        self.comboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"Selene", None))
        self.comboBox.setItemText(4, QCoreApplication.translate("MainWindow", u"Lara", None))
        self.comboBox.setItemText(5, QCoreApplication.translate("MainWindow", u"Manuel", None))

        self.btnEntrar.setText(QCoreApplication.translate("MainWindow", u"Entrar", None))
    # retranslateUi



if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())