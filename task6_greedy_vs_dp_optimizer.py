# Define the items with their cost and calorie value.
items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}


# --- Greedy approach ---
def greedy_algorithm(items, budget):
    """
    Selects items maximizing calories/cost ratio without exceeding budget.
    """
    # sort items by calories/cost ratio (descending)
    sorted_items = sorted(
        items.items(),
        key=lambda x: x[1]["calories"] / x[1]["cost"],
        reverse=True
    )

    total_calories = 0
    remaining_budget = budget
    chosen_items = []

    for name, details in sorted_items:
        if details["cost"] <= remaining_budget:
            chosen_items.append(name)
            total_calories += details["calories"]
            remaining_budget -= details["cost"]

    return total_calories, budget - remaining_budget, chosen_items


# --- Dynamic Programming approach ---
def dynamic_programming(items, budget):
    """
    Dynamic Programming solution to maximize calories.
    """
    item_names = list(items.keys())
    n = len(item_names)

    # DP table: (n+1) x (budget+1)
    dp_table = [[0 for _ in range(budget + 1)] for _ in range(n + 1)]

    # Fill table
    for i in range(1, n + 1):
        name = item_names[i - 1]
        cost = items[name]["cost"]
        calories = items[name]["calories"]

        for b in range(budget + 1):
            if cost <= b:
                dp_table[i][b] = max(dp_table[i - 1][b], calories + dp_table[i - 1][b - cost])
            else:
                dp_table[i][b] = dp_table[i - 1][b]

    # Backtrack to find chosen items
    chosen_items = []
    temp_budget = budget
    for i in range(n, 0, -1):
        if dp_table[i][temp_budget] != dp_table[i - 1][temp_budget]:
            name = item_names[i - 1]
            chosen_items.append(name)
            temp_budget -= items[name]["cost"]

    total_calories = dp_table[n][budget]
    spent = budget - temp_budget

    return total_calories, spent, chosen_items[::-1]


if __name__ == '__main__':
    budget = 100

    greedy_result = greedy_algorithm(items, budget)
    dp_result = dynamic_programming(items, budget)

    # Greedy results unpack
    greedy_cal, greedy_spent, greedy_items = greedy_result
    print("=== Greedy Algorithm ===")
    print(f"Budget: {budget}")
    print(f"Spent: {greedy_spent}")
    print(f"Total Calories: {greedy_cal}")
    print(f"Chosen items: {', '.join(greedy_items) if greedy_items else 'None'}")
    print()

    # Dynamic Programming results unpack
    dp_cal, dp_spent, dp_items = dp_result
    print("=== Dynamic Programming ===")
    print(f"Budget: {budget}")
    print(f"Spent: {dp_spent}")
    print(f"Total Calories: {dp_cal}")
    print(f"Chosen items: {', '.join(dp_items) if dp_items else 'None'}")

