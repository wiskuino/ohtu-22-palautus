# "Muistava tekoäly"
from collections import Counter,deque

class Muisti():
    def __init__(self):
        self.muistin_koko = 10
        self.muisti_dq = deque([],self.muistin_koko)
        
    
    def vie_siirto_muistiin(self,siirto):
        self.muisti_dq.append(siirto)
        return self.muisti_dq
    
    def vapaa_indeksi(self):
        return len(self.muisti_dq)

    def __str__(self) -> str:
        return self.vapaa_indeksi()


class TekoalyParannettu:
    def __init__(self, muistin_koko):
        self.erikoistunut_muisti = Muisti()
        self._muisti = []
        self.muistin_koko= muistin_koko
        self._vapaa_muisti_indeksi = 0
        self.tulos_lista = []
        self.vertailu = []
        

    def aseta_siirto(self, siirto):
        self._muisti = self.erikoistunut_muisti.vie_siirto_muistiin(siirto)
        
        # muistin  täyttyessä vanhin poistetaan
        #if self.muistin_koko == len(self._muisti):
        #    self._muisti.pop(0)
        #    
#
        #    self._vapaa_muisti_indeksi = len(self._muisti)
#
        #self._muisti.append(siirto)
        #
        #print(f"alkuperäinen {self._muisti}")
        self._vapaa_muisti_indeksi = self.erikoistunut_muisti.vapaa_indeksi()
    
        #self._vapaa_muisti_indeksi = self._vapaa_muisti_indeksi + 1
        #print(f"alkuperäinen {str(self._vapaa_muisti_indeksi)}")
    #
    def ennusta_ekan_siirto(self,viimeisin_siirto):
        pass
        #indeksi = self._muisti.index(viimeisin_siirto)
       #if not indeksi == None:
       #    for alkio in range(len(self._muisti)-1):
       #        lista= list(zip(self._muisti[indeksi:-1],self._muisti[indeksi+1:]))
       #    lista
       #    result = Counter([tup for tup in lista if tup[0] == viimeisin_siirto]).most_common(2)
       #    if len(result) == 0 or (len(result) ==2 and result[0][1] == result [1][1]):
       #        self.tulos_lista.append("s")
       #    else:
       #        self.tulos_lista.append(result[0][0][1])
       #else:
       #    self.tulos_lista.append("s")
       #
       #
       #lista= list(zip(self._muisti[indeksi:-1],self._muisti[indeksi+1:]))
       #result = Counter([tup for tup in lista if tup[0] == viimeisin_siirto]).most_common(2)
       ##result = Counter(self._muisti[indeksi+1:self._vapaa_muisti_indeksi - 1]).most_common(3)
       #if len(result) == 0 or (len(result) ==2 and result[0][1] == result [1][1]):
       #    self.tulos_lista.append("s")
       #else:
       #    self.tulos_lista.append(result[0][0][1])

    def anna_siirto(self):
        if self._vapaa_muisti_indeksi == 0 or self._vapaa_muisti_indeksi == 1:
            return "k"

        viimeisin_siirto = self._muisti[self._vapaa_muisti_indeksi - 1]
        
        self.ennusta_ekan_siirto(viimeisin_siirto)

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
            self.vertailu.append("k")
            return "p"
        elif p > k or p > s:
            self.vertailu.append("p")
            return "s"
        else:
            self.vertailu.append("s")
            return "k"

        # Tehokkaampiakin tapoja löytyy, mutta niistä lisää
        # Johdatus Tekoälyyn kurssilla!
