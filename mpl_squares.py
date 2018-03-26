"""Строит простой график квадратов чисел от 0 до 10"""
import matplotlib.pyplot as plt
input_values = [1, 2, 3, 4, 5]


def squares():
    """Рассчитывает квадраты чисел."""
    square = []
    for i in input_values:
        square.append(i * i)
    return square


def plt_settings():
    """Настройки отображения графика"""
    # Назначение заголовка диаграммы и меток осей
    plt.title("Квадраты чисел от 0 до 10", fontsize=18)
    plt.xlabel("Числа", fontsize=14)
    plt.ylabel("Квадраты чисел", fontsize=14)

    # Размер шрифта делений на осях
    plt.tick_params(axis="both", labelsize=14)


plt.plot(input_values, squares(), linewidth=5)
plt_settings()
plt.show()
