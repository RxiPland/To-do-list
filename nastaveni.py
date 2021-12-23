from typing import overload
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import webbrowser
import shutil
import sqlite3
from os.path import exists
from os import remove


class Ui_MainWindow_nastaveni(object):

    def PomocnaFunkceProOverovani(self):

        # funkce která vrátí číslo, se kterým bude pracovat main.py

    
        if overeni1 == 1:

            return 1

        else:

            return 2


    def otevritGithub (self):

        # otevře github se zdrojovým kódem

        webbrowser.open("https://github.com/RxiPland")


    def napovedaStaraDatabaze (self):

        # otevře nápovědu, jak přiřadit starou databázi

        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Question)
        msgBox.setWindowTitle("Nápověda")
        msgBox.setText("Přejděte do složky s programem, odeberte (přesuňte jinam) stávající databázi (databaze.db) a starou (zálohovanou) databázi přejmenujte na databaze.db\n\nPo zavření programu a znovu otevření by se databáze i s daty měla automaticky načíst.")
        msgBox.setStandardButtons(QMessageBox.Ok)
        msgBox.exec()

    def smazatDatabazi (self):

        # funkce pro smazání databáze

        zalohovat = self.checkBox.isChecked()

        if zalohovat == True:

            zalohovatStav = "(v pořádku)"

            zalohovatInfo = "Databáze se bude zálohovat (uloží se pod jiným jménem ve stejné složce jako program)"

        elif zalohovat == False:

            zalohovatStav = "(v ohrožení)"
            
            zalohovatInfo = 'Databáze se nezálohuje a bude navždy smazána!\n-pokud ji chcete zálohovat, je nutné zaškrknout políčko "zálohovat"'

        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Warning)
        msgBox.setWindowTitle("Tohle je poslední možnost smazání odvolat!")
        msgBox.setText("Opravdu chcete smazat databázi se všemi úkoly?\n\nSoučasný stav: " + zalohovatStav + "\n\n" + zalohovatInfo)
        msgBox.setStandardButtons(QMessageBox.Yes|QMessageBox.No)
        buttonY = msgBox.button(QMessageBox.Yes)
        buttonY.setText("Smazat")
        buttonN = msgBox.button(QMessageBox.No)
        buttonN.setText("Zrušit")

        returnValue = msgBox.exec()


        if returnValue == QMessageBox.Yes:

            # uživatel se rozhodl, že databázi smaže


            if zalohovat == True:

                cislo2 = str(1)

                while True:

                    novy_nazev = "zaloha_databaze_" + cislo2 + ".db"

                    file_exists = exists(novy_nazev)

                    if file_exists == False:

                        try:

                            shutil.copy("databaze.db", novy_nazev)

                            break

                        except:

                            pass

                    cislo2 = int(cislo2)

                    cislo2 += 1

                    cislo2 = str(cislo2)


            try:
                

                sqliteConnection = sqlite3.connect('databaze.db')
                cursor = sqliteConnection.cursor()

                sqlite_insert_query = "DROP TABLE 'tabulka'"
                cursor.execute(sqlite_insert_query)

                VytvoritTabulku = "CREATE TABLE 'tabulka' ('Nazev' TEXT, 'Dulezitost' TEXT, 'Datum_odevzdani' DATE, 'Postup' TEXT, 'ID' TEXT PRIMARY KEY NOT NULL, 'Datum_zadani' DATE, 'Poznamky' TEXT)"
                cursor.execute(VytvoritTabulku)

                sqliteConnection.commit()
                cursor.close()


                msgBox = QMessageBox()
                msgBox.setIcon(QMessageBox.Question)
                msgBox.setWindowTitle("Oznámení")
                msgBox.setText("Databáze byla úspěšně smazána.")
                msgBox.setStandardButtons(QMessageBox.Ok)
                msgBox.exec()

                global overeni1

                overeni1 = 2

                self.PomocnaFunkceProOverovani()



            except:

                msgBox = QMessageBox()
                msgBox.setIcon(QMessageBox.Warning)
                msgBox.setWindowTitle("Chyba!")
                msgBox.setText("Databázi se nepodařilo smazat!")
                msgBox.setStandardButtons(QMessageBox.Ok)
                msgBox.exec()

                sqliteConnection = sqlite3.connect('databaze.db')
                cursor = sqliteConnection.cursor()

                VytvoritTabulku = "CREATE TABLE 'tabulka' ('Nazev' TEXT, 'Dulezitost' TEXT, 'Datum_odevzdani' DATE, 'Postup' TEXT, 'ID' TEXT PRIMARY KEY NOT NULL, 'Datum_zadani' DATE, 'Poznamky' TEXT)"
                cursor.execute(VytvoritTabulku)

                sqliteConnection.commit()
                cursor.close()


        elif returnValue == QMessageBox.No:

            # uživatel se rozhodl databázi nemazat

            overeni1 = 1

            self.PomocnaFunkceProOverovani()



    def DatovyTypNastaveni(self):

        # funkce pro zapsání nastavení datového typu do textového souboru

        while True:

            obsah_boxu = str(self.comboBox.currentText())

            file_exists = exists("config.txt")

            if file_exists == False:

                # vytvoří a zapíše nastavení do textového souboru

                if obsah_boxu == "Čísla (výchozí)":

                    DatovyTyp = str(2)

                elif obsah_boxu == "Písmena":

                    DatovyTyp = str(1)


                with open("config.txt", "w") as output:
                    output.write(str(DatovyTyp))

                break


            elif file_exists == True:

                # pokud už soubor bude existovat, smaže ho a začne smyčku odznova

                remove("config.txt")


    def napoveda_s_datovym_typem (self):

        # zobrazí okno s nápovědou, která píše o tom, k čemu slouží funkce se změnou datového typu

        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Question)
        msgBox.setWindowTitle("Nápověda")
        msgBox.setText("Určuje, pod jakým datovým typem se bude pojmenovávat primární klíč (ID) každého řádku v databázi.\n\nNení to nijak důležité, je to pouze funkce navíc.")
        msgBox.setStandardButtons(QMessageBox.Ok)
        msgBox.exec()


    def setupUi(self, MainWindow):


        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(617, 394)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        MainWindow.setWindowFlag(QtCore.Qt.WindowCloseButtonHint, False)
        MainWindow.setWindowFlag(QtCore.Qt.WindowMaximizeButtonHint, False)
        MainWindow.setWindowFlag(QtCore.Qt.WindowMinimizeButtonHint, False)


        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 24, 181, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")

        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(20, 130, 271, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")


        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(20, 220, 221, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")


        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(380, 5, 350, 16))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")


        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(432, 341, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")


        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(20, 50, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")

        self.pushButton_2.clicked.connect(self.smazatDatabazi)


        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(287, 341, 90, 31))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")

        self.pushButton_3.clicked.connect(self.otevritGithub)
        

        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(294, 130, 31, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setObjectName("pushButton_6")

        self.pushButton_6.clicked.connect(self.napovedaStaraDatabaze)


        self.pushButton_7 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_7.setGeometry(QtCore.QRect(180, 250, 31, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_7.setFont(font)
        self.pushButton_7.setObjectName("pushButton_7")

        self.pushButton_7.clicked.connect(self.napoveda_s_datovym_typem)


        self.checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox.setGeometry(QtCore.QRect(150, 60, 391, 20))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.checkBox.setFont(font)
        self.checkBox.setObjectName("checkBox")


        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(20, 250, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.comboBox.setFont(font)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")

        self.comboBox.activated.connect(self.DatovyTypNastaveni)


        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


    def retranslateUi(self, MainWindow):

        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Nastavení"))
        self.pushButton.setText(_translate("MainWindow", "Uložit nastavení a odejít"))
        self.pushButton_2.setText(_translate("MainWindow", "Smazat"))
        self.label.setText(_translate("MainWindow", "Smazat databázi:"))
        self.checkBox.setText(_translate("MainWindow", "Zálohovat databázi (uloží se pod jiným jménem)"))
        self.label_3.setText(_translate("MainWindow", "Jak přiřadit starou zálohovanou databázi:"))
        self.pushButton_6.setText(_translate("MainWindow", "?"))
        self.label_4.setText(_translate("MainWindow", "Datový typ ID:"))
        self.label_5.setText(_translate("MainWindow", 'Pro ukončení nastavení zmáčkněte tlačítko dole'))
        self.comboBox.setItemText(0, _translate("MainWindow", "Čísla (výchozí)"))
        self.comboBox.setItemText(1, _translate("MainWindow", "Písmena"))
        self.pushButton_7.setText(_translate("MainWindow", "?"))
        self.pushButton_3.setText(_translate("MainWindow", "Zdrojový kód"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow_nastaveni()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
