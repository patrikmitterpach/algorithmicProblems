#oddInt.py

# Given an array of integers, find the one that appears an odd number of times.
# There will always be only one integer that appears an odd number of times.

def find_it(seq):
    
    list = []
    
    for idx, num in enumerate(seq):     # Loop through list, add only ints not in the list, 
            if num in list:             # remove those already in
                list.remove(num)
            else:
                list.append(num)
    
    print(list[0])

find_it([1, 1, 1, 2, 2, 1, 2])