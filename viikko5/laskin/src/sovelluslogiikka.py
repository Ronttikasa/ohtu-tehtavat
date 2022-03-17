class Sovelluslogiikka:
    def __init__(self, tulos=0):
        self.tulos = tulos
        self.edelliset_tulokset = []

    def miinus(self, arvo):
        self.edelliset_tulokset.append(self.tulos)
        self.tulos = self.tulos - arvo

    def plus(self, arvo):
        self.edelliset_tulokset.append(self.tulos)
        self.tulos = self.tulos + arvo

    def nollaa(self):
        self.edelliset_tulokset.append(self.tulos)
        self.tulos = 0

    def aseta_arvo(self, arvo):
        self.tulos = arvo

    def kumoa_viimeisin(self):
        try:
            self.tulos = self.edelliset_tulokset.pop()
        except IndexError:
            pass