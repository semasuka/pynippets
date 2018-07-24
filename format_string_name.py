"""
Given: an array containing hashes of names

Return: a string formatted as a list of names separated by commas except 
for the last two names, which should be separated by an ampersand.

Example:

namelist([ {'name': 'Bart'}, {'name': 'Lisa'}, {'name': 'Maggie'} ])
# returns 'Bart, Lisa & Maggie'

namelist([ {'name': 'Bart'}, {'name': 'Lisa'} ])
# returns 'Bart & Lisa'

namelist([ {'name': 'Bart'} ])
# returns 'Bart'

namelist([])
# returns ''

"""

def namelist(names):
    names_list = []
    for dict_name in names:
        for value in dict_name.values():
            names_list.append(value)
    bigger_names = ""
    if len(names_list) == 0:
        return ""
    elif len(names_list) == 1:
        return names_list[0]
    elif len(names_list) == 2:
        return names_list[0]+" & "+names_list[1]
    elif len(names_list) >= 3:
        #up to the second last
        for name in names_list[:-2]:
            bigger_names+= name+", "
        bigger_names += names_list[-2]+" & "+names_list[-1]
    return bigger_names
print(namelist([{'name': 'Bart'}]))
