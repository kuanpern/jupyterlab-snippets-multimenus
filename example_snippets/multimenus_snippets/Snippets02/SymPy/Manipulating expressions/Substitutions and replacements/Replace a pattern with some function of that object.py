a = symbols("a", cls=Wild, exclude=[])
expr = log(sin(x)) + tan(sin(x**2))
expr.replace(sin(a), lambda a: sin(2*a))