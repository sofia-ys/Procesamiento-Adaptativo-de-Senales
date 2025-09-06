import h5py
import matplotlib.pyplot as plt

# esta pagina te permite ver el contenido de los archivos: myhdf5.hdfgroup.org/

h1 = h5py.File("H-H1_GWOSC_4KHZ_R1-1126257415-4096.hdf5", "r")
l1 = h5py.File("L-L1_GWOSC_4KHZ_R1-1126257415-4096.hdf5", "r")
# los archivos estan organizados como un Python dictionary
# los datos estan guardados en "strain" --> "Strain"

strainH1 = h1["strain"]["Strain"][()]
strainL1 = l1["strain"]["Strain"][()]
sampleRate = 4096  # [Hz]

# para ver la forma de los datos
# plt.plot(strainH1)
# plt.plot(strainL1)
# plt.show()