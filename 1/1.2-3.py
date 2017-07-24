from sympy import *

n = Symbol('n')
# 100n^2=2^n
a,b = solve(100 * n ** 2 - 2 ** n, n)
print N(a)
print N(b)
