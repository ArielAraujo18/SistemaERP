from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QWidget, QFileDialog, QTableWidget, QTableWidgetItem
import traceback
import mysql.connector
import mysql
import pandas as pd

class Ui_frm_Cliente(object):
    def setupUi(self, frm_Cliente):
        frm_Cliente.setObjectName("frm_Cliente")
        frm_Cliente.resize(581, 592)
        frm_Cliente.setFixedSize(581, 592)
        frm_Cliente.setWindowIcon(QIcon("C:/Users/Ariel/PycharmProjects/Scripts/Sistema/Img/AvsB.ico"))
        frm_Cliente.setStyleSheet("QWidget {\n"
"    background-color: #e8f5e9;\n"
"}")
        self.btn_Add = QtWidgets.QPushButton(frm_Cliente)
        self.btn_Add.setGeometry(QtCore.QRect(0, 0, 91, 81))
        self.btn_Add.setStyleSheet("QPushButton {\n"
"    background-color: #ffffff;\n"
"    border: 2px solid #d1c4b2;\n"
"    border-radius: 12px;\n"
"    color: #5a5a5a;\n"
"    font-size: 14px;\n"
"    font-weight: bold;\n"
"    padding: 10px 16px;\n"
"    background-image:url(:/iconAdd/Img/adicionar.png); \n"
"    background-repeat: no-repeat;\n"
"    background-position: center;\n"
"    transition: all 0.3s ease;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #f2ebe0;\n"
"    border-color: #c4b49e;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #e8dfcf; \n"
"    border-color: #b39b8d; \n"
"    padding-left: 12px; \n"
"    padding-top: 4px;\n"
"}")
        self.btn_Add.setText("")
        self.btn_Add.setObjectName("btn_Add")
        self.btn_voltar = QtWidgets.QPushButton(frm_Cliente)
        self.btn_voltar.setGeometry(QtCore.QRect(490, 510, 91, 81))
        self.btn_voltar.setStyleSheet("QPushButton{\n"
"    background-color: #f5f5f5; /* Fundo claro */\n"
"    border: 2px solid #cccccc; /* Borda cinza */\n"
"    border-radius: 10px; /* Bordas arredondadas */\n"
"    padding: 10px; /* Espaçamento interno */\n"
"    color: #333333; /* Cor do texto */\n"
"    font-size: 14px; /* Tamanho do texto */\n"
"    background-image:url(:/iconRet/Img/retornar.png); /* Caminho da imagem */\n"
"    background-repeat: no-repeat; /* Evita repetição da imagem */\n"
"    background-position: center; /* Centraliza a imagem no botão */\n"
"    transition: all 0.3s ease;\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: #e0e0e0; /* Fundo mais claro ao passar o mouse */\n"
"    border-color: #aaaaaa; /* Borda mais escura ao passar o mouse */\n"
"    transform: scale(1.05); \n"
"}\n"
"QPushButton:pressed{\n"
"    background-color: #d6d6d6;\n"
"    border-color: #888888;\n"
"    transform: scale(0.95);\n"
"}")
        self.btn_voltar.setText("")
        self.btn_voltar.setObjectName("btn_voltar")
        self.btn_consul = QtWidgets.QPushButton(frm_Cliente)
        self.btn_consul.setGeometry(QtCore.QRect(180, 0, 91, 81))
        self.btn_consul.setStyleSheet("QPushButton {\n"
"    background-color: #ffffff; \n"
"    border: 2px solid #d1c4b2; \n"
"    border-radius: 12px; \n"
"    color: #5a5a5a;\n"
"    font-size: 14px;\n"
"    font-weight: bold;\n"
"    padding: 10px 16px; \n"
"    background-image:url(:/iconConsu/Img/consultar.png);\n"
"    background-repeat: no-repeat;\n"
"    background-position: center;\n"
"    transition: all 0.3s ease;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #f2ebe0;\n"
"    border-color: #c4b49e;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #e8dfcf;\n"
"    border-color: #b39b8d;\n"
"    padding-left: 12px;\n"
"    padding-top: 4px;\n"
"}")
        self.btn_consul.setText("")
        self.btn_consul.setObjectName("btn_consul")
        self.btn_alterar = QtWidgets.QPushButton(frm_Cliente)
        self.btn_alterar.setGeometry(QtCore.QRect(90, 0, 91, 81))
        self.btn_alterar.setStyleSheet("QPushButton {\n"
"    background-color: #ffffff; \n"
"    border: 2px solid #d1c4b2; \n"
"    border-radius: 12px; \n"
"    color: #5a5a5a; \n"
"    font-size: 14px;\n"
"    font-weight: bold; \n"
"    padding: 10px 16px;\n"
"    background-image:url(:/icon_alt/Img/alterar.png);\n"
"    background-repeat: no-repeat;\n"
"    background-position: center;\n"
"    transition: all 0.3s ease;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #f2ebe0;\n"
"    border-color: #c4b49e;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #e8dfcf; \n"
"    border-color: #b39b8d;\n"
"    padding-left: 12px;\n"
"    padding-top: 4px;\n"
"}")
        self.btn_alterar.setText("")
        self.btn_alterar.setObjectName("btn_alterar")
        self.btn_excluir = QtWidgets.QPushButton(frm_Cliente)
        self.btn_excluir.setGeometry(QtCore.QRect(0, 510, 91, 81))
        self.btn_excluir.setStyleSheet("QPushButton {\n"
"    background-color: #ffebee; \n"
"    border: 2px solid #ffcdd2;\n"
"    border-radius: 10px;\n"
"    color: #b71c1c; \n"
"    font-size: 14px;\n"
"    font-weight: bold;\n"
"    padding: 10px 16px;\n"
"    background-image:url(:/iconExcluir/Img/excluir.png);\n"
"    background-repeat: no-repeat;\n"
"    background-position: center;\n"
"    padding-left: 40px;\n"
"    transition: all 0.3s ease;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #ffcdd2;\n"
"    border-color: #e57373;\n"
"    color: #d32f2f; \n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #e57373;\n"
"    border-color: #b71c1c;\n"
"    padding-left: 44px;\n"
"    padding-top: 2px;\n"
"}")
        self.btn_excluir.setText("")
        self.btn_excluir.setObjectName("btn_excluir")
        self.tbl_cliente = QtWidgets.QTableWidget(frm_Cliente)
        self.tbl_cliente.setGeometry(QtCore.QRect(0, 150, 581, 341))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.tbl_cliente.setFont(font)
        self.tbl_cliente.setStyleSheet("QTableWidget, QTableView {\n"
"    border: 1px solid #dcdcdc; \n"
"    border-radius: 5px; \n"
"    gridline-color: #dcdcdc; \n"
"    background-color: #ffffff; \n"
"    font-size: 14px; \n"
"    color: #333333; \n"
"}\n"
"\n"
"QHeaderView::section {\n"
"    background-color: #f0f0f0; \n"
"    color: #333333;\n"
"    font-weight: bold; \n"
"    border: 1px solid #dcdcdc; \n"
"    padding: 4px; \n"
"}\n"
"\n"
"QTableWidget::item:selected, QTableView::item:selected {\n"
"    background-color: #b3d9ff; \n"
"    color: #000000;\n"
"}\n"
"\n"
"QTableCornerButton::section {\n"
"    background-color: #f0f0f0; \n"
"    border: 1px solid #dcdcdc;\n"
"}\n"
"\n"
"QScrollBar:vertical {\n"
"    background: #f0f0f0;\n"
"    width: 12px; \n"
"    margin: 2px 0 2px 0; \n"
"    border: none; \n"
"}\n"
"\n"
"QScrollBar::handle:vertical {\n"
"    background: #b0bec5; \n"
"    min-height: 20px; \n"
"    border-radius: 6px; \n"
"}\n"
"\n"
"QScrollBar::handle:vertical:hover {\n"
"    background: #90a4ae; \n"
"}\n"
"\n"
"QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {\n"
"    background: none; \n"
"    height: 0px; \n"
"}\n"
"\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"    background: none; \n"
"}\n"
"\n"
"QScrollBar:horizontal {\n"
"    background: #f0f0f0; \n"
"    height: 12px; \n"
"    margin: 0 2px 0 2px; \n"
"    border: none;\n"
"}\n"
"\n"
"QScrollBar::handle:horizontal {\n"
"    background: #b0bec5;\n"
"    min-width: 20px; \n"
"    border-radius: 6px;\n"
"}\n"
"\n"
"QScrollBar::handle:horizontal:hover {\n"
"    background: #90a4ae; \n"
"}\n"
"\n"
"QScrollBar::add-line:horizontal, QScrollBar::sub-line:horizontal {\n"
"    background: none;\n"
"    width: 0px;\n"
"}\n"
"\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal {\n"
"    background: none;\n"
"}\n"
"")
        self.tbl_cliente.setObjectName("tbl_cliente")
        self.tbl_cliente.setColumnCount(4)
        self.tbl_cliente.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_cliente.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_cliente.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_cliente.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_cliente.setHorizontalHeaderItem(3, item)
        self.btn_pesquisar = QtWidgets.QPushButton(frm_Cliente)
        self.btn_pesquisar.setGeometry(QtCore.QRect(530, 110, 21, 21))
        self.btn_pesquisar.setStyleSheet("QPushButton {\n"
"    background-color: #ffffff; \n"
"    border: 2px solid #d1c4b2; \n"
"    border-radius: 12px;\n"
"    color: #5a5a5a; \n"
"    font-size: 14px;\n"
"    font-weight: bold; \n"
"    padding: 10px 16px;\n"
"    background-image: url(:/iconPesq/Img/pesquisar.png); \n"
"    background-repeat: no-repeat;\n"
"    background-position: center;\n"
"    transition: all 0.3s ease; \n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #f2ebe0; \n"
"    border-color: #c4b49e;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #e8dfcf;\n"
"    border-color: #b39b8d; \n"
"    padding-left: 12px; \n"
"    padding-top: 4px;\n"
"}")
        self.btn_pesquisar.setText("")
        self.btn_pesquisar.setObjectName("btn_pesquisar")
        self.lbl_nomeCliente = QtWidgets.QLabel(frm_Cliente)
        self.lbl_nomeCliente.setGeometry(QtCore.QRect(0, 110, 151, 21))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_nomeCliente.setFont(font)
        self.lbl_nomeCliente.setStyleSheet("QLabel {\n"
"    font-size: 16px;\n"
"    color: #333333;\n"
"    font-weight: bold;\n"
"    text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.4);\n"
"}\n"
"")
        self.lbl_nomeCliente.setObjectName("lbl_nomeCliente")
        self.txt_nomeCliente = QtWidgets.QLineEdit(frm_Cliente)
        self.txt_nomeCliente.setGeometry(QtCore.QRect(150, 100, 371, 41))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.txt_nomeCliente.setFont(font)
        self.txt_nomeCliente.setStyleSheet("QLineEdit {\n"
"    border: 2px solid #cccccc; \n"
"    border-radius: 5px; \n"
"    padding: 6px; \n"
"    font-size: 14px; \n"
"    background-color: #ffffff;\n"
"    transition: all 0.3s ease;\n"
"}\n"
"\n"
"QLineEdit:hover {\n"
"    border: 2px solid #3f51b5; \n"
"    background-color: #f5f5f5; \n"
"}\n"
"")
        self.txt_nomeCliente.setObjectName("txt_nomeCliente")
        self.btn_filtro = QtWidgets.QPushButton(frm_Cliente)
        self.btn_filtro.setGeometry(QtCore.QRect(530, 80, 21, 21))
        self.btn_filtro.setStyleSheet("QPushButton {\n"
"    background-color: #ffffff; \n"
"    border: 2px solid #d1c4b2; \n"
"    border-radius: 12px;\n"
"    color: #5a5a5a; \n"
"    font-size: 14px; \n"
"    font-weight: bold;\n"
"    padding: 10px 16px; \n"
"    background-image:url(:/iconFilt/Img/filtro.png);\n"
"    background-repeat: no-repeat;\n"
"    background-position: center;\n"
"    transition: all 0.3s ease; \n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #f2ebe0; \n"
"    border-color: #c4b49e;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #e8dfcf; \n"
"    border-color: #b39b8d; \n"
"    padding-left: 12px;\n"
"    padding-top: 4px;\n"
"}")
        self.btn_filtro.setText("")
        self.btn_filtro.setObjectName("btn_filtro")

        self.retranslateUi(frm_Cliente)
        QtCore.QMetaObject.connectSlotsByName(frm_Cliente)

    def retranslateUi(self, frm_Cliente):
        _translate = QtCore.QCoreApplication.translate
        frm_Cliente.setWindowTitle(_translate("frm_Cliente", "Clientes"))
        item = self.tbl_cliente.horizontalHeaderItem(0)
        item.setText(_translate("frm_Cliente", "ID"))
        item = self.tbl_cliente.horizontalHeaderItem(1)
        item.setText(_translate("frm_Cliente", "Nome"))
        item = self.tbl_cliente.horizontalHeaderItem(2)
        item.setText(_translate("frm_Cliente", "Celular"))
        item = self.tbl_cliente.horizontalHeaderItem(3)
        item.setText(_translate("frm_Cliente", "Cidade"))
        self.lbl_nomeCliente.setText(_translate("frm_Cliente", "Nome do Cliente:"))

        ##Botões sistema##
        self.btn_voltar.clicked.connect(lambda: self.sairTela(frm_Cliente))
        self.btn_filtro.clicked.connect(self.consultarGeral)

        ##Funções sistema
    def sairTela(self, formCliente):
        formCliente.close()

    def consultarGeral(self):
        try:
                mydb = mysql.connector.connect(
                host = 'localhost',
                user = 'root',
                password = 'ARiel18',
                database = 'python',
                )
                print('Conexão bem sucedida!')

        except mysql.connector.Error as err:
            print(f'Erro: {err}')
        except Exception as e:
            print(f"Erro inesperado: {e}")
            traceback.print_exc()  # Exibe a pilha de erro completa
        finally:
            input("Pressione Enter para sair...")  # Aguarda o usuário para não fechar automaticamente

        mycursor = mydb.cursor()
        mycursor.execute('SELECT * FROM cliente')
        myresult = mycursor.fetchall()
        df = pd.DataFrame(myresult, columns= ['idCliente', 'Nome', 'Celular', 'Cidade'])
        self.all_data = df

        numRows = len(self.all_data.index)
        self.tbl_cliente.setColumnCount(len(self.all_data.columns))
        self.tbl_cliente.setRowCount(numRows)
        self.tbl_cliente.setHorizontalHeaderLabels(self.all_data.columns)
        
        for i in range(numRows):
            for j in range(self.all_data.columns):
                self.tbl_cliente.setItem(i, j, QTableWidget(str(self.all_data.iat[i,j])))

        self.tbl_cliente.resizeColumnsToContents()
        self.tbl_cliente.resizeRowsToContents()

        mycursor.close()

import icon_consultar
import icon_adicionar
import icon_alterar
import icon_excluir
import icon_filtro
import icon_pesq
import icon_retornar

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    frm_Main = QtWidgets.QMainWindow()
    ui = Ui_frm_Cliente()
    ui.setupUi(frm_Main)
    frm_Main.show()
    sys.exit(app.exec_())