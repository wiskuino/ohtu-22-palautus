from tuote import Tuote
from ostos import Ostos

class Ostoskori:
    def __init__(self):
        self.kori = {}  # käytetään sanakirjaa ostoskorina, tuotteen nimi on avain ostokseen
        # ostoskori tallettaa Ostos-oliota, yhden per korissa oleva Tuote
        

    def tavaroita_korissa(self):
        tavarat=0       #apumuuttuja jota ei tarvita muissa metodeissa
        for tuote,olio in self.kori.items():
            tavarat += olio.lukumaara()
        return tavarat
        # kertoo korissa olevien tavaroiden lukumäärän
        # eli jos koriin lisätty 2 kpl tuotetta "maito", tulee metodin palauttaa 2 
        # samoin jos korissa on 1 kpl tuotetta "maito" ja 1 kpl tuotetta "juusto", tulee metodin palauttaar 2 

    def hinta(self):
        k_hinta=0       #apumuuttuja jota ei tarvita muissa metodeissa
        for avain,olio in self.kori.items():
            k_hinta += olio.hinta()
        return k_hinta
        ## kertoo korissa olevien ostosten yhteenlasketun hinnan

    def lisaa_tuote(self, lisattava: Tuote):
        if lisattava._nimi not in self.kori:
            self.kori[lisattava._nimi] = Ostos(lisattava)
        else:
            self.kori[lisattava._nimi].muuta_lukumaaraa(1)
        # lisaa tuotteen

    def poista_tuote(self, poistettava: Tuote):
        for tuote,olio in self.kori.items():
            if tuote == poistettava._nimi:
                self.kori[poistettava._nimi].muuta_lukumaaraa(-1)
                if self.tavaroita_korissa() == 0:
                    self.kori = {}
        # poistaa tuotteen

    def tyhjenna(self):
        self.kori = {}
        # tyhjentää ostoskorin

    def ostokset(self):
        return self.kori
        # palauttaa listan jossa on korissa olevat ostos-oliot
        # kukin ostos-olio siis kertoo mistä tuotteesta on kyse JA kuinka monta kappaletta kyseistä tuotetta korissa on
