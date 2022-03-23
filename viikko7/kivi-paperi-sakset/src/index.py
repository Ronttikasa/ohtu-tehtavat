from komennot import Komentovalitsija


def main():
    komentovalitsija = Komentovalitsija()

    while True:
        print("Valitse pelataanko"
              "\n (a) Ihmistä vastaan"
              "\n (b) Tekoälyä vastaan"
              "\n (c) Parannettua tekoälyä vastaan"
              "\nMuilla valinnoilla lopetetaan"
              )

        vastaus = input()

        komentovalitsija.suorita(vastaus)

if __name__ == "__main__":
    main()
