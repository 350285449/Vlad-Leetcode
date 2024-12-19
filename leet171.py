class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        result = 0
        for char in columnTitle:
            result = result * 26 + (ord(char) - ord('A') + 1)
        return result

# Examples
solution = Solution()
print(solution.titleToNumber("A"))  # Output: 1
print(solution.titleToNumber("AB"))  # Output: 28
print(solution.titleToNumber("ZY"))  # Output: 701
