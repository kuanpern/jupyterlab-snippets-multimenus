def format_str_kind(x):
    return 'str({0})'.format(x)
with printoptions(formatter={'str_kind': format_str_kind}):
    print(np.array(['abc', 'xyz']))