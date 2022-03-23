from kivi_paperi_sakset import KiviPaperiSakset as KPS


class KPSPelaajaVsPelaaja(KPS):
    def _toisen_siirto(self, ensimmaisen_siirto):
        siirto = input("Toisen pelaajan siirto: ")
        return siirto