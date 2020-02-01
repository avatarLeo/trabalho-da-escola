# -*- coding: utf-8 -*-



from PyQt5 import QtCore, QtGui, QtWidgets
import banco

class Inscricao(object):
    def setupUi(self, jan_matricula):
        jan_matricula.setObjectName("jan_matricula")
        jan_matricula.resize(400, 428)
        font = QtGui.QFont()
        font.setPointSize(10)
        jan_matricula.setFont(font)
        self.centralwidget = QtWidgets.QWidget(jan_matricula)
        self.centralwidget.setObjectName("centralwidget")

        
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(30, 20, 341, 391))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")


        self.txt_matricula = QtWidgets.QLineEdit(self.groupBox)
        self.txt_matricula.setGeometry(QtCore.QRect(30, 80, 161, 31))
        self.txt_matricula.setObjectName("txt_matricula")


        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(30, 130, 131, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")


        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(30, 50, 141, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")


        self.btn_inscrever = QtWidgets.QPushButton(self.groupBox)
        self.btn_inscrever.setGeometry(QtCore.QRect(230, 230, 75, 61))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btn_inscrever.setFont(font)
        self.btn_inscrever.setObjectName("btn_inscrever")
        self.btn_inscrever.clicked.connect(self.salvarCurso)


        self.rbt_java = QtWidgets.QRadioButton(self.groupBox)
        self.rbt_java.setGeometry(QtCore.QRect(50, 170, 82, 17))
        self.rbt_java.setObjectName("rbt_java")


        self.rbt_PHP = QtWidgets.QRadioButton(self.groupBox)
        self.rbt_PHP.setGeometry(QtCore.QRect(50, 200, 82, 17))
        self.rbt_PHP.setObjectName("rbt_PHP")


        self.rbt_HTML = QtWidgets.QRadioButton(self.groupBox)
        self.rbt_HTML.setGeometry(QtCore.QRect(50, 230, 82, 17))
        self.rbt_HTML.setObjectName("rbt_HTML")


        self.rbt_SQL = QtWidgets.QRadioButton(self.groupBox)
        self.rbt_SQL.setGeometry(QtCore.QRect(50, 250, 131, 31))
        self.rbt_SQL.setObjectName("rbt_SQL")


        self.rbt_Algoritmos = QtWidgets.QRadioButton(self.groupBox)
        self.rbt_Algoritmos.setGeometry(QtCore.QRect(50, 280, 111, 31))
        self.rbt_Algoritmos.setObjectName("rbt_Algoritmos")


        self.rbt_POO = QtWidgets.QRadioButton(self.groupBox)
        self.rbt_POO.setGeometry(QtCore.QRect(50, 320, 82, 17))
        self.rbt_POO.setObjectName("rbt_POO")


        self.rbt_Python = QtWidgets.QRadioButton(self.groupBox)
        self.rbt_Python.setGeometry(QtCore.QRect(50, 340, 82, 41))
        self.rbt_Python.setObjectName("rbt_Python")
        jan_matricula.setCentralWidget(self.centralwidget)

        self.retranslateUi(jan_matricula)
        QtCore.QMetaObject.connectSlotsByName(jan_matricula)

    def retranslateUi(self, jan_matricula):
        _translate = QtCore.QCoreApplication.translate
        jan_matricula.setWindowTitle(_translate("jan_matricula", "Inscrição dos Cursos"))
        self.groupBox.setTitle(_translate("jan_matricula", "Inscrição dos Cursos"))
        self.label.setText(_translate("jan_matricula", "Curso:"))
        self.label_2.setText(_translate("jan_matricula", "Nº da Matrícula"))
        self.btn_inscrever.setText(_translate("jan_matricula", "Inscrever"))
        self.rbt_java.setText(_translate("jan_matricula", "Java"))
        self.rbt_PHP.setText(_translate("jan_matricula", "PHP"))
        self.rbt_HTML.setText(_translate("jan_matricula", "HTML"))
        self.rbt_SQL.setText(_translate("jan_matricula", "SQL Server"))
        self.rbt_Algoritmos.setText(_translate("jan_matricula", "Algoritmos"))
        self.rbt_POO.setText(_translate("jan_matricula", "POO"))
        self.rbt_Python.setText(_translate("jan_matricula", "Python"))
        
    def salvar(self, i):
        if i.text() == "OK":
            res = banco.cadastroEstuda(self.matri, self.curso)
            msg = QtWidgets.QMessageBox()
            msg.setWindowTitle("aviso")
            msg.setText(res)
            x = msg.exec_()
            
            
    def aviso(self, nome, curso):
        msg = QtWidgets.QMessageBox()
        msg.setWindowTitle("Aviso")
        msg.setText("Deseja inscrever "+str(nome)+" no curso de "+curso)
        msg.setIcon(QtWidgets.QMessageBox.Question)
        msg.setStandardButtons(QtWidgets.QMessageBox.Cancel|QtWidgets.QMessageBox.Ok)
        msg.setDefaultButton(QtWidgets.QMessageBox.Cancel)
        
        msg.buttonClicked.connect(self.salvar)
        
        x = msg.exec_()
        
    def salvarCurso(self):
        self.matri = self.txt_matricula.text()
        if self.matri == "":
            msg = QtWidgets.QMessageBox()
            msg.setWindowTitle("aviso")
            msg.setText("Informe a matricula do aluno(a)")

            x = msg.exec_()
        else:
            self.curso = 0
            if self.rbt_java.isChecked() == True:
                self.curso = 1
                self.nCurso = "Java"
            elif self.rbt_PHP.isChecked() == True:
                self.curso = 2
                self.nCurso = "PHP"
            elif self.rbt_HTML.isChecked() == True:
                self.curso = 3
                self.nCurso = "HTML"
            elif self.rbt_SQL.isChecked() == True:
                self.curso = 4
                self.nCurso = "SQL"
            elif self.rbt_Algoritmos.isChecked() == True:
                self.curso = 5
                self.nCurso = "Algoritmos"
            elif self.rbt_POO.isChecked() == True:
                self.curso = 6
                self.nCurso = "POO"
            elif self.rbt_Python.isChecked() == True:
                self.curso = 7
                self.nCurso = "Python"
            else:
                msg = QtWidgets.QMessageBox()
                msg.setWindowTitle("aviso")
                msg.setText("Escolha uma opção de curso")

                x = msg.exec_()
        
        if self.matri != "" and self.curso != 0:
            res = banco.confirmar(self.matri)
            self.nome = res[0][1]
            self.aviso(self.nome, self.nCurso)
    


