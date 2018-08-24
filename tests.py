from uchu.models.SBModel import *
from uchu.models.Galaxy import Galaxy
from uchu.simulation.single_sim import *


galaxy = Galaxy(hlr=55, I_e=50, n=2, r_b=3, I_b=20, ipls=2.5, opls=0.7, alpha=1.3)
model = sersic_profile

full_galaxy_plot(galaxy, model, 500)
