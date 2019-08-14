

import numpy as np
import camb
from camb import model, initialpower



H0 = 67.4
h = H0/100.


ombh2 = 0.022
omch2 = 0.120

pars = camb.CAMBparams()
pars.set_cosmology(H0=H0, ombh2=ombh2, omch2=omch2, mnu=0.06, omk=0, tau=0.06)
pars.InitPower.set_params(As=2e-9, ns=0.965, r=0)
pars.set_for_lmax(2000, lens_potential_accuracy=0)
results = camb.get_results(pars)

# --- calculate power spectrum and plot it using the standard units

powers = results.get_cmb_power_spectra(pars, spectra = ['total'], CMB_unit='muK', raw_cl=False)
totCl = powers['total'][:, 0]

# --- save as numpy array

FileName = 'data/Planck15.npy'
np.save(FileName, totCl) 


