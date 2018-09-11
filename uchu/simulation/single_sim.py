from uchu.models.SBModel import *
from uchu.plotting import galaxy_plot
import numpy as np
from matplotlib import pyplot as plt


def full_galaxy_plot(galaxy, model, size, noise=0):
    params = galaxy.get_params()
    base_image = np.zeros((size, size))
    print(base_image.shape)
    centre_pix = (int(size / 2), int(size / 2))
    for x in range(0, base_image.shape[0]):
        for y in range(0, base_image.shape[1]):
            base_image[x][y] = model(get_dist((x, y), centre_pix), galaxy.get_params())

    return base_image


def model_galaxy(model, params):
    return None


def get_dist(p1, p2, conversion=1):
    """ Returns the distance between pixels p1 and p2. Adjusts to a conversion scaling factor if needed. """
    return np.sqrt(((p2[0] - p1[0]) ** 2) + ((p2[1] - p1[1]) ** 2)) / conversion


def Model1D(galaxy, model, max_r=100, plot=False, rel_convert=False):
    params = galaxy.get_params()
    xs = []
    ys = []
    for r in range(0, max_r):
        xs.append(r)
        ys.append(model(r, params))
    if plot:
        galaxy_plot.plot_1D(xs, ys)
    if rel_convert:
        for ind in range(0, len(xs)):
            xs[ind] /= params["hlr"]
    return xs, ys

