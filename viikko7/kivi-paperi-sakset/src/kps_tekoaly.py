
from kps_pelaaja_vs_pelaaja import KPSPelaajaVsPelaaja


class KPSTekoaly(KPSPelaajaVsPelaaja):
    def __init__(self, tekoaly):
        super().__init__()
        self.tekoaly = tekoaly
        
        
    def hae_ekan_siirto(self):
        self.ekan_siirto =input("Ensimmäisen pelaajan siirto: ")
        return self.ekan_siirto
        
    def hae_tokan_siirto(self):
        self.tokan_siirto = self.tekoaly.anna_siirto()
        self.kerro_tietokoneen_valinta()
        self.talleta_ekan_siirto(self.ekan_siirto)
        return self.tokan_siirto
        
    def kerro_tietokoneen_valinta(self):
        print(f"Tietokone valitsi: {self.tokan_siirto}")

    def talleta_ekan_siirto(self,siirto):
        self.tekoaly.aseta_siirto(siirto)





