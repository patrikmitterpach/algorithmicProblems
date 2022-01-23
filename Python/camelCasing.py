# camelCasing.py

# Complete the solution so that the function will break up camel casing, using a space between words.

def solution(s):
    return_zoznam = []

    for idx, char in enumerate(s):
        if char == char.upper():
            return_zoznam.append(' ')
        return_zoznam.append(char) 

    return "".join(return_zoznam)