for i in range(0, 10, 2):
    print(i)
----------------------
# Display the multiplication table for 7
for i in range(1, 11):  # Loop from 1 to 10
    print(f"7 x {i} = {7 * i}")
------------------------
print("List Iteration")
l = ["geeks", "for", "geeks"]
for i in l:
    print(i)

print("\nTuple Iteration")
t = ("geeks", "for", "geeks")
for i in t:
    print(i)

print("\nString Iteration")
s = "Geeks"
for i in s:
    print(i)

print("\nDictionary Iteration")
d = dict({'x': 123, 'y': 354})
for i in d:
    print("%s  %d" % (i, d[i]))

print("\nSet Iteration")
set1 = {1, 2, 3, 4, 5, 6}
for i in set1:
    print(i),

----------------------------
# Prints all letters except 'e' and 's'

for i in 'geeksforgeeks':

    if i == 'e' or i == 's':
        continue
    print(i)
----------------------
for i in 'geeksforgeeks':

    # break the loop as soon it sees 'e'
    # or 's'
    if i == 'e' or i == 's':
        break

print(i)
---------------------
# An empty loop
for i in 'geeksforgeeks':
    pass
print(i)
-------------------
