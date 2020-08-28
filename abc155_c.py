N = int(input())

all_str = []
for i in range(n):
    str_temp = input()
    all_str.append(str_temp)

unique_str = list(set(all_str))
print(unique_str)
