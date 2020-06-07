def format_all(x):
    return 'repr({0})'.format(repr(x))
with printoptions(formatter={'all': format_all}):
    print(np.array([3, 8]))
    print(np.array([0.1, 0.5]))
    print(np.array([1.4+2.3j, 2.8+4.6j]))
    print(np.array(['abc', 'xyz']))