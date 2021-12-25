# firstUniqueCharacter.py
# For a given string, return the position of the 
# first non-recurring character.

def firstUniqChar(s):
        for char in s:
            if s.count(char) == 1:
                return s.index(char)
        return -1
    
    # Complexity: O(n^2)

# print(firstUniqChar("abcdefghijklmnopqrstuvwxyzabcedfghijklmnopqrstuvwxy"))