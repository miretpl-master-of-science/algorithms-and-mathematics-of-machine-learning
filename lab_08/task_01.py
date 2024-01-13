from numpy import sin, pi, ndarray, linspace, meshgrid, c_
from matplotlib.pyplot import contourf, contour, show


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

contourf(xx, yy, z, levels=10)
contour(xx, yy, z, levels=10, colors='black')
show()
