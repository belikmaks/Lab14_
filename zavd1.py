import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 100)

y = -5 * np.cos(10 * x) * np.sin(3 * x) / np.sqrt(x)

plt.plot(x, y, label='Y(x)=-5*cos(10*x)*sin(3*x)/(x^(1/2))', color="red", linewidth=2)

plt.title('Графік заданої функції', fontsize=15)
plt.xlabel('x', fontsize=12, color='blue')
plt.ylabel('y', fontsize=12, color='blue')

plt.legend()
plt.grid(True)

plt.show()
