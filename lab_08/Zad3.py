import numpy as np
import matplotlib.pyplot as plt


def f(x, y):
    return 0.5 * np.sin(x ** 3) + 0.25 * np.sin((y + np.pi) ** 2)


n = 100
x = np.linspace(-np.pi / 2, np.pi / 2, n)
y = np.linspace(-np.pi, np.pi / 2, n)

xx, yy = np.meshgrid(x, y)
mesh = np.c_[xx.ravel(), yy.ravel()]
z = f(mesh[:, 0], mesh[:, 1]).reshape(xx.shape)

ax = plt.axes(projection='3d')
ax.plot_surface(xx, yy, z, cmap="gist_ncar")
plt.show()
