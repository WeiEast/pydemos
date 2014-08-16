
import math
import timeit


def aa():
    aa = math.sqrt
    for i in range(1000):
        cc = aa(25)


def bb():
    for i in range(1000):
        cc = math.sqrt(25)

t1 = timeit.timeit(aa, 'import math', number=1000)
t2 = timeit.timeit(bb, 'import math', number=1000)

print(t1, t2, sep='\n')


import profile
profile.run('aa()')
