# "Muistava tekoäly"
from collections import Counter,deque

class Muisti():
    def __init__(self, muistin_koko):
        
        self.muistin_koko = muistin_koko
        
        self._muisti_dq = deque([],self.muistin_koko)
        
    
    def vie_siirto_muistiin(self,siirto):
        if siirto == "k" or siirto == "p" or siirto == "s":
            self._muisti_dq.append(siirto)
            return self._muisti_dq
        else:
            return self._muisti_dq

    def vapaa_indeksi(self):
        return len(self._muisti_dq)

    def anna_ennusteen_pohja(self, viimeisin_siirto):
        return [ seuraava_siirto for siirto,seuraava_siirto  in zip(list(self._muisti_dq)[:-1],list(self._muisti_dq)[1:]) if siirto == viimeisin_siirto ]
        

class TekoalyParannettu:
    def __init__(self, muistin_koko):
        self.erikoistunut_muisti = Muisti(muistin_koko)
        self._muisti = []
        self.muistin_koko = muistin_koko
        self._vapaa_muisti_indeksi = 0

    def kerro_muistin_koko(self):
        return self.muistin_koko

    def aseta_siirto(self, siirto):
        self._muisti = self.erikoistunut_muisti.vie_siirto_muistiin(siirto)
        

    def anna_siirto(self):
        if self.erikoistunut_muisti.vapaa_indeksi() == 0 or self.erikoistunut_muisti.vapaa_indeksi() == 1:
            return "k"

        viimeisin_siirto = self._muisti[self.erikoistunut_muisti.vapaa_indeksi() - 1]

        pohja = (self.erikoistunut_muisti.anna_ennusteen_pohja(viimeisin_siirto))
        
       
       #k = 0
       #p = 0
       #s = 0

       #for i in range(0, self._vapaa_muisti_indeksi - 1):
       #    if viimeisin_siirto == self._muisti[i]:
       #        seuraava = self._muisti[i + 1]

       #        if seuraava == "k":
       #            k = k + 1
       #        elif seuraava == "p":
       #            p = p + 1
       #        else:
       #            s = s + 1

        #print(k,p,s)
        #print(pohja.count("k"),pohja.count("p"),pohja.count("s"))

        k=pohja.count("k")
        p=pohja.count("p")
        s=pohja.count("s")

        
        

        # Tehdään siirron valinta esimerkiksi seuraavasti;
        # - jos kiviä eniten, annetaan aina paperi
        # - jos papereita eniten, annetaan aina sakset
        # muulloin annetaan aina kivi
        if k > p or k > s:
            
            return "p"
        elif p > k or p > s:
            
            return "s"
        else:
            
            return "k"

        # Tehokkaampiakin tapoja löytyy, mutta niistä lisää
        # Johdatus Tekoälyyn kurssilla!
