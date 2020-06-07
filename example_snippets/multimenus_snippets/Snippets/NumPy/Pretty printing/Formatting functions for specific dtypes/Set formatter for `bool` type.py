def format_bool(x):
    if x:
        return 'TRUE'
    else:
        return 'FALSE'
with printoptions(formatter={'bool': format_bool}):
    print(np.random.randint(0,2,10).astype(bool))