a = np.arange(60).reshape((5,3,4))
b = np.arange(84).reshape((3,4,7))
n = 2
np.tensordot(a, b, n)