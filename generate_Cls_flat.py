

import numpy as np
import camb
from camb import model, initialpower



H0 = 67.4
h = H0/100.


for Ob0 in np.arange(0.02, 1.01, 0.02):

    for Ocdm0 in np.arange(0.02, 1.01, 0.02):
    
        print('{0:.2f} {1:.2f}'.format(Ob0, Ocdm0))

        # --- Set up a new set of parameters for CAMB
        
        ombh2 = Ob0*h**2
        omch2 = Ocdm0*h**2
        pars = camb.CAMBparams()
        pars.set_cosmology(H0=H0, ombh2=ombh2, omch2=omch2, mnu=0.06, omk=0, tau=0.06)
        pars.InitPower.set_params(As=2e-9, ns=0.965, r=0)
        pars.set_for_lmax(2000, lens_potential_accuracy=0)
        results = camb.get_results(pars)

        # --- calculate power spectrum and plot it using the standard units

        powers = results.get_cmb_power_spectra(pars, spectra = ['total'], CMB_unit='muK', raw_cl=False)
        totCl = powers['total'][:, 0]

        # --- save as numpy array

        FileName = 'data/flat/{0:.2f}_{1:.2f}.npy'.format(Ob0, Ocdm0)
        np.save(FileName, totCl) 


