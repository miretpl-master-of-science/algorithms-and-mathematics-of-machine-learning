import matplotlib.pyplot as plt
import matplotlib.animation
import numpy as np


def f(x, y, t):
    return 0.5 * np.sin(x ** 3) + 0.25 * np.sin((y - t * 0.05) ** 2)


x = np.arange(-np.pi / 2, np.pi / 2, 0.1)
y = np.arange(0, np.pi * 1.5, 0.01)

fig, ax = plt.subplots(figsize=(10, 7))
ax.set_xlim(-np.pi / 2, np.pi / 2)
ax.set_ylim(0, np.pi * 1.5)


def animate(frame):
    plt.clf()

    z = [[f(xx, yy, frame) for xx in x] for yy in y]
    xx, yy = np.meshgrid(x, y)

    plt.contourf(xx, yy, z, levels=10)
    plt.contour(xx, yy, z, levels=10, colors='black')


ani = matplotlib.animation.FuncAnimation(fig, animate, frames=80, interval=0.1, repeat=False)
plt.show()
