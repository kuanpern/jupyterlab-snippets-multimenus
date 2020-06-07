expr = exp(pi*I*2*(x+y))
assumption = Q.integer(x) & Q.integer(y)
expr = refine(expr, assumption)