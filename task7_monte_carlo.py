import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Кількість кидків
N = 1_000_000

# Імітація кидків двох кубиків
dice1 = np.random.randint(1, 7, N)
dice2 = np.random.randint(1, 7, N)
sums = dice1 + dice2

# Підрахунок кількості появ кожної суми
values, counts = np.unique(sums, return_counts=True)
probabilities_mc = counts / N

# Аналітичні ймовірності (теоретичні)
probabilities_theoretical = {
    2: 1/36,  3: 2/36,  4: 3/36,  5: 4/36,  6: 5/36,
    7: 6/36,  8: 5/36,  9: 4/36, 10: 3/36, 11: 2/36, 12: 1/36
}

# Створення таблиці для порівняння
df = pd.DataFrame({
    "Сума": values,
    "Ймовірність (Монте-Карло)": probabilities_mc,
    "Ймовірність (аналітична)": [probabilities_theoretical[v] for v in values]
})

print(df)

# Побудова графіка
plt.bar(df["Сума"] - 0.2, df["Ймовірність (Монте-Карло)"], width=0.4, label="Монте-Карло")
plt.bar(df["Сума"] + 0.2, df["Ймовірність (аналітична)"], width=0.4, label="Аналітична")
plt.xlabel("Сума на двох кубиках")
plt.ylabel("Ймовірність")
plt.title("Ймовірність сум при киданні двох кубиків")
plt.legend()
plt.grid(True, axis="y", linestyle="--", alpha=0.7)
plt.show()