# This one is honestly just a bunch of if statements
#

def count_deaf_rats(town):
    
    listTown = list(town)
    currDir = "R"
    count = 0

    while len(listTown) > 0:
        if currDir == "R" and listTown[0] == "O" and listTown[1] == "~":
            count += 1
            listTown.remove("O"), listTown.remove("~")
        elif currDir == "R" and listTown[0] == "~" and listTown[1] == "O":
            listTown.remove("~"), listTown.remove("O")
        
        if currDir == "L" and listTown[0] == "O" and listTown[1] == "~":
            listTown.remove("O"), listTown.remove("~")
        elif currDir == "L" and listTown[0] == "~" and listTown[1] == "O":
            count += 1  
            listTown.remove("~"), listTown.remove("O")

        elif listTown[0] == " ":
            listTown.remove(" ")
        
        elif listTown[0] == "P":
            currDir = "L"
            listTown.remove("P")
        
        print(listTown)
    
    return count

print( count_deaf_rats("~O~O~O~O P") )
print( count_deaf_rats("P O~ O~ ~O O~") )
print( count_deaf_rats("~O~O~O~OP~O~OO~") )