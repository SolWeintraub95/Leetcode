class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        k = len(digits)-1
        digits[k] += 1
        while k > 0:
            if digits[k] == 10:
                digits[k-1] += 1
                digits[k] = 0
            k -= 1
        if digits[k] == 10:
            digits.insert(0, 1)
            digits[k + 1] = 0
        return digits
result = Solution().plusOne([8,9,9])
print(result)
