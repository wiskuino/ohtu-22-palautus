KAPASITEETTI = 5
OLETUSKASVATUS = 5


class IntJoukko:
    def __init__(self, kapasiteetti=KAPASITEETTI, laajennus=OLETUSKASVATUS):
        
        self.kapasiteetti = kapasiteetti
        if not isinstance(kapasiteetti, int) or kapasiteetti < 0:
            raise Exception("Väärä kapasiteetti")  

        self.laajennus = OLETUSKASVATUS
        self.ljono = [0] * self.kapasiteetti
        self.alkioiden_lkm = 0

    def kuuluu(self, alkio):
        return True if alkio in self.ljono[:self.alkioiden_lkm] else False
    
    def lisaa(self, lisattava_alkio):
        if self.alkioiden_lkm == 0:
            self.ljono[0] = lisattava_alkio
            self.alkioiden_lkm += 1

        else:
            if not self.kuuluu(lisattava_alkio):
                self.ljono[self.alkioiden_lkm] = lisattava_alkio
                self.alkioiden_lkm += 1

        if self.alkioiden_lkm == len(self.ljono):
            self.ljono += self.laajennus*[0]

    def poista(self, n):
        self.ljono =[alkio for alkio in self.ljono if alkio !=n ]
        self.alkioiden_lkm = self.ljono.index(0)

    def kopioi_taulukko(self, a:list, b:list):
        for alkio in range(0, len(a)):
            b[alkio] = a[alkio]

    def mahtavuus(self):
        return self.alkioiden_lkm

    def to_int_list(self):
        return [alkio for alkio in self.ljono if self.ljono.index(alkio) < self.alkioiden_lkm ]

    @staticmethod
    def yhdiste(a_joukko, b_joukko):
        yhdiste_joukko = IntJoukko()
        a_jono = a_joukko.to_int_list()
        b_jono = b_joukko.to_int_list()

        [yhdiste_joukko.lisaa(alkio) for alkio in a_jono]
        [yhdiste_joukko.lisaa(alkio) for alkio in b_jono]

        return yhdiste_joukko

    @staticmethod
    def leikkaus(a_joukko, b_joukko):
        leikkaus_joukko = IntJoukko()
        a_jono = a_joukko.to_int_list()
        b_jono = b_joukko.to_int_list()

        [leikkaus_joukko.lisaa(alkio) for alkio in a_jono if alkio in b_jono]
        return leikkaus_joukko

    @staticmethod
    def erotus(a_joukko, b_joukko):
        erotus_joukko = IntJoukko()
        a_jono = a_joukko.to_int_list()
        b_jono = b_joukko.to_int_list()

        [erotus_joukko.lisaa(alkio) for alkio in a_jono]
        [erotus_joukko.poista(alkio) for alkio in a_jono if alkio in b_jono]

        return erotus_joukko

    def __str__(self):
        if self.alkioiden_lkm == 0:
            return "{}"
        elif self.alkioiden_lkm == 1:
            return "{" + str(self.ljono[0]) + "}"
        else:
            comma_space = ", "
            return "{" + comma_space.join(map(str,self.ljono[:self.alkioiden_lkm])) + "}"
