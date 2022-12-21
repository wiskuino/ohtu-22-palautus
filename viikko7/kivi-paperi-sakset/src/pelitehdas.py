from kps_pelaaja_vs_pelaaja import KPSPelaajaVsPelaaja
from kps_tekoaly import KPSTekoalyPeli

from tekoaly import Tekoaly
from tekoaly_parannettu import TekoalyParannettu


class KPSPeliTehdas:
    def __init__(self):
        pelaaja_vastaan_pelaaja = KPSPelaajaVsPelaaja()
        pelaaja_vastaan_tekoaly = KPSTekoalyPeli(Tekoaly())
        pelaaja_vastaan_parempi_tekoaly = KPSTekoalyPeli(TekoalyParannettu(10))
        
        self.pelit = {"a":pelaaja_vastaan_pelaaja,"b":pelaaja_vastaan_tekoaly,"c":pelaaja_vastaan_parempi_tekoaly}
    
    
    
    def hae_peli(self,peli_valinta):
        if peli_valinta in self.pelit:
            return self.pelit[peli_valinta]
        else:
            exit
