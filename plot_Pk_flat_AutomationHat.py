

import automationhat as a
import numpy as np
import plot_Pk_flat


# --- this should check to see if the button is pressed and if so regenerate the plot.
# --- actually we could just check for a noticeable change (\delta Ocmd0 > 0.02) in analog.one, analog.two and use that as our prompt 



def read_parameters():

    Ob0 = a.analog.one.read()/3.3 
    Ocdm0 = a.analog.two.read()/3.3 

    plot_Pk_flat.plot_Pk(Ob0, Ocdm0)


while True:

    # --- check to see if button pressed