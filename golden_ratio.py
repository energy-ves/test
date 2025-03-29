def maximum(a:float | int, b:float | int) -> float:
    """
    Данная функция предназначена для определения точки
    максимума функция методом золотого сечения
    """
    a = a
    b = b
    prop = 1.618  # a___x_1___x_2___b
    while True:
        x_1 = b - (b - a) / prop
        x_2 = a + (b - a) / prop
        y_1 = f(x_1)
        y_2 = f(x_2)
        if y_1 <= y_2:
            a = x_1
        else:
            b = x_2
        if abs(b - a) < 0.001:
            break
    return (a + b) / 2


def minimum(a:float | int, b:float | int) -> float:
    """
    Данная функция предназначена для определения точки
    минимума функция методом золотого сечения
    """
    a = a
    b = b
    prop = 1.618  # a___x_1___x_2___b
    while True:
        x_1 = b - (b - a) / prop
        x_2 = a + (b - a) / prop
        y_1 = f(x_1)
        y_2 = f(x_2)
        if y_1 >= y_2:
            a = x_1
        else:
            b = x_2
        if abs(b - a) < 0.001:
            break
    return (a + b) / 2


def root(a: float | int, b: float | int) -> float:
    """
    Данная функция предназначена для определения
    корня функция методом половинного деления
    """
    a = a
    b = b
    x_1 = (a + b) / 2 # a___x_1___b
    f_1 = f(x_1)
    if f_1 == 0:
        return (a + b) / 2
    if f(a) < 0: # если функция возрастает
        while True:
            if f_1 < 0:
                a = x_1
            else:
                b = x_1
            x_1 = (a + b) / 2
            f_1 = f(x_1)
            if abs(b - a) < 0.001:
                break
        return (a + b) / 2
    if f(a) > 0: # если функция убывает
        while True:
            if f_1 > 0:
                a = x_1
            else:
                b = x_1
            x_1 = (a + b) / 2
            f_1 = f(x_1)
            if abs(b - a) < 0.001:
                break
        return (a + b) / 2


def f(x):
    """
    Функция для которой находится точка экстремума или корень
    """
    return -(x - 2) ** 2 + 1


print(maximum(1, 3))
print(root(2.7, 3.4))