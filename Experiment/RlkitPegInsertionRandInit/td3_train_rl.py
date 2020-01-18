from copy import deepcopy
from td3fd.rlkit_td3.params.peginholerandinit import params_config as base_params

params_config = deepcopy(base_params)
params_config["config"] = ("TD3",)
params_config["demo_strategy"] = "none"
params_config["seed"] = 0 # tuple(range(2))