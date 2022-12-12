from tuomari import Tuomari
from tekoaly import Tekoaly


class KPSTekoaly:
    def __init__(self):
        
        self.ekan_siirto= ""
        self.tokan_siirto= ""

    def pelaa(self):
        tuomari = Tuomari()
        
        self.pelaa_siirrot()

        while self._onko_ok_siirto(self.ekan_siirto) and self._onko_ok_siirto(self.tokan_siirto):
            tuomari.kirjaa_siirto(self.ekan_siirto, self.tokan_siirto)
            print(tuomari)

            self.pelaa_siirrot()

        print("Kiitos!")
        print(tuomari)

    def _onko_ok_siirto(self, siirto):
        return siirto == "k" or siirto == "p" or siirto == "s"

    def pelaa_siirrot(self):
        tekoaly = Tekoaly()
        self.ekan_siirto = input("Ensimmäisen pelaajan siirto: ")
        self.tokan_siirto = tekoaly.anna_siirto()
        print(f"Tietokone valitsi: {self.tokan_siirto}")