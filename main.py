# Udělal RxiPland

# python 3.9.9

# 26.12.2021


from PyQt5.QtWidgets import QAbstractItemView, QMessageBox, QMainWindow, QApplication
from hlavni_menu import Ui_MainWindow_HlavniMenu
from pridat_ukol import Ui_MainWindow_PridatUkol
from nastaveni import Ui_MainWindow_nastaveni
from podrobnosti import Ui_MainWindow_Podrobnosti
from upravit_ukol import Ui_MainWindow_upravit_ukol
from os import execl
from os.path import exists
from PyQt5.QtWidgets import QMessageBox
import sqlite3



class hlavni_menu(QMainWindow, Ui_MainWindow_HlavniMenu):

    def __init__(self, *args, **kwargs):
        QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)

    def aktualizovatDatabazi (self):

        # po zmáčknutí tlačítka aktualizovat data v hlavním menu, se program resetuje, aby se znova mohla načíst tabulka

        # nebo tahle funkce může fungovat obecně pro znovu načtení tabulky

        menu.tableWidget.setCurrentCell(-1, -1)
        
        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Question)
        msgBox.setWindowTitle("Oznámení")
        msgBox.setText("Pro načtení dat se program restartuje")
        msgBox.setStandardButtons(QMessageBox.Ok)
        msgBox.exec()

        python = sys.executable
        execl(python, python, * sys.argv)


    def vymazatUkol(self):

        # tato funkce se aktivuje po zmáčknutí tlačítka smazat úkol v hlavním menu

        id2 = self.pomocnafunkce()

        if id2 == True:
            
            msgBox = QMessageBox()
            msgBox.setIcon(QMessageBox.Warning)
            msgBox.setWindowTitle("Chyba!")
            msgBox.setText("Vyberte řádek, který chcete smazat!\n\nStačí kliknout kamkoli do tabulky na vybraný řádek.")
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec()

        else:

            db_exists = exists("databaze.db")

            if db_exists == True:


                try:

                    connection = sqlite3.connect('databaze.db')
                    cur = connection.cursor()

                    sql_delete_radek = ("DELETE FROM tabulka WHERE ID='{id2}'").format(id2=id2)

                    cur.execute(sql_delete_radek)
                    connection.commit()
                    cur.close()

                    msgBox = QMessageBox()
                    msgBox.setIcon(QMessageBox.Question)
                    msgBox.setWindowTitle("Oznámení")
                    msgBox.setText("Smazání proběhlo úspěšně")
                    msgBox.setStandardButtons(QMessageBox.Ok)
                    msgBox.exec()

                    self.aktualizovatDatabazi()

                except:


                    msgBox = QMessageBox()
                    msgBox.setIcon(QMessageBox.Warning)
                    msgBox.setWindowTitle("Chyba!")
                    msgBox.setText("Řádek se nepodařilo smazat!")
                    msgBox.setStandardButtons(QMessageBox.Ok)
                    msgBox.exec()

            else:


                msgBox = QMessageBox()
                msgBox.setIcon(QMessageBox.Warning)
                msgBox.setWindowTitle("Chyba!")
                msgBox.setText("Databáze neexistuje!")
                msgBox.setStandardButtons(QMessageBox.Ok)
                msgBox.exec()


                msgBox = QMessageBox()
                msgBox.setIcon(QMessageBox.Question)
                msgBox.setWindowTitle("Oznámení o restartu")
                msgBox.setText("Resetuji program pro znovu vytvoření")
                msgBox.setStandardButtons(QMessageBox.Ok)
                msgBox.exec()

                python = sys.executable
                execl(python, python, * sys.argv)
        


class okno_nastaveni(QMainWindow, Ui_MainWindow_nastaveni):

    def __init__(self, *args, **kwargs):
        QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)


    def otevritMenu(self):

        # aktivuje se po zmáčknutí tlačítka "uložit a odejít z nastavení" v okně s nastavením

        # program se restartuje

        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Question)
        msgBox.setWindowTitle("Oznámení")
        msgBox.setText("Nastavení bylo uloženo, pro správné fungování se program restartuje.")
        msgBox.setStandardButtons(QMessageBox.Ok)
        msgBox.exec()

    

        python = sys.executable
        execl(python, python, * sys.argv)

    
    def zapnoutOknoSNastavenim(self):

        # aktivuje se po zmáčknutí tlačítka "více" v hlavním menu (otevře se nastavení), musí se přiřadit správný datový typ jako současný text v comboBoxu, pokud ho uživatel zadával v minulosti

        file_exists = exists("config.txt")

        if file_exists == True:
                
                read1 = open("config.txt", 'r')

                NastaveniList = []

                for line in read1:

                    NastaveniList.append(line)

                read1.close()

                DatovyTypStr = int(NastaveniList[0])

                if DatovyTypStr == 1:

                    self.comboBox.setCurrentText("Písmena")

                    self.comboBox.update()


                elif DatovyTypStr == 2:

                    self.comboBox.setCurrentText("Čísla (výchozí)")

                    self.comboBox.update()



        else:

            # nastaví se text v comboBoxu na "Čísla (výchozí)" pokud config.txt neexistuje

            self.comboBox.setCurrentText("Čísla (výchozí)")

            self.comboBox.update()

        
        nastaveni.show()

    
    def PoSmazaniDatabazeReload(self):

        # provede se, pokud dal uživatel v nastavení tlačítko smazat

        cislo2 = self.PomocnaFunkceProOverovani()


        # pokud cislo2 = 1, znamená to, že uživatel v posledním upozornění před smazáním dal "zrušit" a žádný restart nebude

        # pokud cislo2 = 2, znamená to, že se uživatel rozhodl databázi smazat a provede se restart programu


        if cislo2 == 1:

            pass

        else:

            python = sys.executable
            execl(python, python, * sys.argv)


