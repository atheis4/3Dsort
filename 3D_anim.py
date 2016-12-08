"""
3D_anim.py.

Takes an image file (.jpg or .png preferred)
returns an animated 3 dimensional scatterplot of the image's pixel values.
"""

import os

from PIL import Image

from matplotlib import animation
import matplotlib.pyplot as plt

from mpl_toolkits.mplot3d import Axes3D


def open_pil_image(source):
    """Take file location as source, return PIL image object."""
    return Image.open(source)


def resize_pil_image(pil_img):
    """Resize PIL image object.

    Input: PIL image object
    Output: PIL image object (resized)

    This f(x) first judges whether the image is landscape or portrait
    by finding the ratio between the width and height of the image.

    The largest dimension is then set to 135 pixels (for improved performance)
    and the smaller dimension is calculated based on the initial ratio of w/h.

    The returned pil image is resized to these new dimensions.
    """
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
    """Use Image object getdata() method to return flat list of RGB tuples.

    Input: PIL image object
    Output: (R, G, B) tuple for each pixel
    """
    return pil_img.getdata()


def return_xyz_from_rgb(pixel_data):
    """Create x, y, z positions for scatterplot.

    Input: list of RGB tuples
    Output: x, y, z lists
    """
    x = []
    y = []
    z = []
    for (r, g, b) in pixel_data:
        x.append(r)
        y.append(g)
        z.append(b)
    return x, y, z


def create_cmap(pixel_data):
    """Refactor RGB tuple data to create synced colormap."""
    return [(r/255.0, g/255.0, b/255.0) for (r, g, b) in pixel_data]


def init():
    """Scatterplot initialization function."""
    return ax.scatter(x, y, z, c=color_map, linewidth=0.0)


def animate(i):
    """Animation view initialization function."""
    return ax.view_init(elev=15, azim=i)


# path = '../PAM_proj/transform/'
#
# for filename in os.listdir(path):
#     source = path + filename

pil_img = open_pil_image('../PAM_proj/PAM_originals/monet_nympheas.jpg')
pil_img = resize_pil_image(pil_img)
color_data = get_rgb_tuple(pil_img)
x, y, z = return_xyz_from_rgb(color_data)
color_map = create_cmap(color_data)

fig = plt.figure()
ax = Axes3D(fig)
ax.set_xlabel('R values: 0 - 255')
ax.set_ylabel('G values: 0 - 255')
ax.set_zlabel('B values: 0 - 255')

anim = animation.FuncAnimation(
    fig, animate, init_func=init, frames=720, interval=20
)

anim.save('../PAM_proj/mp4s/monet_nympheas.mp4', fps=30, extra_args=['-vcodec', 'libx264'])
