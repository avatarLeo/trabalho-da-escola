# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from menuPrimcipal import Ui_janelaPrincipal
import banco
import sys


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(302, 195)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        # button =======================================================================
        self.btn_entrar = QtWidgets.QPushButton(self.centralwidget)
        self.btn_entrar.setGeometry(QtCore.QRect(30, 120, 75, 23))
        self.btn_entrar.setObjectName("btn_entrar")
        self.btn_entrar.setIcon(QtGui.QIcon("escola.png"))
        self.btn_entrar.clicked.connect(self.entrar)

        self.btn_cancelar = QtWidgets.QPushButton(self.centralwidget)
        self.btn_cancelar.setGeometry(QtCore.QRect(140, 120, 75, 23))
        self.btn_cancelar.setObjectName("btn_cancelar")
        self.btn_cancelar.clicked.connect(self.sair)

        #linetext ===========================================================================
        self.txt_login = QtWidgets.QLineEdit(self.centralwidget)
        self.txt_login.setGeometry(QtCore.QRect(100, 30, 113, 20))
        self.txt_login.setObjectName("txt_login")

        self.txt_senha = QtWidgets.QLineEdit(self.centralwidget)
        self.txt_senha.setGeometry(QtCore.QRect(100, 70, 113, 20))
        self.txt_senha.setObjectName("txt_senha")
        self.txt_senha.setEchoMode(QtWidgets.QLineEdit.Password)

        #label ============================================================================
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 30, 47, 13))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(30, 70, 47, 13))
        self.label_2.setObjectName("label_2")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def sair(self):
        sys.exit()

    def entrar(self):
        self.log = self.txt_login.text()
        self.sen = self.txt_senha.text()
        if self.log == "aluno" and self.sen == "aluno":
            self.jan_principal = QtWidgets.QMainWindow()
            self.ui = Ui_janelaPrincipal()
            self.ui.setupUi(self.jan_principal)
            MainWindow.hide()
            self.jan_principal.show()


            self.aviso1 = banco.criarBanco()
            self.aviso2 = banco.criarTabela()
            self.aviso3 = banco.criarCursos()
            self.aviso4 = banco.criarEstuda()
            self.aviso5 = banco.registrarCursos()

            if self.aviso1 != None or self.aviso2 != None:
                msg = QtWidgets.QMessageBox.warning(self.jan_principal,'Aviso', str(self.aviso1)+str(self.aviso2))
        else:
            msg = QtWidgets.QMessageBox.warning(MainWindow,'erro', 'Login ou senha incorreto! ')

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btn_entrar.setText(_translate("MainWindow", "Entrar"))
        self.btn_cancelar.setText(_translate("MainWindow", "Cancelar"))
        self.label.setText(_translate("MainWindow", "Login"))
        self.label_2.setText(_translate("MainWindow", "Senha"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
