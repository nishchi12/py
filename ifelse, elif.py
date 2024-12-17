#note: we have to initialize var beforehand for both "for" and if else statements
# if statement example
if 10 > 5:
    print("10 greater than 5")
print("Program ended")
------------------------
# if..else statement example
x = 3
if x == 4:
    print("Yes")
else:
    print("No")
----------------------------
number = -2
# Ternary conditional to check if number is positive or negative
result = "Positive" if number >= 0 else "Negative"
print(result)
-----------------------------
age = 25
experience = 10
# Using > & 'and' with IF..ELSE
if age > 23 and experience > 8:
    print("Eligible.")
else:
    print("Not eligible.")

#oneline code
age = 25
experience = 10
var = "Eligible." if age > 23 and experience > 8 else "Not eligible."
print(var)
--------------------------
i = 10
if (i == 10):
#  First if statement
    if (i < 15):
        print("i is smaller than 15")
        # Nested - if statement
        # Will only be executed if statement above
        # it is true
    if (i < 12):
        print("i is smaller than 12 too")
    else:
        print("i is greater than 15")
else:
    print("i is not equal to 10")
---------------------------------
#Syntax: [on_true] if [expression] else [on_false]
#expression: conditional_expression | lambda_expr
#Ternary Expression


