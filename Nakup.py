class Produkt:
    def __init__(self, nazev, cena):
        self.nazev = nazev
        self.cena = cena

    def popis(self):
        return f"{self.nazev} stojí {self.cena} Kč"

    def zdrazit(self, zdrazeni):
        self.cena = self.cena + zdrazeni
        return self.cena


class NakupniSeznam:
    def __init__(self):
        self.polozky = []

    def pridat(self, produkt):
        self.polozky.append(produkt)
        return self.polozky

    def add(self):

        while True:
            polozka = input(
                "napis jméno produktu co chceš přidat do seznamu a nebo stop pro konec přidávání\n"
            )

            if polozka == "stop":
                break
            while True:

                try:
                    cena = input("napis cenu produktu co chceš přidat do seznamu\n  ")
                    cena = int(cena)
                    novy = Produkt(polozka, cena)
                    break
                except ValueError:
                    print("neplatný formát čísla")

            self.pridat(novy)

    def celkova_cena(self):
        celkem = 0
        for produkt in self.polozky:
            celkem = produkt.cena + celkem
        return celkem

    def vypis(self):
        for produkt in self.polozky:
            print(produkt.popis())

    def nejdrazsi(self):

            nejdrazsi = self.polozky[0]

            for produkt in self.polozky:
                if nejdrazsi.cena < produkt.cena:
                    nejdrazsi = produkt
            return nejdrazsi

    def ulozit_nakup(self):
        with open("nakup.txt", "w", encoding="utf-8") as soubor:
            for produkt in self.polozky:

                soubor.write(f"{produkt.nazev};{produkt.cena}\n")

    def nacti_nakup(self):

        try:
            with open("nakup.txt", "r", encoding="utf-8") as soubor:
                for radek in soubor:
                    radek = radek.strip()
                    nazev, cena = radek.split(";")
                    novy = Produkt(nazev, int(cena))
                    self.pridat(novy)
        except FileNotFoundError:
            pass

        return self.polozky


nakup = NakupniSeznam()
nakup.nacti_nakup()


while True:
    volba = input(
        "co chceš dělat \n 1 přidat do nákupu \n 2 vypsat položky nákupu  \n 3 odejít z programu \n 4 vypsat celkovou cenu nákupu\n 5 vypsat nejdražší položku\n"
    )
    if volba == "1":
        nakup.add()
    elif volba == "2":
        nakup.vypis()
    elif volba == "3":
        nakup.ulozit_nakup()
        break
    elif volba == "4":
        print(f" celkova cena nákupu je {nakup.celkova_cena()}")
    elif volba == "5":
        if len(nakup.polozky) == 0:
            print("nákup je prázdný")
        else :
         nejdrazsi = nakup.nejdrazsi()
         print(f"nejdrazší položka nákupu je {nejdrazsi.popis()}")
    else:
        print("Neznámá volba, zkus to znovu.")
