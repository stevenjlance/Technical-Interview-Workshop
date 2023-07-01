# 1. Take a look at the code below:

def sum_of(n):
    total_sum = 0
    while n >= 1:
        total_sum += n
        n -= 1
    return total_sum

sum_of(10)

# a. How many lines of code will likely be run?

# b. As n grows, how will the number of run lines change?

# c. What Big O notation is this?

'''
If the number of lines run is linearly dependent on the data, we can say it has an order of n, or O(n) for short.
'''

# 2. Take a look at this next piece of code:
def sum_of(n):
    total_sum = n * (n + 1)
    total_sum /= 2
    return total_sum

sum_of(20)
# a. How many lines of code will likely be run?

# b. As n grows, how will the number of run lines change?

# c. What Big O notation is this?

'''
If the number of lines run is consistent or independent of the data inputted, it has an order of 1, or O(1)
'''

# 3. What would your intuition tell you about the following code?

def get_pairs(students):
    pairs = []
    for student1 in students:
        for student2 in students:
            if student1 != student2:
                pairs.append((student1, student2))
    return pairs

students = ["Rafael", "Steven", "Manny", "Jeff"]
print(get_pairs(students))

# a. How many lines of code will likely be run?

# b. As n grows, how will the number of run lines change?

# c. What Big O notation is this?

'''
If the number of lines run is square dependent on the data, we can say it has an order of n, or O(n^2) for short.
'''

# 4. Go to the README to see the solutions for questions 1 to 3.


# 5. Look at the following code snippets and determine their Big O. NOTE: some of these code snippets are not realistic, but they are here to test your knowledge on Big O.

# Mild

# 
def practice1(n):
	for i in range(n):
		print(i)

# 
def practice2(n):
	for i in range(n):
		for j in range(n):
			print(i, j)

# 
def practice3(n):
	i = 0
	while i < n:
		print(i)
		i += 2

# 
def practice4(n):
	if n > 9:
		n = 9
	print(n)

# 
def practice5(n):
	for i in range(n):
		print(i)
	for j in range(n):
		print(j)

# Medium

# 
def practice6(n):
	i = 0
	while False:
		print(i)
		i += 2

# 
def practice7(n):
	i = 1
	while i < n:
		print(i)
		i = i * 2

# 
def practice8(n):
	for i in range(n):
		for j in range(i, n):
			print(i, j)

# 
def practice9(n):
	for i in range(n):
		for j in range(n):
			print(i, j)
			break

# SPICY
# 
def practice10(n):
	for i in range(n):
		for j in range(i, n):
			for k in range(j, n):
				print(i, j, k)

# 
def practice11(n):
	if n > 100:
		print("too big")
	elif n > 0:
		for i in range(n):
			print(i)
	else:
		print("too small")

# 
def practice12(n):
	print(n)
	if n <= 1:
		print("Hurray!")
	else:
		practice12(n - 1)
 
# 6. Notice these 2 ways to code the same search function:
def findA(n, data):
    for idx, value in enumerate(data):
        if n == value:
            return idx
    return -1

def findB(n, data):
    left = 0
    right = len(data)
        
    while left <= right:
        mid = right // 2

        if n < data[mid]:
            right = mid - 1
        elif n > data[mid]:
            left = mid + 1
        else: # ==
            return mid
            
    return -1

#  a. What are the similarities between function `findA` and `findB`?


#  b. As the size of the _data_ list grows, how will the number of run lines change for each function?


#  c. [Bonus] What kind of search is `findA` and `findB` doing?


# d. What is the Big O notation for each of these?


# 7. Martha is running a **slushy stand** and can think of 3 different ways to save her data for her orders:

# 1
slushy_orders = {
    'berry': 8, 
    'lemon': 13, 
    'lime': 8, 
    'orange': 9, 
    'raspberry': 12
}

# 2
slushy_orders = ['raspberry', 'lime', 'berry', 'orange', 'lime', 'berry', 'lemon', 'berry', 'lemon', 'berry', 'lemon', 'lemon', 'orange', 'lime', 'lemon', 'lemon', 'lime', 'lemon', 'raspberry', 'lemon', 'raspberry', 'raspberry', 'orange', 'orange', 'orange', 'raspberry', 'raspberry', 'raspberry', 'orange', 'raspberry', 'lemon', 'lemon', 'lemon', 'raspberry', 'raspberry', 'lime', 'lemon', 'orange', 'lemon', 'orange', 'lime', 'orange', 'lime', 'raspberry', 'raspberry', 'berry', 'berry', 'berry', 'lime', 'berry']

# 3
slushy_order_types = ['berry', 'lemon', 'lime', 'orange', 'raspberry']
slushy_orders_counts = [8, 13, 8, 9, 12]

# a. Think of an instance where #1 would be the best data structure to use? ...#2? ...#3?

# b. Open the `slushy.py` and complete the challenges. Then as a comment, label each with their time complexity. To run your code use the command python3 slushy.py


## SPICY PROBLEMS

# 1. Given a list of numbers. How would you find the indexes of the 2 numbers that add up to the largest sum? Take a minute to yourself to think about 2 different solutions. Then, share them with your partner and compare.



# 2. Below, code the solutions that you and your partner came up with in number 1. Then as a comment, label each with their time complexity.

numbers = [67, 56, 35, -50, 34, 41, -70, -73, -82, -15, 63, -55, 80, -98, -67, 99, -75, -87, 79, -90, 44, 30, 11, 95, 91, 22, -29, -51, 96, -4, -76, -80, -23, 29, 16, 4, 9, -25, -18, -36, -78, -34, 83, -91, -93, -13, -88, -5, -48, 53]





# 3. SPICY: I can think of 5 different ways to code number 1. Below are the time complexities. Come up with all 5 ways (or potentially more)!
# - O(n) - (2 different O(n) ways)
# - O(n * log n)
# - O(1) - Hint: there's an exception here
# - O(n^2)