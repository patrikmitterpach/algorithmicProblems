# Define a function that takes in two non-negative integers a and b
#  and returns the last decimal digit of a**b.
#  Note that a and b may be very large!
#
# Can be solved trivially by tracking the possible periods of
#  a to the powers of 1,2,3,4. Period has a maxium length of four,
#  according to elementary number theory. After finding possible
#  last digits of the powers, return the element on position
#  equal to (n2 modulo period - 1). 
def findPeriod(digits):
    return digits[:len(set(digits))] 

def lastDigit(n1, n2):
    if not n2: return 1
    periodArr = []
    currPower = n1

    for i in range(4):
        periodArr.append(currPower % 10)
        currPower *= n1
    
    periodArr = findPeriod(periodArr)
    return periodArr[n2 % len(periodArr) - 1] 
    


print( lastDigit(3715290469715693021198967285016729344580685479654510946723, 68819615221552997273737174557165657483427362207517952651) )