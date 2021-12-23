from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QAbstractItemView, QMessageBox
from datetime import date
import sqlite3


class Ui_MainWindow_HlavniMenu(object):
    

    def pomocnafunkce(self):

        #funkce pro zjištění id vybraného políčka v tabulce

        vybraneJmeno = str(self.tableWidget.currentRow())


        if vybraneJmeno != "-1" and vybraneJmeno != "":

            vybraneJmeno = self.tableWidget.currentRow()

            try:

                idVybranehoJmena = str(self.tableWidget.item(vybraneJmeno, 4).text())

                return str(idVybranehoJmena)

            except:

                return True

        else:

            return True


    def loaddata(self):

        # načte data z databáze do tabulky, popřípadně databázi vytvoří, pokud ji nenajde

        connection = sqlite3.connect('databaze.db')
        cur = connection.cursor()

        try:

            # načtení dat z existující db

            sqlstr = 'SELECT * FROM tabulka'

            tablerow=0
            pocetRadku=1
            results = cur.execute(sqlstr)

            self.tableWidget.setRowCount(pocetRadku)

            for row in results:
                self.tableWidget.setRowCount(pocetRadku)
                self.tableWidget.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(row[0]))
                self.tableWidget.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(row[1]))
                self.tableWidget.setItem(tablerow, 2, QtWidgets.QTableWidgetItem(row[2]))
                self.tableWidget.setItem(tablerow, 3, QtWidgets.QTableWidgetItem(row[3]))
                self.tableWidget.setItem(tablerow, 4, QtWidgets.QTableWidgetItem(row[4]))
                tablerow+=1
                pocetRadku = tablerow+1


        except:

            # vytvoření nové db

            VytvoritTabulku = "CREATE TABLE 'tabulka' ('Nazev' TEXT, 'Dulezitost' TEXT, 'Datum_odevzdani' DATE, 'Postup' TEXT, 'ID' TEXT PRIMARY KEY NOT NULL, 'Datum_zadani' DATE, 'Poznamky' TEXT)"

            cur.execute(VytvoritTabulku)

            connection.commit()
            cur.close()
            self.loaddata()


    def setupUi(self, MainWindow):


        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1000, 455)
        MainWindow.setWindowFlag(QtCore.Qt.WindowCloseButtonHint, True)
        MainWindow.setWindowFlag(QtCore.Qt.WindowMaximizeButtonHint, False)
        MainWindow.setWindowFlag(QtCore.Qt.WindowMinimizeButtonHint, True)


        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(750, 410, 181, 16))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label.setFont(font)
        self.label.setObjectName("label")


        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(40, 50, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")


        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(40, 230, 161, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")


        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(40, 360, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")

        
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(40, 110, 201, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setObjectName("pushButton_4")



        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(180, 50, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setObjectName("pushButton_5")


        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(200, 360, 81, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setObjectName("pushButton_6")


        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.horizontalHeader().setDefaultAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget.setGeometry(QtCore.QRect(370, 50, 592, 351))
        self.tableWidget.setMinimumSize(QtCore.QSize(511, 0))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.tableWidget.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setRowCount(0)
        self.tableWidget.setColumnWidth(0,240)  # Název
        self.tableWidget.setColumnWidth(1,90)   # Důležitost
        self.tableWidget.setColumnWidth(2,110)  # Datum odevzdání
        self.tableWidget.setColumnWidth(3,80)   # Postup
        self.tableWidget.setColumnWidth(4,20)   # ID
        self.loaddata()

        self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)


        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)

        self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)

        self.tableWidget.cellClicked.connect(self.pomocnafunkce)


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
        MainWindow.setWindowTitle(_translate("MainWindow", "Zápisník úkolů (To do list)"))

        self.tableWidget.setSortingEnabled(True)
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Název"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Důležitost"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Datum odevzdání"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Postup (%)"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "ID"))

        self.pushButton.setText(_translate("MainWindow", "Přidat nový úkol"))
        self.pushButton_2.setText(_translate("MainWindow", "Smazat vybraný úkol"))
        self.pushButton_3.setText(_translate("MainWindow", "Aktualizovat tabulku"))
        self.pushButton_4.setText(_translate("MainWindow", "Podrobnosti o vybraném úkolu"))
        self.pushButton_5.setText(_translate("MainWindow", "Upravit vybraný úkol"))
        self.pushButton_6.setText(_translate("MainWindow", "Více"))
        self.label.setText(_translate("MainWindow", "Dnešní datum: " + datum2))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow_HlavniMenu()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
