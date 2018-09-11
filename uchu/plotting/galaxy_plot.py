from matplotlib import pyplot as plt


def display_galaxy(galaxy_image, params=None):
    """
    Plots the image of a galaxy, along with optional information.
    :param galaxy_image:
    :param params:
    :return:
    """
    plt.imshow(galaxy_image)
    if params is not None:
        readout = "n= " + str(params["n"]) + "\nr_eff= " + str(params["hlr"]) + "\nI_eff= " + str(params["I_e"])
        plt.text(20, 100, readout, color='white')
    plt.xticks([])
    plt.yticks([])
    plt.show()


def plot_1D(xs, ys):
    """
    Plot a xs vs ys plot (for a 1-D galaxy model)
    :param xs:
    :param ys:
    :return:
    """
    plt.plot(xs, ys, color="black")
    plt.yscale('log')
    plt.show()
    return None