from astropy.io import fits
import numpy as np
import matplotlib.pyplot as plt

Vc, hd=fits.getdata('B5_VLA_GBT_model_vc_QA.fits', header=True)


def dv_dr(Vc, xx, yy, x0, y0):
    """
    Function to calculate the velocity difference and its 
    corresponding distance for all points in an image.
    -----
    Params:
    Vc: Array of centroid velocity.
    xx: Array of x-position
    yy: Array of y-position
    x0: X-coordinate for center of difference calculation
    y0: Y-coordinate for center of difference calculation
    """
    if x0.size > 1:
        dv=np.array([])
        dd=np.array([])
        for index in np.arange(x0.size):
            dv_i, d_i = dv_dr(Vc, xx, yy, x0[index], y0[index])
            dv=np.append( dv, dv_i)
            dd=np.append( dd, d_i)
    else: 
        dv = Vc-Vc[y0,x0]
        dd=np.sqrt( (xx-x0)**2 + (yy-y0)**2)
        gd_i=np.isfinite(dv)
        dv=dv[gd_i]
        dd=dd[gd_i]
    return dv, dd

size=Vc.shape
xpos, ypos=np.meshgrid(np.arange(0,size[1]), np.arange(0,size[0]), sparse=False, indexing='xy')

gd=np.isfinite(Vc)

dv_i, d_i = dv_dr(Vc, xpos, ypos, xpos[gd], ypos[gd])
