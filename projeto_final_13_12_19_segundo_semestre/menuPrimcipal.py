# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'menuPrincipal.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from matrcula import Ui_jan_matricula
from mostar import Ui_jan_mostar
from editando import Ui_jan_editar
from inscricaocurso import Inscricao
from aluno_curso import Ui_jan_alcu
from cursos import Ui_jan_cursos
import sys


class Ui_janelaPrincipal(object):
    def setupUi(self, janelaPrincipal):
        janelaPrincipal.setObjectName("janelaPrincipal")
        janelaPrincipal.resize(578, 329)
        self.centralwidget = QtWidgets.QWidget(janelaPrincipal)
        self.centralwidget.setObjectName("centralwidget")

        #group box =================================================================================
        self.gpb_menu = QtWidgets.QGroupBox(self.centralwidget)
        self.gpb_menu.setGeometry(QtCore.QRect(40, 40, 501, 241))
        self.gpb_menu.setObjectName("gpb_menu")

        #button ========================================================================================
        self.btn_matricula = QtWidgets.QPushButton(self.gpb_menu)
        self.btn_matricula.setGeometry(QtCore.QRect(10, 30, 111, 81))
        self.btn_matricula.setObjectName("btn_matricula")
        self.btn_matricula.setIcon(QtGui.QIcon("icons/inscricao.png"))
        self.btn_matricula.setIconSize(QtCore.QSize(60, 60))
        self.btn_matricula.setToolTip("Matricular Alunos")
        self.btn_matricula.clicked.connect(self.matricula)

        self.btn_cancelar = QtWidgets.QPushButton(self.gpb_menu)
        self.btn_cancelar.setGeometry(QtCore.QRect(370, 120, 111, 81))
        self.btn_cancelar.setObjectName("btn_cancelr")
        self.btn_cancelar.setIcon(QtGui.QIcon("icons/claro.png"))
        self.btn_cancelar.setIconSize(QtCore.QSize(60, 60))
        self.btn_cancelar.setToolTip("Cancelar")
        self.btn_cancelar.clicked.connect(self.sair)


        self.btn_pesquisar = QtWidgets.QPushButton(self.gpb_menu)
        self.btn_pesquisar.setGeometry(QtCore.QRect(250, 30, 111, 81))
        self.btn_pesquisar.setObjectName("btn_pesquisar")
        self.btn_pesquisar.setIcon(QtGui.QIcon("icons/verifica.png"))
        self.btn_pesquisar.setIconSize(QtCore.QSize(60, 60))
        self.btn_pesquisar.setToolTip("<h2>Cursos Disponíveis</h2")
        self.btn_pesquisar.clicked.connect(self.cursos)

        self.btn_mostrar_notas = QtWidgets.QPushButton(self.gpb_menu)
        self.btn_mostrar_notas.setGeometry(QtCore.QRect(250, 120, 111, 81))
        self.btn_mostrar_notas.setObjectName("btn_mostrar_notas")
        self.btn_mostrar_notas.setIcon(QtGui.QIcon("icons/apresentacoes.png"))
        self.btn_mostrar_notas.setIconSize(QtCore.QSize(60, 60))
        self.btn_mostrar_notas.setToolTip("<h2>Curso dos Alunos</h2>")
        self.btn_mostrar_notas.clicked.connect(self.aluno_curso)

        self.btn_notas = QtWidgets.QPushButton(self.gpb_menu)
        self.btn_notas.setGeometry(QtCore.QRect(130, 120, 111, 81))
        self.btn_notas.setObjectName("btn_notas")
        self.btn_notas.setIcon(QtGui.QIcon("icons/caderno.png"))
        self.btn_notas.setIconSize(QtCore.QSize(60, 60))
        self.btn_notas.setToolTip("<h2>Adicionar Curso do aluno</h2>")
        self.btn_notas.clicked.connect(self.inscricaoCurso)

        self.btn_mostrar = QtWidgets.QPushButton(self.gpb_menu)
        self.btn_mostrar.setGeometry(QtCore.QRect(130, 30, 111, 81))
        self.btn_mostrar.setObjectName("btn_mostrar")
        self.btn_mostrar.setIcon(QtGui.QIcon("icons/estudantes.png"))
        self.btn_mostrar.setIconSize(QtCore.QSize(60, 60))
        self.btn_mostrar.setToolTip("Mostrar Alunos")
        self.btn_mostrar.clicked.connect(self.mostrar)

        self.btn_editar = QtWidgets.QPushButton(self.gpb_menu)
        self.btn_editar.setGeometry(QtCore.QRect(10, 120, 111, 81))
        self.btn_editar.setObjectName("btn_editar")
        self.btn_editar.setIcon(QtGui.QIcon("icons/editar.png"))
        self.btn_editar.setIconSize(QtCore.QSize(60, 60))
        self.btn_editar.setToolTip("Editar")
        self.btn_editar.clicked.connect(self.editar)

        self.btn_excluir = QtWidgets.QPushButton(self.gpb_menu)
        self.btn_excluir.setGeometry(QtCore.QRect(370, 30, 111, 81))
        self.btn_excluir.setObjectName("btn_excluir")
        self.btn_excluir.setIcon(QtGui.QIcon("icons/arquivo.png"))
        self.btn_excluir.setIconSize(QtCore.QSize(60, 60))
        self.btn_excluir.setToolTip("<h2>Excluir Aluno</h2>")

        janelaPrincipal.setCentralWidget(self.centralwidget)

        self.retranslateUi(janelaPrincipal)
        QtCore.QMetaObject.connectSlotsByName(janelaPrincipal)
        
    def cursos(self):
        self.jan_curso = QtWidgets.QMainWindow()
        self.ui = Ui_jan_cursos()
        self.ui.setupUi(self.jan_curso)
        self.jan_curso.show()
        
        
    def aluno_curso(self):
        self.jan_aluno_curso = QtWidgets.QMainWindow()
        self.aluno = Ui_jan_alcu()
        self.aluno.setupUi(self.jan_aluno_curso)
        self.jan_aluno_curso.show()



    def matricula(self):
        self.jan_matricula = QtWidgets.QMainWindow()
        self.ui =  Ui_jan_matricula()
        self.ui.setupUi(self.jan_matricula)
        self.jan_matricula.show()


    def mostrar(self):
        self.jan_mostrar = QtWidgets.QMainWindow()
        self.ui = Ui_jan_mostar()
        self.ui.setupUi(self.jan_mostrar)
        self.jan_mostrar.show()


    def editar(self):
        self.jan_editar = QtWidgets.QMainWindow()
        self.ui = Ui_jan_editar()
        self.ui.setupUi(self.jan_editar)
        self.jan_editar.show()
        
        
    def inscricaoCurso(self):
        self.jan_inscricao = QtWidgets.QMainWindow()
        self.ui = Inscricao()
        self.ui.setupUi(self.jan_inscricao)
        self.jan_inscricao.show()


    def sair(self):
        sys.exit()


    def retranslateUi(self, janelaPrincipal):
        _translate = QtCore.QCoreApplication.translate
        janelaPrincipal.setWindowTitle(_translate("janelaPrincipal", "Seja Bem Vindo Ao Mine Suap"))
        self.gpb_menu.setTitle(_translate("janelaPrincipal", "Menu"))
        self.btn_matricula.setText(_translate("janelaPrincipal", ""))
        self.btn_cancelar.setText(_translate("janelaPrincipal", ""))
        self.btn_pesquisar.setText(_translate("janelaPrincipal", ""))
        self.btn_mostrar_notas.setText(_translate("janelaPrincipal", ""))
        self.btn_notas.setText(_translate("janelaPrincipal", ""))
        self.btn_mostrar.setText(_translate("janelaPrincipal", ""))
        self.btn_editar.setText(_translate("janelaPrincipal", ""))
        self.btn_excluir.setText(_translate("janelaPrincipal", ""))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    janelaPrincipal = QtWidgets.QMainWindow()
    ui = Ui_janelaPrincipal()
    ui.setupUi(janelaPrincipal)
    janelaPrincipal.show()
    sys.exit(app.exec_())
