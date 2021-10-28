# Given two arrays a and b write a function comp(a, b) (orcompSame(a, b)) that 
# checks whether the two arrays have the "same" elements, with the same
# multiplicities. "Same" means, here, that the elements in b are the 
# elements in a squared, regardless of the order.

def comp(array1, array2):
    for idx, num in enumerate(array1):
        if  num**2 not in array2:
            return  False
            
        array2.remove(num**2)
    
    return len(array2) == 0

assert comp([1,2,3], [1,4,9]) == True