# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'cursos.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import banco


class Ui_jan_cursos(object):
    def setupUi(self, jan_cursos):
        jan_cursos.setObjectName("jan_cursos")
        jan_cursos.resize(540, 456)
        self.centralwidget = QtWidgets.QWidget(jan_cursos)
        self.centralwidget.setObjectName("centralwidget")


        font = QtGui.QFont()
        font.setPointSize(14)
        self.tab_cursos = QtWidgets.QTableWidget(self.centralwidget)
        self.tab_cursos.setGeometry(QtCore.QRect(15, 50, 500, 321))
        self.tab_cursos.setMouseTracking(False)
        self.tab_cursos.setObjectName("tab_alunos")
        self.tab_cursos.setRowCount(0)
        self.tab_cursos.setColumnCount(4)
        self.tab_cursos.horizontalHeader().setVisible(True)
        self.tab_cursos.verticalHeader().setVisible(True)
        self.tab_cursos.setFont(font)

        self.btn_carregar = QtWidgets.QPushButton(self.centralwidget)
        self.btn_carregar.setGeometry(QtCore.QRect(10, 390, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btn_carregar.setFont(font)
        self.btn_carregar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_carregar.setObjectName("btn_carregar")
        self.btn_carregar.clicked.connect(self.carregar)

        jan_cursos.setCentralWidget(self.centralwidget)

        self.retranslateUi(jan_cursos)
        QtCore.QMetaObject.connectSlotsByName(jan_cursos)

    def retranslateUi(self, jan_cursos):
        _translate = QtCore.QCoreApplication.translate
        jan_cursos.setWindowTitle(_translate("jan_cursos", "Mostrando Cursos"))
        jan_cursos.setToolTip(_translate("jan_cursos", "Cursos"))
        self.btn_carregar.setText(_translate("jan_cursos", "Carregar"))

    def carregar(self):
        self.resultado = banco.mostrarCursos()
        if self.resultado[0] == True:
        # msg = QMessageBox.warning(jan_mostrar,'erro', str(self.resultado[1]))
            print(self.resultado[1])
        else:
        #QSqlRelationalDelegate (view)

            self.tab_cursos.setRowCount(0)
            for self.row_number, self.row_data in enumerate(self.resultado):
                self.tab_cursos.insertRow(self.row_number)
                for self.column_number, self.data in enumerate(self.row_data):
                    self.tab_cursos.setItem(self.row_number, self.column_number, QtWidgets.QTableWidgetItem(str(self.data)))
            self.tab_cursos.setHorizontalHeaderLabels(('id', 'Nome', 'carga', 'totalaulas'))
            self.tab_cursos.resizeColumnsToContents()
            self.tab_cursos.resizeRowsToContents()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    jan_cursos = QtWidgets.QMainWindow()
    ui = Ui_jan_cursos()
    ui.setupUi(jan_cursos)
    jan_cursos.show()
    sys.exit(app.exec_())
