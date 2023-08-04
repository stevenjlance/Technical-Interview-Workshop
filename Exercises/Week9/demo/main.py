from wiki import root

# class Page(object):
#   def __init__(self, x):
#     self.value = x
#     self.links = []

# NOTE: If you're having trouble conceptualizing the flow of the graph, you can either peak at the `wikipedia` variable in `wiki.py`.

# 1. Print out the value and links of the root
print(root.value, root.links)

# 2. Breadth First Search (BFS): Wisits all nodes at the current depth level before moving on to the nodes at the next depth level.


# Use a queue to hold th values that need to be visited
# Otherwise, add the node's children to the queue if they haven't already been added.

def BFS(start_node, destination_value):
	# Check if starting node is the destination. Return if true!
	if start_node.value == destination_value:
		return start_node
	# Initialize a queue and put starting node in the queue
	queue = [start_node]
	# Make a set to keep track of where we have visited
	visited = set()
	# Iterate while there are values in the queue
	while queue:
		# Pop node off queue and check if it is the destination 
		current_node = queue.pop(0)
		if current_node.value == destination_value:
			return current_node
		# Add current node to the set and print value so we can trace
		visited.add(current_node)
		# Iterate through neighbors of the current node
		for neighbor in current_node.links:
			# To help show the path
			print(neighbor)
			# If the neighbor has not been visited, add it to the queue
			if neighbor not in visited:
				queue.append(neighbor)
				print(queue)
	return None

print(BFS(root, 'A'))


# 3. Depth First Search (DFS): Explore as far along one branch as possible before backtracking

def DFS(start_node, destination_value, visited = None):
	# Create set to keep track of visited nodes
	if visited == None:
		visited = set()
	# Check if start_node is the destination. Return if it is!
	if start_node.value == destination_value:
		return start_node
	# Mark start_node as visisted
	visited.add(start_node)
	# Explore each unvisited neighbor recursivly, so that we can explore a full path first
	for neighbor in start_node.links:
		# Recursive call if node hasn't been visited
		if neighbor not in visited:
			# To help show the path
			print(neighbor.value)
			result_node = DFS(neighbor, destination_value, visited)
			# If recursive call returns the Node, then return it
			if result_node:
				return result_node
	# Not Found? return None
	return None

print(DFS(root, 'Z').value)