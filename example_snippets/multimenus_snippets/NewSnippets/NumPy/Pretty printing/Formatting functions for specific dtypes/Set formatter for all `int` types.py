def format_int_kind(x):
    return 'int({0})'.format(x)
with printoptions(formatter={'int_kind': format_int_kind}):
    print(np.random.randint(-100, 100, 10))