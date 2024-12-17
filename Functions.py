#conditional statements
#infinite loop
count = 0
while (count == 0):
    print("Hello Geek")
------------------------
#for loop
l1 = ["eat", "sleep", "repeat"]

for count, ele in enumerate(l1):
    print (count, ele)
----------------------
#while loop
i = 1  # Initialize the outer loop variable
while i <= 3:  # Outer loop will run from 1 to 3
    j = 1  # Initialize the inner loop variable
    while j <= 3:  # Inner loop will also run from 1 to 3
        print(i, j)  # Print the pair
        j += 1  # Increment the inner loop variable
    i += 1  # Increment the outer loop variable

 #if-else loop
 i = 1
 if i <=3:
     j=1
     if j<=3:
         print(i,j)
         j+=1


i = 1
if i <= 3:
    j = 1
    if j <= 3:
        print(i, j)
        j += 1
    elif j > 3:
        j = 1
        i += 1
elif i > 3:
    print(i, j)
--------------------

#list comprehension
numbers =[x for x in sum(range(10))]
print(numbers)

---------------------
def check_status(a, b, flag):
    ##Your code here
    ##Either True or False is returned
    if (a >= 0) != (b >= 0) and not flag:
        return True
    if a < 0 and b < 0 and flag:
        return True
    return False

check_status(-1,1,flag = True)
----------------------------------
def sum(n1:int, n2:int) -> int:
    n3 = n1+n2
    return n3
n1,n2 = 10,5
ans = sum(n1, n2)
print(f"The addition of {n1} and {n2} results {ans}.")
------------------------------
def prime(n):
    if n in [2,3]:# is prime number
        return True
    if (n == 1 ) or (n%2 == 0):#even number
        return False
    r = 3
    while r * r <= n:#checks square
        if n % r == 0:
           return False
        r+=2 #3+2 = 5 , .....
        return True
print(prime(34),prime(21))
-------------------------
def evenOdd(x):
    if (x % 2 == 0):
        print("even")
    else:
        print("odd")

evenOdd(2)
evenOdd(3)
----------------
def prime(n):
    count = 0
    x = 2
    count < n:
    for d in range (2,x,1):
        if x % d ==0
            x +=1
    else:
        print(x)
        x+=1
        count+=1
n = 10

# print statement
print("First 10 prime numbers are:  ", prime(n))





