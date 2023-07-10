from data import train_cars

first_train = "277"

print(train_cars[first_train])

# Challenges
# For each challenge, DO NOT use dictionary or list methods 


# -- Mild --

# Print the first train's data. The first train is stored in the variable first_train
print("---------Question 1---------")
print(train_cars[first_train])

# What color is the second train in sequence? (without peaking at the data)
print("---------Question 2---------")
print(train_cars[first_train]["next_train"])

# Write a function `print_trains(train_cars, first_train)` that prints all the train cars in sequence order

def print_trains(train_cars, first_train):
	current = first_train
	while current is not None:
		print(train_cars[current])
		next_train = train_cars[current]["next_train"]
		current = next_train
print("---------Question 3---------")	
print_trains(train_cars, first_train)	

# -- Medium --

new_train = {
    "id": 777,
    "color": "red",
    "weight": 9112,
    "material": "titanium",
}

# Write a function `append(train)` that adds a new train to the end of the linked list.
# Be sure to check your results

def append(train):
	current = first_train
	while current is not None:
		if train_cars[current]["next_train"] == None:
			# When the train car is found, need to update the pointer index and add the train to the end
			train_cars[train["id"]] = {
				"color": train["color"],
		        "weight": train["weight"],
		        "material": train["material"],
		        "next_train": None,
            }
			train_cars[current]["next_train"] = train["id"]
			break
		else:
			next_train = train_cars[current]["next_train"]
			current = next_train
	
print("---------Question 4---------")	
append(new_train)

print_trains(train_cars, first_train)
# Write a function `pop()` that removes the last item of the linked list

def pop():
	second_last_train = None
	current = first_train
	while current is not None:
		next = train_cars[current]["next_train"]
		if next is None:
			break
		second_last_train = current
		current = next
	train_cars[second_last_train]["next_train"] = None
print("---------Question 5---------")	
pop()
print_trains(train_cars, first_train)

# Write a function `insert(idx, train)` that inserts the new_train at a specified index and returns the ID of the first_train

def insert(idx, train):
	current = first_train
	while current is not None and current != idx:
		current = train_cars[current]["next_train"]
	if current == idx:
		successor = train_cars[current]		
		# Insert the train
		train_cars[train["id"]] = {
				"color": train["color"],
		        "weight": train["weight"],
		        "material": train["material"],
		        "next_train": successor["next_train"],
            }
		# Update pointer
		train_cars[current]["next_train"] = train["id"]
print("---------Question 6---------")	
insert("011", new_train)
print_trains(train_cars, first_train)

# Write a function `remove(idx)` that removes a train from the chain (but not the dictionary) and returns the ID of the first_train

def remove(idx, first_train):
	current = first_train
	previous = None
	while current != idx and current is not None:
		previous = current
		current = train_cars[current]["next_train"]
	if current == idx:
		if previous != None:
			train_cars[previous] = train_cars[current]
		else:
			first_train = current

print("---------Question 7---------")	
remove(777, first_train)
print_trains(train_cars, first_train)

# -- Spicy --

# Write a function `reverse(train_cars, first_train)` that makes the last train car first and the first train car last.



# The function should return the new first_train




# Write a function sort_trains(train_cars, first_train). Use your favorite sorting algorithm to sort the trains by weight.
# The heaviest should be at the front and lightest at the back.




# [Super Spicy] Convert the linked list using object oriented programming.
# - Create a new file `Link.py` that defines 2 classes: "Train" and "Car"
# - Train should have the `first_train` variable and a methods to append a new train
# - Car should have all the attributes in the dictionary above -- include "next_train" and "id"



# [Super Spicy] Add and adjust `print_trains()` and the rest of the functions from the Medium challenges in your "Train" class
# The print for each train should display the color, material, and weight.