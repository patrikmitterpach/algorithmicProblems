# LeetCode #739
# Given an array of integers temperatures represents the daily temperatures,
#  return an array answer such that answer[i] is the number of days you have
#  to wait after the ith day to get a warmer temperature. 
# If there is no future day for which this is possible, keep answer[i] == 0 instead.


def temperatures(daysArr):
    # This problem can be solved in O(n) time using a stack
    #  to track previous temperatures and corressponding indices.
    # For every day the stack is checked. Stack itself is sorted in a 
    #  non-ascending order, so we check the currDay against the last
    #  element of the list:
    # While higher than the last element of the list,
    #  the element is popped and the corresponding index
    #  in returnArr is updated.
    # Element is then added to a stack.
    #
    # Practically, in the loop the days are only determined when
    #  the next highest element is hit, not when the element itself
    #  is hit, like in the O(n**2) solution at the bottom.

    returnArr = [0]*len(daysArr)
    stack = [] # stack consists of pair [currDayTemp, currDayIdx]

    for currDayIdx, currDayTemp in enumerate(daysArr):
        while stack and currDayTemp > stack[-1][0]:
            print(stack)
            stackTemperature, stackIndex = stack.pop()
            returnArr[stackIndex] = currDayIdx - stackIndex
        stack.append([currDayTemp, currDayIdx])    
    return returnArr
    
print( temperatures([73,74,75,71,69,72,76,73]) )


# O(n**2) solution
# def temperatures(days):
#     days = days[::-1]
#     runningMaximum = [days[0]]
#     returnArr = []
#
#     for idx, day in enumerate(days):
#         lastMax = 0
#         for ii in range(idx, -1, -1):
#             print(day, days[ii])
#             if days[ii] > day:
#                 lastMax = idx-ii
#                 break
#         returnArr.append(lastMax)
#       
#     return returnArr[::-1]
