def rot13(message):
    messageList = list(message)
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
               'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
               'q', 'r', 's', 't', 'u', 'v', 'w', 'x',
               'y', 'z']
    returnList = []
    
    for idx, str in enumerate(messageList) :
        if str.lower() not in letters:
            returnList.append(str)
            continue
        if letters.index(str.lower()) < 10:
            passBy = letters.index(str.lower())+13
        else:
            passBy = 13-(26-letters.index(str.lower()))
        
        if str.isupper():
            returnList.append(letters[passBy].upper())
        else:
            returnList.append(letters[passBy])

    print(returnList)
    return "".join(returnList)

print(rot13('Test'))