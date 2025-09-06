import numpy as np
import scipy as sp
import h5py

h1 = h5py.File("H-H1_GWOSC_4KHZ_R1-1126257415-4096.hdf5", "r")
l1 = h5py.File("L-L1_GWOSC_4KHZ_R1-1126257415-4096.hdf5", "r")
# los archivos estan organizados como un Python dictionary
# los keys son: ['meta', 'quality', 'strain']