
from pelitehdas import KPSPeliTehdas

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











