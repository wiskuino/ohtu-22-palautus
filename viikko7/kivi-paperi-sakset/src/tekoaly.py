from enum import Enum


class Siirto(Enum):
    Kivi = "k"
    Paperi = "p"
    Sakset = "s"


class Muisti:
    def __init__(self):
        self.siirto_indeksi=0
        self.siirrot = [Siirto.Kivi.value,Siirto.Paperi.value,Siirto.Sakset.value]
        self.seuraava_indeksi = 0

    def tallenna_seuraavan_siirron_indeksi(self,indeksi):
        self.seuraava_indeksi = indeksi

    def anna_seuraavan_siirron_indeksi(self):
        return self.seuraava_indeksi

class Tekoaly:
    def __init__(self):
        self._muisti = Muisti()
        self._siirto_indeksi=0
        self.siirrot = [Siirto.Kivi.value,Siirto.Paperi.value,Siirto.Sakset.value]


    def anna_siirto(self):
        self._siirto_indeksi = self._muisti.anna_seuraavan_siirron_indeksi()
        self._siirto_indeksi += 1
        self._siirto_indeksi = self._siirto_indeksi % 3
        self._muisti.tallenna_seuraavan_siirron_indeksi(self._siirto_indeksi)

        return self._muisti.siirrot[self._siirto_indeksi]

    def aseta_siirto(self, siirto):
        # ei tehdä mitään
        pass
