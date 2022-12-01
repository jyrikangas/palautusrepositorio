KAPASITEETTI = 5
OLETUSKASVATUS = 5


class IntJoukko:
    def __init__(self, kapasiteetti=5, kasvatuskoko=5):
        self.kapasiteetti = kapasiteetti
        self.kasvatuskoko = kasvatuskoko

        self.ljono = [0] * self.kapasiteetti

        self.alkioiden_lkm = 0

    def kuuluu(self, etsittava_luku):
        for alkio in self.ljono:
            if alkio == etsittava_luku:
                return True

    def kasvata_taulukkoa(self):
            taulukko_old = self.ljono
            self.ljono = [0] * (self.alkioiden_lkm + self.kasvatuskoko)
            self.kopioi_taulukko(taulukko_old, self.ljono)
            
    def lisaa(self, lisattava):
        if self.kuuluu(lisattava):
            return False
        
        self.ljono[self.alkioiden_lkm] = lisattava
        self.alkioiden_lkm += 1
        if self.alkioiden_lkm == len(self.ljono):
            self.kasvata_taulukkoa()
        return True

    def poista(self, poistettava):
        for kohta in range(0, self.alkioiden_lkm):
            if poistettava == self.ljono[kohta]:
                self.ljono[kohta] = 0
                for j in range(kohta, self.alkioiden_lkm - 1):
                    self.ljono[j] = self.ljono[j + 1]
                    self.ljono[j + 1] = 0
                self.alkioiden_lkm = self.alkioiden_lkm - 1
                return True
        return False

    def kopioi_taulukko(self, kopioitava, kopio):
        for i in range(0, len(kopioitava)):
            kopio[i] = kopioitava[i]

    def mahtavuus(self):
        return self.alkioiden_lkm

    def to_int_list(self):
        taulu = self.ljono[0:self.alkioiden_lkm]
        return taulu

    @staticmethod
    def yhdiste(yhdistettava_a, yhdistettava_b):
        uusi = IntJoukko()
        a_taulu = yhdistettava_a.to_int_list()
        b_taulu = yhdistettava_b.to_int_list()

        for i in range(0, len(a_taulu)):
            uusi.lisaa(a_taulu[i])

        for i in range(0, len(b_taulu)):
            uusi.lisaa(b_taulu[i])

        return uusi

    @staticmethod
    def leikkaus(leikattava_joukko_a, leikattava_joukko_b):
        leikkaus = IntJoukko()
        a_taulu = leikattava_joukko_a.to_int_list()
        b_taulu = leikattava_joukko_b.to_int_list()

        for i in range(0, len(a_taulu)):
            for j in range(0, len(b_taulu)):
                if a_taulu[i] == b_taulu[j]:
                    leikkaus.lisaa(b_taulu[j])

        return leikkaus

    @staticmethod
    def erotus(erotettava, erottaja):
        erotus = IntJoukko()
        erotettavat = erotettava.to_int_list()
        erottajat = erottaja.to_int_list()

        for i in range(0, len(erotettavat)):
            erotus.lisaa(erotettavat[i])

        for i in range(0, len(erottajat)):
            erotus.poista(erottajat[i])

        return erotus

    def __str__(self):
        if self.alkioiden_lkm == 0:
            return "{}"
        elif self.alkioiden_lkm == 1:
            return "{" + str(self.ljono[0]) + "}"
        else:
            tuotos = "{"
            for i in range(0, self.alkioiden_lkm - 1):
                tuotos = tuotos + str(self.ljono[i])
                tuotos = tuotos + ", "
            tuotos = tuotos + str(self.ljono[self.alkioiden_lkm - 1])
            tuotos = tuotos + "}"
            return tuotos
