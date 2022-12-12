from enum import Enum


class Siirto(Enum):
    Kivi = "k"
    Paperi = "p"
    Sakset = "s"


class Tekoaly:
    def __init__(self):
        self._siirto=0
        self.siirrot = [Siirto.Kivi,Siirto.Paperi,Siirto.Sakset]


    def anna_siirto(self):
        self._siirto += 1
        self._siirto = self._siirto % 3
        return self.siirrot[self._siirto].value

    def aseta_siirto(self, siirto):
        # ei tehdä mitään
        pass




