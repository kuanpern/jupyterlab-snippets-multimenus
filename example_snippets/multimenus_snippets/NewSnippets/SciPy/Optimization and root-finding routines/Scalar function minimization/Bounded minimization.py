from scipy.special import j1  # Test function
res = optimize.minimize_scalar(j1, bounds=(4, 7), method='bounded')
print(res.x)