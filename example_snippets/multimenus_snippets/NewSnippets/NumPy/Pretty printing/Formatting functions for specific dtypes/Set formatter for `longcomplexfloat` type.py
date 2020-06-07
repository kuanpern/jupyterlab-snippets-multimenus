def format_longcomplexfloat(x):
    return '{0.real}+1j*{0.imag}'.format(x)
with printoptions(formatter={'longcomplexfloat': format_longcomplexfloat}):
    print(np.random.random(5).astype(np.longfloat)+1j*np.random.random(5).astype(np.longfloat))