def charakterystyka_bialka(*, sekwencja, masa, pI):
    return (
        f"Białko o sekwencji {sekwencja} "
        f"ma masę {masa} kDa oraz punkt izoelektryczny pI = {pI}."
    )


def sumuj_cechy_bialek(**kwargs):
    suma_mas = 0
    suma_pI = 0
    liczba_bialek = len(kwargs)

    for nazwa, cechy in kwargs.items():
        suma_mas += cechy["masa"]
        suma_pI += cechy["pI"]

    srednie_pI = suma_pI / liczba_bialek

    return suma_mas, srednie_pI


opis = charakterystyka_bialka(
    sekwencja="MSTNPKPQRK",
    masa=55.2,
    pI=6.8
)

print(opis)

suma_mas, srednie_pI = sumuj_cechy_bialek(
    HXK1={"masa": 55.2, "pI": 6.8},
    BRCA1={"masa": 220.5, "pI": 5.9},
    TP53={"masa": 43.7, "pI": 6.3}
)

print("Suma mas:", suma_mas)
print("Średnie pI:", srednie_pI)