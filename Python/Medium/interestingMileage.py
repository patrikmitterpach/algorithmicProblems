

# "7777...8?!??!", exclaimed Bob, "I missed it again! Argh!"
#  Every time there's an interesting number coming up, 
#  he notices and then promptly forgets. Who doesn't like 
#  catching those one-off interesting mileage numbers?

# Let's make it so Bob never misses another interesting number.
#  We've hacked into his car's computer, and we have a box hooked up
#  that reads mileage numbers. We've got a box glued to his dash that
#  lights up yellow or green depending on whether 
#  it receives a 1 or a 2 (respectively).
# 
# It's up to you, intrepid warrior, to glue the parts together.
#  Write the function that parses the mileage number input, and returns a 2
#  if the number is "interesting" (see below),
#  a 1 if an interesting number occurs within the next two miles,
#  or a 0 if the number is not interesting.

# Interesting numbers:
#  - any digit followed by all zeroes
#  - every digit is the same number
#  - digits are sequential, increasing
#  - digits are sequential, decreasing
#  - digits are a palindrome
#  - digits match on of the values of a given list



def isPalindrome(number):
    if number < 100:
        return False
    numList = [int(digit) for digit in str(number)]
    numLength = len(numList)
        
    for idx, digit in enumerate(numList):
        if digit == numList[numLength - idx - 1]:
            pass
        else:
            return False
    return True

def followedByZeroes(number):
    if number < 100:
        return False
    return number % (10 ** ( len(str(number)) - 1) ) == 0

def digitsTheSame(number):
    if number < 100:
        return False
    numSet = set([int(digit) for digit in str(number)])
    return len(numSet) == 1

def sequentialInts(number, reverse):
    if number < 100:
            return False
    numList = [int(digit) for digit in str(number)]

    if reverse:
        numList = numList[::-1]

    for i in range( 1, len(numList) ):
        if numList[i]-1 == numList[i-1] or (numList[i] == 0 and numList[i-1] == 9 and not reverse):
            pass
        else:
            return False
    return True
        
def is_interesting(number, awesomePhrases):
    for i in range(number, number + 3):
        isInteresting = isPalindrome(i) or followedByZeroes(i) or digitsTheSame(i) or sequentialInts(i, 0) or sequentialInts(i, 1) or (i in awesomePhrases)

        print(isPalindrome(i))
        print(followedByZeroes(i))
        print(digitsTheSame(i))
        print(sequentialInts(i, 1))


        if isInteresting:
            if i == number:
                return 2
            return 1
    
    return 0
    
print(is_interesting(109, []))