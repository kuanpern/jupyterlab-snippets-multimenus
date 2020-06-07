dx0, dx1 = symbols("dx0, dx1")
formula = as_finite_diff(f(x).diff(x), [x-dx0, x, x+dx1])