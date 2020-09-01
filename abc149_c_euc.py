def euc_gcd(x, y):
    if x < y:
        temp = x
        x = y
        y = temp
    #x > y
    ans = 0
    while True:
        mod = x % y
        if mod == 0:
            ans = y
            break
        x = y
        y = mod
    return ans
        
tempstr = input().split()
num1 = int(tempstr[0])
num2 = int(tempstr[1])

ans = num1 * num2 / euc_gcd(num1, num2)

print(int(ans))
