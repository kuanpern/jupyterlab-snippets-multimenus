from scipy import integrate
def integrand(y, x):
    return x * y**2
x_lower_lim, x_upper_lim = 0.0, 0.5
y_lower_lim, y_upper_lim = lambda x:0.0, lambda x:1.0-2.0*x
# int_{x=0}^{0.5} int_{y=0}^{1-2x} x y dx dy
integral,error = integrate.dblquad(integrand,
                                   x_lower_lim, x_upper_lim,
                                   y_lower_lim, y_upper_lim)
print(integral, error)