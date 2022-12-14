from tuomari import Tuomari
from tekoaly_parannettu import TekoalyParannettu
from kps_tekoaly import KPSTekoaly


class KPSParempiTekoaly(KPSTekoaly):
    def __init__(self):
        self.tekoaly = TekoalyParannettu(10)
       
       
    
    def pelaa(self):
        tuomari = Tuomari()
        

        self.ekan_siirto = self.hae_ekan_siirto()
        self.tokan_siirto = self.hae_tokan_siirto()

        self.kerro_tietokoneen_valinta()

        while tuomari.tarkasta_siirrot(self.ekan_siirto,self.tokan_siirto):

            self.ekan_siirto = self.hae_ekan_siirto()
            self.tokan_siirto = self.hae_tokan_siirto()

            self.kerro_tietokoneen_valinta()
            self.tekoaly.aseta_siirto(self.ekan_siirto)

    
    def hae_ekan_siirto(self):
        return input("Ensimmäisen pelaajan siirto: ")
    
    
    def hae_tokan_siirto(self):
        return self.tekoaly.anna_siirto()

    def kerro_tietokoneen_valinta(self):
        print(f"Tietokone valitsi: {self.tokan_siirto}")
        
