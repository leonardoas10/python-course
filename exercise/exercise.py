names = ['leonardo', 'ana', 'grecia', 'paolo', 'hermana']

def len_of_names(names):
    for name in names:
        print('length of the name ',name, len(name))
        if len(name) > 5:
            print('more that 5 characters ', name)
        if 'n' in name or 'N' in name:
            print('i have n in my name ', name)

len_of_names(names)

while True:
    names.pop()
    if len(names) == 0:
        break
    print(names)