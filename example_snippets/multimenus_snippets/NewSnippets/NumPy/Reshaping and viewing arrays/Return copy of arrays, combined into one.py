a = np.arange(30).reshape((2,3,5))
b = np.arange(42).reshape((2,3,7))
c = np.concatenate((a, b), axis=1)