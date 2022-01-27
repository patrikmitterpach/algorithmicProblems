# Digital root is the recursive sum of all the digits in a number.
# Given n, take the sum of the digits of n. If that value has more than one digit, continue reducing in this way until a single-digit number is produced. The input will be a non-negative integer.

def digitalRoot(n):
    currDigits = [int(digit) for digit in str(n)]
    currSum = sum(currDigits)
    if currSum > 9:
        return digitalRoot(currSum)
    return currSum

print( digitalRoot(493193) )