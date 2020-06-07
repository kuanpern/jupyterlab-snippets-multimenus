def format_float(x):
    return '{0:+0.2f}'.format(x)
with printoptions(formatter={'float': format_float}):
    print(np.random.random(10)-0.5)