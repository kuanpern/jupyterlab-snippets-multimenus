from scipy import integrate
def integrand(z, y, x):
    return x * y**2 + z
x_lower_lim, x_upper_lim = 0.0, 0.5
y_lower_lim, y_upper_lim = lambda x:0.0, lambda x:1.0-2.0*x
z_lower_lim, z_upper_lim = lambda x,y:-1.0, lambda x,y:1.0+2.0*x-y
# int_{x=0}^{0.5} int_{y=0}^{1-2x} int_{z=-1}^{1+2x-y} (x y**2 + z) dz dy dx
integral,error = integrate.tplquad(integrand,
                                   x_lower_lim, x_upper_lim,
                                   y_lower_lim, y_upper_lim,
                                   z_lower_lim, z_upper_lim)
print(integral, error)