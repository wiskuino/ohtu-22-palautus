from tuomari import Tuomari
from tekoaly import Tekoaly


class KPSTekoaly:
    def __init__(self):
        
        self.ekan_siirto= ""
        self.tokan_siirto= ""

    def pelaa(self):
        tuomari = Tuomari()
        tekoaly = Tekoaly()
        self.ekan_siirto = input("Ensimmäisen pelaajan siirto: ")
        self.tokan_siirto = tekoaly.anna_siirto()
        print(f"Tietokone valitsi: {self.tokan_siirto}")


        while tuomari.tarkasta_siirrot(self.ekan_siirto,self.tokan_siirto):
            
            self.ekan_siirto = input("Ensimmäisen pelaajan siirto: ")
            self.tokan_siirto = tekoaly.anna_siirto()
            print(f"Tietokone valitsi: {self.tokan_siirto}")