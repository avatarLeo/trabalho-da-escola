# -*- coding: utf-8 -*-



import banco
from PyQt5 import QtCore, QtGui, QtWidgets
import sys


class Ui_jan_mostar(object):
    def setupUi(self, jan_mostar):
        jan_mostar.setObjectName("jan_mostar")
        jan_mostar.resize(809, 456)
        self.centralwidget = QtWidgets.QWidget(jan_mostar)
        self.centralwidget.setObjectName("centralwidget")

        font = QtGui.QFont()
        font.setPointSize(12)

        font = QtGui.QFont()
        font.setPointSize(12)

        #table ===============================================================================
        self.tab_alunos = QtWidgets.QTableWidget(self.centralwidget)
        self.tab_alunos.setGeometry(QtCore.QRect(15, 50, 781, 321))
        self.tab_alunos.setMouseTracking(False)
        self.tab_alunos.setObjectName("tab_alunos")
        self.tab_alunos.setRowCount(0)
        self.tab_alunos.setColumnCount(7)
        self.tab_alunos.horizontalHeader().setVisible(True)
        self.tab_alunos.verticalHeader().setVisible(True)
        #self.tab_alunos.setStyleSheet('background-color: green')


        #button ====================================================================================
        self.btn_carregar = QtWidgets.QPushButton(self.centralwidget)
        self.btn_carregar.setGeometry(QtCore.QRect(10, 390, 131, 41))
        self.btn_carregar.setFont(font)
        self.btn_carregar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_carregar.setObjectName("btn_carregar")
        self.btn_carregar.clicked.connect(self.carregar)

        self.btn_cancelar = QtWidgets.QPushButton(self.centralwidget)
        self.btn_cancelar.setGeometry(QtCore.QRect(160, 390, 131, 41))
        self.btn_cancelar.setFont(font)
        self.btn_cancelar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_cancelar.setObjectName("btn_cancelar")
        self.btn_cancelar.clicked.connect(QtWidgets.qApp.quit)


        jan_mostar.setCentralWidget(self.centralwidget)

        self.retranslateUi(jan_mostar)
        QtCore.QMetaObject.connectSlotsByName(jan_mostar)


    def sair(self):
        sys.exit()

    def retranslateUi(self, jan_mostar):
        _translate = QtCore.QCoreApplication.translate
        jan_mostar.setWindowTitle(_translate("jan_mostar", "Mostrando Alunos"))
        jan_mostar.setToolTip(_translate("jan_mostar", "Alunos"))
        self.btn_carregar.setText(_translate("jan_mostar", "Carregar"))
        self.btn_cancelar.setText(_translate("jan_mostar", "Cancelar"))


    def carregar(self):
        self.resultado = banco.relatorio_de_alunos()
        if self.resultado[0] == True:
            msg = QtWidgets.QMessageBox()
            msg.setWindowTitle("aviso")
            msg.setText(str(self.resultado[1]))

            x = msg.exec_()
            
        elif len(self.resultado[0]) == 0:
            msg = QtWidgets.QMessageBox()
            msg.setWindowTitle("aviso")
            msg.setText("Não há alunos matriculados")

            x = msg.exec_()
            print("Não Há alunos cadastrados")
        else:
            #QSqlRelationalDelegate (view)

            self.tab_alunos.setRowCount(0)
            for self.row_number, self.row_data in enumerate(self.resultado):
                self.tab_alunos.insertRow(self.row_number)
                for self.column_number, self.data in enumerate(self.row_data):
                    self.tab_alunos.setItem(self.row_number, self.column_number, QtWidgets.QTableWidgetItem(str(self.data)))
            self.tab_alunos.setHorizontalHeaderLabels(('Matricula', 'Nome', 'Sexo', 'Ano De Nascimento', 'Endereço', 'Nome do Pai', 'Nome da Mãe'))
            self.tab_alunos.resizeColumnsToContents()
            self.tab_alunos.resizeRowsToContents()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    jan_mostar = QtWidgets.QMainWindow()
    ui = Ui_jan_mostar()
    ui.setupUi(jan_mostar)
    jan_mostar.show()
    sys.exit(app.exec_())
