import numpy
a = numpy.arange(10)
expr = sin(x)
f = lambdify(x, expr, "numpy")
vals = f(a)