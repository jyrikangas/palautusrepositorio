class Sovelluslogiikka:
    def __init__(self, tulos=0):
        self.tulos = tulos
        self.edellinen = 0




class Miinus:
    def __init__(self, sovelluslogiikka, io):
        self.io = io
        self._sovelluslogiikka = sovelluslogiikka

    def suorita(self):
        self._sovelluslogiikka.edellinen = self._sovelluslogiikka.tulos
        luku = int(self.io())
        self._sovelluslogiikka.tulos -= luku

class Plus:
    def __init__(self, sovelluslogiikka, io):
        self.io = io
        self._sovelluslogiikka = sovelluslogiikka

    def suorita(self):
        self._sovelluslogiikka.edellinen = self._sovelluslogiikka.tulos
        luku = int(self.io())
        self._sovelluslogiikka.tulos += luku
        
class Nollaa:
    def __init__(self, sovelluslogiikka, io):
        self.io = io
        self._sovelluslogiikka = sovelluslogiikka
    def suorita(self):
        self._sovelluslogiikka.edellinen = self._sovelluslogiikka.tulos
        self._sovelluslogiikka.tulos = 0

class Kumoa:
    def __init__(self, sovelluslogiikka, io):
        self.io = io
        self._sovelluslogiikka = sovelluslogiikka
    def suorita(self):
        tulos = self._sovelluslogiikka.tulos
        self._sovelluslogiikka.tulos = self._sovelluslogiikka.edellinen
        self._sovelluslogiikka.edellinen = tulos
