# 1 - O(n)
# Find max and second max simultaneously
first = float('-inf')
second = float('-inf')
for num in numbers:
    if num > first:
        second = first
        first = num
    elif num > second:
        second = num
print("#1 -", first, second)


# 2 - O(n)
# find max then loop through a and find second max
first = numbers[0]
for num in numbers:
    if num > first:
        first = num
        
second = numbers[0]
for num in numbers:
    if num > second and num != first:
        second = num
print("#2 -", first, second)


# 3 - O(n*log n)
# sort the list and pop the last 2 numbers
def quicksort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        left = [x for x in arr[1:] if x < pivot]
        right = [x for x in arr[1:] if x >= pivot]
        return quicksort(left) + [pivot] + quicksort(right)
        
sorted_numbers = quicksort(numbers)
first = sorted_numbers[-1]
second = sorted_numbers[-2]
print("#3 -", first, second)


# 4 - O(1)
# pop last 2 (NOTE: Only Works if Sorted!)
first = sorted_numbers[-1]
second = sorted_numbers[-2]
print("#4 -", first, second)


# 5 - O(n^2)
# find permutations of size 2 and remember the max 
max_sum = float('-inf')
first = second = None
for idx, n1 in enumerate(numbers):
    for n2 in numbers[idx+1:]:
        if n1+n2 > max_sum:
            first = max(n1, n2)
            second = n1+n2 - first # mathy way to get the other number
            max_sum = n1+n2

print("#5 -", first, second)
