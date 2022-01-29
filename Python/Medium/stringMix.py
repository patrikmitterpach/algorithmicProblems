# Return the count for every valid char in two arrays in a specific format
#  C:LLLLL/C:LLLLL/C:LLLL where C stands for the array with the maximum count
#  and L for the string consisting of the letter times the count

def validLetter(letter):
    return letter.lower() in 'abcdefghijklmnopqrstuvwxyz'

def mix(s1, s2):
    arrayOne = [ letter for letter in s1 if validLetter(letter)]
    arrayTwo = [ letter for letter in s2 if validLetter(letter)]
    returnArr = []

    for l in 'abcdefghijklmnopqrstuvwxyz':
        currLetterCountOne = arrayOne.count(l)
        currLetterCountTwo = arrayTwo.count(l)
        
        if currLetterCountOne > currLetterCountTwo:
            returnArr.append(f'1:{l*currLetterCountOne}')
        elif currLetterCountOne < currLetterCountTwo:
            returnArr.append(f'2:{l*currLetterCountTwo}')
        else:
            returnArr.append(f'3:{l*currLetterCountOne}')

    returnArr = [elem for elem in returnArr if len(elem) > 3]
    returnArr = sorted(returnArr, key=lambda x:(-len(x), int(x[0]), x[2]) )

    for idx, elem in enumerate(returnArr):
        if elem[0] == '3': returnArr[idx] = f'={elem[1:]}'  
    # print(returnArr)
    return "/".join(returnArr)

print( mix("my&friend&Paul has heavy hats! xx&", "my friend John has many many friends &") )
    
