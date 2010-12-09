#
#	Script for plotting vector fields in gnuplot
#
#
#########################################
import string
import os
#import Numeric as N
from pylab import *
from numpy import ma
import matplotlib.pyplot as plt
import numpy as np
import array
import scipy
#d:\Temp\POY\2\SP\node_0 
rootdir ="f:/data/Bank/Constant Speed 001/RESULTS_MPI4-50ms/IM"
outdir = rootdir 
maindir = rootdir + "/IMAGE.npz" 
N = 1 #number of nodes
from scipy.io.numpyio import fwrite, fread
#/////////////////////////
Xsize = 13201
Zsize = 1921
vmodel = fread (open('f:/data/BP2004/modelq.bin','rb'),Xsize*Zsize,'f').reshape ((13201,1921)).transpose()
partmod = vmodel[::1,0:2600:1]
partmod = partmod - scipy.ndimage.filters.gaussian_filter(partmod,2)
partmod = np.abs (np.clip (partmod*0.001,-1.,1.))
modrgba = np.zeros ((partmod.shape[0],partmod.shape[1],4),dtype = 'f')
modrgba[:,:,0] = partmod
modrgba[:,:,3] = 1.



Image = np.load("%s"%maindir, mmap_mode='r')['arr_0.npy']
#SNorm = np.load("%s/s_norm.npz"%rootdir, mmap_mode='r')['arr_0.npy']
#sigma =3
#blurred = scipy.ndimage.filters.gaussian_filter(Image,sigma)
#
#filtered = Image - blurred
#
#filtered = np.clip(Image*3,-1,1)

part = np.abs(Image[::1,0:2600:1])#/SNorm[::1,0:2600:1]
part = np.clip (part*1000,0.,1.)

modrgba [:,:,1]  = part
fig = plt.figure(figsize=(8, 6),facecolor='w')
fig.subplots_adjust(top = 1,wspace = 0.12,hspace = 0.2,left = 0.05, right = 0.96)
fig.clear()
ax = fig.add_subplot(111)
ax.clear()
#cax = ax.imshow(part, interpolation='lanczos',cmap='gray')
#axis('off')
#ax = fig.add_subplot(111)
cax = ax.imshow(modrgba, interpolation='lanczos')
axis('off')
#cb = colorbar(cax,orientation='horizontal',format ='%.3f',pad=0.01)
#imaxes = gca()
#axes(cb.ax)
#xticks(fontsize=10)
#axes(imaxes)

filename = outdir + '/img.png'
plt.savefig(filename, dpi=200)
    
#np.savez ("%s\\image_flitered.npz"%outdir,filtered)
