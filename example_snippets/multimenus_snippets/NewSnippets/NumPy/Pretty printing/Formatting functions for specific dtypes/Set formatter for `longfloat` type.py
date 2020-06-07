def format_longfloat(x):
    return 'long{0}'.format(x)
with printoptions(formatter={'longfloat': format_longfloat}):
    print(np.random.random(10).astype(np.longfloat))