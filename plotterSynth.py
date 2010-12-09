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
#d:\Temp\POY\2\SP\node_0 
#indir = "f:/data/BP2004/R/"


indir = "f:/data/Bank/Constant Speed 001/RESULTS_MPI2/S/" 
#indir = '/mnt/portable/data/BP2004/temp/'
#indir = '/media/E21E5CAC1E5C7B8B/data/BP2004/temp/'
#outdir = '/mnt/portable/data/BP2004/temp/'
outdir = indir + "img/"
os.system ("mkdir -p %s"%outdir)
N = len(filter (lambda q: q.find('node_')!=-1 ,os.listdir(indir)) ) #number of nodes
#from scipy.io.numpyio import fwrite, fread
from numpyIO import fwrite, fread
Header = 9
#/////////////////////////
fileob = open(indir+"node_0", mode='rb')
binvalues = array.array('i')
#binvalues = np.array(dtype=integer)
binvalues.read(fileob, Header)
if Header == 9:
    tstart = binvalues[6]
    tend = binvalues[7]
    tstep = binvalues[8]
    fileobj=[]
    xstart=[]
    xend=[]
    zstart=[]
    zend=[]
    xstep=[]
    zstep=[]
    print N
    for i in range (0,N):
        fle = (indir+"node_%d"%i)
        fileobj.append(open(fle, mode='rb'))
        binvalues = array.array('i')
        binvalues.read(fileobj[i], 9)
        xstart.append(binvalues[0])
	xend.append(binvalues[1])
        xstep.append(binvalues[2])
        zstart.append(binvalues[3])
        zend.append(binvalues[4])
	zstep.append(binvalues[5])
        print binvalues

if Header == 13:
    tstart = binvalues[6+4]
    tend = binvalues[7+4]
    tstep = binvalues[8+4]
    fileobj=[]
    xstart=[]
    xend=[]
    zstart=[]
    zend=[]
    xstep=[]
    zstep=[]
    print N
    for i in range (0,N):
        fle = (indir+"node_%d"%i)
        fileobj.append(open(fle, mode='rb'))
        binvalues = array.array('i')
        binvalues.read(fileobj[i], 13)
        xstart.append(binvalues[0+4])
	xend.append(binvalues[1+4])
        xstep.append(binvalues[2+4])
        zstart.append(binvalues[3+4])
        zend.append(binvalues[4+4])
	zstep.append(binvalues[5+4])
        print binvalues







#exit()
Nt = tend/tstep+1
xsizes = []
zsizes = []
for i in range(0,N):
    xsizes.append((xend[i]-xstart[i])/xstep[i]+1)
    zsizes.append((zend[i]-zstart[i])/zstep[i]+1)

xsize = (max(xend)-min(xstart))/xstep[0] + 1
zsize = (max(zend)-min(zstart))/zstep[0] + 1

#print (xsize,zsize)

pres = np.zeros((zsize,xsize), dtype=float)
#pz = np.zeros((zsize,xsize), dtype=float)
#px = np.zeros((zsize,xsize), dtype=float)

#exit()
ion()
fig = plt.figure(figsize=(8, 6))
fig.subplots_adjust(top = 0.9,wspace = 0.12,hspace = 0.2,left = 0.05, right = 0.96)

#Xgr = range(0,xsize)
#Zgr = range(0,zsize)
Xgr,Zgr = np.mgrid[0:zsize,0:xsize]

#data = array.array('d')
#data.read(fileobj,65*xsize*zsize*3)

for i in range (1,Nt,1):
    for j in range (0,N):
        spsize = xsizes[j]*zsizes[j]
        shape = (xsizes[j],zsizes[j])

        fileobj[j].seek(Header*4 + 4*(i)*spsize)
        data = fread(fileobj[j],spsize,'f')
        data = data.reshape(shape).transpose()
        pres[zstart[j]/zstep[j]:zend[j]/zstep[j]+1,xstart[j]/xstep[j]:xend[j]/xstep[j]+1] = data
#        print pres[:,xstart[i]/xstep[i]:xend[i]/xstep[i]+1].shape
#        print data.shape        
#    outfile = open("%s\\data.dat"%(outdir),mode='w')
#    c=0

    print amax(pres)

    fig.clear()
    ax = fig.add_subplot(111)
    ax.clear()
    cax = ax.imshow(pres[:,:], interpolation='nearest')
    axis('off')
    cb = colorbar(cax,orientation='horizontal',format ='%.3f',pad=0.01)
    imaxes = gca()
    axes(cb.ax)
    xticks(fontsize=10)
    axes(imaxes)

#    Q = quiver(px,pz,scale=3)
#    K = 10
#    Q = quiver(Zgr[::K,::K],Xgr[::K,::K],px[::K,::K],pz[::K,::K],headwidth=1.5,headlength=2)
    filename = outdir +str('%04d' % i) + '.png'
    plt.savefig(filename, dpi=300)
    
    
#for j in range (0,N):
#    fileobj[j].close()
