# bugger.py

# Write a function, persistence, that takes in a positive parameter num and 
# returns its multiplicative persistence, which is the number of times you must # multiply the digits in num until you reach a single digit.

def persistence(n):
    
    list = [int(i) for i in str(n)]
    pers_count = 0
    

    while len(list) > 1:
        curr_sum = 1

        for idx, num in enumerate(list):
            curr_sum *= num

        list = [int(i) for i in str(curr_sum)]
        pers_count += 1

    return pers_count


        

