import pandas as pd
import matplotlib.pyplot as plt

# Projekt standardowy - analiza sekwencji DNA drożdży
# Dane dotyczą krótkich fragmentów sekwencji związanych m.in. z genami HXK/GLK.

def wczytaj_fasta(nazwa_pliku):
    sekwencje = {}
    nazwa = ""
    sekwencja = ""

    try:
        plik = open(nazwa_pliku, "r", encoding="utf-8")

        for linia in plik:
            linia = linia.strip()

            if linia == "":
                continue

            if linia.startswith(">"):
                if nazwa != "":
                    sekwencje[nazwa] = sekwencja.upper()

                nazwa = linia.replace(">", "")
                sekwencja = ""
            else:
                sekwencja = sekwencja + linia

        if nazwa != "":
            sekwencje[nazwa] = sekwencja.upper()

        plik.close()

    except FileNotFoundError:
        print("Nie znaleziono pliku", nazwa_pliku)

    return sekwencje


def dodaj_sekwencje_uzytkownika(nazwa_pliku):
    print("\nMożesz dodać własną sekwencję DNA.")
    print("Jeżeli nie chcesz dodawać sekwencji, naciśnij ENTER.")

    nazwa = input("Podaj nazwę sekwencji: ")

    if nazwa == "":
        return "", ""

    sekwencja = input("Podaj sekwencję DNA: ").upper()

    if sekwencja == "":
        print("Nie podano sekwencji.")
        return "", ""

    nazwa = "user_" + nazwa

    plik = open(nazwa_pliku, "a", encoding="utf-8")
    plik.write("\n>" + nazwa + "\n")
    plik.write(sekwencja + "\n")
    plik.close()

    return nazwa, sekwencja


def czy_poprawna(sekwencja):
    dobre_litery = ["A", "T", "G", "C"]

    for znak in sekwencja:
        if znak not in dobre_litery:
            return False

    return True


def policz_gc(sekwencja):
    if len(sekwencja) == 0:
        return 0

    gc = sekwencja.count("G") + sekwencja.count("C")
    wynik = gc / len(sekwencja) * 100
    return round(wynik, 2)


def policz_at(sekwencja):
    if len(sekwencja) == 0:
        return 0

    at = sekwencja.count("A") + sekwencja.count("T")
    wynik = at / len(sekwencja) * 100
    return round(wynik, 2)


def licz_bledne_znaki(sekwencja):
    bledy = 0

    for znak in sekwencja:
        if znak not in ["A", "T", "G", "C"]:
            bledy = bledy + 1

    return bledy


def zrob_slownik_z_parametrami(sekwencje):
    dane = {}

    for nazwa, sekwencja in sekwencje.items():
        dane[nazwa] = {
            "nazwa": nazwa,
            "sekwencja": sekwencja,
            "dlugosc": len(sekwencja),
            "GC_percent": policz_gc(sekwencja),
            "AT_percent": policz_at(sekwencja),
            "A": sekwencja.count("A"),
            "T": sekwencja.count("T"),
            "G": sekwencja.count("G"),
            "C": sekwencja.count("C"),
            "bledne_znaki": licz_bledne_znaki(sekwencja),
            "czy_start_ATG": sekwencja.startswith("ATG"),
            "liczba_kodonow": len(sekwencja) // 3,
            "czy_poprawna": czy_poprawna(sekwencja)
        }

    return dane


def oczysc_dataframe(df):
    # usunięcie sekwencji z błędnymi literami
    df = df[df["czy_poprawna"] == True]

    # usunięcie duplikatów na podstawie identycznej sekwencji
    df = df.drop_duplicates(subset="sekwencja")

    return df


def zrob_wykresy(df):
    plt.figure()
    plt.hist(df["dlugosc"])
    plt.title("Długość sekwencji")
    plt.xlabel("Długość")
    plt.ylabel("Liczba sekwencji")
    plt.savefig("wykres_1_dlugosc.png")
    plt.close()

    plt.figure()
    plt.hist(df["GC_percent"])
    plt.title("Zawartość GC")
    plt.xlabel("GC [%]")
    plt.ylabel("Liczba sekwencji")
    plt.savefig("wykres_2_gc.png")
    plt.close()

    suma_A = df["A"].sum()
    suma_T = df["T"].sum()
    suma_G = df["G"].sum()
    suma_C = df["C"].sum()

    plt.figure()
    plt.bar(["A", "T", "G", "C"], [suma_A, suma_T, suma_G, suma_C])
    plt.title("Liczba nukleotydów")
    plt.xlabel("Nukleotyd")
    plt.ylabel("Liczba")
    plt.savefig("wykres_3_nukleotydy.png")
    plt.close()


def main():
    nazwa_pliku = "sekwencje.txt"

    sekwencje = wczytaj_fasta(nazwa_pliku)

    if len(sekwencje) == 0:
        print("Brak sekwencji do analizy.")
        return

    nazwa_user, sekwencja_user = dodaj_sekwencje_uzytkownika(nazwa_pliku)

    if nazwa_user != "":
        sekwencje[nazwa_user] = sekwencja_user

    slownik = zrob_slownik_z_parametrami(sekwencje)
    df = pd.DataFrame(slownik.values())

    print("\nDataFrame przed czyszczeniem:")
    print(df[["nazwa", "dlugosc", "GC_percent", "AT_percent", "bledne_znaki", "czy_start_ATG", "liczba_kodonow"]])

    df_czysty = oczysc_dataframe(df)

    print("\nDataFrame po usunięciu duplikatów i błędnych sekwencji:")
    print(df_czysty[["nazwa", "dlugosc", "GC_percent", "AT_percent", "A", "T", "G", "C", "czy_start_ATG", "liczba_kodonow"]])

    df.to_csv("wszystkie_sekwencje.csv", index=False)
    df_czysty.to_csv("oczyszczone_sekwencje.csv", index=False)

    zrob_wykresy(df_czysty)

    print("\nGotowe. Program zapisał pliki CSV oraz trzy wykresy.")


main()
