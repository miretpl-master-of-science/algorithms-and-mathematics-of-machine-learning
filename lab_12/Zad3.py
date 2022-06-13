from numpy import array, sin, cos, ndarray, radians, c_, ones
from matplotlib.pyplot import show, subplots, draw
from matplotlib.animation import FuncAnimation


matrix = array([
    [1, 1],
    [-1, 1],
    [-1, -1],
    [1, -1]
])


def transform_matrix(mat: ndarray, k: float) -> ndarray:
    angle = k * radians(5)
    return mat @ array([
        [cos(angle), -sin(angle), 1 + k * 0.1],
        [sin(angle), cos(angle), 1 + k * 0.1],
        [0, 0, 1]
    ]).T


fig, ax = subplots(figsize=(10, 7))


def animate(k: float) -> None:
    new_mat = transform_matrix(c_[matrix, ones((matrix.shape[0], 1))], k)

    ax.clear()
    ax.fill(new_mat[:, 0], new_mat[:, 1])
    ax.set_title('Animacja')
    ax.set_xlim(-3, 10)
    ax.set_ylim(-3, 10)
    draw()


anim = FuncAnimation(fig, animate, frames=40, interval=0.1, repeat=False)
show()
