import unittest
from int_joukko import IntJoukko


def main():
    joukko = IntJoukko()

    joukko.lisaa(1)
    joukko.lisaa(2)
    joukko.lisaa(3)
    joukko.lisaa(-2)
    joukko.lisaa(5)
    joukko.lisaa(-1)
    joukko.kopioi_taulukko([0,0],[1,2])
    joukko.poista(3)
    
    print(joukko.mahtavuus())

    print(joukko.to_int_list())


if __name__ == "__main__":
    main()
