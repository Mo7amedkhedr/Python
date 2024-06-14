#!/usr/bin/python3

import os


path = os.environ['PATH']
print(path)

#set new environment
os.environ['Test']='var 1'

#get the value of new environment
my_var = os.environ['Test']

print(my_var)

#access the "Test" environment variable
variable_name = 'Test'
value = os.environ.get(variable_name)


for key,value in os.environ.items():
    print(f"{key}: {value}")
       
     

