from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon


class Ui_frm_Main(object):
    def setupUi(self, frm_Main):
        frm_Main.setObjectName("frm_Main")
        frm_Main.resize(719, 294)
        frm_Main.setFixedSize(719, 294)
        frm_Main.setStyleSheet("")
        frm_Main.setWindowIcon(QIcon("C:/Users/Ariel/PycharmProjects/Scripts/Sistema/Img/AvsB.ico"))
        self.centralwidget = QtWidgets.QWidget(frm_Main)
        self.centralwidget.setStyleSheet("background-color: #2c2c2c;")
        self.centralwidget.setObjectName("centralwidget")
        self.btn_cliente = QtWidgets.QPushButton(self.centralwidget)
        self.btn_cliente.setGeometry(QtCore.QRect(0, 0, 81, 71))
        self.btn_cliente.setStyleSheet("QPushButton{\n"
"    background-color: #f5f5f5;\n"
"    border: 2px solid #cccccc;\n"
"    border-radius: 10px; \n"
"    padding: 10px; \n"
"    color: #333333; \n"
"    font-size: 14px;\n"
"    background-image: url(:/icons/Img/cliente.png);\n"
"    background-repeat: no-repeat;\n"
"    background-position: center;\n"
"    transition: all 0.3s ease;\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: #e0e0e0;\n"
"    border-color: #aaaaaa;\n"
"    transform: scale(1.05); \n"
"}\n"
"QPushButton:pressed{\n"
"    background-color: #d6d6d6;\n"
"    border-color: #888888;\n"
"    transform: scale(0.95);\n"
"}")
        self.btn_cliente.setText("")
        self.btn_cliente.setObjectName("btn_cliente")
        self.btn_receber = QtWidgets.QPushButton(self.centralwidget)
        self.btn_receber.setGeometry(QtCore.QRect(480, 0, 81, 71))
        self.btn_receber.setStyleSheet("QPushButton{\n"
"    background-color: #f5f5f5;\n"
"    border: 2px solid #cccccc;\n"
"    border-radius: 10px; \n"
"    padding: 10px;\n"
"    color: #333333;\n"
"    font-size: 14px; \n"
"    background-image:url(:/iconR/Img/receber.png);\n"
"    background-repeat: no-repeat; \n"
"    background-position: center; \n"
"    transition: all 0.3s ease;\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: #e0e0e0; \n"
"    border-color: #aaaaaa; \n"
"    transform: scale(1.05); \n"
"}\n"
"QPushButton:pressed{\n"
"    background-color: #d6d6d6;\n"
"    border-color: #888888;\n"
"    transform: scale(0.95);\n"
"}")
        self.btn_receber.setText("")
        self.btn_receber.setObjectName("btn_receber")
        self.btn_produtos = QtWidgets.QPushButton(self.centralwidget)
        self.btn_produtos.setGeometry(QtCore.QRect(160, 0, 81, 71))
        self.btn_produtos.setStyleSheet("QPushButton{\n"
"    background-color: #f5f5f5;\n"
"    border: 2px solid #cccccc;\n"
"    border-radius: 10px;\n"
"    padding: 10px; \n"
"    color: #333333; \n"
"    font-size: 14px; \n"
"    background-image:url(:/iconP/Img/produtos.png); \n"
"    background-repeat: no-repeat; \n"
"    background-position: center; \n"
"    transition: all 0.3s ease;\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: #e0e0e0;\n"
"    border-color: #aaaaaa;\n"
"    transform: scale(1.05); \n"
"}\n"
"QPushButton:pressed{\n"
"    background-color: #d6d6d6;\n"
"    border-color: #888888;\n"
"    transform: scale(0.95);\n"
"}")
        self.btn_produtos.setText("")
        self.btn_produtos.setObjectName("btn_produtos")
        self.btn_vendas = QtWidgets.QPushButton(self.centralwidget)
        self.btn_vendas.setGeometry(QtCore.QRect(240, 0, 81, 71))
        self.btn_vendas.setStyleSheet("QPushButton{\n"
"    background-color: #f5f5f5;\n"
"    border: 2px solid #cccccc;\n"
"    border-radius: 10px; \n"
"    padding: 10px;\n"
"    color: #333333;\n"
"    font-size: 14px; \n"
"    background-image: url(:/iconV/Img/venda.png);\n"
"    background-repeat: no-repeat; \n"
"    background-position: center; \n"
"    transition: all 0.3s ease;\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: #e0e0e0;\n"
"    border-color: #aaaaaa;\n"
"    transform: scale(1.05); \n"
"}\n"
"QPushButton:pressed{\n"
"    background-color: #d6d6d6;\n"
"    border-color: #888888;\n"
"    transform: scale(0.95);\n"
"}")
        self.btn_vendas.setText("")
        self.btn_vendas.setObjectName("btn_vendas")
        self.btn_pagar = QtWidgets.QPushButton(self.centralwidget)
        self.btn_pagar.setGeometry(QtCore.QRect(320, 0, 81, 71))
        self.btn_pagar.setStyleSheet("QPushButton{\n"
"    background-color: #f5f5f5; \n"
"    border: 2px solid #cccccc; \n"
"    border-radius: 10px;\n"
"    padding: 10px;\n"
"    color: #333333;\n"
"    font-size: 14px;\n"
"    background-image:url(:/iconPa/Img/contasPagar.png);\n"
"    background-repeat: no-repeat;\n"
"    background-position: center;\n"
"    transition: all 0.3s ease;\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: #e0e0e0;\n"
"    border-color: #aaaaaa; \n"
"    transform: scale(1.05); \n"
"}\n"
"QPushButton:pressed{\n"
"    background-color: #d6d6d6;\n"
"    border-color: #888888;\n"
"    transform: scale(0.95);\n"
"}")
        self.btn_pagar.setText("")
        self.btn_pagar.setObjectName("btn_pagar")
        self.btn_bancos = QtWidgets.QPushButton(self.centralwidget)
        self.btn_bancos.setGeometry(QtCore.QRect(400, 0, 81, 71))
        self.btn_bancos.setStyleSheet("QPushButton{\n"
"    background-color: #f5f5f5;\n"
"    border: 2px solid #cccccc;\n"
"    border-radius: 10px;\n"
"    padding: 10px;\n"
"    color: #333333;\n"
"    font-size: 14px;\n"
"    background-image:url(:/iconB/Img/banco.png);\n"
"    background-repeat: no-repeat;\n"
"    background-position: center;\n"
"    transition: all 0.3s ease;\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: #e0e0e0;\n"
"    border-color: #aaaaaa; \n"
"    transform: scale(1.05); \n"
"}\n"
"QPushButton:pressed{\n"
"    background-color: #d6d6d6;\n"
"    border-color: #888888;\n"
"    transform: scale(0.95);\n"
"}")
        self.btn_bancos.setText("")
        self.btn_bancos.setObjectName("btn_bancos")
        self.btn_caixa = QtWidgets.QPushButton(self.centralwidget)
        self.btn_caixa.setGeometry(QtCore.QRect(560, 0, 81, 71))
        self.btn_caixa.setStyleSheet("QPushButton{\n"
"    background-color: #f5f5f5;\n"
"    border: 2px solid #cccccc; \n"
"    border-radius: 10px; \n"
"    padding: 10px; \n"
"    color: #333333; \n"
"    font-size: 14px;\n"
"    background-image:url(:/iconCa/Img/caixa.png); \n"
"    background-repeat: no-repeat; \n"
"    background-position: center; \n"
"    transition: all 0.3s ease;\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: #e0e0e0;\n"
"    border-color: #aaaaaa;\n"
"    transform: scale(1.05); \n"
"}\n"
"QPushButton:pressed{\n"
"    background-color: #d6d6d6;\n"
"    border-color: #888888;\n"
"    transform: scale(0.95);\n"
"}")
        self.btn_caixa.setText("")
        self.btn_caixa.setObjectName("btn_caixa")
        self.btn_fornecedor = QtWidgets.QPushButton(self.centralwidget)
        self.btn_fornecedor.setGeometry(QtCore.QRect(80, 0, 81, 71))
        self.btn_fornecedor.setStyleSheet("QPushButton{\n"
"    background-color: #f5f5f5;\n"
"    border: 2px solid #cccccc;\n"
"    border-radius: 10px;\n"
"    padding: 10px;\n"
"    color: #333333;\n"
"    font-size: 14px;\n"
"    background-image:url(:/icon/Img/fornecedor.png);\n"
"    background-repeat: no-repeat;\n"
"    background-position: center;\n"
"    transition: all 0.3s ease;\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: #e0e0e0;\n"
"    border-color: #aaaaaa; \n"
"    transform: scale(1.05); \n"
"}\n"
"QPushButton:pressed{\n"
"    background-color: #d6d6d6;\n"
"    border-color: #888888;\n"
"    transform: scale(0.95);\n"
"}")
        self.btn_fornecedor.setText("")
        self.btn_fornecedor.setObjectName("btn_fornecedor")
        self.btn_sair = QtWidgets.QPushButton(self.centralwidget)
        self.btn_sair.setGeometry(QtCore.QRect(640, 0, 81, 71))
        self.btn_sair.setStyleSheet("QPushButton{\n"
"    background-color: #f5f5f5; \n"
"    border: 2px solid #cccccc; \n"
"    border-radius: 10px; \n"
"    padding: 10px; \n"
"    color: #333333; \n"
"    font-size: 14px; \n"
"    background-image:url(:/iconSa/Img/sair.png); \n"
"    background-repeat: no-repeat; \n"
"    background-position: center; \n"
"    transition: all 0.3s ease;\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: #e0e0e0;\n"
"    border-color: #aaaaaa;\n"
"    transform: scale(1.05); \n"
"}\n"
"QPushButton:pressed{\n"
"    background-color: #d6d6d6;\n"
"    border-color: #888888;\n"
"    transform: scale(0.95);\n"
"}")
        self.btn_sair.setText("")
        self.btn_sair.setObjectName("btn_sair")
        frm_Main.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(frm_Main)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 719, 34))
        self.menubar.setStyleSheet("QMenuBar {\n"
"    background-color: #2E3440;\n"
"    color: white;\n"
"    padding: 5px;\n"
"}\n"
"\n"
"QMenuBar::item {\n"
"    background: transparent;\n"
"    padding: 4px 10px;\n"
"}\n"
"\n"
"QMenuBar::item:selected {   \n"
"    background: #3B4252;    \n"
"    color: #88C0D0;          \n"
"}\n"
"\n"
"QMenu {\n"
"    background-color: #2E3440;\n"
"    color: white; \n"
"    border: 1px solid #4C566A;\n"
"}\n"
"\n"
"QMenu::item:selected {      \n"
"    background-color: #3B4252;\n"
"    color: #A3BE8C;\n"
"}\n"
"")
        self.menubar.setObjectName("menubar")
        self.menuCadastros = QtWidgets.QMenu(self.menubar)
        self.menuCadastros.setObjectName("menuCadastros")
        self.menuOpera_es = QtWidgets.QMenu(self.menubar)
        self.menuOpera_es.setObjectName("menuOpera_es")
        self.menuSa_da_de_produtos = QtWidgets.QMenu(self.menuOpera_es)
        self.menuSa_da_de_produtos.setObjectName("menuSa_da_de_produtos")
        self.menuEstoque = QtWidgets.QMenu(self.menuOpera_es)
        self.menuEstoque.setObjectName("menuEstoque")
        self.menuCompras = QtWidgets.QMenu(self.menuOpera_es)
        self.menuCompras.setObjectName("menuCompras")
        self.menuFinanceiro = QtWidgets.QMenu(self.menubar)
        self.menuFinanceiro.setObjectName("menuFinanceiro")
        self.menuConsultas = QtWidgets.QMenu(self.menubar)
        self.menuConsultas.setObjectName("menuConsultas")
        self.menuVendas = QtWidgets.QMenu(self.menuConsultas)
        self.menuVendas.setObjectName("menuVendas")
        self.menuConsumos = QtWidgets.QMenu(self.menuConsultas)
        self.menuConsumos.setObjectName("menuConsumos")
        frm_Main.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(frm_Main)
        self.statusbar.setObjectName("statusbar")
        frm_Main.setStatusBar(self.statusbar)
        self.actionCliente = QtWidgets.QAction(frm_Main)
        self.actionCliente.setObjectName("actionCliente")
        self.actionFornecedor = QtWidgets.QAction(frm_Main)
        self.actionFornecedor.setObjectName("actionFornecedor")
        self.actionUsu_rio_do_sistema = QtWidgets.QAction(frm_Main)
        self.actionUsu_rio_do_sistema.setObjectName("actionUsu_rio_do_sistema")
        self.actionVenda = QtWidgets.QAction(frm_Main)
        self.actionVenda.setObjectName("actionVenda")
        self.actionConsumo_de_produtos = QtWidgets.QAction(frm_Main)
        self.actionConsumo_de_produtos.setObjectName("actionConsumo_de_produtos")
        self.actionSaldo = QtWidgets.QAction(frm_Main)
        self.actionSaldo.setObjectName("actionSaldo")
        self.actionCompras_2 = QtWidgets.QAction(frm_Main)
        self.actionCompras_2.setObjectName("actionCompras_2")
        self.actionPedido = QtWidgets.QAction(frm_Main)
        self.actionPedido.setObjectName("actionPedido")
        self.actionCancelar_compra = QtWidgets.QAction(frm_Main)
        self.actionCancelar_compra.setObjectName("actionCancelar_compra")
        self.actionCaixa = QtWidgets.QAction(frm_Main)
        self.actionCaixa.setObjectName("actionCaixa")
        self.actionBanco = QtWidgets.QAction(frm_Main)
        self.actionBanco.setObjectName("actionBanco")
        self.actionContas_para_pagar = QtWidgets.QAction(frm_Main)
        self.actionContas_para_pagar.setObjectName("actionContas_para_pagar")
        self.actionContas_para_receber = QtWidgets.QAction(frm_Main)
        self.actionContas_para_receber.setObjectName("actionContas_para_receber")
        self.actionContas_pagas = QtWidgets.QAction(frm_Main)
        self.actionContas_pagas.setObjectName("actionContas_pagas")
        self.actionContas_recebidas = QtWidgets.QAction(frm_Main)
        self.actionContas_recebidas.setObjectName("actionContas_recebidas")
        self.actionGeral = QtWidgets.QAction(frm_Main)
        self.actionGeral.setObjectName("actionGeral")
        self.actionResumido = QtWidgets.QAction(frm_Main)
        self.actionResumido.setObjectName("actionResumido")
        self.actionGeral_3 = QtWidgets.QAction(frm_Main)
        self.actionGeral_3.setObjectName("actionGeral_3")
        self.actionResumido_2 = QtWidgets.QAction(frm_Main)
        self.actionResumido_2.setObjectName("actionResumido_2")
        self.menuCadastros.addAction(self.actionCliente)
        self.menuCadastros.addAction(self.actionFornecedor)
        self.menuCadastros.addAction(self.actionUsu_rio_do_sistema)
        self.menuSa_da_de_produtos.addAction(self.actionVenda)
        self.menuSa_da_de_produtos.addAction(self.actionConsumo_de_produtos)
        self.menuEstoque.addAction(self.actionSaldo)
        self.menuCompras.addAction(self.actionCompras_2)
        self.menuCompras.addAction(self.actionPedido)
        self.menuCompras.addAction(self.actionCancelar_compra)
        self.menuOpera_es.addAction(self.menuSa_da_de_produtos.menuAction())
        self.menuOpera_es.addAction(self.menuEstoque.menuAction())
        self.menuOpera_es.addAction(self.menuCompras.menuAction())
        self.menuFinanceiro.addAction(self.actionCaixa)
        self.menuFinanceiro.addAction(self.actionBanco)
        self.menuFinanceiro.addAction(self.actionContas_para_pagar)
        self.menuFinanceiro.addAction(self.actionContas_para_receber)
        self.menuFinanceiro.addAction(self.actionContas_pagas)
        self.menuFinanceiro.addAction(self.actionContas_recebidas)
        self.menuVendas.addAction(self.actionGeral)
        self.menuVendas.addAction(self.actionResumido)
        self.menuConsumos.addAction(self.actionGeral_3)
        self.menuConsumos.addAction(self.actionResumido_2)
        self.menuConsultas.addAction(self.menuVendas.menuAction())
        self.menuConsultas.addAction(self.menuConsumos.menuAction())
        self.menubar.addAction(self.menuCadastros.menuAction())
        self.menubar.addAction(self.menuOpera_es.menuAction())
        self.menubar.addAction(self.menuConsultas.menuAction())
        self.menubar.addAction(self.menuFinanceiro.menuAction())

        self.retranslateUi(frm_Main)
        QtCore.QMetaObject.connectSlotsByName(frm_Main)

    def retranslateUi(self, frm_Main):
        _translate = QtCore.QCoreApplication.translate
        frm_Main.setWindowTitle(_translate("frm_Main", "Tela Principal"))
        self.menuCadastros.setTitle(_translate("frm_Main", "Cadastros"))
        self.menuOpera_es.setTitle(_translate("frm_Main", "Operações"))
        self.menuSa_da_de_produtos.setTitle(_translate("frm_Main", "Saída de produtos"))
        self.menuEstoque.setTitle(_translate("frm_Main", "Estoque"))
        self.menuCompras.setTitle(_translate("frm_Main", "Compras"))
        self.menuFinanceiro.setTitle(_translate("frm_Main", "Financeiro"))
        self.menuConsultas.setTitle(_translate("frm_Main", "Consultas"))
        self.menuVendas.setTitle(_translate("frm_Main", "Vendas"))
        self.menuConsumos.setTitle(_translate("frm_Main", "Consumos"))
        self.actionCliente.setText(_translate("frm_Main", "Cliente"))
        self.actionFornecedor.setText(_translate("frm_Main", "Fornecedor"))
        self.actionUsu_rio_do_sistema.setText(_translate("frm_Main", "Usuário"))
        self.actionVenda.setText(_translate("frm_Main", "Venda"))
        self.actionConsumo_de_produtos.setText(_translate("frm_Main", "Consumo de produtos"))
        self.actionSaldo.setText(_translate("frm_Main", "Saldo"))
        self.actionCompras_2.setText(_translate("frm_Main", "Compras"))
        self.actionPedido.setText(_translate("frm_Main", "Pedido"))
        self.actionCancelar_compra.setText(_translate("frm_Main", "Cancelar"))
        self.actionCaixa.setText(_translate("frm_Main", "Caixa"))
        self.actionBanco.setText(_translate("frm_Main", "Banco"))
        self.actionContas_para_pagar.setText(_translate("frm_Main", "Contas para pagar"))
        self.actionContas_para_receber.setText(_translate("frm_Main", "Contas para receber"))
        self.actionContas_pagas.setText(_translate("frm_Main", "Contas pagas"))
        self.actionContas_recebidas.setText(_translate("frm_Main", "Contas recebidas"))
        self.actionGeral.setText(_translate("frm_Main", "Geral"))
        self.actionResumido.setText(_translate("frm_Main", "Resumido"))
        self.actionGeral_3.setText(_translate("frm_Main", "Geral"))
        self.actionResumido_2.setText(_translate("frm_Main", "Resumido"))
##Imagens Sistema##
import icon_bancos
import icon_caixa
import icon_cliente
import icon_fornecedor
import icon_pagar
import icon_produtos
import icon_receber
import icon_sair
import icon_vendas

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    frm_Main = QtWidgets.QMainWindow()
    ui = Ui_frm_Main()
    ui.setupUi(frm_Main)
    frm_Main.show()
    sys.exit(app.exec_())
