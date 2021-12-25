# highestRank.py

# Complete the method which returns the number which is most 
#   frequent in the given input array. If there is a tie for most 
#   frequent number, return the largest number among them.
#
#   Note: no empty arrays will be given.

def highest_rank(arr):
    arr.sort(reverse = True)
    pos_list = []

    for idx, num in enumerate(arr):
        pos_list.append(arr.count(num))
    
    return arr[pos_list.index(max(pos_list))]
    
    
        

assert highest_rank([12, 10, 8, 12, 7, 6, 4, 10, 12]) == 12;
assert highest_rank([12, 10, 8, 12, 7, 6, 4, 10, 10]) == 10;
assert highest_rank([12, 10, 8, 12, 7, 6, 4, 10, 12, 10]) == 12;
