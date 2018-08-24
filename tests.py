from uchu.models.SBModel import *
from uchu.models.Galaxy import Galaxy
from uchu.simulation.single_sim import *
from matplotlib import pyplot as plt


galaxy = Galaxy(hlr=30, I_e=30, n=0.7, sb_eff=23, r_b=3, I_b=10, ipls=0.20, opls=0.77, alpha=6.50, I_0=40)
model = core_sersic_profile

profiles = []
for n in range(1, 10):
    galaxy.n = n
    profiles.append(Model1D(galaxy, model, rel_convert=True))

full_galaxy_plot(galaxy, model, size=200)

# for x in profiles:
#     plt.plot(x[0], x[1], color="black")
#
# plt.yscale('log')
# plt.show()
