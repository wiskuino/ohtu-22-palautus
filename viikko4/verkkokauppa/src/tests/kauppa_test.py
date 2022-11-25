import unittest
from unittest.mock import Mock, ANY
from kauppa import Kauppa
from viitegeneraattori import Viitegeneraattori
from varasto import Varasto
from tuote import Tuote
from ostoskori import Ostoskori

class TestKauppa(unittest.TestCase):
    def setUp(self):
        self.pankki_mock = Mock()
        self.viitegeneraattori_mock = Mock()

        # palautetaan aina arvo 42
        self.viitegeneraattori_mock.uusi.return_value = 42

        self.varasto_mock = Mock()

        # tehdään toteutus saldo-metodille
        def varasto_saldo(tuote_id):
            if tuote_id == 1:
                return 10
            if tuote_id == 2:
                return 20
            if tuote_id == 3:
                return 0
            if tuote_id == 4:
                return 100
            
        # tehdään toteutus hae_tuote-metodille
        def varasto_hae_tuote(tuote_id):
            if tuote_id == 1:
                return Tuote(1, "maito", 5)
            if tuote_id == 2:
                return Tuote(2, "nakit", 10)
            if tuote_id == 3:
                return Tuote(3, "olut", 20)
            if tuote_id == 4:
                return Tuote(3, "toinen_olut", 25)   

        # otetaan toteutukset käyttöön
        self.varasto_mock.saldo.side_effect = varasto_saldo
        self.varasto_mock.hae_tuote.side_effect = varasto_hae_tuote


        
        # alustetaan kauppa
        self.kauppa = Kauppa(self.varasto_mock, self.pankki_mock, self.viitegeneraattori_mock)

    
    def test_ostoksen_paaytyttya_pankin_metodia_tilisiirto_kutsutaan(self):
        
        # tehdään ostokset
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.tilimaksu("pekka", "12345")

        # varmistetaan, että metodia tilisiirto on kutsuttu
        self.pankki_mock.tilisiirto.assert_called()
        # toistaiseksi ei välitetä kutsuun liittyvistä argumenteista

    def test_ostoksen_paatyttya_pankin_metodia_tilisiirto_kutsutaan_oikeilla_parametreilla(self):

        # tehdään ostokset
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.tilimaksu("pekka", "12345")

        # varmistetaan, että metodia tilisiirto on kutsuttu
        self.pankki_mock.tilisiirto.assert_called_with("pekka",ANY,"12345","33333-44455",5)
        # toistaiseksi ei välitetä kutsuun liittyvistä argumenteista

    def test_kahden_eri_ostoksen_paatyttya_pankin_metodia_tilisiirto_kutsutaan_oikeilla_parametreilla(self):

        # tehdään ostokset
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.lisaa_koriin(2)
        self.kauppa.tilimaksu("pekka", "12345")
        
        # varmistetaan, että metodia tilisiirto on kutsuttu
        self.pankki_mock.tilisiirto.assert_called_with("pekka",ANY,"12345","33333-44455",15)
        # toistaiseksi ei välitetä kutsuun liittyvistä argumenteista

    def test_2_saman_ostoksen_paatyttya_pankin_metodia_tilisiirto_kutsutaan_oikeilla_parametreilla(self):
        # tehdään ostokset
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(2)
        self.kauppa.lisaa_koriin(2)
        self.kauppa.tilimaksu("pekka", "12345")

        # varmistetaan, että metodia tilisiirto on kutsuttu
        self.pankki_mock.tilisiirto.assert_called_with("pekka",ANY,"12345","33333-44455",20)
        # toistaiseksi ei välitetä kutsuun liittyvistä argumenteista

    def test_2_ostoksen_paatyttya_toisen_saldo_0_pankin_metodia_tilisiirto_kutsutaan_oikeilla_parametreilla(self):
        # tehdään ostokset
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(2)
        self.kauppa.lisaa_koriin(3)
        self.kauppa.tilimaksu("pekka", "12345")
        
        # varmistetaan, että metodia tilisiirto on kutsuttu
        self.pankki_mock.tilisiirto.assert_called_with("pekka",ANY,"12345","33333-44455",10)
        # toistaiseksi ei välitetä kutsuun liittyvistä argumenteista'

    def test_ostoskori_on_tyhja_ostosten_alkaessa(self):
        # aloitetaan ostokset
        self.kauppa.aloita_asiointi()
        
        # maksetaan oletettu tyhjä kori ennen 1 ostosta
        self.kauppa.tilimaksu("pekka", "12345")
        self.pankki_mock.tilisiirto.assert_called_with(ANY,ANY,ANY,ANY,0)
        #maksu summan pitää olla "0"
    

    def test_pyydetaan_uusi_viite_jokaiseen_maksuun(self):
        
        #pankki_mock = Mock()
        viitegeneraattori_mock = Mock(wraps=Viitegeneraattori())
        self.kauppa = Kauppa(self.varasto_mock,self.pankki_mock, viitegeneraattori_mock)
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.tilimaksu("pekka", "12345")
        # tarkistetaan että tässä vaiheessa viitegeneraattorin metodia uusi on kutsuttu kerran
        self.assertEqual(viitegeneraattori_mock.uusi.call_count, 1)
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(2)
        self.kauppa.tilimaksu("pekka", "12345")
        # tarkistetaan että tässä vaiheessa viitegeneraattorin metodia uusi on kutsuttu kaksi kertaa
        self.assertEqual(viitegeneraattori_mock.uusi.call_count, 2)
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.tilimaksu("pekka", "12345")
        # tarkistetaan että tässä vaiheessa viitegeneraattorin metodia uusi on kutsuttu kolme kertaa
        self.assertEqual(viitegeneraattori_mock.uusi.call_count, 3)
        self.pankki_mock.tilisiirto.assert_called_with(ANY,4,ANY,ANY,ANY)


    def test_kaksi_eri_ostostosta_joista_ensimmäinen_poistetaan_korista_metodia_tilisiirto_kutsutaan_oikeilla_parametreilla(self):
        # tehdään ostokset
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.lisaa_koriin(2)
        self.kauppa.poista_korista(1)
        self.kauppa.tilimaksu("pekka", "12345")

        # varmistetaan, että metodia tilisiirto on kutsuttu
        self.pankki_mock.tilisiirto.assert_called_with("pekka",ANY,"12345","33333-44455",10)
        # toistaiseksi ei välitetä kutsuun liittyvistä argumenteista