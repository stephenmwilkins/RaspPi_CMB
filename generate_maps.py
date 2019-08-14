

import healpy as hp
import numpy as np
from matplotlib import pyplot as plt


# --- generate Planck CMB colormap
from matplotlib.colors import ListedColormap
colombi1_cmap = ListedColormap(np.loadtxt("Planck_Parchment_RGB.txt")/255.)
colombi1_cmap.set_bad("white") # color of missing pixels
colombi1_cmap.set_under("white") # color of background, necessary if you want to use
cmap = colombi1_cmap





def plot_map(totCl, FileName = False, view = 'Mollweide'):

    np.random.seed(42)

    l = np.arange(len(totCl)) + 1

    totCl_raw = totCl * 2*np.pi / (l*(l+1))

    # --- create healpix map
    map = hp.synfast(totCl_raw,nside=2048)

    if view == 'Mollweide':

        # --- Mollweide plot
        m = hp.mollview(map, return_projected_map = True, cmap = cmap)
        
        dpi = 600
        figsize_inch = 6, 4
        fig = plt.figure(figsize=figsize_inch, dpi=dpi)
        ax = fig.add_axes([0,0,1,1])
        ax.imshow(m, cmap = cmap)
        ax.axis('off')
    
        if FileName:
            fig.savefig(FileName, dpi=dpi, bbox_inches="tight") # save
        else:
            plt.show()

        fig.clf()

    if view == 'Cartesian':
    
        # --- Cartesian view of a 20 deg2 region
    
        # hp.cartview(map=None, fig=None, rot=None, zat=None, coord=None, unit='', xsize=800, ysize=None, lonra=None, latra=None, title='Cartesian view', nest=False, remove_dip=False, remove_mono=False, gal_cut=0, min=None, max=None, flip='astro', format='%.3g', cbar=True, cmap=None, badcolor='gray', bgcolor='white', norm=None, aspect=None, hold=False, sub=None, margins=None, notext=False, return_projected_map=False)

        m = hp.cartview(map=map, xsize=300, lonra=[-5,5], latra=[-5,5], title=None, return_projected_map = True)
        plt.close()
        
        dpi = 150
        figsize_inch = 2, 2
        fig = plt.figure(figsize=figsize_inch, dpi=dpi)
        ax = fig.add_axes([0,0,1,1])
        ax.imshow(m, cmap = cmap, vmin = -500, vmax = 500)
        ax.axis('off')
    
        if FileName:
            fig.savefig(FileName, dpi=dpi) # save
        else:
            plt.show()
            
        fig.clf()


Planck15_totCl = np.load('Cls/Planck15.npy') # --- read in Planck Cls

plot_map(Planck15_totCl, FileName = 'maps/Planck15.png', view = 'Cartesian')



for Ob0 in np.arange(0.02, 1.01, 0.02):

    for Ocdm0 in np.arange(0.02, 1.01, 0.02):
    
        print('{0:.2f} {1:.2f}'.format(Ob0, Ocdm0))

        # --- save as numpy array

        try:

            totCl = np.load('Cls/flat/{0:.2f}_{1:.2f}.npy'.format(Ob0, Ocdm0))
            plot_map(totCl, FileName = 'maps/flat/{0:.2f}_{1:.2f}.png'.format(Ob0, Ocdm0), view = 'Cartesian')
    
        except:
    
            print('Could not find Cls')





