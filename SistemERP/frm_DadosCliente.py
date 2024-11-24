from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon

class Ui_frm_DadosCliente(object):
    def setupUi(self, frm_DadosCliente):
        frm_DadosCliente.setObjectName("frm_DadosCliente")
        frm_DadosCliente.resize(512, 327)
        frm_DadosCliente.setFixedSize(512, 327)
        frm_DadosCliente.setStyleSheet("QWidget {\n"
"    background-color: #eaf2f8;\n"
"    border-radius: 8px;\n"
"}")
        frm_DadosCliente.setWindowIcon(QIcon("C:/Users/Ariel/PycharmProjects/Scripts/Sistema/Img/AvsB.ico"))
        self.lbl_nome = QtWidgets.QLabel(frm_DadosCliente)
        self.lbl_nome.setGeometry(QtCore.QRect(50, 50, 61, 21))
        self.lbl_nome.setStyleSheet("QLabel {\n"
"    font-size: 16px;\n"
"    color: #333333;\n"
"    font-weight: bold;\n"
"    text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.4);\n"
"}\n"
"")
        self.lbl_nome.setObjectName("lbl_nome")
        self.txt_nome = QtWidgets.QLineEdit(frm_DadosCliente)
        self.txt_nome.setGeometry(QtCore.QRect(120, 40, 371, 41))
        self.txt_nome.setStyleSheet("QLineEdit {\n"
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
        self.txt_nome.setObjectName("txt_nome")
        self.lbl_celular = QtWidgets.QLabel(frm_DadosCliente)
        self.lbl_celular.setGeometry(QtCore.QRect(30, 100, 81, 16))
        self.lbl_celular.setStyleSheet("QLabel {\n"
"    font-size: 16px;\n"
"    color: #333333;\n"
"    font-weight: bold;\n"
"    text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.4);\n"
"}\n"
"")
        self.lbl_celular.setObjectName("lbl_celular")
        self.lbl_cidade = QtWidgets.QLabel(frm_DadosCliente)
        self.lbl_cidade.setGeometry(QtCore.QRect(50, 150, 61, 16))
        self.lbl_cidade.setStyleSheet("QLabel {\n"
"    font-size: 16px;\n"
"    color: #333333;\n"
"    font-weight: bold;\n"
"    text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.4);\n"
"}\n"
"")
        self.lbl_cidade.setObjectName("lbl_cidade")
        self.btn_cancelar = QtWidgets.QPushButton(frm_DadosCliente)
        self.btn_cancelar.setGeometry(QtCore.QRect(130, 220, 91, 81))
        self.btn_cancelar.setStyleSheet("QPushButton {\n"
"    background-color: #ffebee; \n"
"    border: 2px solid #ffcdd2;\n"
"    border-radius: 10px;\n"
"    color: #b71c1c; \n"
"    font-size: 14px;\n"
"    font-weight: bold;\n"
"    padding: 10px 16px;\n"
"    background-image: url(:/iconCanc/Img/cancelar.png);\n"
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
        self.btn_cancelar.setText("")
        self.btn_cancelar.setObjectName("btn_cancelar")
        self.btn_cadastrar = QtWidgets.QPushButton(frm_DadosCliente)
        self.btn_cadastrar.setGeometry(QtCore.QRect(280, 220, 91, 81))
        self.btn_cadastrar.setStyleSheet("QPushButton {\n"
"    background-color: #ffffff;\n"
"    border: 2px solid #d1c4b2;\n"
"    border-radius: 12px;\n"
"    color: #5a5a5a;\n"
"    font-size: 14px;\n"
"    font-weight: bold;\n"
"    padding: 10px 16px;\n"
"    background-image:url(:/iconCad/Img/cadastrar.png); \n"
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
        self.btn_cadastrar.setText("")
        self.btn_cadastrar.setObjectName("btn_cadastrar")
        self.txt_celular = QtWidgets.QLineEdit(frm_DadosCliente)
        self.txt_celular.setGeometry(QtCore.QRect(120, 90, 371, 41))
        self.txt_celular.setStyleSheet("QLineEdit {\n"
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
        self.txt_celular.setObjectName("txt_celular")
        self.txt_cidade = QtWidgets.QLineEdit(frm_DadosCliente)
        self.txt_cidade.setGeometry(QtCore.QRect(120, 140, 371, 41))
        self.txt_cidade.setStyleSheet("QLineEdit {\n"
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
        self.txt_cidade.setObjectName("txt_cidade")

        self.retranslateUi(frm_DadosCliente)
        QtCore.QMetaObject.connectSlotsByName(frm_DadosCliente)

    def retranslateUi(self, frm_DadosCliente):
        _translate = QtCore.QCoreApplication.translate
        frm_DadosCliente.setWindowTitle(_translate("frm_DadosCliente", "Dados Cliente"))
        self.lbl_nome.setText(_translate("frm_DadosCliente", "Nome:"))
        self.lbl_celular.setText(_translate("frm_DadosCliente", "Celular: "))
        self.lbl_cidade.setText(_translate("frm_DadosCliente", "Cidade:"))
        self.txt_celular.setInputMask(_translate("frm_DadosCliente", "(00) 0 0000-0000"))

        ##Imagens sistemas
import icon_cadastrar
import icon_cancelar


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    frm_Main = QtWidgets.QMainWindow()
    ui = Ui_frm_DadosCliente()
    ui.setupUi(frm_Main)
    frm_Main.show()
    sys.exit(app.exec_())
