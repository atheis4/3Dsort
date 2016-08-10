"""."""

from PIL import Image

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


def create_and_show_scatter_plot(x, y, z, color_map):
    """."""
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(x, y, z, c=color_map, linewidth=0.0)
    ax.set_xlabel('red value 0-255')
    ax.set_ylabel('green value 0-255')
    ax.set_zlabel('blue value 0-255')
    plt.show()


def main():
    """."""
    source = '../../seekhue/test_imgs/cassatt_1.jpg'
    pil_img = open_pil_image(source)
    pil_img = resize_pil_image(pil_img)
    color_data_rgb = get_rgb_tuple(pil_img)
    x, y, z = return_xyz_from_rgb(color_data_rgb)
    color_map = create_cmap(color_data_rgb)
    create_and_show_scatter_plot(x, y, z, color_map)


if __name__ == '__main__':
    main()
