# Note: `exclude=` specifies that the Wild cannot match any item in the list
a, b = symbols("a, b", cls=Wild, exclude=[x,y])
expr = 2*x + y + z
wild = a*x + b
replacement = b - a
# Note: `exact=True` demands that all Wilds have nonzero matches
expr = expr.replace(wild, replacement, exact=True)