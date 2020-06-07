expr = x**2 + x**4
replacements = {x**2: y}
expr = expr.xreplace(replacements)