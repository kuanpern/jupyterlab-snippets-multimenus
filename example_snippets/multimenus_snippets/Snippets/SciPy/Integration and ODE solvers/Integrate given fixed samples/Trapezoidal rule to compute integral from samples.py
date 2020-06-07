x = np.linspace(1, 5, num=100)
y = 3*x**2 + 1
integrate.trapz(y, x) # Exact value is 128