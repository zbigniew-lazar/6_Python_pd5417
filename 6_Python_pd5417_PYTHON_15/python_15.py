import pandas as pd
import numpy as np

dane = {
    "Gen": ["GenA", "GenB", "GenC", "GenD"],
    "Proba1": [5.1, 2.3, np.nan, 4.4],
    "Proba2": [3.2, 4.5, 3.9, np.nan],
    "Proba3": [6.3, 5.6, np.nan, 6.6]
}

df = pd.DataFrame(dane)

print("Oryginalny DataFrame:")
print(df)

print("\nBrakujące wartości:")
print(df.isna())

df_bez_nan = df.dropna()
print("\nDataFrame po usunięciu wierszy z NaN:")
print(df_bez_nan)

df_uzupelniony = df.copy()
kolumny_prob = ["Proba1", "Proba2", "Proba3"]
df_uzupelniony[kolumny_prob] = df_uzupelniony[kolumny_prob].fillna(
    df_uzupelniony[kolumny_prob].mean()
)

print("\nDataFrame po uzupełnieniu NaN średnimi kolumn:")
print(df_uzupelniony)

gen_a = df[df["Gen"] == "GenA"]
print("\nDane dla GenA:")
print(gen_a)

srednie_prob = df[kolumny_prob].mean()
print("\nŚrednia ekspresja dla każdej próby:")
print(srednie_prob)

geny_proba1 = df[df["Proba1"] > 4]
print("\nGeny z ekspresją w próbie 1 większą niż 4:")
print(geny_proba1)

df_uzupelniony.to_csv("wynik.csv", index=False)

print("\nDataFrame zapisano do pliku wynik.csv")