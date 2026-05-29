import numpy as np

# Macierz ekspresji genów (4 geny x 3 próby)
macierz = np.array([
    [5.0, 2.5, 7.0],
    [3.2, 4.0, 6.0],
    [8.1, 9.3, 2.5],
    [4.5, 5.7, 6.9]
])

print("Oryginalna macierz:")
print(macierz)

# Zwiększenie ekspresji o 5%
macierz_plus_5 = macierz * 1.05

print("\nMacierz po zwiększeniu o 5%:")
print(macierz_plus_5)

# Średnia dla każdego genu (wiersze)
srednie_genow = np.mean(macierz, axis=1)

print("\nŚrednia ekspresja dla każdego genu:")
print(srednie_genow)

# Suma dla każdej próby (kolumny)
sumy_prob = np.sum(macierz, axis=0)

print("\nSuma ekspresji dla każdej próby:")
print(sumy_prob)

# Wprowadzenie brakujących danych
macierz_nan = macierz.copy()

macierz_nan[0, 1] = np.nan
macierz_nan[2, 2] = np.nan

print("\nMacierz z wartościami NaN:")
print(macierz_nan)

# Średnia ignorująca NaN
srednie_bez_nan = np.nanmean(macierz_nan, axis=1)

print("\nŚrednia ekspresja genów (ignorując NaN):")
print(srednie_bez_nan)