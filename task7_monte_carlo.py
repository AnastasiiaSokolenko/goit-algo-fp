import random
import matplotlib.pyplot as plt
import pandas as pd

# Теоретичні ймовірності сум при киданні двох кубиків
probabilities_theoretical = {
    2: 1/36,  3: 2/36,  4: 3/36,  5: 4/36,  6: 5/36,
    7: 6/36,  8: 5/36,  9: 4/36, 10: 3/36, 11: 2/36, 12: 1/36
}
def simulate_dice_rolls(num_rolls):
    # Лічильник сум
    counts = {s: 0 for s in range(2, 13)}
    
    # Симуляція кидків
    for _ in range(num_rolls):
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        s = dice1 + dice2
        counts[s] += 1
    
    # Обрахування ймовірності випаду кожної суми
    probabilities = {s: counts[s] / num_rolls for s in counts}
    
    return probabilities


def plot_probabilities(probabilities, accuracy=10000):
    sums = list(probabilities.keys())
    probs = list(probabilities.values())
    
    # Створення графіка
    plt.bar(sums, probs, tick_label=sums)
    plt.xlabel('Сума чисел на кубиках')
    plt.ylabel('Ймовірність')
    plt.title('Ймовірність суми чисел на двох кубиках (симуляція - {} кидків)'.format(accuracy))
    
    # Додавання відсотків випадання на графік
    for i, prob in enumerate(probs):
        plt.text(sums[i], prob, f"{prob*100:.2f}%", ha='center', va='bottom')
    
    plt.show()


if __name__ == "__main__":
    for accuracy in [100, 1000, 10_000, 100_000, 1_000_000]:
        print(f"\nSimulating {accuracy} rolls:")
        probabilities = simulate_dice_rolls(accuracy)
        for s, p in probabilities.items():
            print(f"Sum {s}: {p:.4f}")
        
        plot_probabilities(probabilities, accuracy)

        # --- Додатковий порівняльний графік для 1 000 000 кидків ---
        if accuracy == 1_000_000:
            sums = sorted(probabilities.keys())
            probs_mc = [probabilities[s] for s in sums]
            probs_theoretical = [probabilities_theoretical[s] for s in sums]

            plt.bar([s - 0.2 for s in sums], probs_mc, width=0.4, label="Монте-Карло")
            plt.bar([s + 0.2 for s in sums], probs_theoretical, width=0.4, label="Теоретичнa")

            plt.xlabel("Сума на двох кубиках")
            plt.ylabel("Ймовірність")
            plt.title("Порівняння ймовірностей: Теоретичнa vs Монте-Карло (1 000 000)")
            plt.legend()
            plt.grid(True, axis="y", linestyle="--", alpha=0.7)
            plt.show()