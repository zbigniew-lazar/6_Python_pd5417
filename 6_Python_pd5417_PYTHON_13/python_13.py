import os
from datetime import datetime
from biologia import opis_komorki, licz_nukleotydy

# wyświetlenie opisu komórki
print(opis_komorki())

# przykładowa sekwencja DNA
dna = "AGCTTAGCTAAGGCT"

# zliczanie nukleotydów
wynik = licz_nukleotydy(dna)

# utworzenie katalogu
folder = "dane_bio"
os.makedirs(folder, exist_ok=True)

# ścieżka do pliku
plik = os.path.join(folder, "nukleotydy.txt")

# aktualna data i czas
teraz = datetime.now()

# zapis do pliku
with open(plik, "w", encoding="utf-8") as f:
    f.write("Liczba nukleotydów:\n")

    for nukleotyd, liczba in wynik.items():
        f.write(f"{nukleotyd}: {liczba}\n")

    f.write(f"\nData utworzenia: {teraz}\n")

print("Wyniki zapisano do:", plik)