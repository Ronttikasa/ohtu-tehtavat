from tekoaly import Tekoaly
from kivi_paperi_sakset import KiviPaperiSakset as KPS


class KPSTekoaly(KPS):
    def __init__(self):
        self._tekoaly = Tekoaly()

    def _toisen_siirto(self, ensimmaisen_siirto):
        siirto = self._tekoaly.anna_siirto()
        print(f"Tietokone valitsi: {siirto}")
        return siirto
        


