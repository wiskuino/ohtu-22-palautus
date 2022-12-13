from tuomari import Tuomari
from tekoaly_parannettu import TekoalyParannettu


class KPSParempiTekoaly:
    def __init__(self):
  
        self.ekan_siirto= ""
        self.tokan_siirto= ""
    
    def pelaa(self):
        tuomari = Tuomari()
        tekoaly = TekoalyParannettu(10)

        self.ekan_siirto = input("Ensimmäisen pelaajan siirto: ")
        self.tokan_siirto = tekoaly.anna_siirto()

        print(f"Tietokone valitsi: {self.tokan_siirto}")

        while tuomari.tarkasta_siirrot(self.ekan_siirto,self.tokan_siirto):

            self.ekan_siirto = input("Ensimmäisen pelaajan siirto: ")
            self.tokan_siirto = tekoaly.anna_siirto()

            print(f"Tietokone valitsi: {self.tokan_siirto}")
            tekoaly.aseta_siirto(self.ekan_siirto)


