from tuomari import Tuomari
from tekoaly_parannettu import TekoalyParannettu
from kps_tekoaly import KPSTekoaly


class KPSParempiTekoaly(KPSTekoaly):
    def __init__(self):
        self.tekoaly = TekoalyParannettu(10)
       
    def hae_ekan_siirto(self):
        self.ekan_siirto = input("Ensimmäisen pelaajan siirto: ")
        return self.ekan_siirto

    def hae_tokan_siirto(self):
        self.tokan_alykas_siirto = self.tekoaly.anna_siirto()
        self.kerro_tietokoneen_valinta()
        return self.tokan_alykas_siirto

    def kerro_tietokoneen_valinta(self):
        print(f"Tietokone valitsi: {self.tokan_alykas_siirto}")
        print(self.tekoaly.vertailu)
        print(self.tekoaly.tulos_lista)
        self.tekoaly.aseta_siirto(self.ekan_siirto)
        
