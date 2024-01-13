from numpy import array, sin, cos, ndarray, radians
from matplotlib.pyplot import show, subplots, draw
from matplotlib.animation import FuncAnimation


matrix = array([
    [1, 1],
    [-1, 1],
    [-1, -1],
    [1, -1]
])


def rotate(mat: ndarray, k: float) -> ndarray:
    angle = k * radians(5)
    return mat @ array([
        [cos(angle), -sin(angle)],
        [sin(angle), cos(angle)]
    ])


def shear(mat: ndarray, k: float) -> ndarray:
    return mat @ array([
        [1 + k * 0.1, 0],
        [0, 1 + k * 0.1]
    ])


def stretch(mat: ndarray, k: float) -> ndarray:
    return mat @ array([
        [1, 0],
        [1 + k * 0.1, 1]
    ])


fig, axis = subplots(1, 3, figsize=(10, 7))


def animate(k: float) -> None:
    new_rotate_mat = rotate(matrix, k)
    new_shear_mat = shear(matrix, k)
    new_stretch_mat = stretch(matrix, k)

    titles = ('Rotate', 'Scale', 'Skew')

    for ax, mat, title in zip(axis, (new_rotate_mat, new_shear_mat, new_stretch_mat), titles):
        ax.clear()
        ax.fill(mat[:, 0], mat[:, 1])
        ax.set_title(title)
        ax.set_xlim(-10, 10)
        ax.set_ylim(-10, 10)

    draw()


anim = FuncAnimation(fig, animate, frames=40, interval=0.1, repeat=False)
show()
