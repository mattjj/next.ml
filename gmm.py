from __future__ import division
import numpy as np
from pybasicbayes import models, distributions

data = np.loadtxt('data.txt')

alpha_0 = 3.
obs_hypparams = dict(
    mu_0=np.zeros(2),sigma_0=np.eye(2),
    kappa_0=0.05,nu_0=5)

model = models.Mixture(
    alpha_0=alpha_0,
    components=[distributions.Gaussian(**obs_hypparams)
                for _ in range(10)]
)

model.add_data(data)

for _ in xrange(100):
    model.resample_model()





# import itertools, sys, json
# for i in itertools.count():
#     model.resample_model()
#     if i % 3 == 0:
#         print json.dumps(model.to_json_dict())
#         sys.stdout.flush()

