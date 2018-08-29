# 2D Galaxy Modelling

To generate galaxies with Uchu, you need to have two objects: A galaxy object with sufficient parameters and a valid model.

```
from uchu.models.SBModel import *
from uchu.models.Galaxy import Galaxy
from uchu.simulation.single_sim import *
from matplotlib import pyplot as plt

galaxy = Galaxy(hlr=30, I_e=30, n=0.7, sb_eff=23, r_b=3, I_b=10, ipls=0.20, opls=0.77, alpha=6.50, I_0=40)
model = nuker_sersic_profile

full_galaxy_plot(galaxy, model, size=200)
```


The models currently available include:
* sersic_intensity  : Basic Single_Sersic intensity model based on *Sersic (1968)*
* sersic_sb       : Single Sersic magnitude model based on *Sersic (1968) and Graham (2005)*
* nuker            : Core profile based on the nuker law, found in *Erwin et al. (2003)*
* core_sersic      : Combined Nuker and Sersic profile to model core and outer regions together. Trujillo (2004)

The galaxy settings in the example produce a standard galaxy with a low Sersic index. These values can be shifted and fine tuned. 
Please note that the model is not assigned with any curved brackets. Parameters are assigned in ```full_galaxy_plt()```.

It is also important to know that different models require different parameters. Sersic models only require iffective intensity, effective radius, and the Sersic index, whereas a core-seric model requires more.
