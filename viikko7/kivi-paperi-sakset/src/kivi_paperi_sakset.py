from tuomari import Tuomari

class KiviPaperiSakset:

    @staticmethod
    def luo_kaksinpeli():
        from kps_pelaaja_vs_pelaaja import KPSPelaajaVsPelaaja
        return KPSPelaajaVsPelaaja()

    @staticmethod
    def luo_helppo_yksinpeli():
        from kps_tekoaly import KPSTekoaly
        return KPSTekoaly()

    @staticmethod
    def luo_vaikea_yksinpeli():
        from kps_parempi_tekoaly import KPSParempiTekoaly
        return KPSParempiTekoaly()

    def pelaa(self):
        tuomari = Tuomari()

        while True:
            ekan_siirto = self._ensimmaisen_siirto()
            if not self._siirto_ok(ekan_siirto):
                break
            tokan_siirto = self._toisen_siirto(ekan_siirto)

            if self._siirto_ok(tokan_siirto):
                tuomari.kirjaa_siirto(ekan_siirto, tokan_siirto)
                print(tuomari)
            else:
                break

        print("Kiitos!")
        print(tuomari)

    def _ensimmaisen_siirto(self):
        return input("Ensimmäisen pelaajan siirto: ")

    def _toisen_siirto(self, ensimmaisen_siirto):
        return "p"

    def _siirto_ok(self, siirto):
        return siirto in ['k', 'p', 's']