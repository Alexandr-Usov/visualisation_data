from die import Die
import pygal

# Создание двух кубиков
die_1 = Die()
die_2 = Die()

# Моделирование серии бросков с сохранением результатов в списке
results = []
for roll_num in range(50000):
    result = die_1.roll()+die_2.roll()
    results.append(result)

# Анализ результатов.
frequencies = []
max_result = die_1.num_sides + die_2.num_sides
for value in range(2, max_result + 1):
    frequency = results.count(value)
    frequencies.append(frequency)

# Визуализация результатов.
hist = pygal.Bar()
hist.title = "Результаты броска одного шестигранного кубика 1000 раз."
hist.x_labels = list(range(2, max_result + 1))
hist.x_title = "Результат"
hist.y_title = "Частота выпадения"
hist.add('D6', frequencies)
hist.render_to_file('die_visual.svg')
