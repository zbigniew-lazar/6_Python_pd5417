# Lista nukleotydów w przykładowej sekwencji DNA
nukleotydy = ["A", "T", "G", "C", "A", "T", "G", "G"]

# Krotka z pełnymi nazwami zasad azotowych
zasady_azotowe = ("Adenina", "Tymina", "Cytozyna", "Guanina")

print("Pierwszy element listy:", nukleotydy[0])
print("Ostatni element listy:", nukleotydy[-1])

print("Pierwszy element krotki:", zasady_azotowe[0])
print("Ostatni element krotki:", zasady_azotowe[-1])

# Modyfikacja elementu listy
nukleotydy[1] = "C"
print("Lista po modyfikacji:", nukleotydy)

# Dodanie nowego elementu na końcu listy
nukleotydy.append("A")
print("Lista po dodaniu elementu:", nukleotydy)

print("Elementy listy:")
for nukleotyd in nukleotydy:
    print(nukleotyd)

print("Elementy krotki:")
for zasada in zasady_azotowe:
    print(zasada)

# List comprehension
nukleotydy_male = [nukleotyd.lower() for nukleotyd in nukleotydy]
print("Nowa lista małymi literami:", nukleotydy_male)