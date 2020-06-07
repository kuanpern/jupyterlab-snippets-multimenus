expr = x**2 + y*x**2 + x*y + y + z*y
expr = collect(expr, [x, y])