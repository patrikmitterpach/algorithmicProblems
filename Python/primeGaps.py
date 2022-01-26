# The prime numbers are not regularly spaced.
# For example from 2 to 3 the gap is 1. From 3 to 5 the gap is 2. From 7 to 11 it is 4. 
# Between 2 and 50 we have the following pairs of 2-gaps primes: 
#      3-5, 5-7, 11-13, 17-19, 29-31, 41-43
#
# Your function should return the first pair of two prime numbers spaced
#  with a gap of g between the limits m, n if these numbers exist otherwise None.

def isPrime(number):
    if number == 2 or number == 3:
        return True
    if not number % 2:
        return False

    for i in range(3, int(number ** 0.5) + 1):
        if number % i == 0:
            return False

    return True

def gap(gap, start, end):
    areSuccessive = True

    for i in range(start, end):
        if isPrime(i) and isPrime(i+gap): # find primes with desired gap
            
            for ii in range(i + 1, i + gap): # check for any primes 
                if isPrime(ii):              #  between i+1 and i+gap
                    areSuccessive = False
            
            if areSuccessive:        
                return [i, i+gap]
            else:
                areSuccessive = True
    
    return None

