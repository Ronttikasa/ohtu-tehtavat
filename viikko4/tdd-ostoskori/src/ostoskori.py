from tuote import Tuote
from ostos import Ostos

class Ostoskori:
    def __init__(self):
        self.sisalto = []
        # ostoskori tallettaa Ostos-oliota, yhden per korissa oleva Tuote

    def tavaroita_korissa(self):
        lukumaara = 0
        for ostos in self.sisalto:
            lukumaara += ostos.lukumaara()
        return lukumaara

    def hinta(self):
        hinta = 0
        if not len(self.sisalto) == 0:
            for ostos in self.sisalto:
                hinta += ostos.hinta()
        return hinta
        # kertoo korissa olevien ostosten yhteenlasketun hinnan

    def lisaa_tuote(self, lisattava: Tuote):
        for ostos in self.sisalto:
            if ostos.tuotteen_nimi() == lisattava.nimi():
                ostos.muuta_lukumaaraa(1)
                return
        uusi_ostos = Ostos(lisattava)
        self.sisalto.append(uusi_ostos)

    def poista_tuote(self, poistettava: Tuote):
        # poistaa tuotteen
        for ostos in self.sisalto:
            if ostos.tuotteen_nimi() == poistettava.nimi():
                ostos.muuta_lukumaaraa(-1)
                if ostos.lukumaara() == 0:
                    self.sisalto.remove(ostos)
                    return

    def tyhjenna(self):
        self.sisalto = []
        # tyhjentää ostoskorin

    def ostokset(self):
        return self.sisalto
        # palauttaa listan jossa on korissa olevat ostos-oliot
        # kukin ostos-olio siis kertoo mistä tuotteesta on kyse JA kuinka monta kappaletta kyseistä tuotetta korissa on
