# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'aluno_curso.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import banco


class Ui_jan_alcu(object):
    def setupUi(self, jan_mostar):
        jan_mostar.setObjectName("jan_mostar")
        jan_mostar.resize(481, 477)
        self.centralwidget = QtWidgets.QWidget(jan_mostar)
        self.centralwidget.setObjectName("centralwidget")
        
        font = QtGui.QFont()
        font.setPointSize(15)
        self.tab_alunos_cursos = QtWidgets.QTableWidget(self.centralwidget)
        self.tab_alunos_cursos.setGeometry(QtCore.QRect(15, 50, 781, 321))
        self.tab_alunos_cursos.setMouseTracking(False)
        self.tab_alunos_cursos.setObjectName("tab_alunos")
        self.tab_alunos_cursos.setRowCount(0)
        self.tab_alunos_cursos.setColumnCount(2)
        self.tab_alunos_cursos.horizontalHeader().setVisible(True)
        self.tab_alunos_cursos.verticalHeader().setVisible(True)
        self.tab_alunos_cursos.setFont(font)
        
        
        self.btn_carregar = QtWidgets.QPushButton(self.centralwidget)
        self.btn_carregar.setGeometry(QtCore.QRect(80, 400, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btn_carregar.setFont(font)
        self.btn_carregar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_carregar.setObjectName("btn_carregar")
        self.btn_carregar.clicked.connect(self.mostrar)
        
        
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(30, 30, 421, 331))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        jan_mostar.setCentralWidget(self.centralwidget)

        self.retranslateUi(jan_mostar)
        QtCore.QMetaObject.connectSlotsByName(jan_mostar)
        
        

    def retranslateUi(self, jan_mostar):
        _translate = QtCore.QCoreApplication.translate
        jan_mostar.setWindowTitle(_translate("jan_mostar", "Alunos - Cursos"))
        jan_mostar.setToolTip(_translate("jan_mostar", "Alunos"))
        self.btn_carregar.setText(_translate("jan_mostar", "Carregar"))
        self.groupBox.setTitle(_translate("jan_mostar", "Alunos - Cursos"))
        
    def mostrar(self):
        self.resultado = banco.mostrarEstuda()
        if self.resultado[0] == True:
            print(self.resultado)
        else:
            self.tab_alunos_cursos.setRowCount(0)
            for self.row_number, self.row_data in enumerate(self.resultado):
                self.tab_alunos_cursos.insertRow(self.row_number)
                for self.column_number, self.data in enumerate(self.row_data):
                    self.tab_alunos_cursos.setItem(self.row_number, self.column_number, QtWidgets.QTableWidgetItem(str(self.data)))
            self.tab_alunos_cursos.setHorizontalHeaderLabels(('Matricula', 'Nome', 'Sexo', 'Ano De Nascimento', 'Endereço', 'Nome do Pai', 'Nome da Mãe'))
            self.tab_alunos_cursos.resizeColumnsToContents()
            self.tab_alunos_cursos.resizeRowsToContents()



