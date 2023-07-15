from boss_files import home

# class Folder():
#     def __init__(self, name):
#         self.name = name
#         self.folders = []
#         self.files = []

## Mild

# 1. Print the name of the "home" folder
print(home.name)
# 2. How many folders are in the 'Home' folder?
print(len(home.folders))
# 3. How many files are in the 'Home' folder?
print(len(home.files))

# 4. Write a function that prints the folder names in the current folder.
# Test it out with the 'Home' folder, then the 'Home/Desktop' folder

def print_folders(folder):
	for folder in folder.folders:
		print(folder.name)

print_folders(home)

## Medium

# 5. Write a function that uses recursion to print the tree as a dictionary

# Printing as a directory
def print_directory(folder, indent=""):
	print(indent + folder.name + "/")
	for file in folder.files:
		print(indent + " " + file)
	for subfolder in folder.folders:
		print_directory(subfolder, indent + "  ")

print_directory(home)

# Printing as a dictionary
def print_dict(folder, indent = ""):
	print(indent, "{")
	files = folder.files
	if files:
		print(indent + " 'files': {")
		for file_name in files:
			# True that it exists
			print(indent + f" '{file_name}': True,")
		print(indent + " },")
	subfolders = folder.folders
	if subfolders:
		print(indent + "	'folders': {")
		for subfolder in subfolders:
			print(indent + f"        '{subfolder.name}':")
			print_dict(subfolder, indent + "	")
		print(indent +"    },")
	print(indent + "}")
print_dict(home)


# 6. Write a function that uses recursion to find a file by name.
# It should return True if it exists or False if not.
test = [
 'chocolate.png', 'vanilla.png', 'write_offs.pdf', 'procedure.txt',
 'recall.txt'
]
answer = [True, False, True, True, False]


def find(file_name, folder):
	for file in folder.files:
		if file_name == file:
			return True
	for subfolder in folder.folders:
		if find(file_name, subfolder):
			return True
	return False

print(find('chocolate.png', home))
print(find('vanilla.png', home))
print(find('write_offs.pdf', home))
print(find('procedure.txt', home))
print(find('recall.txt', home))

# 7. Modify the above function to return the file path.
# For example: find('procedure.txt') => 'Home/Desktop/Projects/Weddings/procedure.txt'

def find_with_path(file_name, folder, current_path=""):
	for file in folder.files:
		if file_name == file:
			return current_path + "/" + file
	for subfolder in folder.folders:
		# Call function again passing the updated path.
		found_path = find_with_path(file_name, subfolder, current_path + "/" + subfolder.name)
		if found_path:
			return found_path
	return False
print(find_with_path("chocolate.png", home))


# 8. Write a function that finds a folder by name and returns the node if found. Otherwise, it should return None.

def goTo(target_folder, folder):
	if target_folder == folder.name:
		return folder
	for subfolder in folder.folders:
		result = goTo(target_folder, subfolder)
		if result:
			return result
	return None

## Spicy

# 9. Find the 'color_palette_templates' folder and move it to the Passion_Projects folder
# Check that the color_palette_templates's parent folder no longer holds it and that Passion_Projects does




# 10. Write a function that finds the lowest common ancestor folder that holds the 2 inputted files
# For example: common_ancestor('ny_invoice.pdf', 'la_invoice.pdf) => 'Finances'
# For example: common_ancestor('roster_screenshot.jpg', 'New_Years2023') => 'Desktop'
