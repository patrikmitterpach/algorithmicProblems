# facebook-likes.py

# You probably know the "like" system from Facebook and other pages. People can 
# "like" blog posts, pictures or other items. We want to create the text that 
# should be displayed next to such an item.

def likes(names):
    
    length = len(names)
    
    if length == 0:
        return 'no one likes this'
    elif length == 1:
        return '{} likes this'.format(names[0])
    elif length == 2:
        return '{} and {} like this'.format(names[0], names[1])
    elif length == 3:
        return '{}, {} and {} like this'.format(names[0], names[1], names[2])
    else:
        return '{}, {} and {} others like this'. format(names[0], names[1], length-2) 