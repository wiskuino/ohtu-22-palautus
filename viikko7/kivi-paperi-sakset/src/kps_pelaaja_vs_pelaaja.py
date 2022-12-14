from tuomari import Tuomari

class KPSPelaajaVsPelaaja():
    def __init__(self):
    
        self.ekan_siirto = None
        self.tokan_siirto = None
    
    def pelaa(self):
        
        
        tuomari = Tuomari()

        self.ekan_siirto = self.hae_ekan_siirto()
        self.tokan_siirto = self.hae_tokan_siirto()

        while tuomari.tarkasta_siirrot(self.ekan_siirto,self.tokan_siirto):

            self.ekan_siirto = self.hae_ekan_siirto()
            self.tokan_siirto = self.hae_tokan_siirto()

    
    def hae_ekan_siirto(self):
        return input("Ensimmäisen pelaajan siirto: ")

    
    def hae_tokan_siirto(self):
        return input("Toisen pelaajan siirto: ")
        