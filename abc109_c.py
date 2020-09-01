import math
from functools import reduce


def gcd_list(numbers):
    return reduce(math.gcd, numbers)

tempstr = input().split()
N = int(tempstr[0])
X = int(tempstr[1])

tempstr = input().split()
crd = []
for i in range(N):
    crd.append(int(tempstr[i]) - X)
    
print(gcd_list(crd))
    
