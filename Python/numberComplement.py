# numberComplement.py

# The complement of an integer is the integer you get when you 
#   flip all the 0's to 1's and all the 1's to 0's in its binary representation.
# For example, The integer 5 is "101" in binary and its complement
#   is "010" which is the integer 2.
# 
# Given an integer num, return its complement.

def findComplement(num):
    binaryList = []
    
    # Convert the number to binary
    while (num > 0):
        binaryList.append(num%2)
        num = (num - (num%2)) / 2

    currPow = 0
    complement = 0
    
    # Switch digits and add to the complement
    for idx, num in enumerate(binaryList):
        if num:
            binaryList[idx] = 0
        else:
            binaryList[idx] = 1

        complement += binaryList[idx] * 2**currPow
        currPow += 1
    
    return complement

print(findComplement(5))