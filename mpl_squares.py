"""Строит простой график квадратов чисел от 0 до 10"""
import matplotlib.pyplot as plt


def squares():
    """Рассчитывает квадраты чисел."""
    index = -10
    square = []
    while index <=10:
        square.append(index * index)
        index += 1
    return square


def plt_settings():
    """Настройки отображения графика"""
    # Назначение заголовка диаграммы и меток осей
    plt.title("Квадраты чисел от 0 до 10", fontsize=18)
    plt.xlabel("Числа", fontsize=14)
    plt.ylabel("Квадраты чисел", fontsize=14)

    # Размер шрифта делений на осях
    plt.tick_params(axis="both", labelsize=14)


plt.plot(squares())
plt_settings()
plt.show()
