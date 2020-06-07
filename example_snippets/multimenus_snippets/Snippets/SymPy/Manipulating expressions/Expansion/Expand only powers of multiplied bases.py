a, b = symbols("a, b", positive=True)
expr = (a*b)**z
expr = expand_power_base(expr)