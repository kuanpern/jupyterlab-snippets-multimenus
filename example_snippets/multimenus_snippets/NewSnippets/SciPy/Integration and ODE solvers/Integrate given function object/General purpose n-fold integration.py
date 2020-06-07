from scipy import integrate
def integrand(x0, x1, x2):
    return x2 * x1**2 + x0
x2_lim = (0.0, 0.5)
x1_lim = lambda x2:(0.0, 1.0-2.0*x2)
x0_lim = lambda x1,x2:(-1.0, 1.0+2.0*x2-x1)
# int_{x2=0}^{0.5} int_{x1=0}^{1-2x2} int_{x0=-1}^{1+2x2-x1} (x2 x1**2 + x0) dx0 dx1 dx2
integral,error = integrate.nquad(integrand, [x0_lim, x1_lim, x2_lim])
print(integral, error)