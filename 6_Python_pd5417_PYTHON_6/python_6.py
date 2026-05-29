# Przykładowe fragmenty genu heksokinazy
sekwencja_1 = "ATGCGTAC"
sekwencja_2 = "GTTAGCAA"

# Połączenie dwóch sekwencji DNA
pelna_sekwencja = sekwencja_1 + sekwencja_2

# Wycięcie fragmentu sekwencji
fragment = pelna_sekwencja[3:10]

liczba_a = pelna_sekwencja.count("A")
pozycja_tac = pelna_sekwencja.find("TAC")
zamieniona = pelna_sekwencja.replace("A", "T")

print(f"Pełna sekwencja DNA:\n\t{pelna_sekwencja}")
print(f"Fragment sekwencji od indeksu 3 do 9:\n\t{fragment}")
print(f"Liczba nukleotydów A: {liczba_a}")
print(f"Pozycja motywu TAC: {pozycja_tac}")
print(f"Sekwencja po zamianie A na T:\n\t{zamieniona}")