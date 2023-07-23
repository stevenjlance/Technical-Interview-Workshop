# Note: If you get stuck refer to the ReadMe.md

# Helper Functions
def head_idx():
    return 0

def left_of(idx):
    return 2*idx + 1

def right_of(idx):
    return 2*idx + 2

def parent_of(idx):
    return (idx-1) // 2 

# CHALLENGES
min_heap = [2, 3, 6, 8, 10, 15, 18]

# 1. Use the head_idx function to print out the value at the head index of min_heap

head_value = min_heap[head_idx()];
print(head_value)

# min_heap can be represented as the tree shown below
'''
        2
			/   \
	   3     6
		/ \   / \
	 8  10 15 18
'''
# How do the left and right index values relate to the index value of their parent?

# 2. Using head_idx() and left_of() helper functions, print out the left child (3) of the head value (2) in min_heap. 
left = min_heap[left_of(head_idx())]
print(left)
# 3. Using head_idx() and left_of() helper functions, print out the right child (6) of the head value (2) in min_heap.
right = min_heap[right_of(head_idx())]
print(right)

# 4. Using the head_idx(), right_of(), and left_of() helper functions, print out the value 10 in min_heap. HINT: It may help to nest function calls inside of one another!
target = min_heap[right_of(left_of(head_idx()))]
print(target)


# HEAPIFY!

# Adding to a heap means putting the new value at the head and then "heapify"-ing it down to its proper position. Here are the 2 steps:
	# i. Add the new value to the head; aka the beginning of the list.
	# ii. (Heapify) while the inputted value is greater than either of the two children, swap with the smaller of the 2.

# 5. Finish the code by writing the min_heapify function to add a value to a min heap
def min_heapify(heap, idx):
  # Get the indices of the left and right children of the current node
  left_idx = left_of(idx)
  right_idx = right_of(idx)

  # Assume the current node has the minimum value
  min_idx = idx

  # Compare the value of the current node with its left child
  if left_idx < len(heap) and heap[left_idx] < heap[min_idx]:
    min_idx = left_idx

  # Compare the value of the current node with its right child
  if right_idx < len(heap) and heap[right_idx] < heap[min_idx]:
    min_idx = right_idx

  # If the current node is not the minimum, swap it with the smallest child
  if min_idx != idx:
    heap[idx], heap[min_idx] = heap[min_idx], heap[idx]
    # Recursively call min_heapify on the swapped child to maintain the heap property
    min_heapify(heap, min_idx)

def push(value, heap):
	heap = [value] + heap
	min_heapify(heap, head_idx())
	return heap

min_heap = push(9, min_heap)
print(min_heap)         # [2, 6, 3, 9, 8, 10, 15, 18]

# 6. Finish the code and pop the head out of the list. Use your min_heapify function from before.

min_heap = [2, 3, 6, 8, 10, 15, 18]

def pop_min_heap(heap):
	# Swap the head with the last element
	heap[head_idx()], heap[-1] = heap[-1], heap[head_idx()]
	# Remove the last element (previously the head)
	popped_value = heap.pop()
	# Restore the heap property by heapifying from the head
	min_heapify(heap, head_idx())
	
	return popped_value


print("Minimum Value:", pop_min_heap(min_heap))  # 2
print(min_heap)             # [3, 6, 10, 9, 8, 18, 15]



# 7. Write a function that returns the indexes of all the leaf nodes in a heap.
#  left child index and right child index will be greater than or equal to the length of the heap.
def find_leaf_indexes(heap):
  leaf_indexes = []
  for i in range(len(heap)):
    left_child_idx = left_of(i)
    right_child_idx = right_of(i)
    # Check if both left and right child indexes are greater than or equal to the heap length
    if left_child_idx >= len(heap) and right_child_idx >= len(heap):
      leaf_indexes.append(i)

  return leaf_indexes

# Example usage:
min_heap = [2, 3, 6, 8, 10, 15, 18]
leaf_indexes = find_leaf_indexes(min_heap)
print(leaf_indexes)  # Output: [3, 4, 5, 6]


# 8. Write a function `max_heapify(heap)` that does the same as `min_heapify(heap)`, but keeps the greatest value at the head.



# 9. Write a function `build_max(heap)` that turns a list into a max heap.
# You will need to use functions you've built previously
# Check to see that your final answer has been turned into a Max Heap

data = [13, 17, 1, 5, 4, 9, 14, 10, 6]

def build_max(heap):
    pass

max_heap = build_max(data)
# print(max_heap)



# 10. Given a list of unsorted values, write a function `heap_sort(data)` that sorts the values from least to greatest.

unsorted_list = [13, 17, 1, 5, 4, 9, 14, 10, 6]