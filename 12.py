class Solution:
    def intToRoman(self, num: int) -> str:
        roman_num = ""
        value_symbols = [
            (1000, "M"),
            (900, "CM"),
            (500, "D"),
            (400, "CD"),
            (100, "C"),
            (90, "XC"),
            (50, "L"),
            (40, "XL"),
            (10, "X"),
            (9, "IX"),
            (5, "V"),
            (4, "IV"),
            (1, "I"),
        ]
        for number, symbol in value_symbols:
            if num == 0:
                break
            count = num // number
            roman_num += symbol * count
            num -= count * number
        return roman_num
