# tickets.py

# The new "Avengers" movie has just been released! There are a lot of people
# at the cinema box office standing in a huge line. Each of them has a single 
# 100, 50 or 25 dollar bill. An "Avengers" ticket costs 25 dollars.

# Vasya is currently working as a clerk. He wants to sell a ticket to every 
# single person in this line.
#
# Can Vasya sell a ticket to every person and give change if he initially has 
# no money and sells the tickets strictly in the order people queue?
# Return YES, if Vasya can sell a ticket to every person and give change with 
# the bills he has at hand at that moment. Otherwise return NO.

def tickets(people): 
    # Init count of notes - both 0 as stated in the requirements
    current_25 = 0 
    current_50 = 0
    
    # Loop through the list, adjust counts of 25 and 50 notes based on payment 
    # (note two options for a payment of 100)
    for idx, num in enumerate(people):

        if num == 25:
            current_25 += 1
        
        elif num == 50 and current_25 > 0:
            current_25 -= 1
            current_50 += 1
        
        elif num == 100 and current_50 > 0 and current_25 > 0 :
            current_25 -= 1
            current_50 -= 1
        
        elif num == 100 and current_25 > 2:
            current_25 -= 3
        
        else:
            return "NO" # If at any point a transaction cannot be made,
                        #   "NO" is returned

    return "YES"        # If the loop goes through all customers successfully, 
                        #   "YES" is returned
        
