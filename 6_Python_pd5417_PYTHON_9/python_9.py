# Zbiór genów
geny = {"HXK1", "BRCA1", "TP53"}

# Słownik: gen -> funkcja
funkcje_genow = {
    "HXK1": "heksokinaza",
    "BRCA1": "naprawa DNA",
    "TP53": "supresor nowotworowy"
}

# Dodanie nowego elementu
geny.add("EGFR")
funkcje_genow["EGFR"] = "receptor wzrostu"

# Sprawdzenie obecności elementów
print("Czy HXK1 jest w zbiorze?", "HXK1" in geny)
print("Czy BRCA1 jest w słowniku?", "BRCA1" in funkcje_genow)

# Usunięcie elementu ze zbioru
geny.remove("TP53")

print("\nZawartość słownika:")
for gen, funkcja in funkcje_genow.items():
    print(gen, "->", funkcja)

# Instrukcja if-else dla długości zbioru
if len(geny) > 3:
    print("\nZbiór zawiera więcej niż 3 elementy.")
else:
    print("\nZbiór zawiera 3 lub mniej elementów.")

# Sprawdzenie klucza w słowniku
if "HXK1" in funkcje_genow:
    print("Funkcja genu HXK1:", funkcje_genow["HXK1"])

# Łączenie zbiorów
geny_dodatkowe = {"MYC", "KRAS"}
wszystkie_geny = geny.union(geny_dodatkowe)

print("\nPołączony zbiór genów:")
print(wszystkie_geny)