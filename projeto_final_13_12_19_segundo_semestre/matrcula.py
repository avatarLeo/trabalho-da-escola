# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets
import banco
from random import randint
from PyQt5.QtCore import *
import sys

class Ui_jan_matricula(object):
    def setupUi(self, jan_matricula):
        jan_matricula.setObjectName("jan_matricula")
        jan_matricula.resize(637, 494)
        font = QtGui.QFont()
        font.setPointSize(10)
        jan_matricula.setFont(font)
        self.centralwidget = QtWidgets.QWidget(jan_matricula)
        self.centralwidget.setObjectName("centralwidget")


        # font====================================================================================
        font = QtGui.QFont()
        font.setPointSize(12)

        font = QtGui.QFont()
        font.setPointSize(12)

        font = QtGui.QFont()
        font.setPointSize(12)

        font = QtGui.QFont()
        font.setPointSize(12)

        font = QtGui.QFont()
        font.setPointSize(14)

        font = QtGui.QFont()
        font.setPointSize(12)

        font = QtGui.QFont()
        font.setPointSize(12)

        font = QtGui.QFont()
        font.setPointSize(10)

        font = QtGui.QFont()
        font.setPointSize(10)

        # groupBox ===============================================================
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(30, 30, 561, 411))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.label_7 = QtWidgets.QLabel(self.groupBox)
        self.label_7.setGeometry(QtCore.QRect(30, 340, 171, 16))

        self.groupBox_2 = QtWidgets.QGroupBox(self.groupBox)
        self.groupBox_2.setGeometry(QtCore.QRect(390, 50, 141, 131))
        self.groupBox_2.setFont(font)
        self.groupBox_2.setObjectName("groupBox_2")
        font = QtGui.QFont()
        font.setPointSize(12)
        

        #label============================================================
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")

        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(30, 110, 91, 16))
        self.label.setFont(font)
        self.label.setObjectName("label")

        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(30, 30, 47, 13))
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")

        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(30, 190, 121, 16))
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")

        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setGeometry(QtCore.QRect(30, 270, 121, 16))
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")

        #text line ==============================================================================
        self.txt_nome = QtWidgets.QLineEdit(self.groupBox)
        self.txt_nome.setGeometry(QtCore.QRect(30, 50, 321, 31))
        self.txt_nome.setObjectName("txt_nome")

        self.txt_mae = QtWidgets.QLineEdit(self.groupBox)
        self.txt_mae.setGeometry(QtCore.QRect(30, 290, 321, 31))
        self.txt_mae.setObjectName("txt_mae")

        self.txt_endereco = QtWidgets.QLineEdit(self.groupBox)
        self.txt_endereco.setGeometry(QtCore.QRect(30, 130, 321, 31))
        self.txt_endereco.setObjectName("txt_endereco")

        self.txt_pai = QtWidgets.QLineEdit(self.groupBox)
        self.txt_pai.setGeometry(QtCore.QRect(30, 210, 321, 31))
        self.txt_pai.setObjectName("txt_pai")


        #date =========================================================================
        self.date_nascimento = QtWidgets.QDateEdit(self.groupBox)
        self.date_nascimento.setGeometry(QtCore.QRect(30, 360, 131, 31))
        self.date_nascimento.setObjectName("date_nascimento")
        self.date_nascimento.setDate(QtCore.QDate(1954, 7, 7))


       #radio Button ===================================================================
        self.rbt_masculino = QtWidgets.QRadioButton(self.groupBox_2)
        self.rbt_masculino.setGeometry(QtCore.QRect(20, 30, 101, 17))
        self.rbt_masculino.setFont(font)
        self.rbt_masculino.setObjectName("rbt_masculino")
        self.rbt_masculino.setChecked(False)

        self.rbt_feminino = QtWidgets.QRadioButton(self.groupBox_2)
        self.rbt_feminino.setGeometry(QtCore.QRect(20, 80, 101, 17))
        self.rbt_feminino.setFont(font)
        self.rbt_feminino.setObjectName("rbt_feminino")


        #button ====================================================================================
        self.btn_matricula = QtWidgets.QPushButton(self.groupBox)
        self.btn_matricula.setGeometry(QtCore.QRect(400, 200, 75, 61))
        self.btn_matricula.setFont(font)
        self.btn_matricula.setObjectName("btn_matricula")
        self.btn_matricula.clicked.connect(self.salvar)

        jan_matricula.setCentralWidget(self.centralwidget)

        self.retranslateUi(jan_matricula)
        QtCore.QMetaObject.connectSlotsByName(jan_matricula)


    def limparTela(self):
        self.txt_nome.setText("")
        #self.txt_nascimento.setText("")
        self.txt_endereco.setText("")
        self.txt_pai.setText("")
        self.txt_mae.setText("")
        self.rbt_masculino.setChecked(False)
        self.rbt_feminino.setChecked(False)
        self.date_nascimento.setDate(QtCore.QDate(1954, 7, 7))


    def mensagem(self, erro):
        msg = QtWidgets.QMessageBox()
        msg.setWindowTitle("aviso")
        msg.setText(erro)

        x = msg.exec_()


    def salvar(self):
        self.sexo = ""
        if self.rbt_masculino.isChecked() == True:
            self.sexo = "M"
        elif self.rbt_feminino.isChecked() == True:
            self.sexo = "F"
        self.nome = self.txt_nome.text()
        self.data = self.date_nascimento.date()
        self.nascimento = self.data.toString(Qt.ISODate)
        self.endereco = self.txt_endereco.text()
        self.nomePai = self.txt_pai.text()
        self.nomeMae = self.txt_mae.text()
        self.matricula = randint(100, 999)

        if self.nome == "" or self.nascimento == "" or self.endereco == "" or self.nomePai == "" or self.nomeMae == "" or self.sexo == "":
            self.erro = "Preencha todos os campos!"
        else:
            self.limparTela()
            self.erro = banco.cadastrarAluno(self.matricula, self.nome, self.sexo, self.nascimento, self.endereco, self.nomePai, self.nomeMae)

        self.mensagem(self.erro)


    def retranslateUi(self, jan_matricula):
        _translate = QtCore.QCoreApplication.translate
        jan_matricula.setWindowTitle(_translate("jan_matricula", "Matriculando Aluno"))
        self.groupBox.setTitle(_translate("jan_matricula", "Dados do Aluno"))
        self.label_7.setText(_translate("jan_matricula", "Data de Nascimento"))
        self.label.setText(_translate("jan_matricula", "Endereço"))
        self.label_2.setText(_translate("jan_matricula", "Nome"))
        self.label_3.setText(_translate("jan_matricula", "Nome do Pai"))
        self.label_4.setText(_translate("jan_matricula", "Nome da Mãe"))
        self.groupBox_2.setTitle(_translate("jan_matricula", "Sexo"))
        self.rbt_masculino.setText(_translate("jan_matricula", "Masculino"))
        self.rbt_feminino.setText(_translate("jan_matricula", "Feminino"))
        self.btn_matricula.setText(_translate("jan_matricula", "Matricular"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    jan_matricula = QtWidgets.QMainWindow()
    ui = Ui_jan_matricula()
    ui.setupUi(jan_matricula)
    jan_matricula.show()
    sys.exit(app.exec_())
