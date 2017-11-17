import numpy as np
import scipy
import random

A = [13, 12, 7, 16, 9, 11, 7, 10, 9, 8, 9, 7, 16, 7, 9, 8, 13, 10, 11, 9, 13, 13, 10, 10, 9, 7, 7, 6, 7, 8, 12, 13, 9, 6, 9, 11, 10, 8, 12, 10, 9, 10, 8, 14, 13, 13, 10, 11, 12, 9]
B = [8, 8, 16, 16, 9, 13, 14, 13, 10, 12, 10, 6, 14, 8, 13, 14, 7, 13, 7, 8, 4, 11, 7, 12, 8, 9, 12, 8, 11, 10, 12, 6, 10, 15, 11, 12, 3, 8, 11, 10, 10, 8, 12, 8, 11, 6, 7, 10, 8, 5]

both = A + B
diffcount = 0
for i in range(10000):
    new_A = [both[random.randint(0,len(both) - 1)] for i in A]
    new_B = [both[random.randint(0,len(both) - 1)] for i in B]
    [temp_A, temp_B] = [np.var(new_A), np.var(new_B)]
    if (temp_B - temp_A)**2 > 3**2:
        diffcount += 1
print(diffcount/float(10000))

