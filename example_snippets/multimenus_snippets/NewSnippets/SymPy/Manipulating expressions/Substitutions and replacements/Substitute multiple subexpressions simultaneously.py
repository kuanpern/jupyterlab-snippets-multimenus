expr = (x+y)/y
substitutions = [(x+y, y), (y, x+y)]
expr = expr.subs(substitutions, simultaneous=True)