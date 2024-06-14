#!/usr/bin/python3

my_list = [1,2,5,33,44,8,0,47]

max_num = my_list[0]

for i in my_list:
    if i > max_num:
        max_num=i

print(f"max number in list = {max_num} ")