"""
Gaussian Distribution with Outliers
-----------------------------------
This figure shows the distribution of points drawn from a narrow
Gaussian distribution, with 20% "outliers" drawn from a wider
Gaussian distribution.  Over-plotted are the robust and non-robust
estimators of the mean and standard deviation.
"""
# Author: Jake VanderPlas <vanderplas@astro.washington.edu>
# License: BSD
#   The figure produced by this code is published in the textbook
#   "Statistics, Data Mining, and Machine Learning in Astronomy" (2013)
#   For more information, see http://astroML.github.com

import numpy as np
from matplotlib import pyplot as plt
from scipy.stats import norm, anderson
from astroML.stats import mean_sigma, median_sigmaG

#------------------------------------------------------------
# Create distribution
Npts = 1E6
f_out = 0.2
N_out = int(f_out * Npts)

sigma1 = 1
sigma2 = 3

np.random.seed(1)
x = np.hstack((np.random.normal(0, sigma1, Npts - N_out),
               np.random.normal(0, sigma2, N_out)))

#------------------------------------------------------------
# Compute anderson-darling test
A2, sig, crit = anderson(x)
print "anderson-darling A^2 = %.1f" % A2

#------------------------------------------------------------
# Compute non-robust and robust point statistics
mu_sample, sig_sample = mean_sigma(x)
med_sample, sigG_sample = median_sigmaG(x)

#------------------------------------------------------------
# Plot the results
ax = plt.axes()

# histogram of data
ax.hist(x, 100, histtype='stepfilled', alpha=0.2,
        lw=1.5, color='k', normed=True)

# best-fit normal curves
x_sample = np.linspace(-15, 15, 1000)
ax.plot(x_sample, norm(mu_sample, sig_sample).pdf(x_sample), '-k', lw=1.5,
        label='$\sigma$ fit')
ax.plot(x_sample, norm(med_sample, sigG_sample).pdf(x_sample), '--k', lw=1.5,
        label='$\sigma_G$ fit')

ax.legend()

ax.set_xlim(-8, 8)
ax.set_xlabel('x')
ax.set_ylabel('p(x)')

plt.show()
