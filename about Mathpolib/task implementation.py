import random
import matplotlib.pyplot as plt
import numpy as np
import math

fig = plt.figure(figsize=(5, 5))

ax_1 = fig.add_subplot(3, 1, 1)
x = np.linspace(0, 15, 20)
y1 = x
y2 = []
for i in x:
    if i == 0:
        y2.append(0)  # не можна брати логарифм від нуля
    else:
        a = math.log(i, 10)
        y2.append(a)
ax_1.plot(x, y1, linestyle='-', color='crimson', linewidth=1)
ax_1.scatter(x, y2, color='crimson', marker='o', linewidth=5)
ax_1.set_title('Графік залежності у від х')
ax_1.set_xlabel('X')
ax_1.set_ylabel('Y')
ax_1.grid(True)
ax_1.set_facecolor('BlanchedAlmond')

ax_2 = fig.add_subplot(3, 1, 2)
x = np.arange(2, 9)
y = np.random.randint(2, 20, size=7)
y_error = np.random.rand(7)
ax_2.bar(x, y, color='crimson', yerr=y_error, width=0.2)
ax_2.set_title('Графік залежності у від х')
ax_2.set_xlabel('X')
ax_2.set_ylabel('Y')
ax_2.grid(True)
ax_2.set_facecolor('BlanchedAlmond')

ax_3 = fig.add_subplot(3, 1, 3)
values = []
for i in range(0, 6):
    values.append(random.randint(2, 20))
Num = []
a = 1
for x in range(0, 6):
    Num.append(a)
    a += 1
    pass
ax_3.pie(values, labels=Num, autopct='%1.1f%%',
         shadow=True, startangle=90)
ax_3.axis('equal')

plt.show()
