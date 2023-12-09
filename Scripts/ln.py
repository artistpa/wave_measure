import matplotlib.pyplot as plt
import numpy as np

x = [np.log(0.04), np.log(0.08), np.log(0.12)]
y = [np.log(1.9), np.log(2.59), np.log(2.8)]
a = np.polyfit(x, y, 1, rcond=None, full=False, w=None, cov=False)
print(a)
x = np.linspace(-5,5,1000)
y = [a[0] * x[i] + a[1] for i in range(1000)]

# Построим графики, указав названия
plt.plot(x, y, 'b', label='V = 0.4 * h  + 1.8')
plt.plot(np.log(0.04), np.log(1.9),'ro', label='Измерения')
plt.plot(np.log(0.08), np.log(2.59),'ro')
plt.plot(np.log(0.12),  np.log(2.8),'ro')
# Подпишем оси
plt.ylabel('Логарифм скорости')
plt.xlabel('Логарифм начальной глубины')
# И график целиком
plt.title("Зависимость логарифма скорости распространения волны от логарифма начальной глубины жидкости в кювете")
plt.minorticks_on()
# включаем основную сетку
plt.grid(which='major')
# включаем дополнительную сетку
plt.grid(which='minor', linestyle=':')
plt.tight_layout()
plt.legend()
plt.show()