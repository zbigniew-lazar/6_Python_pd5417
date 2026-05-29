import numpy as np
import matplotlib.pyplot as plt

proby = ["Glukoza", "Glicerol", "Glukoza+Glicerol"]
geny = ["YlHXK1", "YlGLK1", "YlPFK1"]

ekspresja = np.array([
    [7.2, 3.1, 5.8],  # YlHXK1
    [4.5, 6.9, 5.2],  # YlGLK1
    [6.1, 4.8, 7.4]   # YlPFK1
])

# Wykres liniowy
plt.figure()
for i in range(len(geny)):
    plt.plot(proby, ekspresja[i], marker="o", label=geny[i])

plt.title("Zmiany ekspresji genów metabolizmu cukrów")
plt.xlabel("Warunek hodowli")
plt.ylabel("Poziom ekspresji")
plt.legend()
plt.savefig("ekspresja_genow.png")
plt.show()

# Wykres słupkowy
x = np.arange(len(proby))
szerokosc = 0.25

plt.figure()
for i in range(len(geny)):
    plt.bar(x + i * szerokosc, ekspresja[i], width=szerokosc, label=geny[i])

plt.title("Porównanie ekspresji genów w próbach")
plt.xlabel("Warunek hodowli")
plt.ylabel("Poziom ekspresji")
plt.xticks(x + szerokosc, proby)
plt.legend()
plt.show()

# Wykres rozrzutu
plt.figure()
plt.scatter(ekspresja[0], ekspresja[1])
plt.title("Porównanie ekspresji YlHXK1 i YlGLK1")
plt.xlabel("Ekspresja YlHXK1")
plt.ylabel("Ekspresja YlGLK1")
plt.show()