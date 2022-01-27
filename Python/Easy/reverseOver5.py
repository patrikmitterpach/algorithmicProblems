# ~ Stop gninnipS My sdroW!
#  Write a function that takes in a string of one or more words,
#  and returns the same string, but with all five or more letter words reversed
#  (Just like the name of this Kata). Strings passed in will consist of
#  only letters and spaces. Spaces will be included only when 
#  more than one word is present.

def spinWords(sentence):
    sentenceList = sentence.split(" ")

    for idx, word in enumerate(sentenceList):
        if len( word ) > 4:
            sentenceList[idx] = word[::-1]
        
    return " ".join(sentenceList)

print( spinWords("Welcome to the Jungle") )

