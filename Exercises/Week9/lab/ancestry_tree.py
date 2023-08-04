class Hispanic():
    def __init__(self, percent):
        self.percent = percent
        self.mom = None
        self.dad = None

# Luis    
luis = Hispanic(31)

luis_tree = {
    31: (60, 44),
    60: (82, 93),
    44: (65, 88),
    82: (85, 94),
    93: (91, 96),
    65: (75, 80),
    88: (92, 97)
}
queue = [luis]
while queue:
    current_person = queue.pop(0)
    if current_person.percent in luis_tree.keys():
        current_person.mom = Hispanic(luis_tree[current_person.percent][0])
        current_person.dad = Hispanic(luis_tree[current_person.percent][1])
        queue.append(current_person.mom)
        queue.append(current_person.dad)


# Naya       
naya = Hispanic(45)

luis_tree = {
    45: (86, 58),
    86: (90, 93),
    58: (84, None),
    93: (96, None)
}
queue = [luis]
while queue:
    current_person = queue.pop(0)
    if current_person.percent in luis_tree.keys():
        mom = luis_tree[current_person.percent][0]
        dad = luis_tree[current_person.percent][1]
        current_person.mom = Hispanic(mom) if mom else None
        current_person.dad = Hispanic(dad) if dad else None
        queue.append(current_person.mom)
        queue.append(current_person.dad)