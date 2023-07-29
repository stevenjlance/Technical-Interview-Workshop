street_directed_graph = [
  [3],
  [0, 4],
  [1, 5],
  [4],
  [1, 5],
  []
]

street_bidirectional_graph = [
	[1, 3],
	[0, 2, 4],
	[1, 5],
	[0, 4],
	[1, 3, 5],
	[2, 4]
]

# Create a function, isConnected, that returns True if two nodes are connected and False if they are not.

def is_connected(graph, current, destination, visited = None):
	# Keep track of where we have visited
	if visited == None:
		visited = set()
	# Base Case: If the current is the destination, they are connected
	if current == destination:
		return True
	# Mark the node as visited
	visited.add(current)
	# Recursive Case: Check if the destination is connected to any unvisited neighbors 
	for neighbor in graph[current]:
		print(neighbor)
		if neighbor not in visited and is_connected(graph, neighbor, destination, visited):
			return True
	return False

# Can node 0 get to 5?
print(is_connected(street_directed_graph, 0, 5))
# Can node 3 get to 2?
print(is_connected(street_directed_graph, 3, 2))