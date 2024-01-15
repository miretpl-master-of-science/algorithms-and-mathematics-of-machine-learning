from numpy import ndarray, sin, arange, pi, asarray, meshgrid
from matplotlib.pyplot import subplots, clf, show
from mpl_toolkits.mplot3d.axes3d import Axes3D
from matplotlib.animation import FuncAnimation


def f(x: ndarray, y: ndarray, t: int) -> ndarray:
    return 0.5 * sin(x ** 3) + 0.25 * sin((y - t * 0.1) ** 2)


x = arange(-pi / 2, pi / 2, 0.1)
y = arange(0, pi * 1.5, 0.01)
fig, ax = subplots(figsize=(10, 7))


def animate(frame: int) -> None:
    clf()

    z = asarray([[f(x=xx, y=yy, t=frame) for xx in x] for yy in y])
    xx, yy = meshgrid(x, y)

    ax = Axes3D(fig)
    ax.plot_surface(xx, yy, z, cmap="gist_ncar")


anim = FuncAnimation(fig, animate, frames=100, interval=0.1, repeat=False)
show()
