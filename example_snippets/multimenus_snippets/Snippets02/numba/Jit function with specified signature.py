@numba.njit(f8, f8[:])
def bp_func(x, y):
    r"""Some function
    
    Parameters
    ----------
    x : float
    y : float array
    
    """
    for j in xrange(y.size):
        y[j] *= x