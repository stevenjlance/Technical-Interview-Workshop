from tree import tree

# Demo
def get_value(t):
	current_node = t
	while current_node["right"]:
		current_node = current_node["right"]
	return current_node["value"]

print("---------DEMO---------")
print(get_value(tree))

# Mild


# 1. Write a function to get the minimum value in a tree.
def get_min(tree):
	if tree is None:
		return float('inf')  # Return positive infinity for an empty tree
	current_value = tree["value"]
	left_min = get_min(tree["left"])
	right_min = get_min(tree["right"])
	print(left_min, right_min)
	return min(current_value, left_min, right_min)

print("---------QUESTION 1---------")
print(get_min(tree))

# 2. Write a function that searches for a given value n in a tree.
# Should return true if the value exists


def find(n, t):
	current_node = t
	while current_node is not None:
		current_value = current_node["value"]
		if current_value == n:
			return True
		elif current_value < n:
			current_node = current_node["right"]
		else:
			current_node = current_node["left"]
	return False
	print(t.items())

print("---------QUESTION 2 (LOOPS)---------")
print(find(3, tree))

# Same function with recursion
def find_recursive(n, tree):
	if tree is None:
		return False
	current_value = tree["value"]
	if current_value == n:
		return True
	left_result = find_recursive(n, tree["left"])
	right_result = find_recursive(n, tree["right"])
	return left_result or right_result

print("---------QUESTION 2 (RECURSION)---------")
print(find_recursive(4, tree))

# Medium

# 3. Modify the function find() from #2 to return the list of visited nodes if the value exists.

def find_with_nodes(n, t):
	current_node = t
	nodes_visited = []
	while current_node is not None:
		current_value = current_node["value"]
		nodes_visited.append(current_node)
		if current_value == n:
			return nodes_visited
		elif current_value < n:
			current_node = current_node["right"]
		else:
			current_node = current_node["left"]
	return False

print("---------QUESTION 3---------")
print(find_with_nodes(10, tree))

# 4. Write a function called get_parent(n, tree) that returns the parent of a given value or -1.
# For example, get_parent(6, tree) => 8, and get_parent(5, tree) => -1 since there is no parent for 5.

# Spicy

# 5. Write a function called youngest_relative(x, y, tree) that finds the closest common ancestor of a node or -1.
# For example, youngest_relative(6, 10, tree) => 8, youngest_relative(4, 9, tree) => 5


def get_parent(n, tree):
	if tree is None:
		return -1  # Return -1 if the tree is empty
		
	# Check if the left child exists.
	# Check if the value of the left child matches the given value.
	# Return the parent if this is the case!
	if tree["left"] is not None and tree["left"]["value"] == n:
		return tree["value"]

	# Same for right child
	if tree["right"] is not None and tree["right"]["value"] == n:
		return tree["value"]

	
	left_parent = get_parent(n, tree["left"])
	right_parent = get_parent(n, tree["right"])

	if left_parent != -1:
		return left_parent
	elif right_parent != -1:
		return right_parent
	else:
		return -1

print("---------QUESTION 4---------")
print(get_parent(1, tree))