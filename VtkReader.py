# -*- coding: utf-8 -*-
"""
Created on Fri Nov 19 11:57:07 2010

@author: VBaidin
"""

import vtk
import array
import numpy as np
DATA_ROOT = 'f:/data/Bank/Constant Speed 001/RESULTS_MPI4-50ms/IM'
reader = vtk.vtkXMLPImageDataReader()
reader.SetFileName(DATA_ROOT + "/image.pvti")
reader.Update()
#reader.SetFileName(DATA_ROOT + "/node_0_0.vti")
#darray = vtk.vtkDoubleArray()
#coords = [0,0,0]
#reader.GetOutput().GetArrayPointer(darray,coords)
D = reader.GetOutput().GetDimensions()
image = reader.GetOutput().GetPointData().GetArray ('IMAGE')
func = lambda i,j: image.GetTuple1(i+D[0]*j)

Img = np.zeros ((D[0],D[1]),dtype=float)
for i in xrange(D[0]):
    for j in xrange(D[1]):
        Img[i,j]=func(i,j)

np.savez ("%s/IMAGE.npz"%DATA_ROOT,Img)
