# integerToRoman.py
# Given an integer, convert it to a roman numeral.

def intToRoman(numToConvert):
    values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    romans = ["M", "CM", "D", "MD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]

    result = ""
    
    for idx, num in enumerate(values):
        result += numToConvert//num * romans[idx]
        numToConvert %= num

    return result

print(intToRoman(4888))
