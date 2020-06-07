np.random.seed(11)
x = np.linspace(0, 2*np.pi, 20)
y = np.sin(x) + np.random.normal(scale=.1, size=x.shape)
n = 5
p = T.fit(x, y, n)