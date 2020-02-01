from PyQt5 import QtCore, QtGui, QtWidgets
import banco


class Ui_jan_pesquisar(object):
    def setupUi(self, jan_pesquisar):
        jan_pesquisar.setObjectName("jan_pesquisar")
        jan_pesquisar.resize(908, 210)
        self.centralwidget = QtWidgets.QWidget(jan_pesquisar)
        self.centralwidget.setObjectName("centralwidget")

        #table ===========================================================================
        self.tab_pesq = QtWidgets.QTableWidget(self.centralwidget)
        self.tab_pesq.setGeometry(QtCore.QRect(20, 100, 871, 91))
        self.tab_pesq.setObjectName("tab_pesq")
        self.tab_pesq.setRowCount(0)
        self.tab_pesq.setRowCount(0)
        self.tab_pesq.setColumnCount(7)
        self.tab_pesq.horizontalHeader().setVisible(True)
        self.tab_pesq.verticalHeader().setVisible(True)


        #buttoon ==============================================================================================
        self.btn_pesquisar = QtWidgets.QPushButton(self.centralwidget)
        self.btn_pesquisar.setGeometry(QtCore.QRect(20, 40, 101, 41))
        self.btn_pesquisar.setText("")
        self.btn_pesquisar.setObjectName("btn_pesquisar")
        self.btn_pesquisar.clicked.connect(self.pesquisar)
        self.btn_pesquisar.setIcon(QtGui.QIcon("icons/pesquisar.png"))
        self.btn_pesquisar.setIconSize(QtCore.QSize(40, 40))
        self.btn_pesquisar.setToolTip("<h2>Pesquisar Aluno</h2>")


        #text line ================================================================================================
        self.txt_pesquisar = QtWidgets.QLineEdit(self.centralwidget)
        self.txt_pesquisar.setGeometry(QtCore.QRect(150, 40, 491, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.txt_pesquisar.setFont(font)
        self.txt_pesquisar.setObjectName("txt_pesquisar")
        jan_pesquisar.setCentralWidget(self.centralwidget)

        self.retranslateUi(jan_pesquisar)
        QtCore.QMetaObject.connectSlotsByName(jan_pesquisar)

    def retranslateUi(self, jan_pesquisar):
        _translate = QtCore.QCoreApplication.translate
        jan_pesquisar.setWindowTitle(_translate("jan_pesquisar", "Pesquisando Aluno"))



    def pesquisar(self):
        self.aluno = self.txt_pesquisar.text()
        self.resultado = banco.pesquisar_aluno(self.aluno)
        if self.resultado[0] == True:
        # msg = QMessageBox.warning(jan_mostrar,'erro', str(self.resultado[1]))
            print(self.resultado[1])
        else:
        #QSqlRelationalDelegate (view)

            self.tab_pesq.setRowCount(0)
            for self.row_number, self.row_data in enumerate(self.resultado):
                self.tab_pesq.insertRow(self.row_number)
                for self.column_number, self.data in enumerate(self.row_data):
                    self.tab_pesq.setItem(self.row_number, self.column_number, QtWidgets.QTableWidgetItem(str(self.data)))
            self.tab_pesq.setHorizontalHeaderLabels(('Matricula', 'Nome', 'Sexo', 'Ano De Nascimento', 'Endereço', 'Nome do Pai', 'Nome da Mãe'))
            self.tab_pesq.resizeColumnsToContents()
            self.tab_pesq.resizeRowsToContents()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    jan_pesquisar = QtWidgets.QMainWindow()
    ui = Ui_jan_pesquisar()
    ui.setupUi(jan_pesquisar)
    jan_pesquisar.show()
    sys.exit(app.exec_())
