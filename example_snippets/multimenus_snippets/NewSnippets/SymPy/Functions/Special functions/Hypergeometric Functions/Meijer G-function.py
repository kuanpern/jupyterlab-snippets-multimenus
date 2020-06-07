m,n = 1,2
p,q = 4,1
a_j = symbols("a:{0}".format(p)) # numerator parameters
b_k = symbols("b:{0}".format(q)) # denominator parameters
meijerg(a_j[:n], a_j[n:p], b_k[:m], b_k[m:q], x)