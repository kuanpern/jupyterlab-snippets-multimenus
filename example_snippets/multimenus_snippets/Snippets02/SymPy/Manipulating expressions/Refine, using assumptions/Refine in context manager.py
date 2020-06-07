expr = exp(pi*I*2*(x+y))
with assuming(Q.integer(x) & Q.integer(y)):
    expr = refine(expr)