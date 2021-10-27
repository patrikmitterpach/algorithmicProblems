# sum-of-nums

# Given two integers a and b, which can be positive or negative,
# find the sum of all the integers between and including them and return it.
# If the two numbers are equal return a or b. Note: a and b are not ordered!


def get_sum(a,b):
    sum = 0
    list = [a, b]
    list.sort()
    
    for i in range(list[0], list[1]+1):
        sum = sum + i
    
    print(sum)
        
get_sum(1, 2)