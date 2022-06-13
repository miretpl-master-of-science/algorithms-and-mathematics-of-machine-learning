from numpy import ndarray, sin, arange, pi, meshgrid
from matplotlib.pyplot import subplots, clf, contourf, contour, show
from matplotlib.animation import FuncAnimation


def f(x: ndarray, y: ndarray, t: int) -> ndarray:
    return 0.5 * sin(x ** 3) + 0.25 * sin((y - t * 0.05) ** 2)


x = arange(-pi / 2, pi / 2, 0.1)
y = arange(0, pi * 1.5, 0.01)

fig, ax = subplots(figsize=(10, 7))
ax.set_xlim(-pi / 2, pi / 2)
ax.set_ylim(0, pi * 1.5)


def animate(frame: int) -> None:
    clf()

    z = [[f(x=xx, y=yy, t=frame) for xx in x] for yy in y]
    xx, yy = meshgrid(x, y)

    contourf(xx, yy, z, levels=10)
    contour(xx, yy, z, levels=10, colors='black')


anim = FuncAnimation(fig, animate, frames=100, interval=0.1, repeat=False)
show()
