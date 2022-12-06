from enum import Enum
from tkinter import ttk, constants, StringVar


class Komento(Enum):
    SUMMA = 1
    EROTUS = 2
    NOLLAUS = 3
    KUMOA = 4


class Summa:
    def __init__(self,sovellus):
        self._sovellus=sovellus
        
    def suorita(self,arvo:float):
        return self._sovellus.plus(arvo)

class Erotus:
    def __init__(self,sovellus):
        self._sovellus=sovellus

    def suorita(self, arvo:float):
        return self._sovellus.miinus(arvo)

class Nollaus:
    def __init__(self,sovellus):
        self._sovellus=sovellus
        
    def suorita(self, *args):
        return self._sovellus.nollaa()

class Kumoa:
    def __init__(self,sovellus):
        self._sovellus=sovellus

    def suorita(self, *args):
        return self._sovellus.kumoa()


class Kayttoliittyma:
    def __init__(self, sovellus, root):
        self._sovellus = sovellus
        self._root = root
        self.edelliset = []
        self._syote_kentta=0
        self._komennot = {
            Komento.SUMMA: Summa(sovellus),
            Komento.EROTUS: Erotus(sovellus),
            Komento.NOLLAUS: Nollaus(sovellus),
            Komento.KUMOA: Kumoa(sovellus)
        }

    def kaynnista(self):
        self._tulos_var = StringVar()
        self._tulos_var.set(self._sovellus.tulos)
        self._syote_kentta = ttk.Entry(master=self._root)

        tulos_teksti = ttk.Label(textvariable=self._tulos_var)

        summa_painike = ttk.Button(
            master=self._root,
            text="Summa",
            command=lambda: self._suorita_komento(Komento.SUMMA)
        )

        erotus_painike = ttk.Button(
            master=self._root,
            text="Erotus",
            command=lambda: self._suorita_komento(Komento.EROTUS)
        )

        self._nollaus_painike = ttk.Button(
            master=self._root,
            text="Nollaus",
            state=constants.DISABLED,
            command=lambda: self._suorita_komento(Komento.NOLLAUS)
        )

        self._kumoa_painike = ttk.Button(
            master=self._root,
            text="Kumoa",
            state=constants.DISABLED,
            command=lambda: self._suorita_komento(Komento.KUMOA)
        )

        tulos_teksti.grid(columnspan=4)
        self._syote_kentta.grid(columnspan=4, sticky=(constants.E, constants.W))
        summa_painike.grid(row=2, column=0)
        erotus_painike.grid(row=2, column=1)
        self._nollaus_painike.grid(row=2, column=2)
        self._kumoa_painike.grid(row=2, column=3)
    
    def _suorita_komento(self, komento):
        arvo=0
        komento_olio = self._komennot[komento]
        try:
            arvo = float(self._lue_syote())
        except Exception:
            pass

        komento_olio.suorita(arvo)

        self._painike_ikkunan_yllapito()

    
    def _lue_syote(self):
        return float(self._syote_kentta.get()) 
        

    def _painike_ikkunan_yllapito(self):

        if self._sovellus.edelliset == []:
            self._kumoa_painike["state"] = constants.DISABLED
        else:
            self._kumoa_painike["state"] = constants.NORMAL
        
        if self._sovellus.tulos == 0:
            self._nollaus_painike["state"] = constants.DISABLED
        else:
            self._nollaus_painike["state"] = constants.NORMAL
    
        self._syote_kentta.delete(0, constants.END)
       
        self._tulos_var.set(self._sovellus.tulos)