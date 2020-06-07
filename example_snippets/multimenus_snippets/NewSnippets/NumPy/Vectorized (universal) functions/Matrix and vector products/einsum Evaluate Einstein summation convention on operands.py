a = np.arange(6).reshape((3,2))
b = np.arange(12).reshape((4,3))
np.einsum('ki,jk->ij', a, b)