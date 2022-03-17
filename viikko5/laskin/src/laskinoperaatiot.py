class Summa:
    def __init__(self, io, funktio):
        self.io = io
        self.funktio = funktio

    def suorita(self):
        try:
            arvo = int(self.funktio())
        except Exception:
            arvo = 0
        self.io.plus(arvo)

class Erotus:
    def __init__(self, io, funktio):
        self.io = io
        self.funktio = funktio

    def suorita(self):
        try:
            arvo = int(self.funktio())
        except Exception:
            arvo = 0
        self.io.miinus(arvo)

class Nollaus:
    def __init__(self, io):
        self.io = io

    def suorita(self):
        self.io.nollaa()

class Kumoa:
    def __init__(self, io):
        self.io = io
    
    def suorita(self):
        self.io.kumoa_viimeisin()