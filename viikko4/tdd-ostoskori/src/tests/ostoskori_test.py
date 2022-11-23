import unittest
from ostoskori import Ostoskori
from tuote import Tuote

class TestOstoskori(unittest.TestCase):
    def setUp(self):
        self.kori = Ostoskori()

    def test_ostoskorin_hinta_ja_tavaroiden_maara_alussa(self):
        self.assertEqual(self.kori.hinta(), 0)
        self.assertEqual(self.kori.tavaroita_korissa(), 0)
        
    def test_tuotteen_lisaamisen_jalkeen_tuote_ostoskorissa(self):
        self.assertEqual(self.kori.tavaroita_korissa(), 0)
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)
        self.assertEqual(self.kori.tavaroita_korissa(), 1)
        
    def test_tuotteen_lisaamisen_jalkeen_ostoskorin_hinta_on_tuotteen_hinta(self):
        self.assertEqual(self.kori.hinta(), 0)
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)
        self.assertEqual(self.kori.hinta(), 3)

    def test_kahden_eri_tuotteen_lisaamisen_jalkeen_ostoskorissa_2_tuotetta(self):
        maito = Tuote("Maito", 3)
        rahka = Tuote("Rahka", 1)
        self.kori.lisaa_tuote(maito)
        self.kori.lisaa_tuote(rahka)
        self.assertEqual(self.kori.tavaroita_korissa(), 2)
    
    def test_kahden_eri_tuotteen_lisaamisen_jalkeen_ostoskorin_hinta_vastaa_sisaltoa(self):
        maito = Tuote("Maito", 3)
        rahka = Tuote("Rahka", 1)
        self.kori.lisaa_tuote(maito)
        self.kori.lisaa_tuote(rahka)
        self.assertEqual(self.kori.hinta(), 4)
        
    def test_kahden_saman_tuotteen_lisaamisen_jalkeen_ostoskorissa_2_tuotetta(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)
        self.kori.lisaa_tuote(maito)
        self.assertEqual(self.kori.tavaroita_korissa(), 2)
    
    def test_kahden_saman_tuotteen_lisaamisen_jalkeen_ostoskorin_hinta_vastaa_sisaltoa(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)
        self.kori.lisaa_tuote(maito)
        self.assertEqual(self.kori.hinta(), 6)

    def test_yhden_tuotteen_lisaamisen_jalkeen_ostoskorissa_yksi_ostos(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)
        
        ostokset = self.kori.ostokset()
        self.assertEqual(len(ostokset), 1)
    
    def test_yhden_tuotteen_lisaamisen_jalkeen_ostoskorissa_oikea_tuote_ja_maara(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)
        
        ostos = self.kori.ostokset()[0]
        self.assertEqual(ostos.hinta(), 3)
        self.assertEqual(len(self.kori.ostokset()),1)
    
    def test_kahden_eri_tuotteen_lisaamisen_jalkeen_ostoskorissa_kaksi_ostosta(self):
        maito = Tuote("Maito", 3)
        rahka = Tuote("Rahka", 1)
        self.kori.lisaa_tuote(maito)
        self.kori.lisaa_tuote(rahka)
        
        self.assertEqual(len(self.kori.ostokset()), 2)
    
    def test_kahden_saman_tuotteen_lisaamisen_jalkeen_ostoskorissa_1_ostos(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)
        self.kori.lisaa_tuote(maito)
        
        self.assertEqual(len(self.kori.ostokset()),1)
    
    def test_kahden_saman_tuotteen_lisaamisen_jalkeen_ostoskorissa_ostos_jolla_sama_nimi_ja_lukumaara(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)
        self.kori.lisaa_tuote(maito)
        
        ostos = self.kori.ostokset()[0]
        self.assertEqual(ostos.tuotteen_nimi(), "Maito")
        self.assertEqual(ostos.lukumaara(), 2)
    
    def test_kun_korissa_kaksi_samaa_tuotetta_ja_toinen_poistetaan_niin_ostos_lukumaara_1(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)
        self.kori.lisaa_tuote(maito)
        
        ostos = self.kori.ostokset()[0]
        self.assertEqual(ostos.lukumaara(), 2)
        
        self.kori.poista_tuote(maito)
        self.assertEqual(ostos.lukumaara(), 1)

    def test_jos_koriin_lisatty_tuote_ja_sama_tuote_poistetaan_on_kori_tyhjä(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)
        self.kori.poista_tuote(maito)
        self.assertEqual(self.kori.tavaroita_korissa(), 0)

    def test_tyhjenna_tyhjentaa_korin(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)
        self.kori.tyhjenna()
        self.assertEqual(self.kori.tavaroita_korissa(), 0)