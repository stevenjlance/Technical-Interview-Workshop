from boss_files import home

# class Folder():
#     def __init__(self, name):
#         self.name = name
#         self.folders = []
#         self.files = []

## Mild

# 1. Print the name of the "home" folder, folder, and files
print(f'Folder name: {home.name}')
print(f'Folders: {home.folders}')
print(f'Files: {home.files}')

# 2. Print out all the folder names in the Home folder (1 level deep)

def print_folders(folder):
	print(folder.name)
	for subfolder in folder.folders:
		print(f'    {subfolder.name}')

print_folders(home)

# 3. Print out ALL the folders in the file tree

def print_all_folders(folder, indent = ""):
	print(indent + folder.name + "/")
	# Question 4 START
	for file in folder.files:
		print(indent + " " + file)
	# QUESTION 4 END
	for subfolder in folder.folders:
		print_all_folders(subfolder, indent + "   ")

print_all_folders(home)

# 4. Update the function to print all the files as well!

# 5. Write a function that uses recursion to find a file by name.
# It should return True if it exists or False if not.
test = [
 'chocolate.png', 'vanilla.png', 'write_offs.pdf', 'procedure.txt',
 'recall.txt'
]
answer = [True, False, True, True, False]

def find(file_name, folder):
	for file in folder.files:
		if file == file_name:
			return True
	for subfolder in folder.folders:
		if find(file_name, subfolder):
			return True
	return False

print(find(test[0], home)) # True
print(find(test[1], home)) # False