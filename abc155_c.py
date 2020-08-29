# -*- coding: utf-8 -*-
N = int(input())

all_str = []
for i in range(N):
    str_temp = input()
    all_str.append(str_temp)

unique_str = (list(set(all_str)))
unique_str.sort()
max_cnt = 0
str_num = dict()
for i in unique_str:
    cnt = all_str.count(i)
    str_num[i] = cnt
    if max_cnt < cnt:
        max_cnt = cnt

disp_list = []
for i in str_num:
    current_cnt = str_num[i]
    if current_cnt == max_cnt:    
        disp_list.append(i)
    

for i in disp_list:
    print(i)
    
