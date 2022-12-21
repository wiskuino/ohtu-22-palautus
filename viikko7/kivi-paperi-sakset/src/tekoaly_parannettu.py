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

    def viimeinen_siirto(self):
        return self._muisti_dq[len(self._muisti_dq)-1]

    def vapaa_indeksi(self):
        return len(self._muisti_dq)

    def edellisten_valintojen_määrät(self, viimeisin_siirto):
        return [ seuraava_siirto for siirto,seuraava_siirto  in zip(list(self._muisti_dq)[:-1],list(self._muisti_dq)[1:]) if siirto == viimeisin_siirto ]
        

class TekoalyParannettu:
    def __init__(self, muistin_koko):
        self._muisti = Muisti(muistin_koko)

    def aseta_siirto(self, siirto):
        self._muisti.vie_siirto_muistiin(siirto)
        

    def anna_siirto(self):
        if self._muisti.vapaa_indeksi() == 0 or self._muisti.vapaa_indeksi() == 1:
            return "k"

        viimeisin_siirto = self._muisti.viimeinen_siirto()

        k = (self._muisti.edellisten_valintojen_määrät(viimeisin_siirto)).count("k")
        p = (self._muisti.edellisten_valintojen_määrät(viimeisin_siirto)).count("p")
        s = (self._muisti.edellisten_valintojen_määrät(viimeisin_siirto)).count("s")

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
