import numpy as np
import scipy.stats as ss

import scipy.stats as ss
def structfunc(image,function = np.nanmean,p=2):
    yy,xx = np.indices(image.shape)
    ny = np.floor(image.shape[0]/2).astype(np.int)
    nx = np.floor(image.shape[0]/2).astype(np.int)
    xvals = (np.arange(2*nx+1)-nx).astype(np.int)
    yvals = (np.arange(2*ny+1)-ny).astype(np.int)
    surface = np.zeros((2*ny+1,2*nx+1))
    for dx in xvals:
        for dy in yvals:
            delta = np.abs(np.roll(np.roll(image,dy,axis=0),dx,axis=1)-image)**p
            goodpix = ((np.roll(np.roll(yy,dy,axis=0),dx,axis=1)-yy) == -dy)*((np.roll(np.roll(xx,dy,axis=0),dx,axis=1)-xx) == -dx)  
            # This line keeps only pixels that haven't wrapped.
            surface[dy+ny,dx+nx] = function(delta[goodpix])
    yy,xx = np.indices(surface.shape)
    rmat = ((yy-ny)**2+(xx-nx)**2)**(0.5)
    structure_function,edges,counts = ss.binned_statistic(rmat.ravel(),surface.ravel(),statistic=np.nanmean,bins=rmat.max())
    centers = 0.5*(edges[0:-1]+edges[1:])
    return structure_function,centers
