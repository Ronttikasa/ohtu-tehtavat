class IntJoukko:
    def __init__(self, kapasiteetti=5, kasvatuskoko=5):
        self.kapasiteetti = kapasiteetti
        self.kasvatuskoko = kasvatuskoko

        self.__taulukko = [0] * self.__kapasiteetti
        self.__alkioiden_lkm = 0

    @property
    def kapasiteetti(self):
        return self.__kapasiteetti

    @kapasiteetti.setter
    def kapasiteetti(self, kapasiteetti):
        if isinstance(kapasiteetti, int) and kapasiteetti >= 0:
            self.__kapasiteetti = kapasiteetti
        else:
            raise ValueError("Kapasiteetin tulee olla vähintään 0")

    @property
    def kasvatuskoko(self):
        return self.__kasvatuskoko

    @kasvatuskoko.setter
    def kasvatuskoko(self, kasvatuskoko):
        if isinstance(kasvatuskoko, int) and kasvatuskoko >= 0:
            self.__kasvatuskoko = kasvatuskoko
        else:
            raise ValueError("Kasvatuskoon tulee olla vähintään 0")

    def kuuluu(self, haettava):
        for i in range(self.__alkioiden_lkm):
            if haettava == self.__taulukko[i]:
                return True
        return False
        
    def lisaa(self, lisattava):
        if self.kuuluu(lisattava):
            return False
        if self.__alkioiden_lkm == len(self.__taulukko):
            self.__taulukko += [0] * self.__kasvatuskoko
        self.__taulukko[self.__alkioiden_lkm] = lisattava   
        self.__alkioiden_lkm += 1

        return True

    def poista(self, poistettava):
        if not self.kuuluu(poistettava):
            return False

        for i in range(self.__alkioiden_lkm):
            if poistettava == self.__taulukko[i]:
                self.__taulukko = self.__taulukko[:i] + self.__taulukko[i+1:] + [0]
                break

        self.__alkioiden_lkm = self.__alkioiden_lkm - 1
        return True

    def mahtavuus(self):
        return self.__alkioiden_lkm

    def to_int_list(self):
        alkiot = []
        for i in range(self.__alkioiden_lkm):
            alkiot.append(self.__taulukko[i])

        return alkiot

    @staticmethod
    def yhdiste(a, b):
        yhdiste = IntJoukko()
        a_alkiot = a.to_int_list()
        b_alkiot = b.to_int_list()

        for alkio in a_alkiot:
            yhdiste.lisaa(alkio)
        for alkio in b_alkiot:
            yhdiste.lisaa(alkio)

        return yhdiste

    @staticmethod
    def leikkaus(a, b):
        leikkaus = IntJoukko()
        a_alkiot = a.to_int_list()

        for alkio in a_alkiot:
            if b.kuuluu(alkio):
                leikkaus.lisaa(alkio)

        return leikkaus

    @staticmethod
    def erotus(a, b):
        erotus = IntJoukko()
        a_alkiot = a.to_int_list()

        for alkio in a_alkiot:
            if not b.kuuluu(alkio):
                erotus.lisaa(alkio)

        return erotus

    def __str__(self):
        jono = ""
        for alkio in self.to_int_list():
            jono += f"{alkio}, "
        jono = jono[:-2]

        return f"{{{jono}}}"