class pridat_ukol(QMainWindow, Ui_MainWindow_PridatUkol):

    def __init__(self, *args, **kwargs):
        QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)


    def kontrola(self):

        # zkontroluje, že název u přidávání úkolu není prázdný


        nazev = str(self.lineEdit.text())

        if nazev != "":

            menu.show()

            menu.loaddata()

        else:

            pass

    
    def vymazatPole(self):

        # vyčistí pole a otevře okno s přidáním úkolu

        self.Vycistit2()


class podrobnosti_okno(QMainWindow, Ui_MainWindow_Podrobnosti):

    def __init__(self, *args, **kwargs):

        QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)

    def pridatData(self):

        # načte do polí data

        vybraneId = menu.pomocnafunkce()

        if vybraneId == True:

            msgBox = QMessageBox()
            msgBox.setIcon(QMessageBox.Warning)
            msgBox.setWindowTitle("Chyba")
            msgBox.setText("Vyberte řádek, o kterým chcete podrobnosti.\n\nStačí kliknout kamkoli do tabulky na vybraný řádek.")
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec()

        else:

            self.LoadDataFromDB(vybraneId)
            podrobnosti.show()

            menu.tableWidget.setCurrentCell(-1, -1)


class upravit_ukol_okno(QMainWindow, Ui_MainWindow_upravit_ukol):

    def __init__(self, *args, **kwargs):

        QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)

    def NastavitID(self):

        id1 = menu.pomocnafunkce()

        nastavitID = str(id1)

        if id1 == True:

            msgBox = QMessageBox()
            msgBox.setIcon(QMessageBox.Warning)
            msgBox.setWindowTitle("Chyba")
            msgBox.setText("Vyberte řádek, který chcete upravit.\n\nStačí kliknout kamkoli do tabulky na vybraný řádek.")
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec()

        else:

            self.NastavitPuvodniIDPrvni(nastavitID)
            self.NacteniUdajuZdatabaze()
            upravit.show()

            menu.tableWidget.setCurrentCell(-1, -1)

    def restart1(self):

        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Question)
        msgBox.setWindowTitle("Oznámení")
        msgBox.setText("Restartuji program")
        msgBox.setStandardButtons(QMessageBox.Ok)
        msgBox.exec()

        python = sys.executable
        execl(python, python, * sys.argv)



    def pridatDoDB(self):

        chyby = self.UlozitNoveHodnotyDoDB()

        if chyby == "error nazev":

            msgBox = QMessageBox()
            msgBox.setIcon(QMessageBox.Warning)
            msgBox.setWindowTitle("Chyba!")
            msgBox.setText("Pole pro název nemůže být prázdné!")
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec()

        elif chyby == "error id":

            msgBox = QMessageBox()
            msgBox.setIcon(QMessageBox.Warning)
            msgBox.setWindowTitle("Chyba!")
            msgBox.setText("Pole pro ID nemůže být prázdné")
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec()

        elif chyby == "error databaze-neni":

            msgBox = QMessageBox()
            msgBox.setIcon(QMessageBox.Warning)
            msgBox.setWindowTitle("Chyba!")
            msgBox.setText("Databáze neexistuje!\n\nRestartujte program")
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec()

        else:

            msgBox = QMessageBox()
            msgBox.setIcon(QMessageBox.Question)
            msgBox.setWindowTitle("Oznámení")
            msgBox.setText("Uložení proběhlo úspěšně, pro aktualizování databáze restartuji program.")
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec()

            python = sys.executable
            execl(python, python, * sys.argv)




if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    menu = hlavni_menu()
    ukol = pridat_ukol()
    nastaveni = okno_nastaveni()
    podrobnosti = podrobnosti_okno()
    upravit = upravit_ukol_okno()
    menu.pushButton.clicked.connect(ukol.vymazatPole)
    menu.pushButton_2.clicked.connect(menu.vymazatUkol)
    menu.pushButton_3.clicked.connect(menu.aktualizovatDatabazi)
    menu.pushButton_5.clicked.connect(upravit.NastavitID)
    menu.pushButton_4.clicked.connect(podrobnosti.pridatData)
    menu.pushButton_6.clicked.connect(nastaveni.zapnoutOknoSNastavenim)
    nastaveni.pushButton.clicked.connect(nastaveni.otevritMenu)
    nastaveni.pushButton_2.clicked.connect(nastaveni.PoSmazaniDatabazeReload)
    upravit.pushButton.clicked.connect(upravit.pridatDoDB)
    upravit.pushButton_2.clicked.connect(upravit.restart1)
    ukol.pushButton_7.clicked.connect(ukol.kontrola)
    ukol.pushButton_7.clicked.connect(menu.loaddata)
    ukol.pushButton_8.clicked.connect(menu.show)
    menu.show()
    sys.exit(app.exec_())
