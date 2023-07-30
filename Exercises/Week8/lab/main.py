'''
In this lab, you're given the plans of several power grids in sample_data.py. There are a couple of rules we should be looking for to ensure a healthy grid.
1. Can all power plants in the grid receive power? (Good)
2. Are there any cycles or loops of power? (Bad)

Some additional concerns are:
3. Can we find the path from the main power source to any other power plant?
4. Stretch: Is there an optimal cost of power transfer?
'''

# BEFORE YOU CODE ANYTHING, do the following for each power grid in sample_data.py
# 1. Sketch a directed graph for grid1 and grid2 to see how the plants are powering each other in the grid.
# 2. Do all the plants in the grid get power? Use your sketch.
# 3. Are there any cycles (loops of power)? Use your sketch.

# Use any or all 4 grids in sample_data to test your functions

from sample_data import grid1, grid2, grid3, grid4

# 1. Write a function that checks if all power plants have power.
# HINT: Another way of saying this is check that all nodes are visited.	
def full_power(grid, node, visited = set()):
	# If the node has been visited stop
	if node in visited:
		return True
	# If node hasn't been visited, add it to the set
	visited.add(node)
	# Iterate through the nodes that the node points to
	for neighbor in grid[node]:
		# pass each neighbor as the new node.
		if not full_power(grid, neighbor, visited):
			return False
	return True

# print(full_power(grid1, 0))

# 2. Write a function that checks if there is a loop in your power grid.
# HINT: Check for a cycle from every node.

def has_cycle(grid):
	for node in range(len(grid)):
		if check_loop(grid, node):
			return True
	return False

def check_loop(grid, node, visited = set()):
	if node in visited:
		return True
	visited.add(node)
	for neighbor in grid[node]:
		if check_loop(grid, neighbor, visited):
			return True
	return False

print(has_cycle(grid1)) #False
print(has_cycle(grid2)) #True


#[Spicy]
# 3. Write a function that finds all the unique paths from one plant to another.

def get_path(grid, start, end):
	paths = []
	def dfs(node, path):
		if node == end:
			paths.append(path)
			return
		for neighbor in grid[node]:
			if neighbor not in path:
				dfs(neighbor, path + [neighbor])
	dfs(start, [start])
	return paths

print(get_path(grid1, 0, 4)) # [[0, 1, 4]]
print(get_path(grid1, 4, 5)) # [[4, 6, 5], [4, 3, 5], [4, 3, 2, 5], [4, 3, 6, 5]]


from sample_data import grid5, grid6

# 4. Write a function that takes in a weighted directional graph, a start node, and an end node:
# It find the paths from start to end (or return an empty list), and the cost of that path.
# See the ReadMe for more context.

def cheapest_path(power_grid, start, end):
    pass


cheapest_path(grid5, 1, 2)  # [{'path':[1, 2], 'cost':1}, {'path':[1, 4, 2], 'cost':6}]
cheapest_path(grid6, 0, 6)  # []


# 5. Re-write the function from number 5 to return the most cost efficient path.


# (Optional) BONUS

# 6. In the maze.py there's a graph of a maze (a bidirectional graph).
# If 0 is the start node and the index with the value 'exit' is the destination node, find the path that gets you out of the maze.




# 4. Stretch: Is there an optimal cost of power transfer?
# 5. Stretch: Are there any single points of failure?