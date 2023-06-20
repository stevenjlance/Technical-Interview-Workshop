import sample_data
print(sample_data.numbers)
# 1. Create an algorithm that does an insertion sort of the sample numbers data from smallest to largest

def insertSort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

print(insertSort(sample_data.numbers))

# 2. Create an algorithm that does a bubble sort of the sample numbers data from smallest to largest
def bubbleSort(array):
    # loop to access each array element
    for i in range(len(array)):
        # loop to compare array elements
        for j in range(0, len(array) - i - 1):

            # compare two adjacent elements
            # change > to < to sort in descending order
            if array[j] > array[j + 1]:

                # swapping elements if elements
                # are not in the intended order
                temp = array[j]
                array[j] = array[j+1]
                array[j+1] = temp
    return array
    

print(bubbleSort(sample_data.numbers))
# 3. Create an algorithm that does a selection sort of the sample numbers data from smallest to largest

def selectionSort(array):
    size = len(array)
    for step in range(size):
        min_idx = step

        for i in range(step + 1, size):
         
            # to sort in descending order, change > to < in this line
            # select the minimum element in each loop
            if array[i] < array[min_idx]:
                min_idx = i
         
        # put min at the correct position
        (array[step], array[min_idx]) = (array[min_idx], array[step])
    
    return array

print(selectionSort(sample_data.numbers))

'''
4. Pause and discuss. Which algorithm is the most "efficient"? Explain your answer considering how each handles:
    - Number of observations
    - Number of iterations/cycles
    - Number of movements of items
'''


# 5. Spicy. Update your three algorithms to sort values from largest to smallest

# 6. Spicier. Update your three algorithms to sort the list of student dictionaries by a provided key (name, age, or occupation)

# Example of insertion sort based on dictionary key provided 
def sortDic(arr, sortVal):
    for i in range(1, len(arr)):
        key = arr[i]
        val = arr[i][sortVal]
        j = i - 1
        while j >= 0 and val < arr[j][sortVal]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


print(sortDic(sample_data.students, "age"))

# 7. Create a merge sort algorithm to sort the numbers array

# 8. Create a merge sort algorithm to sort the list of student dictionaries by a provided key (name, age, or occupation)