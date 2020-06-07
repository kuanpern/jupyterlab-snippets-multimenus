expr = f(x).diff(x, x) + 9*f(x)
eqn = Eq(expr, 1)  # f''(x) + 9f(x) = 1
soln = dsolve(eqn, f(x))