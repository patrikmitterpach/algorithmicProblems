
def create_phone_number(digitList):

    digitList.insert(0, '(')
    digitList.insert(4, ') ')
    digitList.insert(8, '-')

    return "".join([ str(x) for x in digitList ])

print( create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]) )