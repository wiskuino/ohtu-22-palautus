from enum import Enum


class Siirto(Enum):
    Kivi = "k"
    Paperi = "p"
    Sakset = "s"


class Muisti:
    def __init__(self):
        self.uuden_siirron_indeksi = 0
        self.siirrot = [Siirto.Kivi.value,Siirto.Paperi.value,Siirto.Sakset.value]
        self._siirron_indeksi = 0

    def tallenna_siirron_indeksi(self,indeksi):
        self._siirron_indeksi = indeksi

    def anna_edellisen_siirron_indeksi(self):
        return self._siirron_indeksi

class Tekoaly:
    def __init__(self):
        self._muisti = Muisti()
        self._siirto_indeksi = 0
        self.siirrot = [Siirto.Kivi.value,Siirto.Paperi.value,Siirto.Sakset.value]


    def anna_siirto(self):
        self.uuden_siirron_indeksi = self._muisti.anna_edellisen_siirron_indeksi()
        self.uuden_siirron_indeksi += 1
        self.uuden_siirron_indeksi = self.uuden_siirron_indeksi % 3
        self._muisti.tallenna_siirron_indeksi(self.uuden_siirron_indeksi)

        return self._muisti.siirrot[self.uuden_siirron_indeksi]

    def aseta_siirto(self, siirto):
        # ei tehdä mitään
        pass
