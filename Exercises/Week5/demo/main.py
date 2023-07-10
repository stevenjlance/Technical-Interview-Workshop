# Create your own tests for the following problems.

first_monkey = "Alpha"
monkeys = {
 "Delta": "Echo",
 "Charlie": "Delta",
 "Alpha": "Beta",
 "Beta": "Charlie",
 "Foxtrot": None,
 "Echo": "Foxtrot"
}

# 1 - Print the monkey Alpha is holding
print("-----------Question 1-------------")
print(monkeys[first_monkey])

# 2 - Write a function that prints all the monkeys in their current order.

def printAll():
	pointer = first_monkey
	while pointer is not None:
		print(pointer)
		pointer = monkeys[pointer]

print("-----------Question 2-------------")
printAll()

# 3 - Foxtrot is on vacation. Create a function pop() that eliminates the last monkey, from the chain but not from the dictionary.

def pop():
	pointer = first_monkey
	prev_monkey = None
	# 
	while monkeys[pointer] is not None:
		prev_monkey = pointer
		pointer = monkeys[pointer]
	if prev_monkey is not None:
		monkeys[prev_monkey] = None

pop()
print("-----------Question 3-------------")
printAll()

# 4 - Charlie is on family leave. Create a function remove(NAME) that eliminates the named monkey from the chain but not from the dictionary.
# Then, remove Charlie.

def remove(name, first_monkey):
	# Asign the pointer to the first monkey
	pointer = first_monkey
	# Set previous monkey initially as none
	prev_monkey = None
	# 
	# As long as pointer is not name and not none, keep iterating
	while pointer != name and pointer is not None:
		# Asign prev_monkey to current pointer
		prev_monkey = pointer
		print(pointer)
		# Update pointer value with the new value it points to
		pointer = monkeys[pointer]
	# If pointer is the name and prev_monkey is not none, then set the previous monkey to point to the value in the name
	if pointer == name:
		if prev_monkey != None:
			monkeys[prev_monkey] = monkeys[name]
		else:
			# If it's the first value, swap it out
			first_monkey = name

print("-----------Question 4 and 5-------------")
remove("Charlie", first_monkey)
# printAll()

# 5 - Note: if you remove Alpha, that would mess with the first_monkey variable. Adjust your function to account for this.



# 6 - Foxtrot is back! Create a function append(NAME) that adds the monkey to the end of the list.  Then, add Foxtrot.

def append(name):
	pointer = first_monkey
	# Iterate until you reach the end of the list
	while monkeys[pointer] is not None:
		pointer = monkeys[pointer]
	# Take the last position and set the value to the name and have it point toward None
	monkeys[pointer] = name
	monkeys[name] = None
	
print("-----------Question 6-------------")
append("Foxtrot")
printAll()

# 7 - Charlie is also back! Create a function insert(NAME, AFTER) that adds a monkey after a specified other monkey

def insert(name, after):
	# Set pointer to the first monkey
	pointer = first_monkey
	# While the pointer is not none and the after monkey, keep iterating
	while pointer is not None and pointer != after:
		pointer = monkeys[pointer]
	# if the pointer is after insert the monkey in this position
	if pointer == after:
		successor = monkeys[pointer]
		monkeys[pointer] = name
		monkeys[name] = successor

print("-----------Question 7-------------")
insert("Charlie", "Beta")
printAll()

# 8 - [Spicy] - Write a function that flips the chain upsidedown.
# Foxtrot should be the first monkey, and Alpha the last.
def flip_chain(first_monkey):
	prev_monkey = None
	current_monkey = first_monkey
	while current_monkey is not None:
		next_monkey = monkeys[current_monkey]
		monkeys[current_monkey] = prev_monkey
		prev_monkey = current_monkey
		current_monkey = next_monkey
	first_monkey = prev_monkey

print("-----------Question 8-------------")
flip_chain(first_monkey)
printAll()