from tuomari import Tuomari
from kps_pelaaja_vs_pelaaja import KPSPelaajaVsPelaaja
from tekoaly import Tekoaly



class KPSTekoaly(KPSPelaajaVsPelaaja):
    def __init__(self):
        super().__init__()
        self.tekoaly =Tekoaly()
        
        self.tokan_edellinen_siirto = self.tekoaly.siirrot[0]
        
    
    def hae_ekan_siirto(self):
        return input("Ensimmäisen pelaajan siirto: ")
        
    def hae_tokan_siirto(self):
        self.tokan_alykas_siirto = self.tekoaly.anna_siirto(self.tokan_edellinen_siirto)
        self.kerro_tietokoneen_valinta()
        return self.tokan_alykas_siirto
        
    def kerro_tietokoneen_valinta(self):
        print(f"Tietokone valitsi: {self.tokan_alykas_siirto}")
        self.tokan_edellinen_siirto = self.tokan_alykas_siirto




