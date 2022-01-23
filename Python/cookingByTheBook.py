# cooking-by-the-book.py

# Pete likes to bake some cakes. He has some recipes and ingredients. 
# Unfortunately he is not good in maths. Can you help him to find out, 
# how many cakes he could bake considering his recipes?

# Write a function cakes(), which takes the recipe (object) and the 
# available ingredients (also an object) and returns the maximum number 
# of cakes Pete can bake (integer). For simplicity there are no units for 
# the amounts (e.g. 1 lb of flour or 200 g of sugar are simply 1 or 200). 
# Ingredients that are not present in the objects, can be considered as 0.

def cakes(recipe, available):
    min_count = -1

    for idx, item in enumerate(recipe):
        curr_min_count = 0

        if item in available:
            
            if min_count == -1:
                min_count = available[item] // recipe[item]
            
            curr_min_count = available[item] // recipe[item]
            min_count = curr_min_count if curr_min_count < min_count else min_count
        else:
            return 0 

    return min_count
