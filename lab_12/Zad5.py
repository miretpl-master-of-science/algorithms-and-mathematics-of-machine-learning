from numpy import array, sin, cos, ndarray, radians
from matplotlib.pyplot import show, subplots, draw
from matplotlib.animation import FuncAnimation
from mpl_toolkits.mplot3d.axes3d import Axes3D


matrix = array([
    [1, 1, 1],
    [1, -1, 1],
    [-1, -1, 1],
    [-1, 1, 1],
    [1, 1, 1],
    [1, 1, -1],
    [1, -1, -1],
    [1, -1, 1],
    [1, -1, -1],
    [-1, -1, -1],
    [-1, -1, 1],
    [-1, -1, -1],
    [-1, 1, -1],
    [-1, 1, 1],
    [-1, 1, -1],
    [1, 1, -1],
])


def transform_matrix(mat: ndarray, k: float) -> ndarray:
    angle = k * radians(5)
    return mat @ array([
        [cos(angle), -sin(angle), 0],
        [sin(angle), cos(angle), 0],
        [0, 0, 1]
    ]).T


fig, _ = subplots(figsize=(10, 7))


def animate(k: float) -> None:
    new_mat = transform_matrix(matrix, k)

    ax = Axes3D(fig, auto_add_to_figure=False)
    fig.add_axes(ax)
    ax.plot(new_mat[:, 0], new_mat[:, 1], new_mat[:, 2])
    ax.set_xlim3d(-5, 5)
    ax.set_ylim3d(-5, 5)
    ax.set_zlim3d(-5, 5)
    draw()


anim = FuncAnimation(fig, animate, frames=40, interval=0.1, repeat=False)
show()
