import json, copy
from random import randint


class Folder():
    def __init__(self, name):
        self.name = name
        self.folders = []
        self.files = []



''' Adding Folders and Files to Boss's computer '''
''' Sally has been here: 06 / 2023'''

node = {
    'folders': {},
    'files': {}
}
def get_pics():
    seed = randint(10, 99)
    return [f'IMG_{seed*10 + i}' for i in range(15)]

home = copy.deepcopy(node)

# Home
folders = ['Applications', 'Desktop', 'Documents', 'Downloads']
for folder_name in folders:
    home['folders'][folder_name] = copy.deepcopy(node)
# Applications
f = home['folders']['Applications']
folders = ['Utilities']
files = ['Chrome', 'Mail', 'Notes', 'Photos']
for folder_name in folders:
    f['folders'][folder_name] = copy.deepcopy(node)
for file_name in files:
    f['files'][file_name] = True
# Applications/Utilities
f = f['folders']['Utilities']
files = ['Terminal', 'Bluetooth']
for file_name in files:
    f['files'][file_name] = True
# Documents
f = home['folders']['Documents']
folders = ['Zoom_Recordings']
for folder_name in folders:
    f['folders'][folder_name] = copy.deepcopy(node)
# Documents/Zoom_Recordings
f = f['folders']['Zoom_Recordings']
files = ['01182023.mp4', '02222023.mp4', '03142023.mp4', '03192023.mp4', '04082023.mp4', '04302023.mp4', '06192023.mp4']
for file_name in files:
    f['files'][file_name] = True
# Downloads
f = home['folders']['Downloads']
folders = ['color_palette_templates']
files = ['nyc_event.zip', 'la_event.zip', 'chicago_event.zip', 'boston_event.zip', "color_palette_templates.zip"]
for folder_name in folders:
    f['folders'][folder_name] = copy.deepcopy(node)
for file_name in files:
    f['files'][file_name] = True
# Downloads/color_palette_templates
f = f['folders']['color_palette_templates']
folders = ['Summer', 'Autumn', 'Winter', 'Spring']
files = ['color_palette_readme.md']
for folder_name in folders:
    f['folders'][folder_name] = copy.deepcopy(node)
for file_name in files:
    f['files'][file_name] = True
# Downloads/color_palette_templates/summer
s = f['folders']['Summer']
files = ['summer.pdf', 'pink.png', 'aqua.png', 'sunburst.png']
for file_name in files:
    s['files'][file_name] = True
# Downloads/color_palette_templates/fall
s = f['folders']['Autumn']
files = ['autumn.pdf', 'wine.png', 'pumpkin.png', 'chocolate.png']
for file_name in files:
    s['files'][file_name] = True
# Downloads/color_palette_templates/winter
s = f['folders']['Winter']
files = ['winter.pdf', 'snow.png', 'egg_shell.png', 'evergreen.png']
for file_name in files:
    s['files'][file_name] = True
# Downloads/color_palette_templates/spring
s = f['folders']['Spring']
files = ['spring.pdf', 'lavender.png', 'lemonade.png', 'blush.png']
for file_name in files:
    s['files'][file_name] = True
# Desktop
f = home['folders']['Desktop']
folders = ['Projects', 'Screenshots', 'Ideas', 'Finances']
files = ['family.png', 'New_Years_Resolution.txt']
for folder_name in folders:
    f['folders'][folder_name] = copy.deepcopy(node)
for file_name in files:
    f['files'][file_name] = True
# Desktop/Screenshots
f2 = f['folders']['Screenshots']
files = ['data2023.jpg', 'funny_zoom_pic.jpg', 'Jeffery.jpg', 'IMG_04202023.jpg', 'dream_couch.jpg', 'IMG_07172023.jpg']
for file_name in files:
    f2['files'][file_name] = True
# Desktop/Finances
f2 = f['folders']['Finances']
folders = ['2022', '2023']
for folder_name in folders:
    f2['folders'][folder_name] = copy.deepcopy(node)
# Desktop/Finances/2022
f3 = f2['folders']['2022']
folders = ['Invoices']
files = ['taxes.pdf', 'write_offs.pdf']
for folder_name in folders:
    f3['folders'][folder_name] = copy.deepcopy(node)
for file_name in files:
    f3['files'][file_name] = True
# Desktop/Finances/2022/Invoices
f3 = f3['folders']['Invoices']
files = ['la_invoice.pdf', 'chicago_invoice.pdf']
for file_name in files:
    f3['files'][file_name] = True
# Desktop/Finances/2023
f3 = f2['folders']['2023']
folders = ['Invoices']
files = ['taxes.pdf', 'write_offs.pdf']
for folder_name in folders:
    f3['folders'][folder_name] = copy.deepcopy(node)
for file_name in files:
    f3['files'][file_name] = True
# Desktop/Finances/2023/Invoices
f3 = f3['folders']['Invoices']
files = ['ny_invoice.pdf', 'boston_invoice.pdf']
for file_name in files:
    f3['files'][file_name] = True
