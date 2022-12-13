from tuomari import Tuomari
from kps_pelaa import KPSPelaa
from tekoaly import Tekoaly



class KPSTekoaly(KPSPelaa):
    def __init__(self):
        super().__init__()

        self.ekan_siirto= ""
        self.tokan_edellinen_siirto= "k"
        
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
        tekoaly =Tekoaly()
        return tekoaly.anna_siirto(self.tokan_edellinen_siirto)
        
    def kerro_tietokoneen_valinta(self):
        print(f"Tietokone valitsi: {self.tokan_siirto}")
        self.tokan_edellinen_siirto = self.tokan_siirto




