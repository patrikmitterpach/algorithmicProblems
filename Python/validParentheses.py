# Write a function that takes a string of parentheses,
#  and determines if the order of the parentheses is valid.
#  The function should return true if the string is valid,
#  and false if it's invalid.

def validParentheses(string):
    parentList = [char for char in string]
    parentCount = 0

    for idx, num in enumerate(parentList):
        if num == ")":
            parentCount -= 1
        if num == "(":
            parentCount += 1
        
        print(parentCount)

        if parentCount < 0:
            return False
    
    if parentCount != 0:
        return False
    return True
         
assert ( validParentheses( "()" ) == True)
assert ( validParentheses( "((" ) == False)
assert ( validParentheses( "(())" ) == True)
assert ( validParentheses( "()()))" ) == False)
