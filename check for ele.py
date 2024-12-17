 # Check if any element in list satisfies a condition
# initializing list
test_list = [4, 5, 8, 9, 10, 17]
# printing list
print("The original list : " + str(test_list))
# Check if any element in list satisfies a condition
# Using list comprehension
res = True in (ele > 10 for ele in test_list) #checks for each ele and returns true or false
# Printing result
print("Does any element satisfy specified condition ? : " + str(res))

-------------------------------------------------------------
# Check if any element in list satisfies a condition
test_list = [4, 5, 8, 9, 10, 17]
print("The original list : " + str(test_list))
# Check if any element in list satisfies a condition
# Using any()
res = any(ele > 10 for ele in test_list) #any considers boolean context
#Truthy and Falsy values:
#Truthy values: Values that are considered True in a boolean context (e.g., non-zero numbers, non-empty strings, non-empty lists, etc.).
#Falsy values: Values that are considered False in a boolean context (e.g., 0, False, None, empty lists [], empty strings "", etc.).
# Printing result
print("Does any element satisfy specified condition ? : " + str(res))
---------------------------------------------------------
test_list = [4, 5, 17, 9, 10, 25]
print("The original list : " + str(test_list))
# Using the next() function to check if any element in the list is greater than 10
res = next((ele for ele in test_list if ele > 10), False)
# Printing the result of the check
print("Does any element satisfy specified condition ? : " + str(res))





