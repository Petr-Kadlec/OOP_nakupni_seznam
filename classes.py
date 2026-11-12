class Produkt:
    def __init__(self, nazev, cena):
        self.nazev = nazev
        self.cena = cena

    def popis(self):
        return f"{self.nazev} stojí {self.cena} Kč"
    def zdrazit(self, zdrazeni):
        self.cena = self.cena + zdrazeni
        return self.cena


chleba = Produkt("chleba", 45)
mleko = Produkt("mléko", 28)
syr = Produkt("sýr", 89)
print(syr.cena)
syr.zdrazit(5)
print(syr.cena)
print(chleba.nazev)

print(mleko.cena)
print(syr.popis)
