import numpy as np
import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y1 = [2, 3, 5, 7, 11]  # Первая зависимость
y2 = [1, 4, 6, 8, 10]  # Вторая зависимость

# Создание первого графика в отдельном окне
plt.figure(1)  # Создаем первое окно
plt.plot(x, y1, marker='o', label='Зависимость 1 (y1)', color='blue')
plt.title('График 1: Зависимость 1')
plt.xlabel('x')
plt.ylabel('y1')
plt.grid()
plt.legend()

# Создание второго графика в отдельном окне
plt.figure(2)  # Создаем второе окно
plt.plot(x, y2, marker='s', label='Зависимость 2 (y2)', color='orange')
plt.title('График 2: Зависимость 2')
plt.xlabel('x')
plt.ylabel('y2')
plt.grid()
plt.legend()

# Показать графики
plt.show()