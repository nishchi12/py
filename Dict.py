dict = {1:'hi',2:'yo',3:'varun'}
d2= dict.copy()
print(d2)
print(d2.get(2))
print(dict[1])
#update elements
dict["name"] = 'nish'
print(dict)
#clearing elements in dict
key, val = d.popitem()
print(f"Key: {key}, Value: {val}")

#to iterate through dictionary
dict = {1:'hi',2:'yo',3:'varun'}
for key in dict:
    print(key)
for value in dict.values():
    print(value)
-------------------------
#length of dict
d = {"a": 1, "b": 2, "c": 3}
length = len([key for key in d])
print(length)

#length of dict
d = {"a": 1, "b": 2, "c": 3}
length = sum(1 for i in d)
print(length)



--------------------------

# initializing dictionary
test_dict = {1: 'gfg', 2: 'is', 3: 'best'}
# printing original dictionary
print(test_dict)

------------------------
# Getting length for nesting dictionary
# Python3 code to demonstrate working of
# Dictionary values String Length Summation
# Using for loop
# initializing dictionary
test_dict = {'gfg': '2345',
             'is': 'abcde',
             'best': 'qwerty'}
# printing original dictionary
print("The original dictionary is : " + str(test_dict))

# Dictionary values String Length Summation
# Using for loop
#res declared before lopping statement
res = 0
#output will be sum of no of char values of strings (value is a string here)
for val in test_dict.values():
    res += len(val)

# printing result
print("The string values length summation : " + str(res))
-------------------------------------------------------
print("dictionary iteration")
d = dict()
d['xyz'] = 1
d['abc'] = 2
print(d)
for i in d:
    print("%s %d" %(i,d[i]))
#write for loop in oneline
for i in d:print("%s %d" %(i,d[i]))


---------------------
for i in range(1, 4):
    for j in range(1, 4):
        print(i, j)

#for loop patterns
from __future__ import print_function
for i in range(1, 5):
    for j in range(i):
        print(i, end=' ')
    print()

----------------------------------------------









