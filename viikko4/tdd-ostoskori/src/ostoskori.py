from tuote import Tuote
from ostos import Ostos

class Ostoskori:
    def __init__(self):
        # ostoskori tallettaa Ostos-oliota, yhden per korissa oleva Tuote
        self.kori = {}
        self.ostos = Ostos(Tuote)

    def tavaroita_korissa(self):
        if self.kori == {}:
            return 0
        else:
            return len(self.kori)
        # kertoo korissa olevien tavaroiden lukumäärän
        # eli jos koriin lisätty 2 kpl tuotetta "maito", tulee metodin palauttaa 2 
        # samoin jos korissa on 1 kpl tuotetta "maito" ja 1 kpl tuotetta "juusto", tulee metodin palauttaar 2 

    def hinta(self):
        if self.kori == {}:
            return 0
        else:
            return self.ostos.hinta()
        ## kertoo korissa olevien ostosten yhteenlasketun hinnan

    def lisaa_tuote(self, lisattava: Tuote):
        self.ostos.tuote = lisattava
        self.kori[lisattava._nimi] = self.ostos
        #self.kori.append(self.ostos(lisattava))
        # lisaa tuotteen

    def poista_tuote(self, poistettava: Tuote):
        pass
        # poistaa tuotteen

    def tyhjenna(self):
        pass
        # tyhjentää ostoskorin

    def ostokset(self):
        pass
        # palauttaa listan jossa on korissa olevat ostos-oliot
        # kukin ostos-olio siis kertoo mistä tuotteesta on kyse JA kuinka monta kappaletta kyseistä tuotetta korissa on
