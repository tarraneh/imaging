import numpy as np
import matplotlib.pyplot as plt
from astropy.cosmology import Planck15
from all_functions import *
from astropy.coordinates import Distance
from astropy import units as u
from astropy.io import fits


'''Stacks and median combines a list of images.'''


image_list = ['file1.fits','file2.fits']
              
# Create array of all fits files
image_concat = []

for image in image_list:
    image_concat.append(fits.getdata(image))

# Stacked image
final_image = np.sum(image_concat,axis=0) 

#plt.imshow(final_image,origin='lower')
#plt.scatter(50,50,color='r',s=1)

# Median combine fits files
med_combine = np.median(image_concat,axis=0)
plt.figure(figsize=(10,8))
plt.imshow(med_combine)


# Compute statistics for image a la Peter
h, w = med_combine.shape
patchhalfsize = 25

p = med_combine[h//2 - patchhalfsize:h//2 + patchhalfsize,
         w//2 - patchhalfsize:w//2 + patchhalfsize]

mx = p.max ()
mn = p.min ()
med = np.median (p)
rms = np.sqrt ((p**2).mean ())

print(rms)

