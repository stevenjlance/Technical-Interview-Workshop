# 1. Consider the following algorithm
numbers = [1, 2, 3, 4, 5]

for number in numbers:
	print(number, "is in the list.")

# How many lines will be run in the code above?

'''
Depends on the length of the list, but increases linearly as you add more numbers to the list.

Because of this, we can say that this code has a time complexity order of n, O(n) for short, where n is the length of the list or the number of times the for loop will cycle.
'''

# 2. Another example with an array of numbers
numbers = [1, 2, 3, 4, 5]

fav_num = numbers[0]
print("My favorite number is", fav_num)

# How many lines of code run for the above example

'''
There are 3 lines of code that will be run. No matter how big the list is, 3 lines is all that will run. The list can be 1 element long or 1231241231 elements long. It will always be only 3 lines of code.

Because this number is consistently 3 and not dependent on the list length, this is an order of 1 or O(1) for short.
'''

# 3. Label the following example functions as O(n) or O(1)

names = ["John", "Jacob", "Jingle", "Heimer", "Schmidt"]

# 
def example1():
	for name in names:
		print("Hello", name)


#
def example2():
	for_name = names[4]
	print(for_name)


# 
def example3():
	i = 0
	while (i < len(names)):
		print(names[i])


# 
def example4():
	for name in names:
		print(name)
		break

#
def example5():
	letters = [name[0] for name in names]
	print(letters[0])

'''
1. O(n)
2. O(1)
3. O(n)
4. O(1)
5. O(n)
'''

# 4. Here is a selection sort algorithm we covered in week 2.

randomNumbers = [123, 98, 43, 28, 2]


def selection_sort(arr):
	n = len(arr)
	count = 0
	for i in range(n - 1):
		min_index = i
		for j in range(i + 1, n):
			count += 1
			if arr[j] < arr[min_index]:
				min_index = j
			if min_index != i:
				arr[i], arr[min_index] = arr[min_index], arr[i]
	print(count)
	return arr


# What are the maxium lines of code run for the above example when you call it with the randomNumbers list?

'''
This list is fully unsorted from largest to smallest, so it will run 10 times. If they are stuck, add a count variable to show this!

This is O(n^2) notation. The outer loop runs n-1 times, and the inner loop runs (n-1), (n-2), (n-3), ..., 2, 1 times in each iteration of the outer loop.

The total number of comparisons and swaps can be approximated by the sum of the arithmetic series:

(n-1) + (n-2) + (n-3) + ... + 2 + 1 = (n * (n-1)) / 2

Note that it may be less than n^2, but in the worst scenarios it is n^2
'''

# 5. One final example. This algorithm is designed to give you all permutations of a given list. How many lines of code run when you pass in a list of length 3?
combo = [1, 2, 3]
def permutation(arr):
    if len(arr) == 0:
        return []
    elif len(arr) == 1:
        return [arr]
    else:
        result = []
        for i in range(len(arr)):
            m = arr[i]
            remaining = arr[:i] + arr[i+1:]
            for p in permutation(remaining):
                result.append([m] + p)
        return result

'''
This runs 9 times or a 3! (3 factorial) amount of times. 

As the list grows, this becomes an incredibly ineficient algorithm. A list of 5 elements will require the code above to be executed 120 times.
'''
