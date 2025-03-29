from math import pi, exp
import matplotlib.pyplot as plt
import pandas as pd


L = 2 # длина цилиндра
D = 0.4 # диаметр цилиндра
S = pi * D * L + pi * D ** 2 / 4 * 2 # площадь цилиндра
V = pi * D ** 2 / 4 * L # объем цилиндра

h_tc = 10 # коэффициент теплоотдачи
c_p = 920 # изобарная теплоемкость
dens = 2700 # плотность цилиндра
T_0 = 400 # температура в центре цилиндра
T_a = 20 # температура окружающей среды

N_tc = 10
dt = 10000 # шаг по времени
with open("Al_dt10000_2nd.dat", "w", encoding='utf-8') as f:
    f.write(f"{0} {T_0} {T_0}\n")
T = T_0
time = 0
for i in range(N_tc):
    #T -=  h_tc * (T - T_a) * S / V / dens / c_p * dt
    T_half = T - 0.5 * h_tc * (T - T_a) * S / V / dens / c_p * dt
    T -= h_tc * (T_half - T_a) * S / V / dens / c_p * dt
    time += dt
    T_exact = T_a + (T_0 - T_a) * exp(-h_tc * S * time / V / dens / c_p)
    with open("Al_dt10000_2nd.dat", "a", encoding='utf-8') as f:
        f.write(f"{time} {T} {T_exact}\n")

df_cylinder = pd.read_csv("Al_dt10000_2nd.dat", sep=' ', header=None, names=['time', 'T', 'T_exact'])
plt.figure(1)
plt.plot(df_cylinder['time'] / 3600, df_cylinder['T'], marker='o', label='Calculation')
plt.plot(df_cylinder['time'] / 3600, df_cylinder['T_exact'], marker='s', label='Exact')
plt.title('График зависимости Температуры от времени')
plt.xlabel('Время, ч')
plt.ylabel('Температура, 0_С')
plt.grid()
plt.legend()
plt.figure(2)
plt.plot(df_cylinder['time'] * h_tc * S / (c_p * dens * V), (df_cylinder['T'] - T_a) / (T_0 - T_a), marker='o', label='Calculation')
plt.plot(df_cylinder['time'] * h_tc * S / (c_p * dens * V), (df_cylinder['T_exact'] - T_a) / (T_0 - T_a), marker='s', label='Exact')
plt.title('График зависимости Температуры от времени')
plt.xlabel('Время, ч')
plt.ylabel('Температура, 0_С')
plt.grid()
plt.legend()
plt.show()