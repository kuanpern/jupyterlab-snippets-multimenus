x = np.linspace(1, 5, num=2**7+1)
y = 3*x**2 + 1
integrate.romb(y, x) # Exact value is 128