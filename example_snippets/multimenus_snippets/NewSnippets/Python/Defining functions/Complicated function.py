def bp_some_func(x, y, z=3.14, **kwargs):
    r"""Some function
    
    Does some stuff.
    
    Parameters
    ----------
    x : int
        Description of x
    y : str
        Description of y
    z : float, optional
        Description of z.  Defaults to 3.14
    **kwargs
        Arbitrary optional keyword arguments.
        w : float
            Defaults to 6.28
    
    Returns
    -------
    double
        Some nonsensical number computed from some ugly formula
    
    """
    w = kwargs.pop("w", 6.28)
    if kwargs:
        print("Got {0} unused kwargs".format(len(kwargs)))
    return (x**2 + len(y)) * (w + z)