expr = x*y + x - 3 + 2*x**2 - z*x**2 + x**3
expr = collect(expr, x)