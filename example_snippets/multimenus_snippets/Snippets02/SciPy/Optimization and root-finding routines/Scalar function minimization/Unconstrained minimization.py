f = lambda x: (x - 2) * (x + 1)**2
res = optimize.minimize_scalar(f, method='brent')
print(res.x)