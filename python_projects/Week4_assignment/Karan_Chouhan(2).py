import numpy as n
import matplotlib.pyplot as mplt
import scipy.signal as ss
import random

a = n.random.randint(0,100,10)
print(f'original a is {a}')
b = n.random.randint(0,100,10)
print(f'original b is {b}')

for i in range(len(a)):
    print()
    c = n.random.randint(0,100,10)
    print(c)
    d = n.random.randint(0,100,10)
    print(d)
    a,b = c,d
    print()
    print(f'swapped a is {a}')
    print(f'swapped b is {b}')