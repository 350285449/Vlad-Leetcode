class Solution:
    def isValid(self, s):
        matching_pairs = {')': '(', '}': '{', ']': '['}
        stack = []
        for char in s:
            if char in matching_pairs:
                if stack and stack[-1] == matching_pairs[char]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)
        return not stack
