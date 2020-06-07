def format_int(x):
    return 'int({0})'.format(x)
with printoptions(formatter={'int': format_int}):
    print(np.random.randint(-3, 4, 10))