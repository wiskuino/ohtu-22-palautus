from kps_pelaaja_vs_pelaaja import KPSPelaajaVsPelaaja
from kps_tekoaly import KPSTekoaly
from kps_parempi_tekoaly import KPSParempiTekoaly

class KPSPeliTehdas:
    def __init__(self):
        pelaaja_vastaan_pelaaja = KPSPelaajaVsPelaaja()
        pelaaja_vastaan_tekoaly = KPSTekoaly()
        pelaaja_vastaan_parempi_tekoaly = KPSParempiTekoaly()
        
        self.pelit = {"a":pelaaja_vastaan_pelaaja,"b":pelaaja_vastaan_tekoaly,"c":pelaaja_vastaan_parempi_tekoaly}
    
    
    
    def hae_peli(self,peli_valinta):
        if peli_valinta in self.pelit:
            return self.pelit[peli_valinta]
        else:
            exit

def main():
    pelitehdas = KPSPeliTehdas()
    
    while True:
        print("Valitse pelataanko"
              "\n (a) Ihmistä vastaan"
              "\n (b) Tekoälyä vastaan"
              "\n (c) Parannettua tekoälyä vastaan"
              "\nMuilla valinnoilla lopetetaan"
              )

        peli_valinta = input()
        if peli_valinta.endswith("a") or peli_valinta.endswith("b") or peli_valinta.endswith("c"):
            print(
                "Peli loppuu kun pelaaja antaa virheellisen siirron eli jonkun muun kuin k, p tai s"
            )
            peli = pelitehdas.hae_peli(peli_valinta)
            peli.pelaa()
        else:
            break


if __name__ == "__main__":
    main()











