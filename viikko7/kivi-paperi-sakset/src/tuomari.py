
# Luokka pitää kirjaa ensimmäisen ja toisen pelaajan pisteistä sekä tasapelien määrästä.
class Tuomari:
    def __init__(self):
        self.ekan_pisteet = 0
        self.tokan_pisteet = 0
        self.tasapelit = 0

    def onko_ok_siirto(self, siirto):
        return siirto == "k" or siirto == "p" or siirto == "s"
    
    
    def tarkasta_siirrot(self,ekan_siirto, tokan_siirto):
        if self.onko_ok_siirto(ekan_siirto) and self.onko_ok_siirto(tokan_siirto):
            self.kirjaa_era(ekan_siirto, tokan_siirto)
            print(self.__str__())
            return True
        else:
            self.kiita_lopuksi_ja_kerro_tilanne()
            return False
    
    def kirjaa_era(self, ekan_siirto, tokan_siirto):
        if ekan_siirto == tokan_siirto:
            self.tasapelit = self.tasapelit + 1
        
        elif self._eka_voittaa(ekan_siirto, tokan_siirto):
            self.ekan_pisteet = self.ekan_pisteet + 1
       
        else:
            self.tokan_pisteet = self.tokan_pisteet + 1

    def kiita_lopuksi_ja_kerro_tilanne(self):
        print(f"Kiitos!\n{self.__str__()}")
    

    def __str__(self):
        return f"Pelitilanne: {self.ekan_pisteet} - {self.tokan_pisteet}\nTasapelit: {self.tasapelit}"


    # sisäinen metodi joka tarkastaa voittaako eka pelaaja tokan
    def _eka_voittaa(self, eka, toka):
        näillä_eka_voittaa = "jos ekalla "+eka+" ja tokalla "+toka
        return näillä_eka_voittaa in ["jos ekalla k ja tokalla s", "jos ekalla s ja tokalla p","jos ekalla p ja tokalla k"]

