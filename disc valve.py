from math import exp, log, e, sqrt


f_max = 23 # максимальная площадь проходного сечения клапана, cм^2
H = 80 # максимальное положение шиберной задвижки, мм^2
f_min = 0.02 * f_max # поправка для логарифмической функции
f_max = f_max / 2 * 100
f_min = f_min / 2 * 100


def fff(x):
    c = log(f_max / f_min, e) / H
    return f_min * exp(c * x)


def ravn():
    n = 250
    dx = H / n
    x = []
    f = []
    for i in range(n + 1):
        x.append(i * dx)
        f.append(fff(x[i]))
    df = []
    for i in range(n):
        df.append(f[i + 1] - f[i])
    s = 0
    y = [0]
    y_00 = f_min / H
    for i in range(1, n + 1):
        y.append(df[i - 1] / dx + y_00)
        s += dx * y[i]
    a = sqrt(y[n] ** 2 + x[n] ** 2)
    r = a * a / x[n] / 2
    with open("ravn1.txt", "w", encoding='utf-8') as f:
        for i in range(n + 1):
            f.write(f"{x[i]}    {y[i]}\n")
    with open("ravn2.txt", "w", encoding='utf-8') as f:  # Вручную нужно добавлять символ переноса строки, чтобы разделить файл на строки
        for i in range(1, n + 1):
            f.write(f"{x[i]}    {-y[i]}\n")
    print((s * 10 ** -2) * 2)
    print(r)


ravn()


    #print(x[i], y[i], 0, sep="\t")
    #
