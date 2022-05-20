import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation
import mpl_toolkits.mplot3d.axes3d as p3


def f(x, y, t):
    return 0.5 * np.sin(x ** 3) + 0.25 * np.sin((y - t * 0.1) ** 2)


x = np.arange(-np.pi / 2, np.pi / 2, 0.1)
y = np.arange(0, np.pi * 1.5, 0.01)
fig, ax = plt.subplots(figsize=(10, 7))


def animate(frame):
    plt.clf()

    z = np.asarray([[f(xx, yy, frame) for xx in x] for yy in y])
    xx, yy = np.meshgrid(x, y)

    ax = p3.Axes3D(fig)
    ax.plot_surface(xx, yy, z, cmap="gist_ncar")


ani = matplotlib.animation.FuncAnimation(fig, animate, frames=80, interval=0.1, repeat=False)
plt.show()
