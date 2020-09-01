import math

tempstr = input().split()
num1 = int(tempstr[0])
num2 = int(tempstr[1])

ans = num1 * num2 / math.gcd(num1, num2)

print(int(ans))
