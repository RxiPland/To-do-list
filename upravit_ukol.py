from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtCore import QDate
from random import choice, randint
import sqlite3
from datetime import date
from os.path import exists


class Ui_MainWindow_upravit_ukol(object):


    def napoveda1(self):

        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Question)
        msgBox.setWindowTitle("Nápověda")
        msgBox.setText("Umožňuje změnit ID tohoto úkolu.\n\nID musí být jedinečné (nesmí se opakovat)")
        msgBox.setStandardButtons(QMessageBox.Ok)
        msgBox.exec()


    def povolitPopisek(self):

        # schová/ukáže okno s popisem, pokud je zaškrknuto políčko povolit u popisu

        povolenPopisek = self.checkBox_4.isChecked()

        if povolenPopisek == True:

            self.plaintextEdit.clear()
            
            self.plaintextEdit.setHidden(False)
            self.plaintextEdit.setReadOnly(False)

        else:

            self.plaintextEdit.clear()

            self.plaintextEdit.setReadOnly(True)
            self.plaintextEdit.setHidden(True)


    def hideDatumZadani(self):

        # schová/ukáže políčka se zadáváním datumu, kdy byl úkol vytvořen

        datumZadaniChecked = self.checkBox_2.isChecked()

        if datumZadaniChecked == True:

            self.dateEdit.setHidden(False)


        else:


            self.dateEdit.setHidden(True)


    
    def hideDatumOdevzdani(self):

        # schová/ukáže políčka se zadáváním datumu, kdy má být úkol odevzdán

        datumOdevzdaniChecked = self.checkBox.isChecked()

        if datumOdevzdaniChecked == True:

            self.dateEdit_2.setHidden(False)


        else:


            self.dateEdit_2.setHidden(True)


    def schovatDulezitost(self):

        povoleniDulezitost = self.checkBox_3.isChecked()

        if povoleniDulezitost == True:

            self.comboBox.setHidden(False)

        else:

            self.comboBox.setHidden(True)

    
    def schovatPostup(self):

        povoleniPostup = self.checkBox_5.isChecked()

        if povoleniPostup == True:

            self.comboBox_2.setHidden(False)

            self.spinBox.setHidden(True)

            obsah_boxu = str(self.comboBox_2.currentText())

            if obsah_boxu == "100%":

                self.progressBar.setHidden(False)
                self.progressBar.setValue(int(100))
                self.comboBox_2.setCurrentText("100%")
        
            elif obsah_boxu == "75%":

                self.progressBar.setHidden(False)
                self.progressBar.setValue(int(75))
                self.comboBox_2.setCurrentText("75%")

            elif obsah_boxu == "50%":

                self.progressBar.setHidden(False)
                self.progressBar.setValue(int(50))
                self.comboBox_2.setCurrentText("50%")

            elif obsah_boxu == "25%":

                self.progressBar.setHidden(False)
                self.progressBar.setValue(int(25))
                self.comboBox_2.setCurrentText("25%")

            elif obsah_boxu == "0%":

                self.progressBar.setHidden(False)
                self.progressBar.setValue(int(0))
                self.comboBox_2.setCurrentText("0%")


            else:

                self.comboBox_2.setCurrentText("Vlastní")

                self.spinBox.setHidden(False)
                self.progressBar.setHidden(False)

                try:
                    self.spinBox.setValue(int(statusProcenta))

                    self.progressBar.setValue(int(statusProcenta))

                except:

                    self.spinBox.setValue(int(0))

                    self.progressBar.setValue(int(0))



        else:

            self.comboBox_2.setHidden(True)
            self.spinBox.setHidden(True)
            self.progressBar.setHidden(True)


    def VygenerovatRandomID(self):

        delka1 = int(randint(2,5))

        id2 = ""
        
        chars = "abcdefghijklmnopqrstuvwxyz"

        for x in range(1, delka1):

            id2_char = str(choice(chars))
            id2 = id2 + id2_char

        self.lineEdit_2.setText(str(id2))


    def NastavitPuvodniIDPrvni(self, nastavitID):

        # slouží pro prvotní nastavení ID do řádku

        global aktualniID

        aktualniID = nastavitID
        
        self.lineEdit_2.setText(str(aktualniID))

    
    def NastavitPuvodniIDdruhy(self):

        # slouží pro nastavení původního id přímo z okna

        
        self.lineEdit_2.setText(str(aktualniID))


    def NastavitProcenta(self):

        # nastaví se procenta do loading baru

        value = int(self.spinBox.value())

        self.progressBar.setProperty("value", value)


    def NacteniUdajuZdatabaze(self):

        global nazev, datum_zadani, datum_odevzdani, dulezitost, statusProcenta, idZaloha, poznamky

        db_exists = exists("databaze.db")

        if db_exists == True:

            id1 = aktualniID

            connection = sqlite3.connect('databaze.db')
            cur = connection.cursor()

            potrebneData = ["Nazev", "Dulezitost", "Datum_odevzdani", "Postup", "ID", "Datum_zadani", "Poznamky"]

            for word in potrebneData:

                if word == potrebneData[0]:
                
                    sqlstr = "SELECT {word} FROM tabulka WHERE ID='{id1}'".format(word=word, id1=id1)

                    vysledek1 = cur.execute(sqlstr).fetchall()

                    udaje = vysledek1[0][0]


                    nazev = udaje

                if word == potrebneData[5]:

                    sqlstr = "SELECT {word} FROM tabulka WHERE ID='{id1}'".format(word=word, id1=id1)

                    vysledek1 = cur.execute(sqlstr).fetchall()

                    udaje = vysledek1[0][0]

                    if udaje == "":

                        datum_zadani = QDate(2021, 1, 1)

                        self.checkBox_2.setChecked(False)

                    else:

                        udaje = udaje + "."

                        vysledekDatumStr = ""

                        vysledekDatum = []

                        udaje = list(udaje)


                        for char in udaje:

                            if char != ".":
                            
                                vysledekDatumStr = vysledekDatumStr + char

                            elif char == ".":

                                vysledekDatum.append(vysledekDatumStr)

                                vysledekDatumStr = ""

                        den = int(vysledekDatum[0])
                        mesic = int(vysledekDatum[1])
                        rok = int(vysledekDatum[2])                        

                        datum_zadani = QDate(rok, mesic, den)



                if word == potrebneData[2]:

                    try:

                        sqlstr = "SELECT {word} FROM tabulka WHERE ID='{id1}'".format(word=word, id1=id1)

                        vysledek1 = cur.execute(sqlstr).fetchall()

                        udaje = vysledek1[0][0]

                        if udaje == "":

                            datum_odevzdani = QDate(2021, 1, 1)

                            self.checkBox.setChecked(False)

                        else:

                            udaje = udaje + "."

                            vysledekDatumStr2 = ""

                            vysledekDatum2 = []

                            udaje = list(udaje)


                            for char in udaje:

                                if char != ".":
                            
                                    vysledekDatumStr2 = vysledekDatumStr2 + char

                                elif char == ".":

                                    vysledekDatum2.append(vysledekDatumStr2)

                                    vysledekDatumStr2 = ""


                            den = int(vysledekDatum2[0])
                            mesic = int(vysledekDatum2[1])
                            rok = int(vysledekDatum2[2])                        

                            datum_odevzdani = QDate(rok, mesic, den)

                            self.checkBox.setChecked(True)

                    except:

                        self.checkBox.setChecked(False)


                if word == potrebneData[1]:

                    sqlstr = "SELECT {word} FROM tabulka WHERE ID='{id1}'".format(word=word, id1=id1)

                    vysledek1 = cur.execute(sqlstr).fetchall()

                    udaje = vysledek1[0][0]


                    dulezitost = udaje


                if word == potrebneData[3]:

                    global statusProcenta

                    sqlstr = "SELECT {word} FROM tabulka WHERE ID='{id1}'".format(word=word, id1=id1)

                    vysledek1 = cur.execute(sqlstr).fetchall()

                    udaje = vysledek1[0][0]

                    udaje = udaje.replace('%', "")
                
                    statusProcenta = str(udaje)

                    if statusProcenta != "":


                        self.checkBox_5.setChecked(True)

                    else:

                        self.checkBox_5.setChecked(False)


                if word == potrebneData[4]:

                    sqlstr = "SELECT {word} FROM tabulka WHERE ID='{id1}'".format(word=word, id1=id1)

                    vysledek1 = cur.execute(sqlstr).fetchall()

                    udaje = vysledek1[0][0]

                    idZaloha = str(udaje)


                if word == potrebneData[6]:

                    sqlstr = "SELECT {word} FROM tabulka WHERE ID='{id1}'".format(word=word, id1=id1)

                    vysledek1 = cur.execute(sqlstr).fetchall()

                    udaje = vysledek1[0][0]

                    poznamky = str(udaje)




            connection.commit()
            cur.close()

            self.PriraditUdajeDoPoli()



    def PriraditUdajeDoPoli(self):

        self.lineEdit.setText(nazev)
        self.lineEdit_2.setText(idZaloha)

        if poznamky == "CODE1ZADNYPOPIS":

            self.checkBox_4.setChecked(False)
            self.plaintextEdit.setHidden(True)

        else:

            self.plaintextEdit.setPlainText(poznamky)

        self.dateEdit.setDate(datum_zadani)


        zaskrknuto1 = self.checkBox.isChecked()

        if zaskrknuto1 == True:

            self.dateEdit_2.setDate(datum_odevzdani)



        if dulezitost != "":

            self.comboBox.setCurrentText(dulezitost)
            self.checkBox_3.setChecked(True)

        else:

            self.checkBox_3.setChecked(False)
            self.comboBox.setHidden(True)



        if statusProcenta == "100":

            self.progressBar.setHidden(False)
            self.progressBar.setValue(int(statusProcenta))
            self.comboBox_2.setCurrentText("100%")
        
        elif statusProcenta == "75":

            self.progressBar.setHidden(False)
            self.progressBar.setValue(int(statusProcenta))
            self.comboBox_2.setCurrentText("75%")

        elif statusProcenta == "50":

            self.progressBar.setHidden(False)
            self.progressBar.setValue(int(statusProcenta))
            self.comboBox_2.setCurrentText("50%")

        elif statusProcenta == "25":

            self.progressBar.setHidden(False)
            self.progressBar.setValue(int(statusProcenta))
            self.comboBox_2.setCurrentText("25%")

        elif statusProcenta == "0":

            self.progressBar.setHidden(False)
            self.progressBar.setValue(int(statusProcenta))
            self.comboBox_2.setCurrentText("0%")

        elif statusProcenta == "":

            self.checkBox_5.setChecked(False)

            self.comboBox_2.setHidden(True)

            self.spinBox.setHidden(True)
            self.progressBar.setHidden(True)

        else:

            self.comboBox_2.setCurrentText("Vlastní")

            self.spinBox.setHidden(False)
            self.progressBar.setHidden(False)

            self.spinBox.setValue(int(statusProcenta))

            self.progressBar.setValue(int(statusProcenta))
            


    def UlozitNoveHodnotyDoDB(self):

        novy_nazev = str(self.lineEdit.text())

        if novy_nazev == "":

            return "error nazev"

        else:

            povoleno_datum_zadani = self.checkBox_2.isChecked()

            if povoleno_datum_zadani == True:

                nove_datum_zadani = str(self.dateEdit.text())

            else:

                nove_datum_zadani = ""

            povoleno_datum_odevzdani = self.checkBox.isChecked()

            if povoleno_datum_odevzdani == True:

                nove_datum_odevzdani = str(self.dateEdit_2.text())

            else:

                nove_datum_odevzdani = ""

            povolena_dulezitost = self.checkBox_3.isChecked()

            if povolena_dulezitost == True:

                nova_dulezitost = str(self.comboBox.currentText())

            else:

                nova_dulezitost = ""

            povolen_postup = self.checkBox_5.isChecked()

            if povolen_postup == True:

                novy_postup = str(self.comboBox_2.currentText())

                if novy_postup == "Vlastní":

                    novy_postup = str(self.spinBox.text())

                    novy_postup = novy_postup + "%"

            else:

                novy_postup = ""


            povolen_popis = self.checkBox_4.isChecked()

            if povolen_popis == True:

                novy_popis = str(self.plaintextEdit.toPlainText())

            else:

                novy_popis = "CODE1ZADNYPOPIS"



            nove_ID = str(self.lineEdit_2.text())

            if nove_ID == "":

                return "error id"

            else:

                db_exists = exists("databaze.db")

                if db_exists == True:

                    list_promennych = [novy_nazev, nove_datum_zadani, nove_datum_odevzdani, nova_dulezitost, novy_postup, novy_popis, nove_ID]

                    list_sloupcu = ["Nazev", "Datum_zadani", "Datum_odevzdani", "Dulezitost", "Postup", "Poznamky", "ID"]
            
                    sqliteConnection = sqlite3.connect('databaze.db')
                    cursor = sqliteConnection.cursor()

                    for i in range(7):
                    
                        promenna = list_promennych[i]
                        sloupce = list_sloupcu[i]

                        sqlite_update_query = "UPDATE Tabulka SET {sloupce}='{promenna}' WHERE ID='{idZaloha}'".format(sloupce=sloupce, promenna=promenna, idZaloha=idZaloha)

                        cursor.execute(sqlite_update_query)

                    sqliteConnection.commit()
                    cursor.close()

                else:

                    return "error databaze-neni"



    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1000, 763)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 30, 111, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")


        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(410, 30, 211, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")


        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(30, 115, 121, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")


        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(30, 205, 151, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")


        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(30, 300, 101, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")


        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(30, 559, 61, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")


        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(30, 390, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")


        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(690, 698, 281, 21))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")


        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(40, 690, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")


        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(190, 690, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")


        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(390, 690, 221, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")

        self.pushButton_3.setHidden(True)


        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(200, 590, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setObjectName("pushButton_4")

        self.pushButton_4.clicked.connect(self.NastavitPuvodniIDdruhy)


        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(290, 590, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setObjectName("pushButton_5")

        self.pushButton_5.clicked.connect(self.VygenerovatRandomID)


        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(64, 554, 31, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setObjectName("pushButton_6")

        self.pushButton_6.clicked.connect(self.napoveda1)


        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(30, 60, 261, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit.setFont(font)
        self.lineEdit.setObjectName("lineEdit")

        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(30, 590, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setObjectName("lineEdit_2")


        self.plaintextEdit = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plaintextEdit.setGeometry(QtCore.QRect(410, 60, 531, 571))
        self.plaintextEdit.setObjectName("plaintextEdit")


        self.dateEdit = QtWidgets.QDateEdit(self.centralwidget)
        self.dateEdit.setGeometry(QtCore.QRect(30, 145, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.dateEdit.setFont(font)
        self.dateEdit.setMaximumDate(QDate(9999, 12, 31))
        self.dateEdit.setMinimumDate(QDate(2000, 1, 1))
        self.dateEdit.setObjectName("dateEdit")


        self.dateEdit_2 = QtWidgets.QDateEdit(self.centralwidget)
        self.dateEdit_2.setGeometry(QtCore.QRect(30, 235, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.dateEdit_2.setFont(font)
        self.dateEdit.setMaximumDate(QDate(9999, 12, 31))
        self.dateEdit.setMinimumDate(QDate(2000, 1, 1))
        self.dateEdit_2.setObjectName("dateEdit_2")

        self.dateEdit_2.setHidden(True)


        self.checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox.setGeometry(QtCore.QRect(186, 205, 81, 20))
        self.checkBox.setObjectName("checkBox")
        self.checkBox.stateChanged.connect(self.hideDatumOdevzdani)


        self.checkBox_2 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_2.setGeometry(QtCore.QRect(159, 115, 111, 20))
        self.checkBox_2.setChecked(True)
        self.checkBox_2.setObjectName("checkBox_2")
        self.checkBox_2.stateChanged.connect(self.hideDatumZadani)


        self.checkBox_3 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_3.setGeometry(QtCore.QRect(140, 300, 121, 20))
        self.checkBox_3.setCheckable(True)
        self.checkBox_3.setObjectName("checkBox_3")
        self.checkBox_3.stateChanged.connect(self.schovatDulezitost)


        self.checkBox_4 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_4.setGeometry(QtCore.QRect(480, 30, 121, 20))
        self.checkBox_4.setChecked(True)
        self.checkBox_4.setObjectName("checkBox_4")
        self.checkBox_4.stateChanged.connect(self.povolitPopisek)


        self.checkBox_5 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_5.setGeometry(QtCore.QRect(125, 390, 121, 20))
        self.checkBox_5.setCheckable(True)
        self.checkBox_5.setObjectName("checkBox_5")
        self.checkBox_5.stateChanged.connect(self.schovatPostup)


        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(30, 330, 181, 31))
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



        self.comboBox_2 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_2.setGeometry(QtCore.QRect(30, 420, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.comboBox_2.setFont(font)
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")

        self.comboBox_2.activated.connect(self.schovatPostup)


        self.spinBox = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox.setGeometry(QtCore.QRect(30, 470, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.spinBox.setFont(font)
        self.spinBox.setMaximum(100)
        self.spinBox.setObjectName("spinBox")
        self.spinBox.setHidden(True)

        self.spinBox.valueChanged.connect(self.NastavitProcenta)


        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(120, 470, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.progressBar.setFont(font)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.progressBar.setHidden(True)


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
        MainWindow.setWindowTitle(_translate("MainWindow", "Upravit"))
        self.pushButton.setText(_translate("MainWindow", "Uložit"))
        self.pushButton_2.setText(_translate("MainWindow", "Zrušit"))
        self.pushButton_3.setText(_translate("MainWindow", "Vrátit původní hodnoty"))
        self.label.setText(_translate("MainWindow", "Název:"))
        self.label_2.setText(_translate("MainWindow", "Popis:"))
        self.label_3.setText(_translate("MainWindow", "Datum zadání:"))
        self.label_4.setText(_translate("MainWindow", "Datum odevzdání:"))
        self.checkBox.setText(_translate("MainWindow", "Povolit"))
        self.checkBox_2.setText(_translate("MainWindow", "Povolit"))
        self.label_5.setText(_translate("MainWindow", "Důležitost:"))
        self.checkBox_3.setText(_translate("MainWindow", "Povolit"))
        self.comboBox.setItemText(0, _translate("MainWindow", "Masivní"))
        self.comboBox.setItemText(1, _translate("MainWindow", "Vysoká"))
        self.comboBox.setItemText(2, _translate("MainWindow", "Střední"))
        self.comboBox.setItemText(3, _translate("MainWindow", "Normální"))
        self.comboBox.setItemText(4, _translate("MainWindow", "Nízká"))
        self.comboBox.setItemText(5, _translate("MainWindow", "Žádná"))
        self.comboBox.setCurrentText("Normální")
        self.checkBox_4.setText(_translate("MainWindow", "Povolit"))
        self.label_6.setText(_translate("MainWindow", "ID:"))
        self.pushButton_4.setText(_translate("MainWindow", "Původní"))
        self.checkBox_5.setText(_translate("MainWindow", "Povolit"))
        self.label_7.setText(_translate("MainWindow", "Postup:"))
        self.comboBox_2.setItemText(0, _translate("MainWindow", "100%"))
        self.comboBox_2.setItemText(1, _translate("MainWindow", "75%"))
        self.comboBox_2.setItemText(2, _translate("MainWindow", "50%"))
        self.comboBox_2.setItemText(3, _translate("MainWindow", "25%"))
        self.comboBox_2.setItemText(4, _translate("MainWindow", "0%"))
        self.comboBox_2.setItemText(5, _translate("MainWindow", "Vlastní"))
        self.comboBox_2.setCurrentText("0%")
        self.pushButton_5.setText(_translate("MainWindow", "Náhodné"))
        self.pushButton_6.setText(_translate("MainWindow", "?"))
        self.label_8.setText(_translate("MainWindow", "Dnešní datum: " + datum2))