from tuote import Tuote
from ostos import Ostos

class Ostoskori:
    def __init__(self):
        # ostoskori tallettaa Ostos-oliota, yhden per korissa oleva Tuote
        self.kori = {}
        self.ostos = Ostos(Tuote)
        self.ostos._hinta = 0

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
            hinta=0
            print(self.kori)
            for tuote,olio in self.kori.items():
                hinta = hinta+olio.hinta()
            return hinta
        ## kertoo korissa olevien ostosten yhteenlasketun hinnan

    def lisaa_tuote(self, lisattava: Tuote):
        if not lisattava._nimi in self.kori:
            self.kori[lisattava._nimi] = Ostos(lisattava)
        else:
            self.kori[lisattava._nimi].muuta_lukumaaraa(1)
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
