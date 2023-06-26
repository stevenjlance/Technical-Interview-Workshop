# Mild

# 1. Write a function for the factorial of a number
# ex. 3! = 3*2*1 = 6 -- 5! = 5*4*3*2*1 = 120

def factorial(n):
    if n == 1:
        return n
    else:
        return n * factorial(n - 1)

print(factorial(5))

# 2. Write a function that computes the sum of the digits of a number.
# ex. 2148 => (2+1+4+8) = 15

def sum_digits(n):
    if n == 0:
        return 0
    else:
        return (n % 10) + sum_digits(n//10)

print(sum_digits(2148))

# 3. Write a function that reverses the order of a list.
# ex. [1, 2, 3, 4, 5] => [5, 4, 3, 2, 1]

def reverse(arr):
    if len(arr) == 0:
        return arr
    else:
        # Return the last element and then add it to the function call of the same array passing every element except the last element.
        return [arr[-1]] + reverse(arr[:-1])

print(reverse([1, 2, 3, 4, 5]))
print([5] + [4])
# Medium

# 4. Every number can be represented as a "single digit". Write a function that converts any number to it's "single digit" form
# ex. 7 => 7 -- 57 (5+7) => 12 (1+2) => 3 -- 159 => 15 => 6

def singleDigit(num):
    digits = [int(x) for x in str(num)]
    if len(digits) > 1:
        return singleDigit(sum(digits))
    else:
        return num

print(singleDigit(159))

# 5. Would you rather have a million dollars or a penny that doubles in size for a month (30 days)?
# Write a function that finds how much a penny doubled for 30 days is.

def doublePennies(days, amount):
    if days == 1:
        return amount
    else:
        return doublePennies(days - 1, amount * 2)

print(doublePennies(30, 0.01))

# 6. Is the number prime? Can it only be divided by itself and 1?
# ex. 7 is prime (factors: 1, 7) but 10 is not (factors: 1, 2, 5, 10)
# Hint: Check 2 first (by default) and work your way up until you hit the original number.

def prime(n, next = 2):
    if n == next:
        return True
    elif n % next == 0:
        return False
    else:
        return prime(n, next + 1)

print(prime(10))

# Spicy
# NOTE: These are much easier as recursion than as a loop. Feel free to skip non-recursive version.


# 7. A few chess players have made it to the finals fighting for 1st - 4th place.
# Write a function that will return all the ways the players can get placed.
# ex.   ['Sherman', 'Rosemary', 'Lucero', 'Yareli']
#       ['Sherman', 'Rosemary', 'Yareli', 'Lucero']
#       ['Sherman', 'Lucero', 'Rosemary', 'Yareli']

finalists = ['Sherman', 'Rosemary', 'Lucero', 'Yareli']






# 8. Here's a list of all the chess students before the finals.
# Write a function that finds all the combinations of last 4 finalists that could have ocurred. 
# ex.   ['Raven', 'Dorian', 'Santiago', 'Marisol']
#       ['Raven', 'Dorian', 'Santiago', 'Stephanie']
# NOTE: order doesn't matter here!
# ex.   ['Raven', 'Dorian', 'Santiago', 'Marisol'] making it to the finals is the same as
#       ['Marisol', 'Raven', 'Santiago', 'Dorian']. It's the same 4 people.

all_students = ['Raven', 'Dorian', 'Santiago', 'Marisol', 'Stephanie', 'Roland', 'Sherman', 'Rosemary', 'Lucero', 'Yareli']







# 9. Raven has caught wind of a pop quiz coming up and wants to let everyone in the class know about it.
#   She only has the number of her 2 best friends: Stephanie and Rosemary. They have some other people's phone numbers, and so on.
#   If each student can only text one other person, what would be the chain of communication that get's everyone the information?

# Here's a dictionary of the lines of communication
communications = {
    'Raven': ['Stephanie', 'Rosemary'], 
    'Dorian': ['Santiago', 'Yareli'], 
    'Santiago': ['Dorian', 'Roland'], 
    'Marisol': ['Roland', 'Sherman', 'Yareli'], 
    'Stephanie': ['Raven', 'Rosemary'], 
    'Roland': ['Santiago','Marisol', 'Lucero'], 
    'Sherman': ['Marisol'], 
    'Rosemary': ['Raven', 'Stephanie', 'Lucero'], 
    'Lucero': ['Roland', 'Rosemary'], 
    'Yareli': ['Dorian', 'Marisol']
}





# Recurison Interview Questions
# Make sure to name the inputs and expected outputs that you will use to test that your algorithm is correct!

# 1. Reverse a string using recursion

def reverseStr(str):
    if len(str) == 0:
        return str
    else:
        return str[-1] + reverseStr(str[:-1])

print(reverseStr("Hello"))

# 2. Print a Fibonacci Series using recursion

def fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        sequence = fibonacci(n - 1)
        sequence.append(sequence[-1] + sequence[-2])
        return sequence

print(fibonacci(7))


# 3. Calculate the power of a number using recursion. 
# E.g. power(2, 3) should return 8.

def power(n, p):
    if p == 1:
        return n
    else:
        return n * power(n, p - 1)

print(power(2, 3))

# 4. Write an algorithm to convert decimal to binary using recursion
# E.g. 26 is 11010 in binary

def decimalToBinary(n):
    if n <= 0:
        return ''
    else:
        return decimalToBinary(n // 2) + str(n % 2)


print(decimalToBinary(26))
# 5. Find all permutations of a string using recursion




# Search Interview Questions
# 1. Implement a binary search algorithm in Python.

def binarySearch(arr, val):
    arr.sort()
    # Initial lowest is index 0
    low = 0
    # Initial highest is one is highest posisble index
    high = len(arr) - 1
    while low <= high:
        # Find mid point between high and low as a whole number
        mid = (low + high) // 2
        # Check index in middle if it is equal to the value
        if arr[mid] == val:
            return mid
        # If the val is less than the middle index value, then increase low index by midpoint + one
        elif arr[mid] < val:
            low = mid + 1
        # If the val is higher than the middle index value, then icrease high index by midpoint + one
        else:
            high = mid - 1
    return -1

print(binarySearch([2, 10, 21, 2, 13, 3], 10))


# 2. Write a Python function to perform a linear search in a given list and return the index of the target element. If the element is not found, return -1.

def linarSearch(arr, search):
    for i, x in enumerate(arr):
        if(x == search):
            return i
    return -1

# print(linarSearch([2, 4, 6, 8, 10], 3))


# 3. Explain the time complexity of the binary search algorithm.





# 4. Describe a scenario where you would choose binary search over linear search.





# 5. Can binary search be applied to a linked list? If yes, explain how. If no, why not?



