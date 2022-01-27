class RomanNumerals:

    def to_roman(val):

        values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        romans = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]

        result = ""
        
        for idx, num in enumerate(values):
            result += val//num * romans[idx]
            val %= num

        return result

    def from_roman(string):
        values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        romans = ["M", "CM", "D", "MD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]

        result = 0
        currPos = 0

        while currPos < len(string):
            if currPos + 1 < len(string) and string[currPos:currPos+2] in romans:
                result += values[romans.index(string[currPos:currPos+2])]
                currPos += 2
            else:
                result += values[romans.index(string[currPos])]
                currPos += 1

        return result
        

print(RomanNumerals.to_roman(1000))
print(RomanNumerals.to_roman(4))
print(RomanNumerals.to_roman(1))
print(RomanNumerals.to_roman(1990))
print(RomanNumerals.to_roman(405))
