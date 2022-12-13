from tuomari import Tuomari


class KPSPelaa:
    def __init__(self):
     
        self.ekan_siirto= ""
        self.tokan_siirto= ""
    
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
        return ""

    def hae_tokan_siirto(self):
        return ""

    def kerro_tietokoneen_valinta(self):
        pass