
def wrong_fft():
    synthim = np.random.randn(100,100)
    from astropy.convolution import convolve_fft,convolve
    yy,xx = np.indices(synthim.shape)
    rr =( (xx-99/2.)**2 + (yy-99/2.)**2)**0.5
    sf = [np.sum(np.abs(synthim - convolve_fft(synthim, (rr > ii) & (rr < ii+1)))) for ii in np.arange(0, rr.shape[0]/2., dtype='float') ]
    # wrapped version:
    sf = [np.sum(np.abs(synthim - convolve_fft(synthim, (rr > ii) & (rr <ii+1), boundary='wrap'))) for ii in p.arange(0, rr.shape[0]/2.,dtype='float') ]

def rprof():
    import image_tools
    synthim = np.random.randn(100,100)
    yy,xx = np.indices(synthim.shape)
    rps,ns = [],[]
    p = 2 # order of structure function
    for x,y in zip(xx.flat, yy.flat):
        d = np.abs(synthim-synthim[y,x])**p
        n,_,r = image_tools.radialprofile.azimuthalAverage(d, center=[x,y], return_nr=True, binsize=1)
        # cut off halfway to make sure the arrays are of the same shape (otherwise, would have to pad with NaNs)
        ns.append(n[:xx.shape[0]/2])
        rps.append(r[:xx.shape[0]/2])
        # for timing:
        if x == xx[0,-1]:
            print y,"..",

    # weighted average, where the weight is the # of pixels included in the radial profile
    sf = (np.array(rps)/np.array(ns, dtype='float')).sum(axis=0)
