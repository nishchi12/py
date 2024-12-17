#accessing lst
a = [10, 20, 30, 40, 50]
# Access first element
print(a[0])
# Access last element
print(a[-1])
#append,extend,pop

print(a.append(60)) #returns none
print(a)
print(a.extend(25)) # error
print(a.extend([25]))#list_name.extend(iterable) #no return value
print(a)
print(a.insert(1,1.5))#insert as per index
print(a)
del a[1]
print(a)
------------------------------
#taking input
lst = input('enter value:').split() #split() returns a list with string items
print('present list is: ',lst)

#split?
string = "one,two,three"
words = string.split(',') #split takes seperator(delimitor)
print(words)
---------------------------------------
#taking input using for loop
# Get the number of elements
n = int(input("Enter the number of elements: "))
# Using list comprehension to get the list of elements
a = [input(f"Enter element {i+1}: ") for i in range(n)]
# Print the list
print("List:", a)

---------------------------------
#Methods
index = a.index(40) #get index of element
print(index)
--> #APPEND
a = [1,2]
a.append([3,4]) #this will add list itself
print(a) #check result to see difference
--> #EXTEND
a.extend([5, 6]) #this will add items not list itself
print(a)# see the difference with extend
B=['I','U']
a.extend(B) #added and list to exisitng list
print(a)
v = ('jatin',) #put a comma else enter below to check
v = ('jatin') #without output will be if used in extend a split of chars
print(v)
a.extend(v)
print(a)

------> #add elements to lst using +
lst =[1,2]
a = lst + [55,66]
print(a)
----------------------
------> #iterate over loop

a = [1, 3, 5, 7, 9]
# On each iteration val
# represents the current item/element
for val in a :
    print(val)
#using list comprehension
print(val) for val in a

a = [1, 3, 5, 7, 9]

for i in range(n):
    print(a[i])
#using list comprehension
_ = [print(a[i]) for i in range(len(a))] # just [print(a[i]) for i in range(len(a))] will give a [none,none...] list

a = [1, 3, 5, 7, 9]

[print(val) for val in a]
---------------------
st = 'I am a good boy'
sp = st.split()
p = list(sp)
print(p)
q = list(reversed(p))
print(q)

----------------------
#slicing
s = 'folks'
print(s[1:3])
print(s[1:])
print(s[:2])
print(s[::-1])
s1 = 'g'+s[1:]
print(s1)

s = 'folks'
s2 = s.replace('folks','ICON')
print(s2)

----------------------

a = [i for i in range(10)]
print(a)

a = [(1,2,3),(4,5,6),(7,8,9)]
res = [val for row in a for val in row]

"""res = []
for row in mat:
for val in row:
res.append(val)"""

-------------------
lst = [i for i in range(1,10)]
print(lst)

print(lst[1:8:3])
# list slicing allows out-of-bound indexing without raising errors.
print(lst[1:17:3])
#negative indexing
a = [1, 2, 3, 4]
print(a[:-3])
print(a[-4:-1])
print(a[-1:])
print(a[:1])

-------------
list1 = [1, 2, 3]
list2 = ['a', 'b']
zipped = zip(list1, list2)
print(list(zipped))

test_lst = [('slip',2),('right',1),('left',3)]
print('original' + str(test_lst))
res = list(zip(*test_lst))
print('modified'+ str(res))

tuples = ('z','a','d','f','g','e','e','k')
new_tup = tuples[::-1]
print(new_tup)

--------------------------------------------------
fruits = ["apple", "banana", "cherry"]
colors = ["red", "yellow", "green"]
for fruit, color in zip(fruits, colors):print(fruit, "is", color)
-----------------------------------
a=[1,2,3,4,5,6]
b=[7,8,9,10]
result=[a*b if a>0 and b>0 else none for a,b in zip(a,b)]
print(result)
--------------------------------

