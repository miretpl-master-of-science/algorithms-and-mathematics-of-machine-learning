from numpy import load
from matplotlib.pyplot import subplots, xlabel, ylabel, scatter, show
from matplotlib.image import imread
from matplotlib.offsetbox import OffsetImage, AnnotationBbox


with open('dataset/animals.npz', 'rb') as f:
    animals = load(f)['animals']

weight, height = animals[:, 2].astype(float), animals[:, 3].astype(int)
images = [imread(path) for path in animals[:, 4]]

fig, ax = subplots(figsize=(10, 5))
xlabel('weight')
ylabel('height')
scat = scatter(weight, height)

for i, image in enumerate(images):
    box = OffsetImage(image, zoom=0.5)
    box.image.axes = ax
    ann = AnnotationBbox(
        offsetbox=box,
        xy=(weight[i], height[i]),
        boxcoords='offset points',
        pad=0.5,
        arrowprops={
            'arrowstyle': '->',
            'connectionstyle': 'angle,angleA=0,angleB=90,rad=3'
        }
    )

    ann.set_visible(False)
    ax.add_artist(ann)


def hover(event):
    if scat.contains(event)[0]:
        ind, = scat.contains(event)[1]["ind"]

        w, h = fig.get_size_inches() * fig.dpi
        ws = -1 * (event.x > w / 2) + (event.x <= w / 2)
        hs = -1 * (event.y > h / 2) + (event.y <= h / 2)

        ann.xybox = (120 * ws, -80 * hs)
        ann.set_visible(True)
        ann.xy = (weight[ind], height[ind])

        box.set_data(images[ind])
    else:
        ann.set_visible(False)

    fig.canvas.draw_idle()


fig.canvas.mpl_connect('motion_notify_event', hover)
show()
