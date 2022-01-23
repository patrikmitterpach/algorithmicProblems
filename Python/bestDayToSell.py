# bestDayToSell.py
def maxProfit(List):
    profit = 0

    runningMax = 0
    runningMin = List[0]

    for idx, num in enumerate(List):
        if num < runningMin:
            runningMin = num
            runningMax = 0  
        if num > runningMax:
            runningMax = num
        if runningMax - runningMin > profit:
            profit = runningMax - runningMin

    return profit
    
# Complexity: O(n)

print(maxProfit( [7,1,5,3,6,4] )) 
         