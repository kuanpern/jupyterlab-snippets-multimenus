w = Wild("w")
expr = z*x**y - t*z**y
expr = collect(expr, w**y)