from string import digits


class Solution:
    digits = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }

    def romanToInt(self, s: str) -> int:
        number_list = [self.digits[c] for c in s]
        final_number = 0
        for i in range(len(number_list)):
            a = number_list[i]
            b = number_list[i+1]
            if a < b:
                final_number += b - a
                i += 2
            else:
                final_number += a
                i += 1





print(Solution().romanToInt("MCMXCIV"))
