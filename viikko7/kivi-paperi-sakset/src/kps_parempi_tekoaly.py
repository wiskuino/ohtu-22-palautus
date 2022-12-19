from tuomari import Tuomari
from tekoaly_parannettu import TekoalyParannettu
from kps_tekoaly import KPSTekoaly


class KPSParempiTekoaly(KPSTekoaly):
    def __init__(self):
        self.tekoaly = TekoalyParannettu(10)