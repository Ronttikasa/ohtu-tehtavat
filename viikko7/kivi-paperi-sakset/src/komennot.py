from kivi_paperi_sakset import KiviPaperiSakset as KPS
import sys

class Komentovalitsija:
    def __init__(self):
        self._komennot = {
            "a": KPS.luo_kaksinpeli(),
            "b": KPS.luo_helppo_yksinpeli(),
            "c": KPS.luo_vaikea_yksinpeli()
        }

    def suorita(self, komento):
        if komento in self._komennot:
            self._komennot[komento].pelaa()
        else:
            sys.exit(0)
