from os import remove
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QDate
from PyQt5.QtWidgets import QMessageBox
import sqlite3
from datetime import date
from os.path import exists


class Ui_MainWindow_PridatUkol(object):

    def Vycistit(self):

        #vyčistí se všechna pole v přidání úkolu
        #okno se zavře

        self.lineEdit.clear()
        self.plaintextEdit_2.clear()

        self.checkBox.setChecked(False)
        self.checkBox_2.setChecked(False)
        self.checkBox_3.setChecked(False)

        self.spinBox.setValue(0)

        self.comboBox.setCurrentText("Normální")

        self.ResetKalendare()

        self.close()


    def Vycistit2(self):

        #vyčistí pole v přidání úkolu
        #okno se zobrazí

        self.lineEdit.clear()
        self.plaintextEdit_2.clear()

        self.checkBox.setChecked(False)
        self.checkBox_2.setChecked(False)
        self.checkBox_3.setChecked(False)

        self.spinBox.setValue(0)

        self.comboBox.setCurrentText("Normální")

        self.ResetKalendare()

        self.show()


    def Povoleni(self):

        #když se dá povolit, zobrazí se příslušné věci

        dulezitost = self.checkBox.isChecked()
        odevzdani = self.checkBox_2.isChecked()
        postup = self.checkBox_3.isChecked()

        if dulezitost == True:

            self.comboBox.setHidden(False)

        else:

            self.comboBox.setHidden(True)

        if odevzdani == True:

            self.dateEdit.setReadOnly(False)
            self.dateEdit.setHidden(False)
            self.pushButton_9.setHidden(False)

        else:
            self.dateEdit.setReadOnly(True)
            self.dateEdit.setHidden(True)
            self.pushButton_9.setHidden(True)
            
        if postup == True:

            self.progressBar.setHidden(False)
            self.spinBox.setReadOnly(False)
            self.spinBox.setHidden(False)
            self.label_6.setHidden(False)

        else:
            self.progressBar.setHidden(True)
            self.spinBox.setReadOnly(True)
            self.spinBox.setHidden(True)
            self.label_6.setHidden(True)

    def ResetKalendare(self):

        # vyresetuje kalendář na defaultní hodnotu

        datum3 = date.today()
        datum4 = int(date.strftime(datum3, "%Y"))

        self.dateEdit.setDate(QDate(datum4, 1, 1))




    def NastavitProcenta(self):

        # nastaví se procenta do loading baru

        value = int(self.spinBox.value())

        self.progressBar.setProperty("value", value)




    def PridatDoDatabaze(self):

        # přidá se úkol do databáze

        global id1

        nazev = str(self.lineEdit.text())

        if nazev != "":

            # pokud název není prázdný

            dulezitost = self.checkBox.isChecked()
            odevzdani = self.checkBox_2.isChecked()
            postup = self.checkBox_3.isChecked()


            if dulezitost == True:

                dulezitost = self.comboBox.currentText()

            else:

                dulezitost = ""
            

            if odevzdani == True:

                datum_odevzdani = self.dateEdit.date().toPyDate()

                datum_odevzdani = date.strftime(datum_odevzdani, "%d.%m.%Y")

            else:

                datum_odevzdani = ""
            
            
            if postup == True:

                postup = str(self.spinBox.value()) + '%'

            else:

                postup = ""

            poznamky = str(self.plaintextEdit_2.toPlainText())

            datum_zadani = date.today()
            datum_zadani = date.strftime(datum_zadani, "%d.%m.%Y")

            file_exists = exists("config.txt")



            if file_exists == True:

                # zkontroluje se pokud existuje config.txt kde může být uloženo nastavení o primárním klíči (číslo/písmeno)
                
                read1 = open("config.txt", 'r')

                NastaveniList = []

                for line in read1:

                    NastaveniList.append(line)

                read1.close()

                DatovyTypStr = str(NastaveniList[0])

                if DatovyTypStr == "1":

                    id1 = "a"

                    id1 = list(bytes(id1, 'ascii'))

                    id1 = id1[0]

                    id1 = str(chr(id1))


                elif DatovyTypStr == "2":

                    id1 = int(1)


            else:

                # když config.txt neexistuje, nastavní se datový typ jako číslo    

                id1 = int(1)

                DatovyTypStr = "2"

            while True:

                # samotné přidávání do databáze

                try:

                    sqliteConnection = sqlite3.connect('databaze.db')
                    cursor = sqliteConnection.cursor()

                    sqlite_insert_query = "insert into tabulka('Nazev', 'Dulezitost', 'Datum_odevzdani', 'Postup', 'ID','Datum_zadani', 'Poznamky') values(?, ?, ?, ?, ?, ?, ?)"

                    val = (nazev, dulezitost, datum_odevzdani, postup, str(id1), datum_zadani, poznamky)

                    cursor.execute(sqlite_insert_query, val)
                    sqliteConnection.commit()
                    cursor.close()

                    self.lineEdit.clear()
                    self.plaintextEdit_2.clear()

                    self.Vycistit()

                    break

                except:

                    # DatovyTypStr (1 = písmeno, 2 = číslo)

                    if DatovyTypStr == "2":

                        # v nastavení je nastaven primární klíč jako integer

                        id1 = int(id1 + 1)


                    elif DatovyTypStr == "1":

                        # v nastavení je nastaven primární klíč jako string
                        
                        id1 = list(bytes(id1, 'ascii'))

                        id1 = int(id1[0])

                        if id1 >= 97 and id1 <= 121:
                            
                            # kontroluje, aby se z písmen nezačali dělat speciální znaky

                            id1 += 1

                            id1 = str(chr(id1))


                        else:

                            # pokud by další v pořadí ascii abecedy byl speciální znak => smaže se config.txt, takže defaultní bude číslo jako primární klíč

                            try:   
                                remove("config.txt")

                            except:

                                pass

                            msgBox = QMessageBox()
                            msgBox.setIcon(QMessageBox.Warning)
                            msgBox.setWindowTitle("Problém!")
                            msgBox.setText("Vyčerpali se všechny písmena pro primární klíč.\n\nDatový typ se změnil na (číslo)")
                            msgBox.setStandardButtons(QMessageBox.Ok)
                            msgBox.exec()

                            id1 = int(1)

                            break


        else:

            msgBox = QMessageBox()
            msgBox.setIcon(QMessageBox.Warning)
            msgBox.setWindowTitle("Problém")
            msgBox.setText("Vyplňte název úkolu!")
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec()


    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(918, 435)


        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        MainWindow.setWindowFlag(QtCore.Qt.WindowCloseButtonHint, True)
        MainWindow.setWindowFlag(QtCore.Qt.WindowMaximizeButtonHint, False)
        MainWindow.setWindowFlag(QtCore.Qt.WindowMinimizeButtonHint, True)
        
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(24, 43, 241, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit.setFont(font)
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.setText("")

        self.plaintextEdit_2 = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plaintextEdit_2.setGeometry(QtCore.QRect(370, 75, 511, 331))
        self.plaintextEdit_2.setObjectName("plaintextEdit_2")
        self.plaintextEdit_2.setPlainText("")


        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(24, 19, 211, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label.setFont(font)
        self.label.setObjectName("label")


        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(370, 47, 511, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")


        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(24, 107, 211, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")


        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(24, 199, 211, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")


        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(24, 282, 211, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")


        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(24, 333, 251, 16))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")

        self.label_6.setHidden(True)


        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(690, 20, 181, 21))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")


        self.pushButton_7 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_7.setGeometry(QtCore.QRect(24, 370, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_7.setFont(font)
        self.pushButton_7.setObjectName("pushButton_7")

        self.pushButton_7.clicked.connect(self.PridatDoDatabaze)

        self.pushButton_8 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_8.setGeometry(QtCore.QRect(147, 370, 81, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_8.setFont(font)
        self.pushButton_8.setObjectName("pushButton_8")

        self.pushButton_8.clicked.connect(self.Vycistit)


        self.pushButton_9 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_9.setGeometry(QtCore.QRect(190, 225, 75, 23))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.pushButton_9.setFont(font)
        self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton_9.setHidden(True)

        self.pushButton_9.clicked.connect(self.ResetKalendare)



        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(24, 131, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.comboBox.setFont(font)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setEditable(False)
        self.comboBox.setHidden(True)


        self.dateEdit = QtWidgets.QDateEdit(self.centralwidget)
        self.dateEdit.setGeometry(QtCore.QRect(24, 224, 151, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.dateEdit.setFont(font)
        self.dateEdit.setObjectName("dateEdit")
        self.dateEdit.setMaximumDate(QDate(9999, 12, 31))
        self.dateEdit.setMinimumDate(QDate(2000, 1, 1))
        self.dateEdit.setHidden(True)

        self.ResetKalendare()


        self.checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox.setGeometry(QtCore.QRect(106, 107, 141, 17))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.checkBox.setFont(font)
        self.checkBox.setObjectName("checkBox")

        self.checkBox.stateChanged.connect(self.Povoleni)


        self.checkBox_2 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_2.setGeometry(QtCore.QRect(157, 199, 91, 17))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.checkBox_2.setFont(font)
        self.checkBox_2.setObjectName("checkBox_2")

        self.checkBox_2.stateChanged.connect(self.Povoleni)


        self.checkBox_3 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_3.setGeometry(QtCore.QRect(90, 282, 91, 17))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.checkBox_3.setFont(font)
        self.checkBox_3.setObjectName("checkBox_3")

        self.checkBox_3.stateChanged.connect(self.Povoleni)


        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(124, 307, 118, 23))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")

        self.progressBar.setHidden(True)


        self.spinBox = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox.setGeometry(QtCore.QRect(24, 307, 81, 22))
        self.spinBox.setMinimum(0)
        self.spinBox.setMaximum(100)
        self.spinBox.setObjectName("spinBox"),
        self.spinBox.setHidden(True)
        self.spinBox.setReadOnly(True)

        self.spinBox.valueChanged.connect(self.NastavitProcenta)


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

        MainWindow.setWindowTitle(_translate("MainWindow", "Přidat úkol"))
        self.label.setText(_translate("MainWindow", "Název úkolu (povinné):"))
        self.label_2.setText(_translate("MainWindow", "Popis úkolu (volitelné):"))
        self.label_3.setText(_translate("MainWindow", "Důležitost:"))
        self.label_4.setText(_translate("MainWindow", "Datum odevzdání:"))
        self.label_5.setText(_translate("MainWindow", "Postup:"))
        self.label_6.setText(_translate("MainWindow", "*V případě, že už jste s prací začali"))
        self.label_7.setText(_translate("MainWindow", "Dnešní datum: " + datum2))
        self.pushButton_7.setText(_translate("MainWindow", "Přidat"))
        self.pushButton_8.setText(_translate("MainWindow", "Zrušit"))
        self.pushButton_9.setText(_translate("MainWindow", "Reset"))
        self.comboBox.setItemText(0, _translate("MainWindow", "Masivní"))
        self.comboBox.setItemText(1, _translate("MainWindow", "Vysoká"))
        self.comboBox.setItemText(2, _translate("MainWindow", "Střední"))
        self.comboBox.setItemText(3, _translate("MainWindow", "Normální"))
        self.comboBox.setItemText(4, _translate("MainWindow", "Nízká"))
        self.comboBox.setItemText(5, _translate("MainWindow", "Žádná"))
        self.comboBox.setCurrentText("Normální")
        self.checkBox.setText(_translate("MainWindow", "Povolit"))
        self.checkBox_2.setText(_translate("MainWindow", "Povolit"))
        self.checkBox_3.setText(_translate("MainWindow", "Povolit"))