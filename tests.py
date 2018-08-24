from uchu.models.SBModel import *
from uchu.models.Galaxy import Galaxy
from uchu.simulation.single_sim import *
from matplotlib import pyplot as plt


galaxy = Galaxy(hlr=150, I_e=100, n=1.5, r_b=3, I_b=20, ipls=2.5, opls=0.7, alpha=1.3)
model = sersic_profile

models = []
for x in range(1, 6):
    galaxy.n = x / 2
    models.append(full_galaxy_plot(galaxy, model, 500))

fig, ax = plt.subplots(1, 5)
for x in range(0, 5):
    ax[x].imshow(models[x])
    readout = "n= " + str((x + 1) / 2) + "\nr_eff= " + str(galaxy.get_params()["hlr"]) + "\nI_eff= " + str(galaxy.get_params()["I_e"])
    ax[x].text(20, 100, readout, color='white')
    ax[x].set_xticks([])
    ax[x].set_yticks([])
plt.show()
