from tuomari import Tuomari


class KPSPelaajaVsPelaaja:
    def __init__(self):
     
        self.ekan_siirto= ""
        self.tokan_siirto= ""
    
    def pelaa(self):
        
        
        tuomari = Tuomari()

        self.ekan_siirto = input("Ensimmäisen pelaajan siirto: ")
        self.tokan_siirto = input("Toisen pelaajan siirto: ")

        while tuomari.tarkasta_siirrot(self.ekan_siirto,self.tokan_siirto):

            self.ekan_siirto = input("Ensimmäisen pelaajan siirto: ")
            self.tokan_siirto = input("Toisen pelaajan siirto: ")

