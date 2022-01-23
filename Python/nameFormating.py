# Return a string formatted as a list of names separated by commas
#    except for the last two names, which should be separated by an ampersand.

def namelist(names):
    returnList = []
    while len(names) > 2:
        returnList.append(names[0]['name'])
        names.remove(names[0])    

    if len(names) == 0:
        returnList.append("")
    if len(names) == 1:
        returnList.append(names[0]['name'])
    if len(names) == 2:
        returnList.append(f"{names[0]['name']} & {names[1]['name']}")
    
    return ", ".join(returnList)

# Runtime O(n)

# print( namelist([{'name': 'Bart'},{'name': 'Lisa'},{'name': 'Maggie'},{'name': 'Homer'}]) )
# print( namelist([{'name': 'Bart'},{'name': 'Lisa'},{'name': 'Maggie'}]) )
# print( namelist([{'name': 'Bart'},{'name': 'Lisa'}]) )
# print( namelist([{'name': 'Bart'}]) )
