from scipy.special import gamma, airy
def func(y, t):
    return [t*y[1], y[0]]
x = np.arange(0, 4.0, 0.01)
y_0 = [-1.0 / 3**(1.0/3.0) / gamma(1.0/3.0), 1.0 / 3**(2.0/3.0) / gamma(2.0/3.0)]
Ai, Aip, Bi, Bip = airy(x)
y = odeint(func, y_0, x, rtol=1e-12, atol=1e-12) # Exact answer: (Aip, Ai)