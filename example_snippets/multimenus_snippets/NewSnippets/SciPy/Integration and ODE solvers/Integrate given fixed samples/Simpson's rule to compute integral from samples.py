x = np.linspace(1, 5, num=100)
y = 3*x**2 + 1
integrate.simps(y, x) # Exact value is 128