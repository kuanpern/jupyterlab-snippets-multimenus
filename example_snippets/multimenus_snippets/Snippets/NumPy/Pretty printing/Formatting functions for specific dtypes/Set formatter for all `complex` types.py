def format_complex_kind(x):
    return '{0.real}+1j*{0.imag}'.format(x)
with printoptions(formatter={'complex_kind': format_complex_kind}):
    print(np.random.random(5)+1j*np.random.random(5))