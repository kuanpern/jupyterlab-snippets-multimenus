gaussian = lambda x: 1/np.sqrt(np.pi) * np.exp(-x**2)
a,b = 0,1  # limits of integration
result,err = integrate.fixed_quad(gaussian, a, b, n=5)