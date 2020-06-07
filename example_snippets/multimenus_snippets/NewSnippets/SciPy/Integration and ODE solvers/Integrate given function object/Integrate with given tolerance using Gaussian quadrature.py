gaussian = lambda x: 1/np.sqrt(np.pi) * np.exp(-x**2)
a,b = 0,1  # limits of integration
result,err = integrate.quadrature(gaussian, a, b, tol=1e-8, rtol=1e-8)