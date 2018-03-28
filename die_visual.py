from die import Die
import pygal

# Создание кубика
die = Die()

# Моделирование серии бросков с сохранением результатов в списке
results = []
for roll_num in range(1000):
    result = die.roll()
    results.append(result)

# Анализ результатов.
frequencies = []
for value in range(1, die.num_sides + 1):
    frequency = results.count(value)
    frequencies.append(frequency)

# Визуализация результатов.
hist = pygal.Bar()
hist.title = "Результаты броска одного шестигранного кубика 1000 раз."
hist.x_labels = ['1', '2', '3', '4', '5', '6']
hist.x_title = "Результат"
hist.y_title = "Частота выпадения"
hist.add('D6', frequencies)
hist.render_to_file('die_visual.svg')
