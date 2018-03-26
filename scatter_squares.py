"""Наносит на диаграмму отдельные точки."""
import matplotlib.pyplot as plt


def plt_settings():
    # Назначение заголовка диаграммы и меток осей.
    plt.title("Square Numbers", fontsize=24)
    plt.xlabel("Value", fontsize=14)
    plt.ylabel("Square of Value", fontsize=14)

    # Назначение размера шрифта делений на осях
    plt.tick_params(axis="both", which="major", labelsize=14)

    # Назначение диапазона для каждой оси.
    plt.axes([-5100, 1100, 0, 1100000])


x_values = list(range(-500001, 500001))
y_values = [x**3 for x in x_values]

plt.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Reds,
            edgecolors="none", s=40)
plt_settings()
plt.show()
