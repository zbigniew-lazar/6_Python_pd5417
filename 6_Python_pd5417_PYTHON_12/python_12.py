class NieprawidlowaSekwencjaDNA(Exception):
    pass


try:
    with open("sekwencje.txt", "r") as plik:
        sekwencja = plik.read()
        print("Odczytana sekwencja DNA:", sekwencja)

except FileNotFoundError:
    print("Błąd: plik sekwencje.txt nie istnieje.")


nowa_sekwencja = input("Podaj nową sekwencję DNA: ").upper()

dozwolone = {"A", "T", "C", "G"}

if not set(nowa_sekwencja).issubset(dozwolone):
    raise NieprawidlowaSekwencjaDNA(
        "Sekwencja może zawierać tylko A, T, C i G."
    )

with open("nowa_sekwencja.txt", "w") as plik:
    plik.write(nowa_sekwencja)

print("Sekwencja została zapisana do pliku nowa_sekwencja.txt")