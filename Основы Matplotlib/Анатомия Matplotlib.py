import numpy as np
import matplotlib.pyplot as plt


X = np.linspace(0.5, 3.5, 100)
Y1 = 3 + np.cos(X)
Y2 = 1 + np.cos(1 + X / 0.75) / 2
Y3 = np.random.uniform(Y1, Y2, len(X))
fig = plt.figure(figsize=(12, 12))
ax = fig.add_subplot(1, 1, 1)
ax.plot(X, Y1, c="blue", lw=2, label="Первый сигнал")
ax.plot(X, Y2, c="red", lw=2, label="Второй сигнал")
ax.plot(X, Y3, c="black", lw=0, marker='o', markerfacecolor="yellow")
ax.set_title("Анатомия matplotlib", fontsize=20)
ax.set_xlabel("Подпись по X")
ax.set_ylabel("Подпись по Y")
ax.legend()
ax.text(3.65, 0.1, "Студент Калинин В.Н.",
        fontsize=10, ha="right", color='.5')
plt.show()
