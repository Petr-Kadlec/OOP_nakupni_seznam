class Produkt:
    def __init__(self, nazev, cena):
        self.nazev = nazev
        self.cena = cena


chleba = Produkt("chleba", 45)
mleko = Produkt("mléko", 28)
syr = Produkt("sýr" , 89)

print(chleba.nazev)
print(chleba.cna)
print(mleko.cena)
print(f"{syr.nazev} stojí {syr.cena} Kč")