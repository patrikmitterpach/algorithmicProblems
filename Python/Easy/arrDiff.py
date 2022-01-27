# Your goal in this kata is to implement a difference function, 
#  which subtracts one list from another and returns the result.
# It should remove all values from list a,
#  which are present in list b keeping their order.

def arrayDiff(a, b):
    for idx, num in enumerate(b):
        while num in a:
            a.remove(num)
    return a

print( arrayDiff([1,2,2,2,3],[2]) )