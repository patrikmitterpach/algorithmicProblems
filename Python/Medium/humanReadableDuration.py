def format_duration(seconds):
    if not seconds: return "now"

    modulo     = [31536000, 86400, 3600, 60]
    timeUnits  = ['year', 'day', 'hour', 'minute']
    returnList = []

    for i in range(4):
        unitCount = seconds // modulo[i]
        seconds = seconds % modulo[i]
        if unitCount:
            returnList.extend( [f"{unitCount} {timeUnits[i]}" + ("s" if unitCount > 1 else ""),
                                 ", " if seconds else ""] )
    if seconds:
        returnList.extend([f"{seconds} second" + ("s" if seconds > 1 else ""), ""])
    if len(returnList) > 2: returnList[-3] = " and "
    
    return "".join( returnList )

print( format_duration(1320302403) )