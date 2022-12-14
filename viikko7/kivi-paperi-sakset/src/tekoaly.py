from enum import Enum


class Siirto(Enum):
    Kivi = "k"
    Paperi = "p"
    Sakset = "s"


class Tekoaly:
    def __init__(self):
        self._siirto_indeksi=0
        self.siirrot = [Siirto.Kivi.value,Siirto.Paperi.value,Siirto.Sakset.value]


    def anna_siirto(self,edellinen_siirto):
        self._siirto_indeksi = self.siirrot.index(edellinen_siirto)
        self._siirto_indeksi += 1
        self._siirto_indeksi = self._siirto_indeksi % 3
        return self.siirrot[self._siirto_indeksi]

    def aseta_siirto(self, siirto):
        # ei tehdä mitään
        pass
