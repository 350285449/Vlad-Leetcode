class Solution:
    def addBinary(self, a: str, b: str) -> str:
        max_length = max(len(a), len(b))
        a = a.zfill(max_length)
        b = b.zfill(max_length)
        result = []
        carry = 0
        for i in range(max_length - 1, -1, -1):
            sum_bit = carry + int(a[i]) + int(b[i])
            result.append(str(sum_bit % 2))
            carry = sum_bit // 2
        if carry:
            result.append(str(carry))
        return ''.join(reversed(result))
