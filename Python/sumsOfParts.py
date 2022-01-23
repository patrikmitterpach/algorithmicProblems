def partSums ( arr ):

    returnList = []
    listSum = sum(arr)    
    currSubtract = 0

    for idx, num in enumerate ( arr ):
        returnList.append(listSum - currSubtract)
        currSubtract += num

    returnList.append(0)                  
    return returnList

    # ~ Simpler O(n ** log n) version
    # for i in range ( arrLength ):
    #     returnList.append( sum(arr[i:]) )  
    # returnList.append(0)                  

print( partSums([0, 1, 3, 6, 10]) )