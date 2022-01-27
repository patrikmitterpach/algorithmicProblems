# Given two arrays of strings a1 and a2 return a sorted array r
#  in lexicographical order of the strings of a1 which are substrings of strings of a2.

def inArr(array1, array2):
    resultArr = []
    for element in array1:
        for compElement in array2:
            if element in compElement: # Find out if element is a substring of compElement
                resultArr.append(element)
                break

    return sorted(list(set(resultArr))) # Return only unique values ( set() ),
                                        #    sorted alphabetically ( sorted() )

print( inArr(["live", "mice", "strong"] , ["lively", "alive", "harp", "sharp", "armstrong"]))