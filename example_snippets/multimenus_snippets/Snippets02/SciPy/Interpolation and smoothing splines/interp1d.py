# NOTE: `interp1d` is very slow; prefer `InterpolatedUnivariateSpline`
x = np.linspace(0, 10, 10)
y = np.cos(-x**2/8.0)
f = interpolate.interp1d(x, y, kind='cubic')
X = np.linspace(0, 10, 100)
Y = f(X)