from uchu.models.SBModel import *
from uchu.plotting import *
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
    plt.imshow(base_image)
    readout = "n= " + str(params["n"]) + "\nr_eff= " + str(params["hlr"]) + "\nI_eff= " + str(params["I_e"])
    plt.text(20, 100, readout, color='white')
    plt.show()
def model_galaxy(model, params):
    return None

def get_dist(p1, p2, conversion=1):
    return np.sqrt(((p2[0] - p1[0]) ** 2) + ((p2[1] - p1[1]) ** 2)) / conversion

