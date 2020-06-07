a, b = symbols("a, b", positive=True)
expr = log(a**2*b)
expr = expand_log(expr)