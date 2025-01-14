class Solution:
    def isPalindrome(self, x):

        if x < 0 or (x % 10 == 0 and x != 0):
            return False

        reverted_half = 0
        while x > reverted_half:
            reverted_half = reverted_half * 10 + x % 10
            x //= 10


        return x == reverted_half or x == reverted_half // 10

# Example usage
if __name__ == "__main__":
    solution = Solution()
    print(solution.isPalindrome(121))
    print(solution.isPalindrome(-121))
    print(solution.isPalindrome(10))
