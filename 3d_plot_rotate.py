"""."""

from PIL import Image

import matplotlib.animation as animation

import matplotlib.pyplot as plt

import mpl_toolkits.mplot3d.axes3D as p3


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


pil_img = open_pil_image('../../seekhue/test_imgs/cassatt_1.jpg')
pil_img.show()

fig = plt.figure()
ax = p3.Axes3D(fig)
