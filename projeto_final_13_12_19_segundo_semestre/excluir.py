# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'excluir.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import banco

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(599, 238)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tab_excluir = QtWidgets.QTableView(self.centralwidget)
        self.tab_excluir.setGeometry(QtCore.QRect(20, 110, 551, 101))
        self.tab_excluir.setObjectName("tab_excluir")
        self.tab_excluir.setRowCount(0)
        self.tab_excluir.setColumnCount(7)
        self.tab_excluir.horizontalHeader().setVisible(True)
        self.tab_excluir.verticalHeader().setVisible(True)



        self.btn_excluir = QtWidgets.QPushButton(self.centralwidget)
        self.btn_excluir.setGeometry(QtCore.QRect(400, 50, 75, 31))
        self.btn_excluir.clicked.connect(self.excluir)

        font = QtGui.QFont()
        font.setPointSize(12)
        self.btn_excluir.setFont(font)
        self.btn_excluir.setObjectName("btn_excluir")
        self.txt_nome = QtWidgets.QLineEdit(self.centralwidget)
        self.txt_nome.setGeometry(QtCore.QRect(20, 50, 361, 31))
        font = QtGui.QFont()
        font.setPointSize(19)
        self.txt_nome.setFont(font)
        self.txt_nome.setObjectName("txt_nome")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 20, 111, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


    def excluir(self):
        self.aluno = self.txt_nome.text()
        if self.aluno != "":
            self.res = banco.localisar(self.aluno)

            self.tab_alunos.setRowCount(0)
            for self.row_number, self.row_data in enumerate(self.resultado):
                self.tab_alunos.insertRow(self.row_number)
                for self.column_number, self.data in enumerate(self.row_data):
                    self.tab_alunos.setItem(self.row_number, self.column_number, QtWidgets.QTableWidgetItem(str(self.data)))
            self.tab_excluir.setHorizontalHeaderLabels(('Matricula', 'Nome', 'Sexo', 'Ano De Nascimento', 'Endereço', 'Nome do Pai', 'Nome da Mãe'))
            self.tab_excluir.resizeColumnsToContents()
            self.tab_excluir.resizeRowsToContents()
        else:
            print("Aluno não encontrado")


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btn_excluir.setText(_translate("MainWindow", "Excluir"))
        self.label.setText(_translate("MainWindow", "Nome do Aluno"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
