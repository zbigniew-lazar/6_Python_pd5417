class Organizm:
    def __init__(self, nazwa, rodzaj):
        self.nazwa = nazwa
        self.rodzaj = rodzaj

    def opisz(self):
        return f"Organizm: {self.nazwa}, rodzaj: {self.rodzaj}"

    @staticmethod
    def transkrybuj(sekwencja_dna):
        return sekwencja_dna.replace("T", "U")


class Bakteria(Organizm):
    def __init__(self, nazwa, rodzaj, ksztalt):
        super().__init__(nazwa, rodzaj)
        self.ksztalt = ksztalt

    def opisz(self):
        return f"{super().opisz()}, kształt: {self.ksztalt}"


bakteria_1 = Bakteria("Escherichia coli", "Escherichia", "pałeczka")
bakteria_2 = Bakteria("Bacillus subtilis", "Bacillus", "laseczka")

print(bakteria_1.opisz())
print(bakteria_2.opisz())

sekwencja = "ATGCGTAC"
rna = Organizm.transkrybuj(sekwencja)

print("Sekwencja DNA:", sekwencja)
print("Sekwencja RNA:", rna)