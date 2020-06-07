g = 2*sin(x**3)
g.replace(lambda expr: expr.is_Function, lambda expr: expr**2)