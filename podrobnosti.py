from PyQt5 import QtCore, QtGui, QtWidgets
from datetime import date
import sqlite3
from os import replace


class Ui_MainWindow_Podrobnosti(object):


    def LoadDataFromDB(self, vybraneId):

        connection = sqlite3.connect('databaze.db')
        cur = connection.cursor()

        id1 = vybraneId

        potrebneData = ["Nazev", "Dulezitost", "Datum_odevzdani", "Postup", "ID", "Datum_zadani", "Poznamky"]

        for word in potrebneData:

            if word == potrebneData[0]:
                
                sqlstr = "SELECT {word} FROM tabulka WHERE ID='{id1}'".format(word=word, id1=id1)

                vysledek1 = cur.execute(sqlstr).fetchall()

                udaje = vysledek1[0][0]


                self.lineEdit_2.setText(udaje)

            if word == potrebneData[5]:

                sqlstr = "SELECT {word} FROM tabulka WHERE ID='{id1}'".format(word=word, id1=id1)

                vysledek1 = cur.execute(sqlstr).fetchall()

                udaje = vysledek1[0][0]

                self.lineEdit_3.setText(udaje)

            if word == potrebneData[2]:

                sqlstr = "SELECT {word} FROM tabulka WHERE ID='{id1}'".format(word=word, id1=id1)

                vysledek1 = cur.execute(sqlstr).fetchall()

                udaje = vysledek1[0][0]

                self.lineEdit_4.setText(udaje)

            if word == potrebneData[1]:

                sqlstr = "SELECT {word} FROM tabulka WHERE ID='{id1}'".format(word=word, id1=id1)

                vysledek1 = cur.execute(sqlstr).fetchall()

                udaje = vysledek1[0][0]

                self.lineEdit_5.setText(udaje)

            if word == potrebneData[3]:

                sqlstr = "SELECT {word} FROM tabulka WHERE ID='{id1}'".format(word=word, id1=id1)

                vysledek1 = cur.execute(sqlstr).fetchall()

                udaje = vysledek1[0][0]

                udaje = udaje.replace('%', "")

                if udaje == "":

                    udaje = 0

                self.progressBar.setValue(int(udaje))

            if word == potrebneData[4]:

                sqlstr = "SELECT {word} FROM tabulka WHERE ID='{id1}'".format(word=word, id1=id1)

                vysledek1 = cur.execute(sqlstr).fetchall()

                udaje = vysledek1[0][0]

                self.lineEdit_6.setText(udaje)


            if word == potrebneData[6]:

                sqlstr = "SELECT {word} FROM tabulka WHERE ID='{id1}'".format(word=word, id1=id1)

                vysledek1 = cur.execute(sqlstr).fetchall()

                udaje = vysledek1[0][0]

                if udaje == "CODE1ZADNYPOPIS":

                    udaje = ""

                self.plaintextEdit.setPlainText(udaje)


        connection.commit()
        cur.close()




    def setupUi(self, MainWindow):

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1013, 557)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        MainWindow.setWindowFlag(QtCore.Qt.WindowCloseButtonHint, True)
        MainWindow.setWindowFlag(QtCore.Qt.WindowMaximizeButtonHint, False)
        MainWindow.setWindowFlag(QtCore.Qt.WindowMinimizeButtonHint, False)


        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(450, 35, 191, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")


        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(30, 35, 61, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")

        
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(30, 120, 181, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")

        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(30, 295, 181, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")


        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(30, 210, 151, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")


        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(30, 390, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")


        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(30, 490, 41, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")


        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(800, 515, 191, 20))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")


        self.plaintextEdit = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plaintextEdit.setGeometry(QtCore.QRect(450, 60, 511, 441))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.plaintextEdit.setFont(font)
        self.plaintextEdit.setReadOnly(True)
        self.plaintextEdit.setObjectName("plaintextEdit")


        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(30, 60, 341, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setReadOnly(True)
        self.lineEdit_2.setObjectName("lineEdit_2")


        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(30, 145, 261, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_3.setFont(font)
        self.lineEdit_3.setReadOnly(True)
        self.lineEdit_3.setObjectName("lineEdit_3")
        


        self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_4.setGeometry(QtCore.QRect(30, 235, 261, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_4.setFont(font)
        self.lineEdit_4.setReadOnly(True)
        self.lineEdit_4.setObjectName("lineEdit_4")


        self.lineEdit_5 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_5.setGeometry(QtCore.QRect(30, 320, 261, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_5.setFont(font)
        self.lineEdit_5.setReadOnly(True)
        self.lineEdit_5.setObjectName("lineEdit_5")


        self.lineEdit_6 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_6.setGeometry(QtCore.QRect(60, 490, 50, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_6.setFont(font)
        self.lineEdit_6.setReadOnly(True)
        self.lineEdit_6.setObjectName("lineEdit_6")


        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(30, 418, 261, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.progressBar.setFont(font)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(310, 500, 100, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")

        self.pushButton.clicked.connect(self.close)


        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):

        datum1 = date.today()
        datum2 = date.strftime(datum1, "%d.%m.%Y")

        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Podrobnosti"))
        self.pushButton.setText(_translate("MainWindow", "Odejít"))
        self.label.setText(_translate("MainWindow", "Popis:"))
        self.label_2.setText(_translate("MainWindow", "Název:"))
        self.label_3.setText(_translate("MainWindow", "Datum zadání:"))
        self.label_4.setText(_translate("MainWindow", "Důležitost:"))
        self.label_5.setText(_translate("MainWindow", "Datum odevzdání:"))
        self.label_6.setText(_translate("MainWindow", "Postup:"))
        self.label_7.setText(_translate("MainWindow", "ID:"))
        self.label_8.setText(_translate("MainWindow", "Dnešní datum: " + datum2))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow_Podrobnosti()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
