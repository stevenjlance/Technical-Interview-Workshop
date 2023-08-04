# According to genetic science, you are the product of the genes from your parents and their parents before you and so on. Luis just took a test and found out that he is 31% Hispanic. Culturally he is much more, but this made him curious dive into his roots and study his genetic tree a bit.

# A diagram of Luis's ancestry results is in ancestor_tree.png. The numbers signify the percentage of genes that show Hispanic (eg. 31 => 31% Hispanic). For the diagram, assume left is the biological mother and right is the biological father. For example, level 1 is Luis, level 2 node 1 is his mother, and level 2 node 3 is his grandmother on his father's side, etc.

# 1. Looking at the ancestor_tree.png, which of Luis's parents are most Hispanic? Grandparent?

# 2. Looking at the ancestor_tree.png, which mother in the graph is the least hispanic? 

# The code for this tree is set up as an Object. We can't see the whole thing, but we do have Luis's node.

from ancestry_tree import luis, naya

# class Hispanic():
#     def __init__(self, percent):
#         self.percent = percent
#         self.mom = None
#         self.dad = None

# 3. Print luis' percentage
print(luis.percent)

# 4. Print Luis' mom's percentage
print(luis.mom.percent)
# 5. Print Luis' dad's percentage
print(luis.dad.mom.percent)

# 6. What percent hispanic are Luis's 2 great grandmothers on his father's side?
print(luis.dad.mom.mom.percent)
print(luis.dad.dad.mom.percent)

# 7. Which search would you prefer to use if your looking for the percent of a great-grandparent? BFS or DFS?

# 8. Write a function that returns all the percents in "level order" as a list (ie. [31, 60, 44, 82, 94, etc.])
def level_order_percents(root):
	if root is None:
		return []
	# Create a queue
	queue = [root]
	# Create empty percent list that will be returned
	percents = []
	# run as long as there is a queue
	while queue:
		# Pop current person off queue and add to percents
		current_person = queue.pop(0)
		percents.append(current_person.percent)
		# If they have a mom and/or dad, add to queue
		if current_person.mom:
			queue.append(current_person.mom)
		if current_person.dad:
			queue.append(current_person.dad)
	return percents
print(level_order_percents(luis))
# 9. Write a function that takes the average percent of all the women (left nodes)
def average_women(root):
	if root is None:
		return []
	# Create a queue
	queue = [root]
	# Create empty percent list that will be returned
	percents = []
	sum = 0
	women_count = 0
	# run as long as there is a queue
	while queue:
		# Pop current person off queue and add to percents
		current_person = queue.pop(0)
		percents.append(current_person.percent)
		# If they have a mom and/or dad, add to queue
		if current_person.mom:
			queue.append(current_person.mom)
			print(current_person.mom.percent)
			sum += current_person.mom.percent
			women_count += 1
		if current_person.dad:
			queue.append(current_person.dad)
	if women_count > 0:
		average = sum / women_count
		return average
	return 0

print(average_women(luis))

# 10. Write a function that returns the most genetically hispanic person at each generation (level).
def most_hispanic_at_each_generation(root):
    if root is None:
        return {}

    queue = [(root, 0)]
    most_hispanic = {0: root}

    while queue:
        current_person, level = queue.pop(0)

        if current_person.mom:
            queue.append((current_person.mom, level + 1))
            if level + 1 not in most_hispanic or current_person.mom.percent > most_hispanic[level + 1].percent:
                most_hispanic[level + 1] = current_person.mom

        if current_person.dad:
            queue.append((current_person.dad, level + 1))
            if level + 1 not in most_hispanic or current_person.dad.percent > most_hispanic[level + 1].percent:
                most_hispanic[level + 1] = current_person.dad

    return most_hispanic


# 11. Write a function that returns the average drop for each leaf parent.
# For example, from 85 > 82 > 60 > 31 the percentage dropped 3, then 12, then 29 for an average drop of 14.7 (3+12+29 / 3 = 14.7).