# Desktop/Ideas
f2 = f['folders']['Ideas']
folders = ['Valentines_Day', 'BBQ', 'Saint_Patricks']
files = ['vision_board_2023.png', '2023_outline.txt']
for folder_name in folders:
    f2['folders'][folder_name] = copy.deepcopy(node)
for file_name in files:
    f2['files'][file_name] = True
# Desktop/Ideas/Valentines_Day
f3 = f2['folders']['Valentines_Day']
files = ['vision_board.png', 'notes.txt']
for file_name in files:
    f3['files'][file_name] = True
# Desktop/Ideas/BBQ
f3 = f2['folders']['BBQ']
folders = ['Fails']
files = ['vision_board.png', 'notes.txt']
for folder_name in folders:
    f3['folders'][folder_name] = copy.deepcopy(node)
for file_name in files:
    f3['files'][file_name] = True
# Desktop/Ideas/BBQ/Fails
f3 = f3['folders']['Fails']
files = ['vacant_event.jpg', 'roster_screenshot.jpg', 'summary.txt']
for file_name in files:
    f3['files'][file_name] = True
# Desktop/Ideas/Saint_Patricks
f3 = f2['folders']['Saint_Patricks']
files = ['vision_board.png', 'notes.txt']
for file_name in files:
    f3['files'][file_name] = True
# Desktop/Projects
f2 = f['folders']['Projects']
folders = ['Passion_Projects', 'New_Years2023', 'Thanks_Giving2022', 'Ramadan2022', 'Weddings']
for folder_name in folders:
    f2['folders'][folder_name] = copy.deepcopy(node)
# Desktop/Projects/Passion_Projects
f3 = f2['folders']['Passion_Projects']
folders = ['NYC_music', 'LA_studios', 'Alaska']
for folder_name in folders:
    f3['folders'][folder_name] = copy.deepcopy(node)
# Desktop/Projects/Passion_Projects/NYC_music
f4 = f3['folders']['NYC_music']
folders = ['photos']
files = ['vision_board.jpg', 'notes.txt']
for folder_name in folders:
    f4['folders'][folder_name] = copy.deepcopy(node)
for file_name in files:
    f4['files'][file_name] = True
# Desktop/Projects/Passion_Projects/LA_studios
f4 = f3['folders']['LA_studios']
folders = ['photos']
files = ['vision_board.jpg', 'notes.txt']
for folder_name in folders:
    f4['folders'][folder_name] = copy.deepcopy(node)
for file_name in files:
    f4['files'][file_name] = True
# Desktop/Projects/Passion_Projects/Alaska
f4 = f3['folders']['Alaska']
folders = ['photos']
files = ['vision_board.jpg', 'notes.txt']
for folder_name in folders:
    f4['folders'][folder_name] = copy.deepcopy(node)
for file_name in files:
    f4['files'][file_name] = True
# Desktop/Projects/New_Years2023
f3 = f2['folders']['New_Years2023']
folders = ['collection']
files = ['photo_summary.pdf', 'debrief.txt']
for folder_name in folders:
    f3['folders'][folder_name] = copy.deepcopy(node)
    f3['folders'][folder_name]['files'] = get_pics()
for file_name in files:
    f3['files'][file_name] = True
# Desktop/Projects/Thanks_Giving2022
f3 = f2['folders']['Thanks_Giving2022']
folders = ['collection']
files = ['photo_summary.pdf', 'debrief.txt']
for folder_name in folders:
    f3['folders'][folder_name] = copy.deepcopy(node)
    f3['folders'][folder_name]['files'] = get_pics()
for file_name in files:
    f3['files'][file_name] = True
# Desktop/Projects/Ramadan2022
f3 = f2['folders']['Ramadan2022']
folders = ['collection']
files = ['photo_summary.pdf', 'debrief.txt']
for folder_name in folders:
    f3['folders'][folder_name] = copy.deepcopy(node)
    f3['folders'][folder_name]['files'] = get_pics()
for file_name in files:
    f3['files'][file_name] = True
# Desktop/Projects/Weddings
f3 = f2['folders']['Weddings']
folders = ['Cunningham',
'Santana',
'Lyons',
'Dunlap',
'Rios',
'Franklin',
'Robinson',
'Figueroa',
'Griffin',
'Neal',
'Cook',
'Robertson']
files = ['procedure.txt']
for folder_name in folders:
    f3['folders'][folder_name] = copy.deepcopy(node)
    f3['folders'][folder_name]['files'] = get_pics()
for file_name in files:
    f3['files'][file_name] = True


# print data as dictionary
# print(json.dumps(home, indent=4, sort_keys=True))


### OOP
def populate(dict_node, class_node):
    if dict_node['files']:
        class_node.files = [file_name for file_name in dict_node['files']]
    if dict_node['folders']:
        for folder in dict_node['folders']:
            class_node.folders.append(populate(dict_node['folders'][folder], Folder(folder)))
    return class_node

home = populate(home, Folder('Home'))
