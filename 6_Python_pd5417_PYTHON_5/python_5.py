# Sekwencja fragmentu genu heksokinazy
sekwencja_dna = "ATGCGTACGTTAGC"

print("Sekwencja DNA:", sekwencja_dna)
print("Typ:", type(sekwencja_dna))

# Konwersja napisu na listę nukleotydów
sekwencja_dna = list(sekwencja_dna)

print("Po konwersji:", sekwencja_dna)
print("Typ:", type(sekwencja_dna))

# Użycie funkcji range()
for i in range(len(sekwencja_dna)):
    print(i, sekwencja_dna[i])