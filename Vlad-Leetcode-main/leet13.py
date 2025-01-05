class Solution:
    def isPalindrome(self, x):

        if x < 0 or (x % 10 == 0 and x != 0):
            return False

        reverted_half = 0
        while x > reverted_half:
            reverted_half = reverted_half * 10 + x % 10
            x //= 10

    def romanToInt(self, s):
        roman_to_int = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        total = 0
        prev_value = 0

        for char in reversed(s):
            value = roman_to_int[char]
            if value < prev_value:
                total -= value
            else:
                total += value
            prev_value = value

        return total

