from PyQt5.QtWidgets import QAbstractItemView, QMessageBox, QMainWindow, QApplication
from hlavni_menu import Ui_MainWindow_HlavniMenu
from pridat_ukol import Ui_MainWindow_PridatUkol
from nastaveni import Ui_MainWindow_nastaveni
from podrobnosti import Ui_MainWindow_Podrobnosti
from os import execl
from os.path import exists
from PyQt5.QtWidgets import QMessageBox



class hlavni_menu(QMainWindow, Ui_MainWindow_HlavniMenu):

    def __init__(self, *args, **kwargs):
        QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)

    def aktualizovatDatabazi (self):

        # po zmáčknutí tlačítka aktualizovat data v hlavním menu, se program resetuje, aby se znova mohla načíst tabulka
        
        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Question)
        msgBox.setWindowTitle("Oznámení")
        msgBox.setText("Pro načtení dat se program restartuje")
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



if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    menu = hlavni_menu()
    ukol = pridat_ukol()
    nastaveni = okno_nastaveni()
    podrobnosti = podrobnosti_okno()
    menu.pushButton.clicked.connect(ukol.vymazatPole)
    menu.pushButton_3.clicked.connect(menu.aktualizovatDatabazi)
    menu.pushButton_6.clicked.connect(nastaveni.zapnoutOknoSNastavenim)
    nastaveni.pushButton.clicked.connect(nastaveni.otevritMenu)
    nastaveni.pushButton_2.clicked.connect(nastaveni.PoSmazaniDatabazeReload)
    menu.pushButton_4.clicked.connect(podrobnosti.pridatData)
    ukol.pushButton_7.clicked.connect(ukol.kontrola)
    ukol.pushButton_7.clicked.connect(menu.loaddata)
    ukol.pushButton_8.clicked.connect(menu.show)
    menu.show()
    sys.exit(app.exec_())