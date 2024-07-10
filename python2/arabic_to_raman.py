class translator:

    def deciToRoman(self, num):
        val = [
            1000, 900, 500, 400,
            100, 90, 50, 40,
            10, 9, 5, 4,
            1
        ]
        syb = [
            "M", "CM", "D", "CD",
            "C", "XC", "L", "XL",
            "X", "IX", "V", "IV",
            "I"
        ]
        roman_num = ''
        i = 0
        while num > 0:
            for _ in range(num // val[i]):
                roman_num += syb[i]
                num -= val[i]
            i += 1
        return roman_num

    def romanToDeci(self, s):
        roman_values = {
            'I': 1, 'V': 5, 'X': 10, 'L': 50,
            'C': 100, 'D': 500, 'M': 1000
        }
        decimal_num = 0
        prev_value = 0
        for char in reversed(s):
            value = roman_values[char]
            if value < prev_value:
                decimal_num -= value
            else:
                decimal_num += value
            prev_value = value
        return decimal_num

# Example usage
num = int(input("Enter number to translate : "))

# Instantiate the translator
trans = translator()

# Convert decimal to Roman numeral
roman_numeral = trans.deciToRoman(num)
print(roman_numeral)

# Convert the Roman numeral back to decimal
decimal_number = trans.romanToDeci(roman_numeral)
print(decimal_number)
