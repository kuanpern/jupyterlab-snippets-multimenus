x = np.linspace(1, 5, num=100)
y = 3*x**2 + 1
integrate.cumtrapz(y, x) # Should range from ~0 to ~128