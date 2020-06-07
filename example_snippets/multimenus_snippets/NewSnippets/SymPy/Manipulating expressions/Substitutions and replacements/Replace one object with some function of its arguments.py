expr = log(sin(x)) + tan(sin(x**2))
expr = expr.replace(sin, lambda arg: sin(2*arg))