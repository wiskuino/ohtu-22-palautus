# "Muistava tekoäly"
from collections import Counter,deque

class Muisti():
    def __init__(self):
        self.muistin_koko = 10
        self._muisti_dq = deque([],self.muistin_koko)
        
    
    def vie_siirto_muistiin(self,siirto):
        self._muisti_dq.append(siirto)
        return self._muisti_dq
    
    def vapaa_indeksi(self):
        return len(self._muisti_dq)


class TekoalyParannettu:
    def __init__(self, muistin_koko):
        self.erikoistunut_muisti = Muisti()
        self._muisti = []
        self.muistin_koko= muistin_koko
        self._vapaa_muisti_indeksi = 0


    def aseta_siirto(self, siirto):
        self._muisti = self.erikoistunut_muisti.vie_siirto_muistiin(siirto)
        
        self._vapaa_muisti_indeksi = self.erikoistunut_muisti.vapaa_indeksi()      

    def anna_siirto(self):
        if self._vapaa_muisti_indeksi == 0 or self._vapaa_muisti_indeksi == 1:
            return "k"

        viimeisin_siirto = self._muisti[self._vapaa_muisti_indeksi - 1]
        

        k = 0
        p = 0
        s = 0

        for i in range(0, self._vapaa_muisti_indeksi - 1):
            if viimeisin_siirto == self._muisti[i]:
                seuraava = self._muisti[i + 1]

                if seuraava == "k":
                    k = k + 1
                elif seuraava == "p":
                    p = p + 1
                else:
                    s = s + 1

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
