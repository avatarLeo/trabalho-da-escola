# -*- coding: utf-8 -*-


from PyQt5.QtCore import *
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
import banco


class Ui_jan_editar(object):
    def setupUi(self, jan_editar):
        jan_editar.setObjectName("jan_editar")
        jan_editar.resize(637, 579)
        font = QtGui.QFont()
        font.setPointSize(10)
        jan_editar.setFont(font)
        
        
        # font ===================================================================================
        font = QtGui.QFont()
        font.setPointSize(12)
        
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
        
        font = QtGui.QFont()
        font.setPointSize(14)
        
        font = QtGui.QFont()
        font.setPointSize(12)
        
        font = QtGui.QFont()
        font.setPointSize(12)
        
        self.centralwidget = QtWidgets.QWidget(jan_editar)
        self.centralwidget.setObjectName("centralwidget")
        
        
        #group box==========================================================================
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(30, 140, 561, 411))
        self.groupBox.setObjectName("groupBox")
        
        self.groupBox_2 = QtWidgets.QGroupBox(self.groupBox)
        self.groupBox_2.setGeometry(QtCore.QRect(390, 50, 141, 131))
        self.groupBox_2.setFont(font)
        self.groupBox_2.setObjectName("groupBox_2")
        
        self.gup_pesqisar = QtWidgets.QGroupBox(self.centralwidget)
        self.gup_pesqisar.setGeometry(QtCore.QRect(30, 20, 561, 111))
        self.gup_pesqisar.setFont(font)
        self.gup_pesqisar.setObjectName("gup_pesqisar")
        
        # label =======================================================================================
        self.label_7 = QtWidgets.QLabel(self.groupBox)
        self.label_7.setGeometry(QtCore.QRect(30, 340, 171, 16))
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
        
        self.lbl_image = QtWidgets.QLabel(self.groupBox)
        self.lbl_image.setGeometry(QtCore.QRect(380, 200, 60, 60))
        self.lbl_image.setText("Matricula:")
        self.lbl_image.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_image.setObjectName("lbl_image")
        
        self.lbl_mat = QtWidgets.QLabel(self.groupBox)
        self.lbl_mat.setGeometry(QtCore.QRect(450, 200, 60, 60))
        self.lbl_mat.setText("")
        
        
        self.label_5 = QtWidgets.QLabel(self.gup_pesqisar)
        self.label_5.setGeometry(QtCore.QRect(20, 30, 121, 16))
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        
        
        # line edit ======================================================================
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
        
        self.txt_pesquisa = QtWidgets.QLineEdit(self.gup_pesqisar)
        self.txt_pesquisa.setGeometry(QtCore.QRect(10, 60, 381, 31))
        self.txt_pesquisa.setObjectName("txt_pesquisa")
        
        
        # date =================================================================================
        self.date_nascimento = QtWidgets.QDateEdit(self.groupBox)
        self.date_nascimento.setGeometry(QtCore.QRect(30, 360, 131, 31))
        self.date_nascimento.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.date_nascimento.setObjectName("date_nascimento")
        
        
        # radio button ================================================================
        self.rbt_masculino = QtWidgets.QRadioButton(self.groupBox_2)
        self.rbt_masculino.setGeometry(QtCore.QRect(20, 30, 101, 17))
        self.rbt_masculino.setFont(font)
        self.rbt_masculino.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.rbt_masculino.setObjectName("rbt_masculino")
        
        self.rbt_feminino = QtWidgets.QRadioButton(self.groupBox_2)
        self.rbt_feminino.setGeometry(QtCore.QRect(20, 80, 101, 17))
        self.rbt_feminino.setFont(font)
        self.rbt_feminino.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.rbt_feminino.setObjectName("rbt_feminino")
        
        
        #button ===========================================================================================
      
        
        self.btn_excluir = QtWidgets.QPushButton(self.groupBox)
        self.btn_excluir.setGeometry(QtCore.QRect(360, 330, 75, 61))
        self.btn_excluir.setFont(font)
        self.btn_excluir.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_excluir.setObjectName("btn_matricula")
        self.btn_excluir.clicked.connect(self.aviso)
        
        self.btn_busca = QtWidgets.QPushButton(self.gup_pesqisar)
        self.btn_busca.setGeometry(QtCore.QRect(424, 60, 81, 31))
        self.btn_busca.setFont(font)
        self.btn_busca.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_busca.setObjectName("btn_busca")
        self.btn_busca.clicked.connect(self.localizar)
        
        self.btn_slavar = QtWidgets.QPushButton(self.groupBox)
        self.btn_slavar.setGeometry(QtCore.QRect(245, 330, 75, 61))
        self.btn_slavar.setFont(font)
        self.btn_slavar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_slavar.setObjectName("btn_busca")
        self.btn_slavar.clicked.connect(self.salvar)
        
        jan_editar.setCentralWidget(self.centralwidget)

        self.retranslateUi(jan_editar)
        QtCore.QMetaObject.connectSlotsByName(jan_editar)
        
        
        
    def aviso(self):
        msg = QtWidgets.QMessageBox()
        msg.setWindowTitle("Aviso")
        msg.setText("Tem certeza que você deseja excluir?")
        msg.setIcon(QtWidgets.QMessageBox.Question)
        msg.setStandardButtons(QtWidgets.QMessageBox.Cancel|QtWidgets.QMessageBox.Ok)
        msg.setDefaultButton(QtWidgets.QMessageBox.Cancel)
        
        msg.buttonClicked.connect(self.excluir)
        
        x = msg.exec_()
        
        
    def localizar(self):
        self.nome = self.txt_pesquisa.text()
        if self.nome == "":
            msg = QtWidgets.QMessageBox()
            msg.setWindowTitle("Aviso")
            msg.setText("Informe o nome do Aluno(a) que deseja editar")
            x = msg.exec_()
        else:
            res = banco.localisar(self.nome)
            print(type(res))
            if len(res) == 0:
                print(len(res))
                msg = QtWidgets.QMessageBox()
                msg.setWindowTitle("Aviso")
                msg.setText("Aluno(a) não encontrado")
                x = msg.exec_()
                
            else:
                self.txt_nome.setText(res[0][1])
                self.txt_endereco.setText(res[0][4])
                self.txt_pai.setText(res[0][5])
                self.txt_mae.setText(res[0][6])
                if res[0][2] == "M":
                    self.rbt_masculino.setChecked(True)
                elif res[0][2] == "F":
                    self.rbt_feminino.setChecked(True)
                    
                self.date_nascimento.setDate(QtCore.QDate(res[0][3]))
                self.lbl_mat.setText(str(res[0][0]))
        
        
    def excluir(self, i):
        if i.text() == "OK":
            self.matricula = self.lbl_mat.text()
            if self.matricula == "":
                msg = QtWidgets.QMessageBox()
                msg.setWindowTitle("Aviso")
                msg.setText("Busque um aluno(a) para poder excluir")
                x = msg.exec_()
            else:
                banco.excluir(self.matricula)
                
                
    def salvar(self):
        self.nome = self.txt_nome.text()
        self.endereco = self.txt_endereco.text()
        self.pai = self.txt_pai.text()
        self.mae = self.txt_mae.text()
        self.data = self.date_nascimento.date()
        self.nascimento = self.data.toString(Qt.ISODate)
        self.mat = self.lbl_mat.text()
        self.sexo = ""
        if self.rbt_masculino.isChecked() == True:
            self.sexo = "M"
        elif self.rbt_feminino.isChecked() == True:
            self.sexo = "F"
            
        self.aluno = self.nome, self.sexo, self.nascimento, self.endereco, self.pai, self.mae, self.mat
        if self.nome == "":
            msg = QtWidgets.QMessageBox()
            msg.setWindowTitle("Aviso")
            msg.setText("Informe o nome do aluno")
            x = msg.exec_()
        else:   
            self.aviso = banco.editar_aluno(self.aluno)
            msg = QtWidgets.QMessageBox()
            msg.setWindowTitle("Aviso")
            msg.setText(self.aviso)
            x = msg.exec_()
        
    

    def retranslateUi(self, jan_editar):
        _translate = QtCore.QCoreApplication.translate
        jan_editar.setWindowTitle(_translate("jan_editar", "Editando Aluno"))
        self.groupBox.setTitle(_translate("jan_editar", "Editando Dados do Aluno"))
        self.label_7.setText(_translate("jan_editar", "Data de Nascimento"))
        self.label.setText(_translate("jan_editar", "Endereço"))
        self.label_2.setText(_translate("jan_editar", "Nome"))
        self.label_3.setText(_translate("jan_editar", "Nome do Pai"))
        self.label_4.setText(_translate("jan_editar", "Nome da Mãe"))
        self.groupBox_2.setTitle(_translate("jan_editar", "Sexo"))
        self.rbt_masculino.setText(_translate("jan_editar", "Masculino"))
        self.rbt_feminino.setText(_translate("jan_editar", "Feminino"))
        self.btn_slavar.setText(_translate("jan_editar", "Salvar"))
        self.btn_excluir.setText(_translate("jan_editar", "Excluir"))
        self.gup_pesqisar.setTitle(_translate("jan_editar", "Pesquisando Aluno"))
        self.btn_busca.setText(_translate("jan_editar", "Buscar"))
        self.label_5.setText(_translate("jan_editar", "Nome do Aluno"))

'''
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    jan_editar = QtWidgets.QMainWindow()
    ui = Ui_jan_editar()
    ui.setupUi(jan_editar)
    jan_editar.show()
    sys.exit(app.exec_())
'''