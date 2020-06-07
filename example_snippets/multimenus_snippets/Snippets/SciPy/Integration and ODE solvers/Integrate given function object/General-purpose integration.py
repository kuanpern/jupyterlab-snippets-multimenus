from scipy import integrate
def f(x, a, b):
    return a * x + b
integral,error = integrate.quad(f, 0, 4.5, args=(2,1))  # integrates 2*x+1
print(integral, error)