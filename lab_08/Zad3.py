from numpy import ndarray, sin, pi, linspace, meshgrid, c_
from matplotlib.pyplot import subplots, show
from mpl_toolkits.mplot3d.axes3d import Axes3D


def f(x: ndarray, y: ndarray) -> ndarray:
    return 0.5 * sin(x ** 3) + 0.25 * sin((y + pi) ** 2)


n = 100
x = linspace(-pi / 2, pi / 2, n)
y = linspace(-pi, pi / 2, n)

xx, yy = meshgrid(x, y)
mesh = c_[xx.ravel(), yy.ravel()]
z = f(
    x=mesh[:, 0],
    y=mesh[:, 1]
).reshape(xx.shape)

fig, _ = subplots(figsize=(10, 7))

ax = Axes3D(fig)
ax.plot_surface(xx, yy, z, cmap="gist_ncar")

show()
