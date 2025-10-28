import matplotlib.pyplot as plt
import sys

categories = input("Введите категории через пробел: ").split()
values = input("Введите значения через пробел: ").split()


values = [float(v.strip()) for v in values]
categories = [c.strip() for c in categories]

if len(categories) != len(values):
    sys.exit("Количество категорий не равно количеству значений")


# Создаём фигуру
plt.figure(figsize=(8, 4))
plt.barh(categories,values)
plt.xlabel("Значение")
plt.title("Горизонтальная столбчатая диаграмма (barh)")
plt.tight_layout()
plt.show()
