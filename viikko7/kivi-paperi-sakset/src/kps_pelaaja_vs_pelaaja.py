from tuomari import Tuomari

class KPSPelaajaVsPelaaja():
    def __init__(self):
        pass
        self.ekan_siirto = None
        self.tokan_älykäs_siirto = None
    
    def pelaa(self):
        tuomari = Tuomari()

        while tuomari.tarkasta_siirrot(self.hae_ekan_siirto(),self.hae_tokan_siirto()):
            continue

    def hae_ekan_siirto(self):
        return input("Ensimmäisen pelaajan siirto: ")

    def hae_tokan_siirto(self):
        return input("Toisen pelaajan siirto: ")
        