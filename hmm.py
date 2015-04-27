from __future__ import division
import numpy as np
from matplotlib import pyplot as plt

import pyhsmm
from pyhsmm.util.text import progprint_xrange

plt.ion()
np.random.seed(0)

# load data
data = np.loadtxt('hmm-data.txt')[:1250]
data += 0.5*np.random.normal(size=data.shape)  # some extra noise

# set up the model
Nmax = 25
obs_dim = data.shape[1]
obs_hypparams = dict(
    mu_0=np.zeros(obs_dim), sigma_0=np.eye(obs_dim),
    kappa_0=0.25, nu_0=obs_dim+2)

obs_distns = \
    [pyhsmm.distributions.Gaussian(**obs_hypparams) for state in xrange(Nmax)]
model = pyhsmm.models.WeakLimitStickyHDPHMM(
    kappa=50.,alpha=6.,gamma=6.,init_state_concentration=1.,
    obs_distns=obs_distns)
model.add_data(data)


# run inference!
fig = model.make_figure()
model.plot(fig=fig,draw=False)

for _ in progprint_xrange(250):
    model.resample_model()
    model.plot(fig=fig,update=True)



# from moviepy.video.io.bindings import mplfig_to_npimage
# from moviepy.editor import VideoClip

# fig = model.make_figure()
# model.plot(fig=fig,draw=False)

# def make_frame_mpl(t):
#     model.resample_model()
#     model.plot(fig=fig,update=True,draw=False)
#     return mplfig_to_npimage(fig)

# animation = VideoClip(make_frame_mpl, duration=10)
# animation.write_videofile('gibbs.mp4',fps=40)

