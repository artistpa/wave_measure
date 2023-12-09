import matplotlib.pyplot as plt
import numpy as np
def file_open(name):
    with open(name, 'r') as file:
        data = []
        for f in file:
            data.append(float(f.split()[0]))
    return data
data_40 = 'C:/Users/Павел/Desktop/Прога/Water/Scripts/40measure.txt'
data_80 = 'C:/Users/Павел/Desktop/Прога/Water/Scripts/80measure.txt'
data_120 = 'C:/Users/Павел/Desktop/Прога/Water/Scripts/120measure.txt'


mm40 = file_open(data_40)
mm80 = file_open(data_80)
mm120 = file_open(data_120)
print(len(mm40))
print(len(mm80))
print(len(mm120))

x = np.linspace(0,10,38)
y = [-84.2 * mm120[i] + 192.4 for i in range(38)]

# Построим графики, указав названия
plt.plot(x, y, 'b', label='Уровень воды в кювете')
plt.text(0.01,11,'L = 1.4 м; t = 0.5 c; V = 2.8 м/с')
# Подпишем оси
plt.ylabel('Уровень воды [мм]')
plt.xlabel('Время [с]')
# И график целиком
plt.title("Уровень воды в кювете после открытия торцевой двери (120 mm)")
plt.minorticks_on()
# включаем основную сетку
plt.grid(which='major')
# включаем дополнительную сетку
plt.grid(which='minor', linestyle=':')
plt.tight_layout()
plt.xlim([0,4.5])
plt.ylim([-0.1,105])
plt.legend()
plt.show()
