def format_float_kind(x):
    return '{0:.2%}'.format(x)
with printoptions(formatter={'float_kind': format_float_kind}):
    print(np.random.random(10))