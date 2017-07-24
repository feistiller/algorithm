from sympy import *

a=[1000,1000*60,1000*60*60,1000*60*60*24,1000*60*60*24*30,1000*60*60*24*30*365,1000*60*60*24*30*365*100]

for i in a:
    print i
    print log(i,10)
    print sqrt(i)
    print N(i)
    print i*log(i,10)
    print i**2
    print i**3
    print 2**i
    print factorial(i)
    print '\n'