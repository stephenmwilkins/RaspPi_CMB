

import numpy as np
import camb
from camb import model, initialpower
from astropy.cosmology import LambdaCDM

import time

H0 = 67.
h = H0/100.


t1 = time.time()


Ob0 = 0.05
Om0 = 0.25
Ode0 = 0.7

ombh2 = Ob0*h**2
omch2 = (Om0 - Ob0)*h**2
omk = LambdaCDM(H0, Om0, Ode0, Tcmb0=2.725, Neff=0).Ok0


t2 = time.time()

print(t2-t1)

#Set up a new set of parameters for CAMB
pars = camb.CAMBparams()
pars.set_cosmology(H0=H0, ombh2=ombh2, omch2=omch2, mnu=0.06, omk=0, tau=0.06)
pars.InitPower.set_params(As=2e-9, ns=0.965, r=0)
pars.set_for_lmax(1500, lens_potential_accuracy=0)

results = camb.get_results(pars)


# --- calculate power spectrum and plot it using the standard units

powers = results.get_cmb_power_spectra(pars, spectra = ['total'], CMB_unit='muK', raw_cl=False)
totCl = powers['total'][:, 0]

# np.save(totCl) 


t3 = time.time()

print(t3-t2)

from matplotlib import pyplot as plt

plt.plot(np.arange(len(totCl)),totCl, color='k')
plt.show()