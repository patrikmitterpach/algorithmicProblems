# title-case.py

# A string is considered to be in title case if each word in the 
# string is either (a) capitalised (that is, only the first letter of 
# the word is in upper case) or (b) considered to be an exception and 
# put entirely into lower case unless it is the first word, which is 
# always capitalised.

# Write a function that will convert a string into title case, given 
# an optional list of exceptions (minor words). The list of minor words will 
# be given as a string with each word separated by a space. 
# Your function should ignore the case of the minor words string -- 
# it should behave in the same way even if the case
# of the minor word string is changed.

def title_case(title, minor_words=''):
    
    title_list = title.lower().split()          # Both title and minor_words
    minor_list = minor_words.lower().split()    #   are lowercased and split 
                                                #   into separate lists
                                                
    # Loop through the title,
    # if a word isn't in a minor_list capitalise it 
    if len(title_list) > 0:                     
        for idx, word in enumerate(title_list):

            if word not in minor_list:
                title_list[idx] = title_list[idx].lower().capitalize()
        
        # Capitalise the first word as well
        title_list[0] = title_list[0].capitalize() 
        
    # return title_list joined together as a string
    return ' '.join(word for word in title_list)
    