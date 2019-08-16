import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import os
from matplotlib import font_manager as fm, rcParams
import time
import automationhat as a
import numpy as np
import plot_Pk_flat
from PIL import Image

fpath = os.path.join('Dosis-Regular.ttf')
prop = fm.FontProperties(fname=fpath)
fname = os.path.split(fpath)[1]

# --- this should check to see if the button is pressed and if so regenerate the plot.
# --- actually we could just check for a noticeable change (\delta Ocmd0 > 0.02) in analog.one, analog.two and use that as our prompt 


plt.ion() #interative
def read_parameters(Ob0, Ocdm0, axCl, aximg):
    # Use code from plot_Pk_flat.py file to plot the power spectrum and CMB maps
    plot_Pk_flat.plot_Pk(Ob0, Ocdm0, axCl, aximg)
    #Label the power spectrum axis.
    axCl.set_ylabel(r'Anisotropy L(L +1)CL'.format(fname),fontproperties = prop, fontsize = 12)
    axCl.set_xlabel(r'Scale on Sky, L'.format(fname),fontproperties = prop, fontsize = 12)
    #pause the figure for 1 second
    plt.pause(1)
    #clear both map and power spectrum plots
    axCl.clear()#axis for power spectrum
    aximg.clear()# axis for CMB map
    
# make figure and axis for both power spectrum and cmb maps, this is to make thenm subplots to plot next to each other
fig = plt.figure()
axCl = fig.add_subplot(121)
aximg = fig.add_subplot(122)
#make the figures big screen. To come out of big screen, press Ctrl, Alt ans Delete and then kill python3. Make sure to stop running too!
mng = plt.get_current_fig_manager()
mng.full_screen_toggle()   
#tell the pi to read the parameters on the dial
Ob0_c = a.analog.one.read()/3.3 #normal matter
Ocdm0_c = a.analog.two.read()/3.3 #dark matter
read_parameters(Ob0_c, Ocdm0_c, axCl, aximg) # send them from function that plots the parameters

#make loop for chaning parameters
while True:

    # --- check to see if button pressed
    #read the knobs again for the next parameters
    Ob0 = a.analog.one.read()/3.3
    Ocdm0 = a.analog.two.read()/3.3
    #check how much the knob values have changed from previous
    delta_Ob0 = abs(Ob0_c - Ob0)
    delta_Ocdm0 = abs(Ocdm0_c - Ocdm0)
    #set the new parameters to the old one
    Ob0_c = Ob0
    Ocdm0_c = Ocdm0_c
    #check if the change is greater than 0.02, if so, plots new parameters, else plots with orignal one.
    if delta_Ob0 or delta_Ocdm0 >= 0.02:
        
        read_parameters(Ob0, Ocdm0, axCl, aximg)
   

    