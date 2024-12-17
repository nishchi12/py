def add(a : int ,b : int ):
    """" sum """
    c = a+b
    return c

a,b = 4,5
ans = add(a,b)
print(f"result {a} and {b} results {ans}.")

-----------------------

def is_prime(n):
    if n in [2, 3]:
        return True
    if (n == 1) or (n % 2 == 0):
        return False
    r = 3
    while r * r <= n:
        if n % r == 0:
            return False
        r += 2
    return True
print(is_prime(78), is_prime(79))

--------------------------------

# args and kwargs

def TIM(*args):
    print(args)

TIM('Hello', 'Welcome', 'to', 'GeeksforGeeks')

#kwargs

def myFun(**kwargs):
    for key, value in kwargs.items():
        print("%s == %s" % (key, value))
# Driver code
myFun(first='Geeks', mid='for', last='Geeks')

--------------------------------------------------

def swap(x,y):
    x = temp
    x=y
    temp=y
---------------------------------------



-------------------------------------
letter = "A"

if letter == "B":
    print("letter is B")

else:

    if letter == "C":
        print("letter is C")

    else:

        if letter == "A":
            print("letter is A")

        else:
            print("letter isn't A, B and C")


-----------------------------------------------
a, b = 10, 20

print({True: "a is minimum", False: "b is minimum"} [a < b])


-----------------------------------------------






----------------------












