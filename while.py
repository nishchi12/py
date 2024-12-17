#note: we have to initialize var beforehand for both "for" and if else statements
cnt = 0
while (cnt < 3):
    cnt+=1
    print("Hello Geek")
------------------------
# Prints all letters except 'e' and 's'
i = 0
a = 'codeforcode'
while i < len(a):
    if a[i] == 'e' or a[i] == 's':
        i += 1
        continue

    print(a[i])
    i += 1
---------------------
# break the loop as soon it sees 'e'
# or 's'
i = 0
a = 'geeksforgeeks'
while i < len(a):
    if a[i] == 'e' or a[i] == 's':
        i += 1
        break

    print(a[i])
    i += 1
-----------------------------------
# An empty loop
a = 'geeksforgeeks'
i = 0

while i < len(a):
    i += 1
    pass

print('Value of i :', i)
------------------------------------