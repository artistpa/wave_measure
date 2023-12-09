import matplotlib.pyplot as plt
import numpy as np
def file_open(name):
    with open(name, 'r') as file:
        data = []
        for f in file:
            data.append(float(f.split()[0]))
    return data
data_20 = 'C:/Users/Павел/Desktop/Прога/Water/Data/20.txt'
data_40 = 'C:/Users/Павел/Desktop/Прога/Water/Data/40.txt'
data_60 = 'C:/Users/Павел/Desktop/Прога/Water/Data/60.txt'
data_80 = 'C:/Users/Павел/Desktop/Прога/Water/Data/80.txt'
data_100 = 'C:/Users/Павел/Desktop/Прога/Water/Data/100.txt'
data_120 = 'C:/Users/Павел/Desktop/Прога/Water/Data/120.txt'

mm20 = file_open(data_20)
mm40 = file_open(data_40)
mm60 = file_open(data_60)
mm80 = file_open(data_80)
mm100 = file_open(data_100)
mm120 = file_open(data_120)


y=np.array([20, 40, 60, 80, 100, 120])
a1 = np.mean(mm120, axis = None)
a2 = np.mean(mm100, axis = None)
a3 = np.mean(mm80, axis = None)
a4 = np.mean(mm60, axis = None)
a5 = np.mean(mm40, axis = None)
a6 = np.mean(mm20, axis = None)
print(a1)
print(a2)
print(a3)
print(a4)
print(a5)
print(a6)

x = np.array([a6, a5, a4, a3, a2, a1])
a = np.polyfit(x, y, 1, rcond=None, full=False, w=None, cov=False)
x = np.linspace(0,10,1000)
y = [a[0] * x[i] + a[1] for i in range(1000)]
print(a)

# Построим графики, указав названия
plt.plot(y, x, 'b', label='h = 84.2 * N  - 52.4')
plt.plot(20, a1,'ro', label='Измерения')
plt.plot(40, a2,'ro')
plt.plot(60, a3,'ro')
plt.plot(80, a4,'ro')
plt.plot(100, a5,'ro')
plt.plot(120, a6, 'ro')
# Подпишем оси
plt.ylabel('Отсчёты АЦП')
plt.xlabel('Уровень воды [мм]')
# И график целиком
plt.title("Калибровочный график показаний АЦП от уровня воды")
plt.minorticks_on()
# включаем основную сетку
plt.grid(which='major')
# включаем дополнительную сетку
plt.grid(which='minor', linestyle=':')
plt.tight_layout()
plt.xlim([0,150])
plt.ylim([0,4])
plt.legend()
plt.show()
