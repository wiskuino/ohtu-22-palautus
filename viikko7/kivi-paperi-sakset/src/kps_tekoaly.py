
from kps_pelaaja_vs_pelaaja import KPSPelaajaVsPelaaja
#from tekoaly import Tekoaly
#from kps_tekoaly import KPSTekoaly


class KPSTekoaly(KPSPelaajaVsPelaaja):
    def __init__(self, tekoaly):
        super().__init__()
        self.tekoaly = tekoaly
        
        
    def hae_ekan_siirto(self):
        self.ekan_siirto =input("Ensimmäisen pelaajan siirto: ")
        return self.ekan_siirto
        
    def hae_tokan_siirto(self):
        self.tokan_alykas_siirto = self.tekoaly.anna_siirto()
        self.kerro_tietokoneen_valinta()
        self.talleta_ekan_siirto(self.ekan_siirto)
        return self.tokan_alykas_siirto
        
    def kerro_tietokoneen_valinta(self):
        print(f"Tietokone valitsi: {self.tokan_alykas_siirto}")

    def talleta_ekan_siirto(self,siirto):
        self.tekoaly.aseta_siirto(siirto)





