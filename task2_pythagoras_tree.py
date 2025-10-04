import matplotlib.pyplot as plt
import numpy as np

def draw_branch(depth, x1=400, y1=50, length=100, angle=np.pi/2):
    """
    Recursively draws a fractal tree with given depth.

    depth (int): recursion depth (1 = trunk, 2 = trunk + 2 branches, etc.)
    x1, y1 (float): start coordinates of the branch
    length (float): branch length
    angle (float): branch angle in radians
    """
    if depth == 0:
        return

    # draw current branch
    x2 = x1 + length * np.cos(angle)
    y2 = y1 + length * np.sin(angle)
    plt.plot([x1, x2], [y1, y2], color="green", lw=1)

    # recursion for sub-branches
    new_length = length * 0.7
    delta = np.pi / 6
    draw_branch(depth-1, x2, y2, new_length, angle + delta)
    draw_branch(depth-1, x2, y2, new_length, angle - delta)


if __name__ == "__main__":
    while True:
        try:
            depth = int(input("Вкажіть рівень рекурсії (ціле число >0, 1 = лише стовбур, 2 = стовбур + 2 гілки, і т.д.): "))
            if depth > 0:
                break
            print("Будь ласка, введіть число більше 0.")
        except ValueError:
            print("Некоректне значення. Спробуйте ще раз.")

    plt.figure(figsize=(8, 8))
    plt.axis('off')
    plt.gca().set_aspect("equal")

    draw_branch(depth)
    plt.show()

