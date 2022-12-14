from tuomari import Tuomari
from kps_pelaaja_vs_pelaaja import KPSPelaajaVsPelaaja
from tekoaly import Tekoaly



class KPSTekoaly(KPSPelaajaVsPelaaja):
    def __init__(self):
        super().__init__()
        self.tekoaly =Tekoaly()
        
        self.tokan_edellinen_siirto = self.tekoaly.siirrot[0]
        
    def pelaa(self):
        
        tuomari = Tuomari()
        
        
        self.ekan_siirto = self.hae_ekan_siirto()
        self.tokan_siirto = self.hae_tokan_siirto()
        
        self.kerro_tietokoneen_valinta()

        while tuomari.tarkasta_siirrot(self.ekan_siirto,self.tokan_siirto):
            
            self.ekan_siirto = self.hae_ekan_siirto()
            self.tokan_siirto = self.hae_tokan_siirto()
            
            self.kerro_tietokoneen_valinta()
            
    def hae_ekan_siirto(self):
        return input("Ensimmäisen pelaajan siirto: ")
        
    
    def hae_tokan_siirto(self):
        
        return self.tekoaly.anna_siirto(self.tokan_edellinen_siirto)
        
    def kerro_tietokoneen_valinta(self):
        print(f"Tietokone valitsi: {self.tokan_siirto}")
        self.tokan_edellinen_siirto = self.tokan_siirto




