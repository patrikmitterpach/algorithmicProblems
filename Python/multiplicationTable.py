# multiplicationTable.py

# Create a function that accepts dimensions, of Rows x Columns, 
# as parameters in order to create a multiplication table sized 
# according to the given dimensions. **The return value of the
# function must be an array, and the numbers must be Fixnums, 
# NOT strings.

def multiplication_table(row,col):

    # Initialize empty variables 
    # for the returnList and a rowList
    fullList = []
    rowList = []

    # Main loop
    for i in range(row):
        for ii in range(col):
            rowList.append((i+1)*(ii+1))
        
        # each rowList is added 
        # to a list and reset afterwards
        fullList.append(rowList)
        rowList = []

    return fullList
    

print(multiplication_table(69,69))
