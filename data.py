import numpy as np
from scipy.stats.qmc import Halton





# Sampling parameters from the space grid
parameter_space =   dict(spot=(0.8, 1.2),
                         path_integral=(0, 1.0),
                         ttm=(0.2, 1),
                         t=(0, 0.8)
                         vol=(0.1, 0.5),
                         r=(0, 0.1))
nb_samples = int(51e6)
sampler = Halton(d=6, scramble=True)
sample_params = sampler.random(n=nb_samples)
sample_params = np.array(
    [
        parameter_space["spot"][1] - parameter_space["spot"][0],
        parameter_space["path_integral"][1] - parameter_space["path_integral"][0],
        parameter_space["ttm"][1] - parameter_space["ttm"][0],
        parameter_space["t"][1] - parameter_space["t"][0],
        parameter_space["vol"][1] - parameter_space["vol"][0],
        parameter_space["r"][1] - parameter_space["r"][0]
]) * sample_params + np.array(
    [
        parameter_space["spot"][0],
        parameter_space["path_integral"][0],
        parameter_space["ttm"][0],
        parameter_space["t"][0],
        parameter_space["vol"][0],
        parameter_space["r"][0]
    ]
)

if __name__ == "main":
  
