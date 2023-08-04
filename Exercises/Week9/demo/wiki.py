# This is the same graph as you saw on the slides!
wikipedia = {
    'A': ['C', 'D'],
    'C': ['H'],
    'D': ['C', 'H', 'T', 'Y'],
    'H': ['X', 'Z'],
    'T': ['C', 'Y'],
    'X': ['A'],
    'Z': [],
    'Y': ['X']
}

class Page():
    def __init__(self, x):
        self.value = x
        self.links = []

links = {link:Page(link) for link in wikipedia}
for link in wikipedia:
    for next_link in wikipedia[link]:
        links[link].links.append(links[next_link])

root = links['A']