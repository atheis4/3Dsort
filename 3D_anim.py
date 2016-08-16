"""."""

from PIL import Image

from matplotlib import animation
import matplotlib.pyplot as plt

from mpl_toolkits.mplot3d import Axes3D


def open_pil_image(source):
    """Take file location as source, return PIL image object."""
    return Image.open(source)


def resize_pil_image(pil_img):
    """Resize PIL image object."""
    width, height = pil_img.size[0], pil_img.size[1]
    ratio = width / height
    if ratio > 1:
        width = 135
        height = int(width/ratio)
    else:
        height = 135
        width = int(height * ratio)
    return pil_img.resize((width, height))


def get_rgb_tuple(pil_img):
    """."""
    return pil_img.getdata()


def return_xyz_from_rgb(pixel_data):
    """."""
    x = []
    y = []
    z = []
    for (r, g, b) in pixel_data:
        x.append(r)
        y.append(g)
        z.append(b)
    return x, y, z


def create_cmap(pixel_data):
    """."""
    return [(r/255.0, g/255.0, b/255.0) for (r, g, b) in pixel_data]


pil_img = open_pil_image('../../seekhue/test_imgs/hopper_nighthawks.jpg')
pil_img = resize_pil_image(pil_img)
color_data = get_rgb_tuple(pil_img)
x, y, z = return_xyz_from_rgb(color_data)
color_map = create_cmap(color_data)

fig = plt.figure()
ax = Axes3D(fig)


def init():
    """."""
    return ax.scatter(x, y, z, c=color_map, linewidth=0.0)


def animate(i):
    """."""
    return ax.view_init(elev=15, azim=i)


anim = animation.FuncAnimation(
    fig, animate, init_func=init, frames=720, interval=20
)

anim.save('hopper_nighthawks-elev=15.mp4', fps=30, extra_args=['-vcodec', 'libx264'])
