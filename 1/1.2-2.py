from sympy import *

n = Symbol('n')
# 8n^2=64nlgn
a, b = solve(8 * n ** 2 - 64 * n * log(n, 10), n)
print N(a)
print N(b)
