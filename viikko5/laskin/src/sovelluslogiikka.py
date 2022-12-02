from kayttoliittyma import Kayttoliittyma

class Sovelluslogiikka:
    def __init__(self, tulos=0):
        self.tulos = tulos

    def miinus(self, arvo):
        self.tulos = self.tulos - arvo

    def plus(self, arvo):
        self.tulos = self.tulos + arvo

    def nollaa(self):
        self.tulos = 0

    def kumoa(self,edellinen):
        self.tulos=edellinen

    def aseta_arvo(self, arvo):
        self.tulos = arvo
