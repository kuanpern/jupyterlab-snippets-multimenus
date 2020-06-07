def format_complexfloat(x):
    return '{0.real}+1j*{0.imag}'.format(x)
with printoptions(formatter={'complexfloat': format_complexfloat}):
    print(np.random.random(5)+1j*np.random.random(5))